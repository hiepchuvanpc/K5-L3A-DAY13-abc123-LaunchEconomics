# Báo cáo cá nhân — NguyenNgocMinhDuc-2A202603421

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Minh Đức
- MSSV: 2A202603421
- Email: nguyenngocminhduc2005@gmail.com
- GitHub: MinDuck512
- Vai trong nhóm: Người gắn nhãn 2 & Giữ hồ sơ (TV 4 · Launch Lead)

## 2. Phần việc phụ trách

- Tham gia **Nhiệm vụ C (CP3):** Tự gắn nhãn độc lập 20 ca lỗi Google PAIR trong `nhan_tv4.txt`, đối chiếu với TV 3 và tổng hợp hoàn chỉnh `report/team/bang_loi.md` (bảng 20 ca, quy tắc phân biệt và bảng khắc phục 5 ca).
- Chủ trì **Nhiệm vụ E (CP5):** Hoàn thiện đặc tả chỉ số, danh sách event và rủi ro kinh tế trong `report/team/chi_so.md`; biên soạn trang hồ sơ quyết định `report/team/ho_so_launch_v0.md`.
- Quản lý hồ sơ nộp nhóm: Cập nhật `TEAM.md`, viết tóm tắt `report/team/group_report.md` và chuẩn bị sẵn khung + câu hỏi phản biện cho `report/team/phieu_cham.md` phục vụ duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (`report/team/bang_loi.md`):**
  - Tự gắn nhãn độc lập 20 ca lỗi vào `nhan_tv4.txt` (không trao đổi trước); khi so khớp với `nhan_tv3.txt` của TV 3 đạt **18/20 = 90%** (vượt mốc 80%) và thống nhất chuẩn 20/20 ca.
  - Thiết kế bảng khắc phục cho đủ 5 loại lỗi (ca 9, 7, 18, 4, 17), mỗi dòng đều gắn **event + ngưỡng + tần suất đo được** (như `input_validation_failed > 2%/ngày`, đối soát sổ cái mỗi giờ ngưỡng `> 0 ca`, kiểm toán mẫu `100 đơn/tuần` ngưỡng `> 1%`) và đúng **1 vai trò phụ trách** có thẩm quyền.
- **Nhiệm vụ E1 & E2 (`report/team/chi_so.md`):**
  - Tính thử chính xác 3 chỉ số trên 1.200 yêu cầu: Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200; phạm vi pilot 92,26%), Dùng bỏ qua gợi ý **27,12%** (48/177), An toàn mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%); đề xuất thêm 2 chỉ số Dùng và An toàn mới.
  - Xây dựng danh sách **11 event có `trace_id`** và kiểm tra chéo 1-1 chứng minh toàn bộ chỉ số E1 và chi phí đo thật đều tính được.
  - Đưa **4 dòng rủi ro kinh tế** từ bảng độ nhạy của TV 2 vào Risk Register, giữ nguyên nhãn `[simulated]` và chỉ rõ dấu hiệu cảnh báo + hành động.
- **Nhiệm vụ E3 (`report/team/ho_so_launch_v0.md`) & Hồ sơ nhóm:**
  - Tổng hợp toàn bộ số liệu A–D vào trang hồ sơ 1 trang A4 đủ 7 mục, phân tách rõ trạng thái `Giả lập` (mục 1, 2, 3, 7) và `Xong, có bằng chứng` (mục 4, 5, 6), nêu thẳng các con số bất lợi (xem lại 100% tốn 11.743–12.414 đ `[simulated]`, power ở mức 5 điểm chỉ đạt 0,64).
  - Chốt đề xuất **Go có điều kiện** kèm 5 điều kiện tiên quyết có người phụ trách và ngày kiểm tra cụ thể (`2026-11-26` đến `2026-11-28`).
  - Cập nhật `TEAM.md`, viết `report/team/group_report.md` và chuẩn bị khung `report/team/phieu_cham.md` cho phiên duyệt chéo tại lớp.

## 4. Bằng chứng

- `nhan_tv4.txt`: Bộ nhãn độc lập 20 ca lỗi của TV 4.
- `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI hỗ trợ tổng hợp cấu trúc tài liệu Gate 2a, đối chiếu bảng số liệu liên tài liệu và rà soát quy chuẩn theo `RUBRIC.md` / `RULES.md`.
- **Cách tự kiểm tra và kiểm chứng:**
  - Chạy kiểm tra trực tiếp trên `src/logix_requests.csv` để xác nhận lại các tỉ lệ E1 (994/1.200 = 82,83%, 48/177 = 27,12%, 51/1.200 = 4,25%) và đối chiếu từng con số với `report/team/bang_chi_phi.md` của TV 2.
  - Chạy lệnh tìm kiếm tự động toàn bộ `report/team/` để bảo đảm mọi số phát sinh từ cột `_simulated` có nhãn `simulated`, không dùng `"cả đội"` ở cột phụ trách và không vi phạm từ bị cấm theo quy tắc Gate 2a.

## 6. Tự đánh giá

- **Mức độ hoàn thành:** Hoàn thành toàn bộ phần việc của TV 4 (Nhiệm vụ C và Nhiệm vụ E cùng bộ hồ sơ nhóm), đảm bảo tính đồng nhất dữ liệu từ A đến E và đủ căn cứ số liệu để trình bày 1 phút bảo vệ trước hội đồng Gate 2a.
