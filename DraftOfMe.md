# CẨM NANG DỰNG DỰ ÁN TỪ CON SỐ 0 & NHẬT KÝ THỰC THI (DRAFTOFME)
**Dự án:** Lab 13 · Launch Economics & Kế hoạch Pilot (Gate 2a) — LogiX-VN  
**Vai trò đảm nhiệm:** Thành viên 2 (QC & Analyst) — *Người kiểm số*  
**Nhánh Git:** `feat/bang-chi-phi`  
**File độc quyền phụ trách:** `report/team/bang_chi_phi.md`

---

## PHẦN 1: KIẾN TRÚC TỔNG THỂ & GIẢ LẬP DỰNG MỚI TỪ CON SỐ 0 (FROM-SCRATCH BLUEPRINT)

### 1. Bức tranh toàn cảnh (End-to-End Lifecycle)

Dự án này là một bài toán **Kinh tế học Triển khai Agent (Launch Economics)** trong bối cảnh doanh nghiệp logistics thực tế (**LogiX-VN**: 12 depot, 40 nhân sự CSKH, 45.000 yêu cầu hoàn phí/tháng). Dự án thẩm định xem việc đưa AI Agent vào thay thế/hỗ trợ người có thực sự tiết kiệm chi phí không trước khi bước qua cánh cổng **Gate 2a (Phê duyệt Pilot)**.

Luồng vận hành từ đầu đến cuối (Lifecycle) diễn ra như sau:

```
[Dữ liệu thô (Trace Logs & Nghiệp vụ)]
   ├── src/logix_runs.csv (1.624 lần chạy của Agent: tokens_in, tokens_out, tool_calls, status ok/loi)
   └── src/logix_requests.csv (1.200 yêu cầu hoàn phí: loại đơn, số phút xem lại, số phút làm lại, kết quả)
            │
            ▼
[Tầng tính toán & Mô hình hóa tài chính - Entry Point: src/lab13.py (TV 1 phụ trách)]
   ├── 1. Kiểm thử tiên nghiệm (A1): Kiểm tra 3 công thức xác suất lý thuyết (p=0.8, k=2,3,None)
   ├── 2. Mô hình chi phí thực (A2): Tính Cost Per Success (CPS), bóc tách token, tool, giờ người (xem lại + làm lại)
   ├── 3. Phân khúc nghiệp vụ (A3): Đánh giá 4 loại đơn (noi_dia, hang_nang, quoc_te, doi_tac)
   ├── 4. Phân tích độ nhạy (B1, B2, B3, B4): Biến thiên giá token, tỷ lệ review/rework, chi phí toàn hệ thống
   └── 5. Thống kê thử nghiệm Pilot (D1): Cỡ mẫu hai tỷ lệ, hiệu ứng cụm (Cluster Randomization, ICC, Design Effect)
            │
            ▼
[Tầng Phân tích & Báo cáo độc quyền của TV 2: report/team/bang_chi_phi.md (Integration Point)]
   ├── Khớp nối mọi con số từ src/lab13.py và đối chiếu tính tay độc lập (QC)
   ├── Bóc tách sự thật trần trụi: CPS (4.472 đ) gấp 16,3 lần hóa đơn token (275 đ) do chi phí con người
   ├── Đưa ra khuyến nghị cắt giảm phạm vi (Loại bỏ `quoc_te` và `doi_tac` khỏi Pilot)
   └── Chứng minh giới hạn 2 lần chạy là tối ưu chi phí toàn hệ thống (rẻ nhất cho công ty)
            │
            ▼
[Tầng Tổng hợp Hồ sơ Gate 2a (TV 3 & TV 4)]
   ├── TV 3: Thiết kế kế hoạch thử nghiệm pilot_plan.yaml dựa trên số cỡ mẫu D1 và phạm vi từ Bảng chi phí
   └── TV 4: Tổng hợp hồ sơ ho_so_launch_v0.md, chi_so.md, bang_loi.md để bảo vệ trước Hội đồng chấm chéo
```

---

### 2. Lộ trình giả lập dựng mới từ thư mục trống (From-Scratch Blueprint)

Nếu bạn đứng trước một thư mục trống rỗng và phải tự tay dựng nên toàn bộ hệ thống này, thứ tự tư duy kiến trúc và tạo file sẽ như sau:

#### Bước 1: Khởi tạo Cấu trúc thư mục & Quản lý Phụ thuộc
- Tạo cấu trúc phân tách rõ ràng giữa mã nguồn (`src/`), báo cáo/hồ sơ thẩm định (`report/team/`), và tài liệu đặc tả nghiệp vụ (`docs/`).
- Tạo `.gitignore` để loại bỏ rác môi trường ảo (`.venv/`, `__pycache__/`).
- Tạo `src/requirements.txt` với các thư viện tính toán: `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`.

