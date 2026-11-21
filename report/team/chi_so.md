# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200); trong phạm vi `noi_dia` + `hang_nang` là **92,26%** (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | Chỉ số trong đợt chạy thử là **27,12%** (48/177); trong phạm vi `noi_dia` + `hang_nang` là **21,09%** (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200); trong phạm vi `noi_dia` + `hang_nang` là **3,97%** (39/982) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ áp dụng trợ lý ở nhóm can thiệp & thời gian xem lại thực tế trung bình | Số lượt hiện gợi ý trên số yêu cầu của nhóm can thiệp (`agent_suggestion_shown / refund_request_created (arm=treatment)`); `mean(phut_xem_lai_thuc_te)` từ `staff_review_decision` (kiểm tra ngưỡng hoà vốn ≤ 4,8–5,1 phút) | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm toán mẫu hằng tuần & số ca lệch sổ cái/hoàn trùng | `audit_sample_checked (lech_vnd != 0) / 100 đơn/tuần` (ngưỡng ≤ 1%, bắt lỗi ngầm ca 5, 17); đối soát `ticket_closed` vs `refund_ledger_write` (ngưỡng 0 ca, bắt ca 7, 20) | Không cần tính |

> **Lưu ý:** Chỉ viết *"chỉ số trong đợt chạy thử là 82,83%"*, tuyệt đối không viết *"trợ lý đã nâng chỉ số từ 0,70"* vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

11 event đều mang `trace_id` để nối xuyên suốt với trace của agent và dữ liệu nghiệp vụ.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / CSKH | `request_id, loai, depot, staff_id, arm, so_tien_vnd, trace_id` | Khi tạo yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id, error_code, raw_input_type, trace_id` | Khi đầu vào sai định dạng (bắt ca 9) |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, price_table_version, trace_id` | Sau mỗi lần chạy, kể cả khi lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id, so_tien_de_xuat, policy_ref, trace_id` | Khi gợi ý của trợ lý hiện lên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai_thuc_te, trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id, phut_lam_lai_thuc_te, ly_do, trace_id` | Khi nhân viên làm lại xong ca trợ lý trả sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien_vnd, ket_qua (ok/loi), trace_id` | Khi ghi nhận lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason, tom_tat, loai, trace_id` | Khi agent dừng và chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, dong_trong_24h, ket_qua_cuoi, trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách hàng / CSKH | `reopened_at, reason, mo_lai_trong_7_ngay, trace_id` | Khi yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `sample_week, so_tien_da_hoan, so_tien_dung, lech_vnd, trace_id` | Hằng tuần trên mẫu ngẫu nhiên 100 đơn |

**Kiểm tra chéo:** Cả 5 chỉ số ở bảng E1 và chi phí thực tế đều đo được đầy đủ 100% từ danh sách event trên qua `trace_id`:

- **Chỉ số chính (`dong_trong_24h_khong_mo_lai_7_ngay`):** Tính bằng `refund_request_created` (chia theo `arm`) nối qua `trace_id` với `ticket_closed` (`dong_trong_24h == 1`) và kiểm tra không có `ticket_reopened` trong 7 ngày (`mo_lai_trong_7_ngay == 0`).
- **Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`):** Tính bằng `staff_review_decision` (`quyet_dinh` in `['sua', 'bo']`) chia cho tổng số `agent_suggestion_shown` có phát sinh review.
- **Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách`):** Tính bằng số lượng `ticket_reopened` (trong vòng 7 ngày) chia cho tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất (Tỉ lệ áp dụng & phút xem lại thực tế):** Tính từ `agent_suggestion_shown` / `refund_request_created (arm=treatment)` và `mean(phut_xem_lai_thuc_te)` trong `staff_review_decision`.
- **Chỉ số an toàn tự đề xuất (Kiểm toán mẫu & đối soát sổ cái):** Tính từ `audit_sample_checked` (`lech_vnd != 0`) và đối soát mỗi giờ giữa `ticket_closed` với `refund_ledger_write` (`ket_qua == ok`, duy nhất `idempotency_key`).
- **Chi phí mỗi việc thành công (đo thật thay thế `simulated`):** Tính từ `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`), `staff_review_decision` (`phut_xem_lai_thuc_te`), `staff_rework_completed` (`phut_lam_lai_thuc_te`) nối qua `trace_id` với `ticket_closed`.

## E2 · Rủi ro kinh tế

Số liệu tác động lấy trực tiếp từ bảng độ nhạy (`report/team/bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** `[simulated]` | Tỉ lệ ca làm lại theo tuần > **7%** (đợt chạy thử trong phạm vi là 4,89%, 48/982 ca) | Thu hẹp phạm vi về chỉ còn `noi_dia`, rà soát ngay 20 trace `staff_rework_completed` để vá lỗi nghiệp vụ | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài hoặc tỉ lệ xem lại tăng gấp đôi | Tỉ lệ xem lại ×2 tăng **+40,7%** lên **6.292 đ** `[simulated]`; xem lại 100% đẩy CPS lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.414 đ = 1,03×** (15,3 phút làm lại) `[simulated]`, triệt tiêu tiết kiệm | Tỉ lệ yêu cầu được xem lại vẫn **> 50%** vào cuối bước rollout `0.25` hoặc thời gian xem lại trung bình **> 4,8 phút/ca** | Áp dụng giảm tỉ lệ xem lại theo bậc xuống lấy mẫu khi tỉ lệ `sua + bo < 15%` và tối ưu giao diện duyệt để hạ thời gian xem lại dưới 4,8 phút | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn dự kiến làm đội chi phí cố định 40 triệu đ/tháng | Ở 45.000 YC/tháng cố định = +1.185 đ/việc (tổng CPS 4.599 đ = 0,38×); giảm một nửa còn +2.370 đ/việc (5.784 đ = 0,48×); nếu **< 4.659 việc thành công/tháng** tổng CPS vượt 12.000 đ `[simulated]` | Số việc thành công theo tuần **< 50%** kế hoạch hoặc khối lượng dưới 1.165 việc/tuần | Không mở rộng pilot, rà soát nguyên nhân nghẽn mở trợ lý hoặc đàm phán lại chi phí hạ tầng cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% hoặc cấu hình sai giới hạn chạy lại | Lương tăng 25% làm CPS tăng **+23,1%** lên **5.506 đ** `[simulated]`; cấu hình giới hạn 1 lần chạy đẩy thêm 85 việc sang nhân viên làm tổng chi phí cả hệ thống tăng thêm **+548.561 đ** lên **7.449.781 đ** (so với 6.901.220 đ ở giới hạn 2 lần) `[simulated]` | Tham số `max_attempts != 2` hoặc chi phí nhân công thực tế/giờ vượt giả định 2.000 đ/phút | Khoá cứng tham số giới hạn **2 lần chạy** trong cấu hình agent, kiểm soát thời gian xem lại/làm lại qua event thực tế | Kỹ sư trưởng agent |
