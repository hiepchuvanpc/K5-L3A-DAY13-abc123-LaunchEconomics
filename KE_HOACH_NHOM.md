# 🚀 KẾ HOẠCH HÀNH ĐỘNG & PHÂN CÔNG CÔNG VIỆC NHÓM 4 NGƯỜI
## Lab 13 · Launch Economics & Kế hoạch Pilot (Gate 2a)

---

## 📌 QUY ĐỊNH MỚI TỪ UPSTREAM (BẮT BUỘC ĐỌC)

1. **Cấu trúc thư mục chuẩn (`skeleton-lab`):**
   - Toàn bộ code tính toán nằm trong `src/lab13.py` (chạy tại thư mục `src/`).
   - Toàn bộ 6 file hồ sơ nhóm nằm trong `report/team/`.
   - Thông tin nhóm ghi trong `TEAM.md` ở root. Báo cáo nhóm ngắn ở `report/team/group_report.md`.
2. **Báo cáo cá nhân bắt buộc:**
   - Mỗi thành viên nhân bản file mẫu `report/team/MSSV_HoTen.md` thành `<MSSV>_<HoTen>.md` (ví dụ `report/team/20211234_ChuVanHiep.md`) để tự đánh giá và mô tả công cụ AI đã dùng.
3. **Mốc thời gian & Deadline:**
   - **17:00:** Chốt file `report/team/ho_so_launch_v0.md` để gửi nhóm bạn duyệt chéo Gate 2a tại lớp.
   - **17:45 – 18:00:** Commit và push bản làm việc tại lớp lên GitHub.
   - **23h59 GMT+7:** Hạn chót chính thức nộp bài trên LMS (**Tất cả 4 thành viên đều phải tự đăng nhập tài khoản cá nhân và dán cùng link repo nhóm**).
4. **Quy ước tên repo:** `K5-L3A-DAY13-TenNhom-LaunchEconomics` (hoặc `L3B`).

---

## 👥 1. PHÂN VAI & PHÂN CHIA QUYỀN SỞ HỮU FILE (GIT ZERO CONFLICT)

Để không ai bị đụng code hay xung đột merge trên Git, **mỗi file chỉ ĐÚNG 1 người có quyền commit**:

| Thành viên | Vai trò trong `TEAM.md` | Branch Git | File phụ trách độc quyền (Chỉ người này sửa & commit) |
| :--- | :--- | :--- | :--- |
| **TV 1 (Tech Lead)** | **Người viết code** | `feat/code-model` | `src/lab13.py`, `.gitignore` |
| **TV 2 (QC & Analyst)** | **Người kiểm số** | `feat/bang-chi-phi` | `report/team/bang_chi_phi.md` |
| **TV 3 (Pilot Lead)** | **Người gắn nhãn 1 & Pilot** | `feat/pilot-plan` | `report/team/pilot_plan.yaml`, `nhan_tv3.txt` *(file nháp gắn nhãn)* |
| **TV 4 (Launch Lead)** | **Người gắn nhãn 2 & Giữ hồ sơ** | `feat/launch-dossier` | `report/team/ho_so_launch_v0.md`, `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/phieu_cham.md`, `TEAM.md`, `report/team/group_report.md` |
| **Cả 4 bạn** | Thành viên nhóm | *(Nhánh riêng)* | Mỗi người tự tạo file cá nhân: `report/team/<MSSV>_<HoTen>.md` |

---

## ⏱️ 2. LỘ TRÌNH TRIỂN KHAI THEO 5 CHECKPOINT (CP1 – CP5)

### 📍 CP1 (14:00 – 14:53): Nhiệm vụ A — Mô hình chi phí mỗi việc thành công
*Mục tiêu: Tính chi phí thật cho mỗi yêu cầu và chứng minh nó gấp 16,3 lần hoá đơn token.*
- **TV 1 (Đã hoàn thành):** 
  - Code `src/lab13.py` đã vượt qua 3 test A1 (1,20 · 1,25 · 1,25).
  - Đã tính ra CPS = **4.472 đ** `[simulated]` (gấp 16,3 lần hoá đơn 275 đ).
  - Phân tích xong 4 loại đơn: `noi_dia` (2.696 đ = 0,22×), `hang_nang` (8.221 đ = 0,69×), `quoc_te` (22.515 đ = 1,88×), `doi_tac` (10.215 đ = 0,85×).
- **TV 2:** Mở `report/team/bang_chi_phi.md`, điền bảng A2, A3 từ output của TV 1. Nêu rõ kết luận loại `quoc_te` và `doi_tac` ra khỏi pilot.
- **TV 4:** Mở `report/team/ho_so_launch_v0.md`, điền trước Mục 1 và Mục 3. Điền thông tin nhóm vào `TEAM.md`.

---

