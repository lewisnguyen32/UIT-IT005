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

Tiến độ hiện tại chỉ cập nhật tại [memory.md](../../memory.md); kết quả chi tiết theo chương ở `../../memory/`.
Phần tiến độ từng ghi tại đây đã chuyển nguyên văn sang [bản lưu](../../memory/nguon-va-lich-su.md). Không đồng bộ tiến độ vào README này nữa.
