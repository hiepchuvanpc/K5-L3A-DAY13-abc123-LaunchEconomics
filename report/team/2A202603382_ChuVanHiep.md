# Báo cáo cá nhân — Chử Văn Hiệp (2A202603382)

---

## 1. Thông tin thành viên

- **Họ tên:** Chử Văn Hiệp
- **MSSV:** 2A202603382
- **Email:** 26ai.hiepcv@vinuni.edu.vn
- **Vai trong nhóm:** Người viết code

---

## 2. Phần việc phụ trách

- **Phát triển mã nguồn tính toán (`src/lab13.py`):**
  - Cài đặt và cấu hình môi trường Conda `vinai` với đầy đủ thư viện (`pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`).
  - Viết code giải quyết Nhiệm vụ A1: Ba phép thử kinh tế học của việc chạy lại (đáp án biết trước 1,20 · 1,25 · 1,25).
  - Viết code Nhiệm vụ A2: Mô hình chi phí mỗi việc thành công (CPS - Cost per Success) từ trace dữ liệu và thời gian giả lập `_simulated`.
  - Viết code Nhiệm vụ A3: Phân rã chi phí, tỷ lệ thành công theo 4 loại đơn hàng và lập bảng pivot tỉ lệ OK theo từng attempt.
  - Viết code Nhiệm vụ B: Bảng phân tích độ nhạy 9 kịch bản (B1), kịch bản đổi cặp (B2), tối ưu hóa chi phí toàn hệ thống (B3) và kịch bản xem lại 100% (B4).
  - Viết code Nhiệm vụ D1: Giải thuật tính toán cỡ mẫu cho 5 bài toán thiết kế thử nghiệm pilot (so sánh 2 tỷ lệ độc lập và hệ số thiết kế cụm $DE$).
- **Hỗ trợ quản trị dự án & kỹ thuật:**
  - Cung cấp bảng số liệu chuẩn (Cheat Sheet) cho các thành viên làm báo cáo (`bang_chi_phi.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`).

---

## 3. Đóng góp cụ thể

1. **Nhiệm vụ A1 (Lý thuyết chạy lại):**
   - Cài đặt chính xác 3 hàm: `so_lan_chay_ky_vong(p, k)`, `ti_le_thanh_cong(p, k)`, `he_so_chi_phi_moi_viec_thanh_cong(p, k)`.
   - Vượt qua 3 bài test `assert` với sai số $< 10^{-9}$: $p=0.8, k=2 \rightarrow 1,20$; $p=0.8, k=\text{None} \rightarrow 1,25$; $k=3 \rightarrow 1,25$.
2. **Nhiệm vụ A2 (Mô hình chi phí thực tế):**
   - Xử lý đọc file CSV với tham số bắt buộc `keep_default_na=False` để giữ nguyên các ô rỗng trong `quyet_dinh_xem_lai` không bị ép thành `NaN`.
   - Thiết kế hàm `mo_hinh()` tính đúng quy tắc: **Tử số tính mọi lần chạy (kể cả lỗi)**, **Mẫu số chỉ đếm các đơn có kết quả thành công**.
   - Tính ra kết quả chuẩn: Tổng chi phí **4.373.585 đ** `[có phần simulated]`, số đơn thành công **978**, CPS = **4.472 đ** `[simulated]` (gấp **16,3 lần** hoá đơn token+tool chia đều là 274,7 đ).
   - Làm rõ cơ cấu chi phí: Làm lại chiếm **51,8%** `[sim]`, Xem lại chiếm **40,7%** `[sim]`, thời gian nhân viên chiếm tới **92,5%** tổng chi phí.
3. **Nhiệm vụ A3 (Phân loại đơn & Hành vi chạy lại):**
   - Phân tích chi tiết 4 loại đơn: `noi_dia` (2.696 đ = 0,22×), `hang_nang` (8.221 đ = 0,69×), `quoc_te` (22.515 đ = 1,88×), `doi_tac` (10.215 đ = 0,85×).
   - Lập bảng pivot attempt chỉ ra với đơn `quoc_te`: Lần 1 đúng 30%, lần 2 đúng 11,4%, lần 3 chỉ đúng 2,2% $\rightarrow$ Cung cấp bằng chứng số liệu vững chắc để loại `quoc_te` và `doi_tac` khỏi phạm vi pilot.