### 📍 CP2 (14:53 – 15:20): Nhiệm vụ B — Bảng độ nhạy (Sensitivity Analysis)
*Mục tiêu: Tìm ra yếu tố nhạy nhất và chứng minh tối ưu toàn hệ thống.*
- **TV 1 (Đã hoàn thành):** Đã chạy 9 kịch bản B1, kịch bản đổi cặp B2, chi phí cả hệ thống B3 và kịch bản xem lại 100% B4.
- **TV 2:** Điền bảng B1, B2, B3, B4 vào `report/team/bang_chi_phi.md`:
  - **Xếp hạng 3 yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8%) > 2. Tỉ lệ xem lại (+40,7%) > 3. Lương nhân viên (+23,1%). (Giá token chỉ biến động $\pm 5,6\%$).
  - **Trả lời B3:** Giới hạn 2 lần chạy là rẻ nhất cho toàn công ty (**6.901.220 đ**), dù 1 lần chạy có CPS thấp hơn nhưng đẩy 85 việc sang người làm.
  - **Trả lời B4:** Xem lại 100% thì CPS = **11.743 đ = 0,98×** $\rightarrow$ Hầu như không tiết kiệm vì tiền xem lại chiếm 90% chi phí.
- **TV 4:** Đưa 2 rủi ro tài chính lớn nhất từ bảng độ nhạy vào Risk Register của `report/team/chi_so.md` và `ho_so_launch_v0.md`.

☕ *15:20 – 15:35: Giải lao (15 phút)*

---

### 📍 CP3 (15:35 – 16:08): Nhiệm vụ C — Bảng lỗi Google PAIR (20 ca lỗi)
*Quy tắc liêm chính: Hai người ngồi tách nhau, gắn nhãn độc lập 8 phút, tuyệt đối không bàn trước!*
- **15:35 – 15:43 (8 phút):**
  - **TV 3** tạo file `nhan_tv3.txt`, tự gán 20 ca lỗi vào 5 loại: *Người dùng (ND), Hệ thống (HT), Ngữ cảnh (NC), Giới hạn (GH), Ngầm (NG)*.
  - **TV 4** tự gán 20 ca lỗi của mình vào `nhan_tv4.txt`.
  - *(TV 1 & TV 2 hỗ trợ kiểm tra lại bảng chi phí và chuẩn bị công thức D1).*
- **15:43 – 15:48 (5 phút):** TV 3 và TV 4 so sánh nhãn. Mục tiêu: Đồng thuận $\ge 80\%$ (16/20 ca).
  - *Bộ nhãn chuẩn tham khảo:* ND (1, 6, 9, 14); HT (2, 7, 8, 15, 20); NC (3, 10, 16, 18); GH (4, 11, 13, 19); NG (5, 12, 17).
- **15:48 – 16:05 (17 phút):** TV 4 mở `report/team/bang_loi.md`, điền 2 bộ nhãn, tỷ lệ đồng thuận và **bảng khắc phục 5 ca** (ca 9: User, ca 7: System, ca 18: Context, ca 4: Boundary, ca 17: Silent).
  - *Lưu ý quan trọng:* Mỗi dòng phải có **cách phát hiện đo được** (event, ngưỡng) và **1 vai trò phụ trách cụ thể** (*PM trợ lý, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng* — cấm ghi "cả đội").

---

### 📍 CP4 (16:08 – 16:36): Nhiệm vụ D — Kế hoạch Pilot (`pilot_plan.yaml`)
*Mục tiêu: Bản kế hoạch pilot tách được tác động, đủ cỡ mẫu và có luật dừng viết trước.*
- **TV 1 & TV 2:** Cung cấp kết quả 5 bài toán cỡ mẫu D1 cho TV 3:
  - $a.$ Theo yêu cầu: $1.251$ YC/nhóm.
  - $b.$ Theo nhân viên ($m=75$): Cần $3.103$ YC $\rightarrow$ $42$ người/nhóm ($84 > 40$: Không đủ người).
  - $c.$ 20 nhân viên/nhóm: Trần hiệu dụng $< 1.000 < 1.251$ (Không đạt MDE 5 điểm).
  - $d.$ 6 depot/nhóm: Trần $< 300$ (Quá thấp, loại).
  - $e.$ Chấp nhận MDE 6 điểm: 20 nhân viên cần $m \ge \mathbf{299}$ YC/người ($DE = 6,96$).
- **TV 3:** Mở `report/team/pilot_plan.yaml`:
  - Ghi lời giải D1 và 5 câu "tách được tác động" D2 vào phần comment `#` đầu file.
  - Xóa sạch mọi dấu `?` trong file.
  - Điền **3 luật dừng chuẩn 4 vế**: `NẾU ... TRONG ... THÌ ... KHÔNG THÌ ...` (An toàn: mở lại > 2 điểm hoặc > 6%; Chi phí: > 8.000 đ; Mức dùng: bỏ qua gợi ý > 40%).
  - Kiểm tra cú pháp: `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml')); print('YAML chuẩn!')"`.

---

### 📍 CP5 (16:36 – 18:00): Nhiệm vụ E — Hồ sơ Launch v0 & Duyệt chéo Gate 2a
- **16:36 – 17:00:**
  - **TV 4** hoàn tất `report/team/chi_so.md` (10 event có `trace_id` + ma trận kiểm tra chéo) và `report/team/ho_so_launch_v0.md` (đúng 1 trang A4, gồm 7 mục + Đề xuất: **Go có điều kiện** kèm 5 điều kiện tiên quyết).
  - Cả nhóm rà soát checklist: `grep -rni "production" report/team` (không được xuất hiện từ này!).
