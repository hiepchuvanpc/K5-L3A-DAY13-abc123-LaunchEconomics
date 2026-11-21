# AI_CONTEXT: BỘ NHỚ TRẠNG THÁI & TIẾN ĐỘ DỰ ÁN

## 1. Mục tiêu hiện tại
- **Vai trò:** TV 2 (QC & Analyst) — *Người kiểm số*
- **Nhánh Git:** `feat/bang-chi-phi`
- **Tập tin chịu trách nhiệm:** `report/team/bang_chi_phi.md`
- **Tình trạng:** Đã hoàn thành 100% nhiệm vụ A (A1–A4) và nhiệm vụ B (B1–B4).

---

## 2. Bản đồ tiến độ (Roadmap)
- [x] **Giai đoạn 0: Giải phẫu kiến trúc & Tái tạo từ con số 0**
  - [x] Phân tích End-to-End Lifecycle và Data Trace Model.
  - [x] Giả lập quy trình dựng dự án từ thư mục trống (From-scratch Blueprint).
  - [x] Xác định Integration Point của TV 2.
  - [x] Khởi tạo `DraftOfMe.md` và `AI_CONTEXT.md`.
  - [x] User đã xác nhận hiểu toàn cảnh.
- [x] **Giai đoạn 1: Triển khai toàn diện Nhiệm vụ A & B (TV 2 hoàn tất)**
  - [x] **Bước 1:** Điền và giải thích A1 (3 phép thử lý thuyết đáp án biết trước: 1,20 · 1,25 · 1,25).
  - [x] **Bước 2:** Điền và phân tích A2 (Mô hình chi phí từ trace, CPS 4.472 đ gấp 16,3 lần hóa đơn token).
  - [x] **Bước 3:** Điền và phân tích A3 (Phân khúc theo loại đơn & luận cứ loại bỏ quoc_te và doi_tac).
  - [x] **Bước 4:** Điền và phân tích A4 (Chi phí cố định 40tr & độ nhạy quy mô).
  - [x] **Bước 5:** Điền B1 (9 kịch bản độ nhạy) & B2 (Đổi cặp và xếp hạng 3 yếu tố nhạy nhất).
  - [x] **Bước 6:** Điền và phân tích B3 (Giới hạn tối đa 2 lần chạy rẻ nhất cả hệ thống: 6.901.220 đ).
  - [x] **Bước 7:** Điền và phân tích B4 (Kịch bản xem lại 100% tốn 11.743 đ - 12.414 đ, triệt tiêu tiết kiệm).
  - [x] **Bước 8:** Rà soát toàn diện `report/team/bang_chi_phi.md` (Đảm bảo nhãn `simulated`, không dùng từ cấm "production", câu trả lời dưới 3 dòng có kèm số thực chứng).

---

## 3. Các file & hàm đã tác động
- Đã hoàn thiện: [report/team/bang_chi_phi.md](file:///D:/ProjectVin/K5-L3A-DAY13-abc123-LaunchEconomics/report/team/bang_chi_phi.md).
- Đã ghi nhận kiến trúc & nhật ký: [DraftOfMe.md](file:///D:/ProjectVin/K5-L3A-DAY13-abc123-LaunchEconomics/DraftOfMe.md).
- Đã đồng bộ bộ nhớ trạng thái: [AI_CONTEXT.md](file:///D:/ProjectVin/K5-L3A-DAY13-abc123-LaunchEconomics/AI_CONTEXT.md).

---

## 4. Quyết định kỹ thuật & Ràng buộc đã chốt
- **Quy tắc liêm chính dữ liệu:** Toàn bộ dữ liệu được tính toán và đối chiếu tự nhiên từ `src/lab13.py` trên 1.624 lần chạy và 1.200 yêu cầu. Không có bất kỳ sự hardcode hoặc ép số nào.
- **Quy ước nhãn:** Đã gắn đầy đủ nhãn `[simulated]` cho tất cả các con số phụ thuộc vào thời gian giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`).
- **Quy chuẩn độ dài:** Mọi câu trả lời phân tích đều dưới 3 dòng và đều chứa các con số cụ thể đo từ hệ thống.
- **Ràng buộc an toàn:** Tuyệt đối không chứa từ "production" trong toàn văn báo cáo.
- **Dữ liệu bàn giao cho các thành viên khác:**
  + *Cho TV 3 (`pilot_plan.yaml`):* Phạm vi thu hẹp chỉ gồm `noi_dia` và `hang_nang`. Giới hạn retry là 2 lần chạy.
  + *Cho TV 4 (`ho_so_launch_v0.md` & `chi_so.md`):* Đưa 2 rủi ro hàng đầu vào Risk Register: (1) Số ca làm lại tăng, (2) Tỷ lệ xem lại tăng cao.

---

## 5. Điểm tiếp nối (Exact Next Action)
- Tiến hành commit nhánh `feat/bang-chi-phi` cho file `report/team/bang_chi_phi.md`.
- Bàn giao các số liệu đầu ra cho TV 3 (CP4) và TV 4 (CP5).
