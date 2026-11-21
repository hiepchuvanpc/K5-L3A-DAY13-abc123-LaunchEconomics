# Báo cáo cá nhân — NguyenQuangVu-2A202603407

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Vũ
- MSSV: 2A202603407
- Email: nguyenquangvu755@gmail.com
- GitHub: NguyenVu8888
- Vai trong nhóm: Người kiểm số (TV 2 · QC & Analyst)

---

## 2. Phần việc phụ trách

- Chịu trách nhiệm độc quyền xây dựng và thẩm định toàn bộ số liệu Nhiệm vụ A (A1–A4) và Nhiệm vụ B (B1–B4) trong hồ sơ Launch Economics tại file `report/team/bang_chi_phi.md`.
- Kiểm tra tính độc lập và độ chính xác của các phép tính từ mô hình mã nguồn `src/lab13.py` trên 2 tập dữ liệu log `logix_runs.csv` (1.624 lần chạy) và `logix_requests.csv` (1.200 yêu cầu).
- Hỗ trợ TV 1 và TV 3 tính toán 5 bài toán cỡ mẫu phân tích cụm (D1) cho kế hoạch thử nghiệm `report/team/pilot_plan.yaml`.
- Cùng TV 4 tham gia đọc, phản biện và chấm điểm chéo hồ sơ Gate 2a của nhóm bạn tại `report/team/phieu_cham.md`.

---

## 3. Đóng góp cụ thể

- **Nhiệm vụ A1:** Đối chiếu và kiểm chứng tuyệt đối 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25), đảm bảo tính đúng đắn toán học của mô hình lý thuyết trước khi đo lường dữ liệu thực.
- **Nhiệm vụ A2:** Bóc tách toàn diện cơ cấu chi phí từ trace log; chỉ ra nghịch lý chi phí mỗi việc thành công (CPS = 4.472 đ [simulated]) gấp **16,3 lần** chi phí hóa đơn token/tool (274,7 đ) do chi phí can thiệp của con người chiếm tới **92,5%** tổng ngân sách (làm lại: 51,8%, xem lại: 40,7%).
- **Nhiệm vụ A3:** Phân tích hiệu quả kinh tế trên 4 phân khúc đơn hàng; cung cấp luận cứ định lượng để loại bỏ đơn `quoc_te` (CPS = 22.515 đ = 1,88× so với 12.000 đ) và `doi_tac` (10.215 đ = 0,85×) ra khỏi phạm vi pilot nhằm kiểm soát rủi ro tài chính.
- **Nhiệm vụ A4:** Đánh giá tác động của 40 triệu đ chi phí cố định/tháng theo các kịch bản khối lượng (45.000 YC đạt CPS = 4.599 đ = 0,38×; 22.500 YC đạt CPS = 5.784 đ = 0,48× [simulated]); xác định ngưỡng hòa vốn quy mô tối thiểu là 4.659 việc thành công/tháng.
- **Nhiệm vụ B1 & B2:** Xây dựng ma trận độ nhạy 9 kịch bản; chứng minh số ca làm lại (+51,8%) và tỷ lệ xem lại (+40,7%) là 2 biến số rủi ro lớn nhất cần kiểm soát chặt, trong khi giá token chỉ biến động ±5,6%.
- **Nhiệm vụ B3:** Chứng minh giới hạn **2 lần chạy** là phương án tối ưu chi phí cho toàn công ty (**6.901.220 đ** [simulated]), cảnh báo bẫy tối ưu cục bộ nếu chỉ chạy 1 lần sẽ đẩy chi phí làm tay của nhân viên tăng thêm 548.561 đ.
- **Nhiệm vụ B4:** Thẩm định kịch bản xem lại 100% (CPS đạt 11.743 đ – 12.414 đ = 0,98× – 1,03× so với 12.000 đ), chỉ ra bài học cốt lõi cho pilot là phải tối ưu tỷ lệ xem lại lấy mẫu và rút ngắn thời lượng kiểm tra dưới 4,8 – 5,1 phút/đơn.

---

## 4. Bằng chứng

- **Tập tin sản phẩm:** `report/team/bang_chi_phi.md` đã hoàn thiện đầy đủ 100% các bảng A1–A4 và B1–B4, kèm phân tích định lượng sắc bén dưới 3 dòng có số liệu thực chứng.
- **Git Branch & Commit:** Thực hiện trên nhánh `nguyenquangvu-2A202603407` (hoặc `feat/bang-chi-phi`).
- **Tài liệu kiểm định & học tập:** Đã khởi tạo và duy trì `DraftOfMe.md` (Cẩm nang kiến trúc) và `AI_CONTEXT.md` (Bộ nhớ trạng thái).
- **Tuân thủ quy chuẩn:** Toàn bộ số liệu giả lập đều có nhãn `[simulated]`, không vi phạm từ cấm "production", số liệu khớp 100% với kết quả chạy từ `src/lab13.py`.

---

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity AI Assistant (mô hình Gemini 3.8 Flash).
- **Mục đích sử dụng:**
  - Hỗ trợ giải thích kiến trúc phân tán giữa trace log tầng máy (`runs`) và tầng nghiệp vụ (`requests`).
  - Hỗ trợ kiểm tra chéo các công thức toán tài chính và phân tích độ nhạy.
  - Rà soát tính tuân thủ của báo cáo theo các tiêu chí trong `RUBRIC.md` và `RULES.md`.
- **Cách tự kiểm tra và kiểm chứng:**
  - Tự trực tiếp chạy script `python src/lab13.py` trên môi trường thực tế để lấy log kết quả raw.
  - Tính tay độc lập (QC) các phép toán cộng tuyến tính (B2) và chi phí toàn hệ thống (B3) trước khi đưa vào báo cáo.
  - Dùng lệnh tìm kiếm tự động để rà soát đảm bảo 100% không còn từ cấm hoặc số thiếu nhãn giả lập.

---

## 6. Tự đánh giá

- **Điểm tự đánh giá:** 10/10.
- **Lý do:** Hoàn thành đầy đủ, chính xác toàn bộ nhiệm vụ của Người kiểm số trước thời hạn; số liệu khớp chuẩn xác với ground truth của lab; cung cấp luận cứ kinh tế vững chắc giúp nhóm tự tin bảo vệ hồ sơ Gate 2a trước hội đồng.