4. **Nhiệm vụ B (Độ nhạy & Tối ưu hệ thống):**
   - Lập trình vòng lặp 9 kịch bản B1, xếp hạng chính xác 3 yếu tố nhạy nhất: 1. Số ca làm lại (+51,8%) > 2. Tỉ lệ xem lại (+40,7%) > 3. Lương nhân viên (+23,1%).
   - Cài đặt tham số `max_lan_chay` để mô phỏng kịch bản B3: Chứng minh giới hạn **2 lần chạy** là phương án tiết kiệm nhất cho công ty (**6.901.220 đ**), dù giới hạn 1 lần cho CPS trợ lý thấp hơn nhưng đẩy thêm 85 việc sang nhân viên.
   - Mô phỏng kịch bản B4: Tính ra CPS khi xem lại 100% là **11.743 đ = 0,98×** $\rightarrow$ Kết luận xem lại 100% không đem lại lợi ích kinh tế.
5. **Nhiệm vụ D1 (Cỡ mẫu thử nghiệm lâm sàng):**
   - Cài đặt hàm `co_mau_hai_ti_le()` dùng phân phối chuẩn $z$ chính xác ($z_{0.975} = 1,95996$ và $z_{0.8} = 0,84162$).
   - Tính toán đủ 5 trường hợp: (a) Theo yêu cầu: $1.251$ YC/nhóm; (b) Theo nhân viên ($m=75$): cần $3.103$ YC/nhóm (42 người/nhóm, tổng 84 > 40: loại); (c) 20 nhân viên/nhóm: trần hiệu dụng $< 1.000 < 1.251$ (không đạt); (d) 6 depot: trần $< 300$ (loại); (e) Mức chênh 6 điểm: giải phương trình $20m / (1 + (m-1) \times 0.02) \ge 859 \rightarrow m \ge 299$ yêu cầu/người ($DE = 6,96$).

---

## 4. Bằng chứng

- **File mã nguồn hoàn chỉnh:** [`src/lab13.py`]
- **Lịch sử Git commit:**
  - `3d830c9`: `feat: complete initial lab13.py`
  - `a51c193`: `docs: add team action plan and completed lab13 calculations`
- **Output xác thực từ terminal:**
  - Ba phép thử đáp án biết trước A1: ĐẠT (1,20 · 1,25 · 1,25).
  - A2 CPS: 4.472 đ [simulated], gấp 16,3 lần hoá đơn token+tool.
  - B2 Đổi cặp: 6.543 đ (+46,3%) [simulated].
  - B3 Toàn hệ thống: Tối đa 2 lần = 6.901.220 đ (rẻ nhất).
  - B4 Xem lại 100%: 11.743 đ = 0,98×.
  - D1e: $m \ge 299$ yêu cầu/người, $DE = 6,96$.

---

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Antigravity AI Assistant.
- **Mục đích sử dụng:**
  - Hỗ trợ tra cứu nhanh công thức tính cỡ mẫu thử nghiệm phân cụm (Cluster Randomized Trials) và các thuộc tính của phân phối chuẩn `statistics.NormalDist`.
  - Hỗ trợ xây dựng các hàm định dạng hiển thị tiền tệ `vnd()` và phần trăm `pct()` để xuất kết quả trực quan trên console.
  - Rà soát các trường hợp biên của mô hình chi phí khi lọc theo `max_lan_chay` (chuyển các ca vượt ngưỡng sang nhân viên, set số phút xem lại/làm lại về 0).
  - **Kiểm thử môi trường độc lập:** Chạy trực tiếp script `src/lab13.py` trên môi trường ảo với dữ liệu gốc của đề bài.

---

## 6. Tự đánh giá

- **Mức độ hoàn thành:** 100% công việc của người viết code.
- **Chất lượng sản phẩm:** Code có cấu trúc module rõ ràng, tự động xử lý đường dẫn dữ liệu, in ấn tường minh.
- **Ý thức làm việc nhóm:** Chủ động chuẩn bị tài liệu phân công, bàn giao sớm bộ số liệu đã kiểm chứng cho các thành viên phụ trách tài liệu báo cáo và sẵn sàng hỗ trợ phản biện tại cổng Gate 2a.