- **17:00 – 17:10:** Gửi `ho_so_launch_v0.md` cho nhóm hội đồng (nhóm $n$ gửi nhóm $n+1$).
- **17:10 – 17:25:** Nhận hồ sơ nhóm bạn, TV 4 và TV 2 cùng đọc và chấm điểm vào `report/team/phieu_cham.md`. Chuẩn bị 1 câu hỏi phản biện sắc bén (ví dụ: *"Nếu tuần đầu xem lại 100% thì chi phí có rẻ hơn người tự làm không?"*).
- **17:25 – 17:40:** Bảo vệ chéo tại lớp (TV 4 thuyết trình 1 phút, TV 1/TV 3 phản biện 1 phút, TV 2 đọc điểm chấm 1 phút).
- **17:45 – 18:00:** Commit và push toàn bộ bài làm tại lớp lên GitHub.

---

### 📍 18:00 – 23:59: Hoàn thiện hồ sơ & Nộp LMS
1. **TV 4:** Viết tóm tắt vào `report/team/group_report.md` (tối đa 2 trang, tóm tắt giải pháp, khó khăn, đề xuất cuối).
2. **Mỗi thành viên (TV 1, 2, 3, 4):**
   - Nhân bản file mẫu `report/team/MSSV_HoTen.md` thành `<MSSV>_<HoTen>.md` (ví dụ `report/team/20211234_ChuVanHiep.md`).
   - Điền thông tin cá nhân, vai trò, đóng góp cụ thể và công cụ AI đã dùng.
3. **Commit & Push chốt:**
   ```bash
   git add .
   git commit -m "docs: finalize Day 13 lab submission report and personal reflections"
   git push origin main
   ```
4. **Nộp bài lên LMS:** **Tất cả 4 thành viên đều phải tự đăng nhập LMS và dán cùng đường link repo GitHub của nhóm trước 23h59!**

---

## 🎯 3. BẢNG SỐ LIỆU CHUẨN ĐỂ ĐIỀN BÁO CÁO (CHEAT SHEET)

*(Trích xuất trực tiếp từ code `src/lab13.py` đã chạy thành công 100%)*

- **A2 - Chi phí gốc:**
  - Token: `245.585 đ` | Tool: `84.000 đ` | Attempt > 1: `93.804 đ` *(đo từ trace)*.
  - Xem lại: `1.780.000 đ` `[simulated]` | Làm lại: `2.264.000 đ` `[simulated]`.
  - Tổng CPS: **4.472 đ** `[simulated]` (Thành công 978 ca). Gấp **16,3 lần** hoá đơn token+tool (274,7 đ).
- **A3 - Tách loại đơn:**
  - `noi_dia`: 2.696 đ (0,22×) | `hang_nang`: 8.221 đ (0,69×) $\rightarrow$ *Giữ trong pilot*.
  - `quoc_te`: 22.515 đ (1,88×) | `doi_tac`: 10.215 đ (0,85×) $\rightarrow$ *Loại khỏi pilot*.
- **B1 & B2 - Độ nhạy:**
  - Làm lại gấp đôi: **+51,8%** (6.787 đ) | Xem lại gấp đôi: **+40,7%** (6.292 đ).
  - Lương +25%: **+23,1%** (5.506 đ) | Token gấp đôi: **+5,6%** (4.723 đ).
  - Token x2 + Xem lại x2: **+46,3%** (6.543 đ) `[simulated]`.
- **B3 - Tối ưu hệ thống:** Giới hạn **2 lần chạy** rẻ nhất (6.901.220 đ).
- **B4 - Xem lại 100%:** **11.743 đ = 0,98×** (không có lợi ích kinh tế).
- **D1 - Cỡ mẫu:** 20 nhân viên mỗi nhóm, $m \ge \mathbf{299}$ YC/người, $DE = 6,96$, MDE 6 điểm (n hiệu dụng 859).

---

## ⚠️ 4. CHECKLIST SỐNG CÒN THEO RUBRIC (100 ĐIỂM)

- [ ] **Nhãn `simulated`:** Mọi con số bắt nguồn từ `phut_xem_lai` và `phut_lam_lai` đều có nhãn `simulated` (hoặc `[sim]`).
- [ ] **Không có chữ "production":** Gate 2a chỉ duyệt kế hoạch pilot, tuyệt đối không dùng từ "production".
- [ ] **Không ghi người phụ trách là "cả đội":** Phải ghi vai trò cụ thể có thẩm quyền (*PM trợ lý, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng, Giám đốc vận hành*).
- [ ] **Luật dừng đủ 4 vế:** `NẾU ... TRONG ... THÌ ... KHÔNG THÌ ...`.
- [ ] **File cá nhân:** Cả 4 thành viên đều đã tạo file `report/team/<MSSV>_<HoTen>.md` của riêng mình.
- [ ] **Tất cả 4 thành viên** đều nộp link repo lên LMS trước 23h59.