#### Bước 2: Thiết kế & Khảo sát Mô hình Dữ liệu (Data Layer)
- Lưu trữ 2 file CSV phản ánh 2 góc nhìn của hệ thống:
  1. `src/logix_runs.csv`: Ghi vết tầng máy (Run-level trace) — đo lường tài nguyên tiêu hao (token vào/ra, tool call) của từng lần chạy (`attempt`).
  2. `src/logix_requests.csv`: Ghi vết tầng nghiệp vụ (Request-level) — đo lường kết quả cuối cùng đối với khách hàng và thời gian con người phải can thiệp (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`).
- *Tại sao tách làm 2 file?* Trong thực tế kiến trúc phân tán (Distributed Tracing), 1 Request của người dùng có thể kích hoạt nhiều Runs/Attempts của AI Agent nếu lần chạy đầu bị fail. Việc tách 1-N (One-to-Many) giữa `requests` và `runs` là chuẩn mực kiến trúc log trace.

#### Bước 3: Dựng Tầng Logic & Mô hình Toán kinh tế (`src/lab13.py`)
- Định nghĩa bảng giá tham số chuẩn (Token, Tool, Lương người/phút, Baseline khi người tự làm 100%).
- Viết các hàm toán lý thuyết (A1) làm "hàng rào kiểm thử" (Test-driven development - TDD): số lần chạy kỳ vọng, hệ số CPS lý thuyết.
- Viết engine cốt lõi `mo_hinh(runs, reqs, ...)` có khả năng nhận tham số linh hoạt để chạy quét ma trận độ nhạy (Sensitivity Grid Search).
- Quy tắc bất biến: Tử số cộng dồn mọi chi phí phát sinh; mẫu số chỉ chia cho số yêu cầu thực sự `thanh_cong`.

#### Bước 4: Xây dựng Tầng Báo cáo Thẩm định & QC (`report/team/bang_chi_phi.md`)
- Tạo các bảng biểu chuẩn hóa A1 -> A4 và B1 -> B4.
- Đính kèm nhãn `[simulated]` cho mọi con số phụ thuộc vào các biến giả lập.
- Viết phân tích định lượng (mỗi câu dưới 3 dòng, luôn đi kèm con số thực chứng) làm luận cứ kinh tế cho bản đề xuất Launch.

#### Bước 5: Hoàn thiện Bộ hồ sơ Gate 2a (`pilot_plan.yaml`, `ho_so_launch_v0.md`, ...)
- Dùng kết quả từ Bảng chi phí làm đầu vào để thiết kế cỡ mẫu Pilot, luật dừng (Stop rules), ma trận rủi ro và bản khuyến nghị Go/No-go có điều kiện.

---

### 3. Điểm ghép nối (Integration Point) của TV 2

Trong toàn bộ bức tranh trên, công việc của bạn (**TV 2 - Người kiểm số**) cắm vào mắt xích:
- **Đầu vào (Upstream):** 
  - Output từ script `src/lab13.py` (do TV 1 code).
  - Hai bộ log `src/logix_runs.csv` và `src/logix_requests.csv`.
  - Các tham số kinh tế chuẩn trong `docs/du_lieu_va_cong_thuc.md`.
- **Nhiệm vụ tại chỗ (In-place Processing):**
  - Chạy code, kiểm chứng tính độc lập (QC) từng phép tính.
  - Điền đầy đủ, chính xác các bảng A1, A2, A3, A4 và B1, B2, B3, B4 vào file `report/team/bang_chi_phi.md`.
  - Viết các phân tích, nhận định ngắn gọn (dưới 3 dòng, luôn có số thực chứng).
- **Đầu ra (Downstream):**
  - Cung cấp luận cứ loại bỏ 2 luồng `quoc_te` và `doi_tac` cho TV 3 thiết kế `pilot_plan.yaml`.
  - Cung cấp 2 rủi ro tài chính lớn nhất (Số ca làm lại và Tỷ lệ xem lại) cho TV 4 đưa vào Risk Register của `ho_so_launch_v0.md`.

---

## PHẦN 2: NHẬT KÝ TỪNG BƯỚC TRIỂN KHAI

### Bước 1: Nhiệm vụ A1 · Ba phép thử đáp án biết trước (Pre-flight Tests)
- **Mục tiêu:** Kiểm chứng 3 công thức xác suất cơ bản trong kinh tế học chạy lại (Retry Economics) với $p = 0,8$.
- **Kết quả:**
  - $E[N]$ tối đa 2 lần: `1,20`
  - $E[N]$ chạy đến khi đúng: `1,25`
  - Hệ số chi phí mỗi việc thành công tối đa 3 lần: `1,25`
- **Ý nghĩa:** Chứng minh rằng nếu chi phí mỗi lần chạy cố định, hệ số chi phí lý thuyết luôn bằng $1/p$.

### Bước 2: Nhiệm vụ A2 · Mô hình chi phí thực từ trace
- **Mục tiêu:** Bóc tách toàn bộ chi phí thực tế phát sinh trên 1.200 yêu cầu mẫu.
- **Kết quả:**
  - Token: 245.585 đ | Tool: 84.000 đ | Lần chạy 2 & 3: 93.804 đ.
  - Xem lại: 1.780.000 đ [simulated] | Làm lại: 2.264.000 đ [simulated].
  - Tổng chi phí: 4.373.585 đ [simulated] cho 978 việc thành công.
  - CPS = **4.472 đ** [simulated] so với Hóa đơn token+tool mỗi yêu cầu = **274,7 đ**.
- **Nghịch lý Launch Economics:** CPS thực tế gấp **16,3 lần** hóa đơn API máy móc! Khoản làm lại chiếm 51,8%, xem lại chiếm 40,7% $\rightarrow$ Giờ nhân viên chiếm **92,5%** tổng ngân sách.

### Bước 3: Nhiệm vụ A3 · Phân khúc theo loại yêu cầu
- **Mục tiêu:** Đánh giá hiệu quả kinh tế trên 4 nhóm nghiệp vụ.
- **Kết quả:**
  - `noi_dia`: 824 YC, thành công 95,0%, CPS = 2.696 đ = 0,22× (Rất tốt).
  - `hang_nang`: 158 YC, thành công 74,1%, CPS = 8.221 đ = 0,69× (Tốt).
  - `quoc_te`: 150 YC, thành công 27,3%, CPS = 22.515 đ = **1,88×** (Lỗ nặng, đắt hơn người tự làm 12.000 đ). Chạy lại không giúp vì xác suất đúng giảm mạnh (30% $\to$ 11,4% $\to$ 2,2%).
  - `doi_tac`: 68 YC, thành công 54,4%, CPS = 10.215 đ = 0,85× (Sát ngưỡng, rủi ro điều khoản).
- **Quyết định:** Thu hẹp phạm vi Pilot, chỉ giữ lại `noi_dia` và `hang_nang`.

### Bước 4: Nhiệm vụ A4 · Chi phí cố định và quy mô
- **Mục tiêu:** Đánh giá tác động của 40 triệu đ/tháng chi phí cố định (hạ tầng, bản quyền, duy trì).
- **Kết quả:**
  - Ở quy mô đầy đủ (45.000 YC/tháng): 33.750 việc thành công $\to$ Cố định = 1.185 đ/việc $\to$ Tổng CPS = 4.599 đ = 0,38×.
  - Ở một nửa khối lượng (22.500 YC/tháng): 16.875 việc thành công $\to$ Cố định = 2.370 đ/việc $\to$ Tổng CPS = 5.784 đ = 0,48×.
- **Ý nghĩa:** Chi phí cố định chỉ an toàn khi khối lượng đạt ngưỡng (trên 4.659 việc thành công/tháng).

### Bước 5: Nhiệm vụ B1 & B2 · Phân tích độ nhạy (Sensitivity Analysis)
- **Mục tiêu:** Xác định biến số nào gây rủi ro ngân sách lớn nhất.
- **Kết quả:**
  - Xếp hạng 3 yếu tố nhạy nhất: 
    1. Số ca làm lại (+51,8%)
    2. Tỷ lệ xem lại (+40,7%)
    3. Lương nhân viên (+23,1%)
  - Giá token chỉ ảnh hưởng $\pm 5,6\%$ (Gấp đôi hay giảm một nửa token không giải quyết được bài toán kinh tế).
  - Đổi cặp Token x2 + Xem lại x2 = 6.543 đ (+46,3%) [simulated] do cộng tuyến tính.

### Bước 6: Nhiệm vụ B3 · Tối ưu hóa chi phí toàn hệ thống
- **Mục tiêu:** Tìm giới hạn số lần chạy retry tối ưu cho doanh nghiệp.
- **Kết luận:** Giới hạn **2 lần chạy** là rẻ nhất cho toàn công ty (**6.901.220 đ** [simulated]). 
- **Cảnh báo bẫy tối ưu cục bộ:** Dù giới hạn 1 lần chạy có CPS thấp nhất (4.111 đ), nhưng lại đẩy 85 việc sang con người xử lý (với chi phí 12.000 đ/việc), làm tổn thất thêm hơn 548.000 đ cho toàn công ty.

### Bước 7: Nhiệm vụ B4 · Kịch bản xem lại 100% & Bài toán Pilot
- **Mục tiêu:** Thẩm định tính khả thi nếu áp dụng chính sách "con người duyệt lại 100% mọi kết quả AI".
- **Kết quả:** CPS khi xem lại 100% vọt lên **11.743 đ = 0,98×** (hoặc **12.414 đ = 1,03×** nếu làm lại mất 15,3 phút).
- **Bài học cốt lõi cho Pilot:** Xem lại 100% triệt tiêu hoàn toàn lợi nhuận của Agent. Giai đoạn Pilot phải tìm ra tỷ lệ xem lại lấy mẫu an toàn và rút ngắn thời gian kiểm tra xuống dưới 4,8 – 5,1 phút/đơn để đạt điểm hòa vốn.
