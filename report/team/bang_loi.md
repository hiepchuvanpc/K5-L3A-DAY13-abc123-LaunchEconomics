# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Dương Tuấn Hưng (TV 3) · Người gắn nhãn 2: Nguyễn Ngọc Minh Đức (TV 4) (gắn độc lập trong 8 phút, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (đạt ngưỡng ≥ 80%).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu (tỉ lệ đồng thuận đạt 90% ≥ 80%, bổ sung thêm nguyên tắc đối chiếu nhanh cho các ca dễ nhầm).

- **Ca 9 (Thống nhất: Do người dùng):** Gắn nhãn theo nguyên nhân gốc là khách nhập sai định dạng (mã đơn sàn TMĐT thay vì mã vận đơn); việc trợ lý chưa có bước gợi ý nằm ở cột khắc phục chứ không đổi nhãn gốc thành Hệ thống.
- **Ca 13 (Thống nhất: Giới hạn hệ thống):** Bảo hiểm hàng hoá của công ty đối tác nằm ngoài phạm vi năng lực trợ lý nên gốc lỗi là Giới hạn hệ thống, dù cách trợ lý trả lời chung chung về giới hạn này còn kém (việc cải thiện thông báo từ chối nằm ở khâu khắc phục).
- **Nguyên tắc đối chiếu nhanh cho các ca dễ nhầm khác:** Ca 6 thuộc *Do người dùng* vì gốc lỗi do khách chọn sai mục "Hoàn phí giao trễ"; Ca 8 và 15 thuộc *Hệ thống* vì sai sót đã lộ ra cho người thấy, khác với *Ngầm* (Ca 5, 12, 17) chỉ phát hiện qua kiểm tra mẫu hoặc chi phí; Ca 18 thuộc *Ngữ cảnh* vì số tiền tính đúng chính sách nhưng giả định khách tự hiểu cách tính không khớp thực tế.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`); cảnh báo hằng ngày khi vượt **2%** tổng yêu cầu/ngày | Tự nhận diện định dạng mã sàn TMĐT và tra sang mã vận đơn LogiX; không tra được thì hiển thị hướng dẫn tìm mã kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa `ticket_closed` (tin "đã hoàn") và `refund_ledger_write` (`ket_qua = ok`, kiểm tra `idempotency_key` khớp `trace_id`), ngưỡng cảnh báo **> 0 ca** (đồng thời bắt lỗi hoàn trùng ca 20) | Chỉ phát tin nhắn "đã hoàn" khi sổ cái trả `ok` kèm `idempotency_key` duy nhất; nếu API trả lỗi 503 sau tối đa 2 lần chạy thì báo "đang xử lý" và phát `handoff_to_staff` chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` có lý do khiếu nại số tiền nhưng đối chiếu hệ thống thấy tính đúng chính sách; cảnh báo khi vượt **1%** số yêu cầu đã đóng/tuần | Chuẩn hoá mẫu tin nhắn luôn hiển thị rõ công thức tính tiền (ví dụ: `30.000 đ × 50% = 15.000 đ`) và điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi hằng ngày tỉ lệ event `handoff_to_staff` với `reason = thieu_du_lieu` theo cột `loai`; cảnh báo khi vượt **5%** trên các nhóm trong phạm vi pilot | Giữ cơ chế chuyển nhân viên kèm tóm tắt đầy đủ; loại toàn bộ `quoc_te` (thành công 27,3%, CPS 22.515 đ = 1,88× `[simulated]`) và `doi_tac` khỏi phạm vi pilot, định tuyến thẳng về nhân viên | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu ngẫu nhiên **100 đơn/tuần** so với bảng giá hiện hành; ngưỡng cảnh báo **> 1%** đơn lệch tiền (cũng bắt lỗi ngầm ca 5) | Tự động xoá bộ nhớ đệm (cache invalidation) ngay khi cập nhật bảng giá mới và ghi bắt buộc `price_table_version` vào trace `agent_run_completed` | Kế toán trưởng |
