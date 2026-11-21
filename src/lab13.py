"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Thực hiện: Thành viên 1 (Tech & Code Lead).
Môi trường khuyến nghị: Conda 'vinai' (python >= 3.10, pandas, numpy, scipy, statsmodels).

Chạy trong thư mục src/: python3 lab13.py
Hoặc từ root: python src/lab13.py
"""
import math
import os
import pandas as pd

# ==========================================
# 0. BẢNG GIÁ GIẢ ĐỊNH CỦA LAB
# ==========================================
GIA_VAO = 26        # đ / 1.000 token đầu vào
GIA_RA = 130        # đ / 1.000 token đầu ra
GIA_TOOL = 15       # đ / lần gọi tool
LUONG_PHUT = 2000   # đ / phút nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đ / yêu cầu khi nhân viên tự làm (6 phút = 12.000 đ)
CHI_PHI_CO_DINH = 40_000_000  # đ / tháng


# ==========================================
# 1. NHIỆM VỤ A1 · KINH TẾ CỦA VIỆC CHẠY LẠI
# ==========================================
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình; k=None nghĩa là chạy đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, theo bội số giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, "Lỗi test 1: p=0.8, k=2 phải ra 1.20"
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, "Lỗi test 2: p=0.8, k=None phải ra 1.25"
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, "Lỗi test 3: p=0.8, k=3 phải ra 1.25"
    print("✅ Ba phép thử đáp án biết trước A1: ĐẠT (1,20 · 1,25 · 1,25)")


# ==========================================
# 2. NHIỆM VỤ A2 & B · MÔ HÌNH CHI PHÍ
# ==========================================
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Tính toàn bộ chi phí theo trace và simulated minutes.
    - Tử số: Mọi lần chạy (kể cả lỗi)
    - Mẫu số: Chỉ đếm yêu cầu có ket_qua == 'thanh_cong'
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token_moi_run = (runs['tokens_in'] / 1000.0 * gia_vao) + (runs['tokens_out'] / 1000.0 * gia_ra)
    tien_tool_moi_run = runs['tool_calls'] * gia_tool

    token = tien_token_moi_run.sum()
    tool = tien_tool_moi_run.sum()
    chay_lai = (tien_token_moi_run + tien_tool_moi_run)[runs['attempt'] > 1].sum()

    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = token + tool + xem_lai + lam_lai
    so_yc = len(reqs)
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')

    return {
        'token': token,
        'tool': tool,
        'chay_lai_attempt_gt1': chay_lai,
        'xem_lai_sim': xem_lai,
        'lam_lai_sim': lam_lai,
        'tong': tong,
        'so_yeu_cau': so_yc,
        'thanh_cong': thanh_cong,
        'cps': cps,
        'hoa_don_moi_yc': (token + tool) / so_yc if so_yc > 0 else 0,
        'lan_chay_moi_yc': len(runs) / so_yc if so_yc > 0 else 0,
        'ti_le_tc': thanh_cong / so_yc if so_yc > 0 else 0,
    }


def vnd(x):
    return f"{x:>14,.0f}".replace(',', '.')


def pct(x, d=1):
    return f"{x * 100:.{d}f}%".replace('.', ',')


# ==========================================
# 3. NHIỆM VỤ D1 · CÔNG THỨC CỠ MẪU
# ==========================================
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Tính cỡ mẫu mỗi nhóm (n) so sánh hai tỉ lệ độc lập với z chính xác."""
    from statistics import NormalDist
    z_a = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    z_b = NormalDist().inv_cdf(power)
    pbar = (p1 + p2) / 2.0
    n = (z_a * math.sqrt(2.0 * pbar * (1.0 - pbar)) +
         z_b * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2 / ((p2 - p1) ** 2)
    return math.ceil(n)


def he_so_thiet_ke(m, icc=0.02):
    return 1.0 + (m - 1) * icc


# ==========================================
# 4. CHƯƠNG TRÌNH CHÍNH (MAIN EXECUTION)
# ==========================================
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    data_dir = here if os.path.exists(os.path.join(here, 'logix_runs.csv')) else os.path.dirname(here)

    runs = pd.read_csv(os.path.join(data_dir, 'logix_runs.csv'))
    reqs = pd.read_csv(os.path.join(data_dir, 'logix_requests.csv'), keep_default_na=False)

    print("\n" + "=" * 80)
    print("KẾT QUẢ CHẠY TOÀN BỘ PHẦN CODE CỦA THÀNH VIÊN 1 (TECH & CODE LEAD)")
    print("=" * 80)

    # A1
    kiem_tra_dap_an_biet_truoc()

    # A2
    print("\n" + "-" * 80)
    print("NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ (1.200 YÊU CẦU)")
    print("-" * 80)
    g = mo_hinh(runs, reqs)
    fields = [
        ('token', 'đo từ trace'),
        ('tool', 'đo từ trace'),
        ('chay_lai_attempt_gt1', 'đo từ trace'),
        ('xem_lai_sim', 'simulated'),
        ('lam_lai_sim', 'simulated'),
        ('tong', 'có phần simulated'),
    ]
    for ten, nhan in fields:
        print(f"  {ten:24s}: {vnd(g[ten])} đ  [{nhan}]")
    print(f"  {'thanh_cong':24s}: {g['thanh_cong']:>14d}")
    print(f"  {'cps (mỗi việc thành công)':24s}: {vnd(g['cps'])} đ  [simulated]")
    print(f"  {'hoa_don_moi_yc (token+tool)':24s}: {g['hoa_don_moi_yc']:>14,.1f} đ")
    print(f"  --> Bội số CPS / Hoá đơn: {g['cps'] / g['hoa_don_moi_yc']:.1f} lần")
    print(f"  --> Tỷ trọng: Làm lại = {pct(g['lam_lai_sim'] / g['tong'])} [sim], Xem lại = {pct(g['xem_lai_sim'] / g['tong'])} [sim]")
    print(f"  --> Giờ nhân viên chiếm {pct((g['lam_lai_sim'] + g['xem_lai_sim']) / g['tong'])} tổng chi phí!")

    # A3
    print("\n" + "-" * 80)
    print("NHIỆM VỤ A3 · PHÂN TÍCH THEO LOẠI YÊU CẦU")
    print("-" * 80)
    print(f"  {'Loại':10s} {'Số YC':>8s} {'Tỉ lệ TC':>10s} {'Lần chạy/YC':>12s} {'CPS [sim]':>14s} {'So với 12k':>12s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = mo_hinh(runs, reqs[reqs['loai'] == loai])
        print(f"  {loai:10s} {r['so_yeu_cau']:>8d} {pct(r['ti_le_tc']):>10s} {r['lan_chay_moi_yc']:>12.2f} "
              f"{r['cps']:>12,.0f} đ {r['cps'] / BASELINE:>11.2f}x")

    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    pivot_ok = (m.assign(ok=(m['status'] == 'ok'))
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100).round(1)
    print("\n  Tỉ lệ OK (%) theo lần thử (attempt):")
    print(pivot_ok.to_string())

    # A4 · Chi phí cố định (noi_dia + hang_nang)
    print("\n" + "-" * 80)
    print("NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (40 TRIỆU Đ/THÁNG) - PHẠM VI PILOT")
    print("-" * 80)
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_pilot = runs[runs['request_id'].isin(reqs_pilot['request_id'])].copy()
    res_pilot = mo_hinh(runs_pilot, reqs_pilot)
    cps_bien_doi = res_pilot['cps']
    ti_le_tc_pilot = res_pilot['ti_le_tc']  # 900 / 982 ≈ 91.65%

    for quy_mo, label in [(45_000, "45.000 YC/tháng"), (22_500, "Một nửa khối lượng (22.500 YC/tháng)")]:
        viec_tc = round(quy_mo * ti_le_tc_pilot)
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_tc
        cps_tong = cps_bien_doi + co_dinh_moi_viec
        print(f"  {label:35s}: TC={viec_tc:>6,d}/tháng | Cố định/việc={co_dinh_moi_viec:>6,.0f} đ | "
              f"Tổng CPS={cps_tong:>6,.0f} đ ({cps_tong / BASELINE:.2f}x so với 12.000 đ) [simulated]")

    # Ngưỡng hoà vốn cố định
    viec_hoa_von = math.ceil(CHI_PHI_CO_DINH / (BASELINE - cps_bien_doi))
    yc_hoa_von = math.ceil(viec_hoa_von / ti_le_tc_pilot)
    print(f"  --> Ngưỡng hoà vốn phần cố định: tối thiểu {viec_hoa_von:,d} việc thành công/tháng (~{yc_hoa_von:,d} YC/tháng)")

    # B1 & B2
    print("\n" + "-" * 80)
    print("NHIỆM VỤ B1 & B2 · BẢNG ĐỘ NHẠY (9 KỊCH BẢN)")
    print("-" * 80)
    goc = g['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print(f"  {'Kịch bản':30s} {'CPS [sim]':>14s} {'Thay đổi (%)':>14s}")
    for ten, kw in kich_ban.items():
        res = mo_hinh(runs, reqs, **kw)
        diff = (res['cps'] / goc - 1.0) * 100
        print(f"  {ten:30s} {res['cps']:>12,.0f} đ {diff:>+13.1f}%")

    doi_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"\n  B2 - Đổi cặp: Token x2 + Xem lại x2 = {doi_cap:,.0f} đ ({(doi_cap / goc - 1) * 100:+.1f}%) [sim]")

    # B3
    print("\n" + "-" * 80)
    print("NHIỆM VỤ B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG")
    print("-" * 80)
    print(f"  {'Giới hạn':10s} {'Chi phí Agent [sim]':>20s} {'Ca thất bại':>12s} {'Chi phí cả hệ thống':>22s} {'CPS [sim]':>12s}")
    for k in [1, 2, 3]:
        kw = dict(max_lan_chay=k) if k < 3 else {}
        r = mo_hinh(runs, reqs, **kw)
        that_bai = r['so_yeu_cau'] - r['thanh_cong']
        he_thong = r['tong'] + (that_bai * BASELINE)
        print(f"  Tối đa {k} lần {r['tong']:>18,.0f} đ {that_bai:>12d} {he_thong:>20,.0f} đ {r['cps']:>10,.0f} đ")
    print("  --> KẾT LUẬN B3: Tối đa 2 lần chạy là RẺ NHẤT CHO CÔNG TY (6.901.220 đ)!")

    # B4
    print("\n" + "-" * 80)
    print("NHIỆM VỤ B4 · KỊCH BẢN XEM LẠI 100% (noi_dia + hang_nang)")
    print("-" * 80)
    tien_may = ((runs_pilot['tokens_in'] / 1000 * GIA_VAO) +
                (runs_pilot['tokens_out'] / 1000 * GIA_RA) +
                (runs_pilot['tool_calls'] * GIA_TOOL)).sum()

    ok_reqs = runs_pilot[runs_pilot['status'] == 'ok']['request_id'].unique()
    tien_xem_lai = len(ok_reqs) * 5 * LUONG_PHUT

    so_ca_lam_lai = (reqs_pilot['ket_qua'] == 'lam_lai').sum()
    thanh_cong_b4 = (reqs_pilot['ket_qua'] == 'thanh_cong').sum()

    # Kịch bản 1: Giả định đề bài (9 phút/ca làm lại)
    tien_lam_lai_9m = so_ca_lam_lai * 9 * LUONG_PHUT
    tong_b4_9m = tien_may + tien_xem_lai + tien_lam_lai_9m
    cps_b4_9m = tong_b4_9m / thanh_cong_b4

    # Kịch bản 2: Thời gian làm lại trung bình thực tế từ dữ liệu (15.3 phút/ca)
    phut_lam_lai_tt = reqs_pilot['phut_lam_lai_simulated'].sum()
    tien_lam_lai_tt = phut_lam_lai_tt * LUONG_PHUT
    tong_b4_tt = tien_may + tien_xem_lai + tien_lam_lai_tt
    cps_b4_tt = tong_b4_tt / thanh_cong_b4
    phut_tb = phut_lam_lai_tt / so_ca_lam_lai if so_ca_lam_lai > 0 else 0

    print(f"  Số YC: {len(reqs_pilot)} | Xem lại: {len(ok_reqs)} ca (5p) | Làm lại: {so_ca_lam_lai} ca | TC: {thanh_cong_b4}")
    print(f"  (1) Làm lại 9 phút/ca   : CPS = {cps_b4_9m:,.0f} đ = {cps_b4_9m / BASELINE:.2f}x so với 12.000 đ [simulated]")
    print(f"  (2) Làm lại thực tế {phut_tb:.1f}p: CPS = {cps_b4_tt:,.0f} đ = {cps_b4_tt / BASELINE:.2f}x so với 12.000 đ [simulated] (ĐẮT HƠN NGƯỜI TỰ LÀM!)")
    
    # Ngưỡng hoà vốn thời gian xem lại
    nguong_p_9m = (BASELINE * thanh_cong_b4 - tien_may - tien_lam_lai_9m) / (len(ok_reqs) * LUONG_PHUT)
    nguong_p_tt = (BASELINE * thanh_cong_b4 - tien_may - tien_lam_lai_tt) / (len(ok_reqs) * LUONG_PHUT)
    print(f"  --> Ngưỡng hoà vốn thời gian xem lại mỗi ca: <= {nguong_p_9m:.2f} phút (với 9p) hoặc <= {nguong_p_tt:.2f} phút (với 15.3p)")

    # D1
    print("\n" + "-" * 80)
    print("NHIỆM VỤ D1 · TÍNH CỠ MẪU CHO 5 BÀI TOÁN (BASELINE 0.70)")
    print("-" * 80)
    n_a = co_mau_hai_ti_le(0.70, 0.75)
    print(f"  a) Chia theo yêu cầu (MDE 5 điểm): {n_a} yêu cầu mỗi nhóm")

    de_b = he_so_thiet_ke(75, 0.02)
    n_b = math.ceil(n_a * de_b)
    staff_b = math.ceil(n_b / 75)
    print(f"  b) Theo nhân viên (m=75): DE={de_b:.2f} -> Cần n={n_b} ({staff_b} người/nhóm, tổng {staff_b * 2} > 40: KHÔNG ĐỦ!)")

    tran_c = 20 / 0.02
    print(f"  c) 20 nhân viên mỗi nhóm: Cỡ mẫu hiệu dụng tối đa < c/ICC = {tran_c:.0f} < {n_a} (KHÔNG ĐẠT MDE 5 điểm!)")

    tran_d = 6 / 0.02
    print(f"  d) 6 depot mỗi nhóm: Cỡ mẫu hiệu dụng tối đa < {tran_d:.0f} (QUÁ THẤP, LOẠI!)")

    n_e = co_mau_hai_ti_le(0.70, 0.76)
    m_min = math.ceil((859 * 0.98) / (20 - 859 * 0.02))
    de_e = he_so_thiet_ke(m_min, 0.02)
    print(f"  e) MDE 6 điểm (859/nhóm), 20 nhân viên: cần tối thiểu m >= {m_min} yêu cầu/người (DE={de_e:.2f})")
    print("=" * 80 + "\n")


if __name__ == '__main__':
    main()
