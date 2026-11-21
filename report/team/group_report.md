# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm:
- Lớp:
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Bài làm thẩm định tính khả thi kinh tế (Launch Economics) và thiết kế kế hoạch thử nghiệm (Pilot) tại cổng **Gate 2a** cho trợ lý hoàn phí LogiX-VN dựa trên dữ liệu giả lập gồm `1.200` yêu cầu (`src/logix_requests.csv`) và `1.624` lần chạy (`src/logix_runs.csv`). Nhóm triển khai theo 5 nhiệm vụ A–E và quy tắc Zero Conflict: TV 1 dựng mô hình toán kinh tế trong `src/lab13.py`; TV 2 kiểm số độc lập và phân tích chi phí/độ nhạy; TV 3 và TV 4 gắn nhãn độc lập 20 ca lỗi Google PAIR trước khi đối chiếu, thiết kế kế hoạch thử nghiệm phân cụm đủ sức mạnh thống kê và tổng hợp hồ sơ đề xuất trước hội đồng.

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí và độ nhạy):** [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md) — vượt qua 3 phép thử A1 (1,20 · 1,25 · 1,25), tính chi phí thực tế gồm cả lần chạy lỗi và thời gian xem lại/làm lại `[simulated]`, phân tách 4 loại yêu cầu, tính chi phí cố định 40 triệu đ/tháng và phân tích 9 kịch bản độ nhạy + tối ưu hệ thống.
- **Nhiệm vụ C (Phân loại lỗi Google PAIR):** [bang_loi.md](bang_loi.md) — TV 3 và TV 4 gắn nhãn độc lập 20 ca theo nguyên nhân gốc, đối chiếu đạt đồng thuận 90% (18/20), thống nhất 20/20 ca và lập bảng khắc phục 5 ca có ngưỡng đo và vai trò phụ trách riêng biệt.
- **Nhiệm vụ D (Kế hoạch Pilot):** [pilot_plan.yaml](pilot_plan.yaml) — giải 5 bài toán cỡ mẫu cụm D1, chọn chia theo nhân viên (20 + 20 cụm) phân tầng theo 12 depot, đánh đổi MDE 6 điểm (`n = 859`, `m ≥ 299`, `DE = 6,96`) kèm 3 luật dừng 4 vế và rollback 30 phút.
- **Nhiệm vụ E (Chỉ số, rủi ro & Hồ sơ Gate 2a):** [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md) — đặc tả 5 chỉ số, 11 event có `trace_id`, 4 dòng rủi ro từ bảng độ nhạy và hồ sơ 1 trang với đề xuất **Go có điều kiện**.
- **Duyệt chéo Gate 2a:** [phieu_cham.md](phieu_cham.md) — chuẩn bị sẵn khung chấm 30 điểm và câu hỏi phản biện cho phiên duyệt chéo tại lớp.

## 4. Kết quả

- **Kinh tế học triển khai (A, B):** Chi phí mỗi việc thành công (CPS) toàn mẫu là **4.472 đ** `[simulated]` (gấp **16,3 lần** hoá đơn token+tool 274,7 đ/YC; chi phí giờ nhân viên chiếm 92,5%). Nếu tính cả chi phí nhân viên làm thay ca chuyển người, chi phí cả hệ thống đạt **5.865 đ/YC = 0,49×** so với mức 12.000 đ tự làm `[simulated]`. Phân tích theo loại yêu cầu cho thấy chỉ nên giữ `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×), loại bỏ `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (10.215 đ = 0,85×) `[simulated]`. Giới hạn **2 lần chạy** tối ưu tổng chi phí công ty ở mức **6.901.220 đ** `[simulated]`. Độ nhạy cao nhất nằm ở số ca làm lại (+51,8%) và tỉ lệ xem lại (+40,7%); nếu phải xem lại 100%, CPS vọt lên **11.743–12.414 đ (0,98×–1,03×)** `[simulated]`.
- **Chỉ số đợt chạy thử (E1):** Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200; phạm vi pilot 92,26%), tỉ lệ bỏ qua gợi ý là **27,12%** (48/177), tỉ lệ mở lại trong 7 ngày là **4,25%** (51/1.200; phạm vi pilot 3,97%).
- **Đề xuất cuối tại `ho_so_launch_v0.md`:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` với giới hạn 2 lần chạy, kèm 5 điều kiện tiên quyết (vá khoá chống hoàn trùng và đối soát sổ cái ca 7/20; chặn `quoc_te`/`doi_tac` và sửa mẫu ca 9/18; ký chấp nhận MDE 6 điểm với power 0,64 ở mức 5 điểm; bật đủ 11 event `trace_id` + xoá cache ca 17 + kiểm toán 100 đơn/tuần; lộ trình giảm xem lại theo bậc dưới 4,8 phút/ca).
- **Kết quả duyệt chéo từ hội đồng:** *(Cập nhật sau phiên bảo vệ và chấm chéo Gate 2a tại lớp lúc 17:10–17:40).*

## 5. Khó khăn và cách xử lý

- **Ràng buộc cỡ mẫu cụm:** Với tổng 40 nhân viên và ICC = 0,02, không thể đạt MDE 5 điểm ở thiết kế theo cụm (trần hiệu dụng < 1.000 < 1.251). Nhóm xử lý bằng cách nâng MDE lên 6 điểm (`n = 859`, `m ≥ 299` YC/nhân viên) và công khai rõ mức power giảm còn **0,64** nếu tác động thật là 5 điểm để lãnh đạo ký chấp nhận.
- **Môi trường chạy script:** Máy cục bộ thiếu sẵn `pandas` và `statsmodels` ở Python mặc định; nhóm kiểm chứng song song bằng thư viện chuẩn Python (`csv`, `statistics.NormalDist`) đối chiếu khớp 100% toàn bộ bảng số liệu của `src/lab13.py` và kiểm tra cú pháp YAML bằng `pyyaml` (`yaml.safe_load`).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và các file báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu thời gian xem lại và làm lại hiện là giá trị giả lập (`_simulated`); ngay tuần đầu pilot phải thu thập `phut_xem_lai_thuc_te` và `phut_lam_lai_thuc_te` qua event để hiệu chỉnh lại ngưỡng hoà vốn thực.
- Thử nghiệm chia theo nhân viên trong cùng depot có nguy cơ tràn thông tin; cần áp dụng chặt quyền truy cập theo `staff_id` và theo dõi chéo log mở gợi ý.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu môn học: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`
