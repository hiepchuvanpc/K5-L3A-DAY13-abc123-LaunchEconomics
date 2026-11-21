# Team

## Thông tin nhóm

- Tên nhóm: `abc123`
- Lớp: `L3A` (K5-L3A)
- Repo nhóm: `K5-L3A-DAY13-abc123-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/hiepchuvanpc/K5-L3A-DAY13-abc123-LaunchEconomics` 

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |  |  |  |  | Người viết code (TV 1 · Tech Lead) |
|   2 | Nguyễn Quang Vũ | 2A202603407 | nguyenquangvu755@gmail.com | NguyenVu8888 | Người kiểm số (TV 2 · QC & Analyst) |
|   3 | Dương Tuấn Hưng | 2A202603416 | duongtuanhung2711@gmail.com | hunglun2711 | Người gắn nhãn 1 & Pilot (TV 3 · Pilot Lead) |
|   4 | Nguyễn Ngọc Minh Đức | 2A202603421 | nguyenngocminhduc2005@gmail.com | MinDuck512 | Người gắn nhãn 2 & Giữ hồ sơ (TV 4 · Launch Lead) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md` (giữ nguyên file mẫu `report/team/MSSV_HoTen.md`).

### TV1-

#### Phần việc phụ trách

- Người viết code (TV 1 · Tech Lead): triển khai mô hình tính toán `src/lab13.py`, dựng `KE_HOACH_NHOM.md` và quản lý repo nhóm.

#### Đóng góp cụ thể

- Hoàn thiện các hàm A1 (3 phép thử đáp án biết trước 1,20 · 1,25 · 1,25), mô hình chi phí A2/A3, độ nhạy 9 kịch bản B1–B4 và hàm tính cỡ mẫu cụm D1 trong `src/lab13.py`.
- Đóng gói kế hoạch phân công nhóm theo mô hình Git Zero Conflict trong `KE_HOACH_NHOM.md`.

#### Bằng chứng

- File `src/lab13.py` và `KE_HOACH_NHOM.md` (commit `a51c193`).
- *(Cần TV 1 bổ sung Họ tên, MSSV và tạo file báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`)*.

### NguyenQuangVu-2A202603407

#### Phần việc phụ trách

- Người kiểm số (TV 2 · QC & Analyst): thẩm định và điền toàn bộ Nhiệm vụ A (A1–A4) và B (B1–B4) trong `report/team/bang_chi_phi.md`.

#### Đóng góp cụ thể

- Đối chiếu độc lập kết quả `src/lab13.py`, bóc tách CPS = 4.472 đ `[simulated]` (gấp 16,3× hoá đơn 274,7 đ; giờ người chiếm 92,5%), luận chứng loại bỏ `quoc_te` (1,88×) và `doi_tac` (0,85×), tính chi phí cố định A4 (ngưỡng hoà vốn 4.659 việc/tháng).
- Thực hiện phân tích độ nhạy B1–B4, chứng minh giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ `[simulated]`) và chỉ ra rủi ro xem lại 100% (11.743–12.414 đ `[simulated]`).

#### Bằng chứng

- File `report/team/bang_chi_phi.md`, `report/team/2A202603407_NguyenQuangVu.md`, `DraftOfMe.md`, `AI_CONTEXT.md` (commit `cf09175`, PR #1 `3db555c`).

### DuongTuanHung-2A202603416

#### Phần việc phụ trách

- Người gắn nhãn 1 & Pilot (TV 3 · Pilot Lead): gắn nhãn độc lập 20 ca lỗi (CP3) và xây dựng toàn bộ kế hoạch thử nghiệm `report/team/pilot_plan.yaml` (CP4).

#### Đóng góp cụ thể

- Tự gắn nhãn độc lập 20 ca lỗi Google PAIR vào `nhan_tv3.txt` (không trao đổi trước khi so), đối chiếu đạt đồng thuận 18/20 = 90% và thống nhất 20/20 ca cùng TV 4.
- Tính và giải thích đủ 5 bài toán cỡ mẫu cụm D1 (chỉ ra 40 nhân viên không đủ cho MDE 5 điểm ở cụm nhân viên/depot), trả lời 5 câu tách tác động D2, phân tích tỉ lệ mở lại hiện tại (4,25% toàn mẫu; 3,97% phạm vi pilot) và hoàn thiện `report/team/pilot_plan.yaml` không còn dấu `?`, đủ 3 luật dừng 4 vế, hợp lệ `yaml.safe_load`.

#### Bằng chứng

- File `nhan_tv3.txt`, `report/team/pilot_plan.yaml`, `report/team/2A202603416_DuongTuanHung.md`.

### NguyenNgocMinhDuc-2A202603421

#### Phần việc phụ trách

- Người gắn nhãn 2 & Giữ hồ sơ (TV 4 · Launch Lead): gắn nhãn độc lập 20 ca lỗi (CP3), hoàn thiện `bang_loi.md`, `chi_so.md`, `ho_so_launch_v0.md` (CP5), `TEAM.md`, `group_report.md` và chuẩn bị `phieu_cham.md`.

#### Đóng góp cụ thể

- Tự gắn nhãn độc lập 20 ca lỗi Google PAIR vào `nhan_tv4.txt`, phối hợp TV 3 đối chiếu đạt 90% đồng thuận và hoàn thiện `report/team/bang_loi.md` với bảng khắc phục 5 ca đo được theo từng vai trò phụ trách.
- Tính thử các chỉ số E1 trên 1.200 yêu cầu (82,83% · 27,12% · 4,25%), thiết kế 11 event có `trace_id`, ma trận kiểm tra chéo và 4 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
- Tổng hợp bộ hồ sơ 1 trang `report/team/ho_so_launch_v0.md` với đề xuất **Go có điều kiện** kèm 5 điều kiện tiên quyết, cập nhật `TEAM.md`, `report/team/group_report.md` và chuẩn bị khung `report/team/phieu_cham.md`.

#### Bằng chứng

- File `nhan_tv4.txt`, `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603421_NguyenNgocMinhDuc.md`.
