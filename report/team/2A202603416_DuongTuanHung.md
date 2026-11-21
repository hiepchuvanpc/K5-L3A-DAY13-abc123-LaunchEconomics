# Báo cáo cá nhân — DuongTuanHung-2A202603416

## 1. Thông tin thành viên

- Họ tên: Dương Tuấn Hưng
- MSSV: 2A202603416
- Email: duongtuanhung2711@gmail.com
- GitHub: hunglun2711
- Vai trong nhóm: Người gắn nhãn 1 & Pilot (TV 3 · Pilot Lead)

## 2. Phần việc phụ trách

- Tham gia **Nhiệm vụ C (CP3):** Tự gắn nhãn độc lập toàn bộ 20 ca lỗi theo 5 loại của Google PAIR trong `nhan_tv3.txt`, sau đó đối chiếu với TV 4 để tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và hoàn thiện bảng khắc phục trong `report/team/bang_loi.md`.
- Chủ trì **Nhiệm vụ D (CP4):** Thực hiện 5 bài toán cỡ mẫu phân cụm D1, kiểm tra 5 câu hỏi tách tác động D2, phân tích tỉ lệ mở lại trong 7 ngày trên dữ liệu chạy thử và hoàn thiện bản kế hoạch thử nghiệm `report/team/pilot_plan.yaml`.
- Phối hợp cùng TV 1, TV 2, TV 4 rà soát tính nhất quán số liệu giữa `bang_chi_phi.md`, `pilot_plan.yaml` và `ho_so_launch_v0.md` cho phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (Gắn nhãn lỗi Google PAIR):**
  - Hoàn thành gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (`nhan_tv3.txt`), không trao đổi trước với TV 4.
  - Khi đối chiếu với `nhan_tv4.txt`, đạt tỉ lệ đồng thuận **18/20 = 90%** (vượt mức yêu cầu 80%); cùng TV 4 thống nhất lại ca 9 (*Do người dùng* — gốc do khách nhập sai mã sàn TMĐT) và ca 13 (*Giới hạn hệ thống* — bảo hiểm đối tác nằm ngoài phạm vi trợ lý), đạt chuẩn 20/20 ca.
- **Nhiệm vụ D (Kế hoạch Pilot `pilot_plan.yaml`):**
  - Giải đầy đủ 5 câu **D1**: tính ra cỡ mẫu theo yêu cầu `1.251` YC/nhóm; chứng minh chia theo nhân viên với `m = 75` cần `84` người (`> 40`, không đủ); chỉ ra trần hiệu dụng của 20 nhân viên/nhóm (`< 1.000 < 1.251`) và 6 depot/nhóm (`< 300`); tính được mức đánh đổi **MDE 6 điểm** (`n_per_arm = 859`) với 20 nhân viên/nhóm đòi hỏi **`m >= 299` yêu cầu/nhân viên** (`DE = 6,96`).
  - Trả lời đầy đủ 5 câu **D2** chứng minh tính tách được tác động cho phương án chia theo nhân viên `20 + 20` (đối chứng chạy song song cùng tuần, phân tầng theo 12 depot với `seed = 20261121`, giảm tràn tác động bằng tài khoản `staff_id` và log mở gợi ý, viết trước mọi ngưỡng và ngày quyết định `2027-01-05`), đồng thời nêu rõ con số bất lợi **power = 0,64** nếu tác động thật chỉ 5 điểm.
  - Tính tỉ lệ `mo_lai_trong_7_ngay` thực tế từ dữ liệu (`4,25%` toàn mẫu; `3,97%` phạm vi `noi_dia` + `hang_nang`) để thiết lập ngưỡng an toàn so với đối chứng (≥ +2 điểm %) kèm trần tuyệt đối `6%`, tránh dừng oan ngay tuần đầu.
  - Điền sạch toàn bộ trường trong `report/team/pilot_plan.yaml` (xoá sạch dấu `?` ngoài dòng chú thích), viết đủ 3 luật dừng chuẩn 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, gắn nhãn `simulated` cho các đầu vào chi phí liên quan và gán đúng 1 vai trò chủ trì cho mỗi đầu việc.

## 4. Bằng chứng

- `nhan_tv3.txt`: Bộ nhãn độc lập 20 ca lỗi của TV 3.
- `report/team/pilot_plan.yaml`: Đã hoàn thiện phần chú thích D1–D2, toàn bộ cấu hình pilot, 3 luật dừng 4 vế, không còn dấu `?` ở các trường YAML và vượt qua kiểm tra `yaml.safe_load`.
- `report/team/bang_loi.md`: Ghi nhận đối chiếu giữa bộ nhãn TV 3 và TV 4 (18/20 = 90%).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI hỗ trợ kiểm tra cú pháp YAML, đối chiếu công thức cỡ mẫu cụm và rà soát checklist theo `RUBRIC.md` / `CHECKPOINTS.md`.
- **Cách tự kiểm tra và kiểm chứng:**
  - Tự chạy script Python kiểm tra trực tiếp trên `src/logix_requests.csv` để xác nhận tỉ lệ `mo_lai_trong_7_ngay` (51/1.200 = 4,25% và 39/982 = 3,97%), tỉ lệ phạm vi pilot (`982/1.200 = 81,83%`) và số ngày tối thiểu để đạt `m >= 299`.
  - Chạy lại phép giải tay phương trình `20m / (1 + (m - 1) × 0,02) >= 859` (ra `m >= 298,5 -> 299`) và kiểm tra tính hợp lệ của `report/team/pilot_plan.yaml` bằng `yaml.safe_load`.
  - Dùng lệnh kiểm tra tự động xác nhận không còn dấu `?` trong các trường YAML, không dùng `"cả đội"` và không xuất hiện từ cấm.

## 6. Tự đánh giá

- **Mức độ hoàn thành:** Hoàn thành 100% nhiệm vụ của TV 3 (Nhiệm vụ C phần gắn nhãn độc lập và toàn bộ Nhiệm vụ D) đúng chuẩn rubric 15/15 điểm cho `pilot_plan.yaml` và 10/10 điểm cho phần đồng thuận `bang_loi.md`, sẵn sàng bảo vệ phần thiết kế thử nghiệm trước hội đồng Gate 2a.
