# Dữ liệu tạm đọc và đối chiếu nguồn

Thư mục `NMMMT/tmp/study_audit/` chứa script, trích xuất chữ, OCR và hình phục vụ phân tích. Mọi tệp liên quan đã được gom trong `NMMMT/`; không sửa tài liệu nguồn trong hai thư mục `Giữa Kỳ/` và `Lý thuyết/`.

- `extract_sources.py`: đọc PDF theo trang, DOCX theo đoạn, kiểm kê tệp và bỏ qua ba file đáp án riêng.
- `manifest.json`: đường dẫn nguồn, số trang, lượng chữ/hình và SHA256 của tệp đã trích xuất.
- `prepare_visuals.py`: render hai PDF scan và lấy ảnh nhúng DOCX để đọc.
- `ocr_scans.ps1`: OCR cục bộ Windows cho ảnh scan; máy chỉ có ngôn ngữ OCR en-US. OCR có thể sai dấu, số, đơn vị; phải kiểm ảnh.
- `E01_ocr.txt`, `E02_ocr.txt`, `visuals/`: OCR và ảnh scan.
- `T1.txt`, `T2.txt`, `T3.txt`: trích xuất đủ 69, 105, 109 trang lý thuyết.
- `E03.txt`, `E08.txt`, `E10.txt`: trích xuất ba PDF đề còn lại được giữ.
- `question_classification.json`: phân loại đủ 172 lượt câu theo chương chính, đã được ba subagent kiểm tra.
- `ch1_analysis.md`, `ch2_analysis.md`, `ch3_analysis.md`: phân tích từng chương. Các tệp có chữ `broad_internal` hoặc `archive` lưu vết sàng lọc trước khi phạm vi thay đổi, không dùng làm căn cứ bản kế hoạch cuối.

Phạm vi cuối: năm đề E01/E02/E03/E08/E10, ba tài liệu lý thuyết T1/T2/T3. E06 là bản DOCX trùng E08, không tính riêng. Không dùng đề online, training, đề mẫu, ngân hàng, tài liệu bài tập/phát triển đề hoặc các đáp án riêng. Nội dung từng được trích trước khi người dùng thu hẹp phạm vi chỉ là dữ liệu tạm, không tham gia kết luận cuối.

Kết quả để học: `../../output/KE_HOACH_ON_NMMMT_7_NGAY.md`. Trạng thái và quyết định: `../../memory.md`.

## Tiến độ ôn thi — cập nhật 26/10/2026

- **Hiện tại:** Chương 2, bắt đầu Web/HTTP: object, URL và cấu trúc request/response HTTP/1.1.
- **Tiến độ Chương 2 trước bài này:** **12,5% = 1/8 chặng**, mỗi chặng tính trọng số bằng nhau theo bước 6–13 của `../../output/THU_TU_HOC_NMMMT.md`. Đã học chặng nguyên lý ứng dụng mạng; Web/HTTP đang bắt đầu, chưa cộng hoàn thành. Giữ cùng cách tính và báo % trước bài mới.
- **Nội dung đã học:** bốn loại độ trễ; `d_trans=L/R`, `d_prop=d/s` và đổi đơn vị; cường độ lưu lượng `La/R`, hàng đợi và mất gói; độ trễ của một gói qua nhiều link theo store-and-forward.
- **Chương 1:** đã tổng ôn và làm 8 câu tự kiểm; đúng câu 2/3/5/7/8. Các điểm cần ôn lại là định nghĩa giao thức, tầng xử lý của switch lớp 2/router và cộng đủ độ trễ nhiều link; chi tiết giữ trong memory.
- **Chương 2 đã học:** client–server/P2P; host, process, socket; IP và port. Đã trả lời 3 câu mở đầu và được chỉnh thuật ngữ server, GET, phần file chia sẻ, IP đích.
- **Đã kiểm tra:** trả lời đúng cả 3 câu về chọn TCP cho tải file, UDP không bảo đảm độ trễ và bổ sung TLS để bảo mật theo mô hình bài học.
- **Đã trao đổi thêm:** lý do dùng UDP, minh họa bằng cuộc gọi và game; ví dụ từ tài liệu Riot/Valve không bổ sung nguồn đề thi.
- **Đang học tới:** Web/HTTP phần đầu, LT2 trang PDF 17–19, 25–26, 28 và 51; request/response, dòng đầu/header/body, ý nghĩa Content-Length. Đang chờ 3 câu tự kiểm về object, đọc request và độ dài body; chi tiết lưu trong `../../memory.md`.
- **Bài tiếp theo:** method HTTP và mã trạng thái để hoàn tất chặng Web/HTTP; sau đó cookie/cache theo lộ trình.

Mốc này ghi nội dung đã học, không tự xác nhận đã thành thạo toàn bộ. Khi tiếp tục buổi ôn, đọc `../../memory.md` và cập nhật mốc bài học trong cả hai tệp.
