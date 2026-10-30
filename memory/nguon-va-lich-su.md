# Nguồn, quyết định và lịch sử tổ chức

Chỉ tra cứu khi cần kiểm nguồn, phạm vi hoặc lịch sử; không đọc toàn bộ khi tiếp bài.
Quy tắc hiện hành ở [AGENTS.md](../AGENTS.md), trạng thái hiện tại ở [memory.md](../memory.md).

## Nguồn đang dùng

Danh sách này xác định đúng các PDF người dùng đã chọn; quy tắc sử dụng ở AGENTS.md. T1/T2/T3 là nguồn kiến thức chính. Chỉ năm PDF E01/E02/E03/E08/E10 làm căn cứ đề thi; các nguồn bị loại còn xuất hiện trong lịch sử không được dùng lại.

| Mã | PDF gốc |
|---|---|
| T1 / LT1 | [Chương 1 — Giới thiệu](<../Lý thuyết/[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf>) |
| T2 / LT2 | [Chương 2 — Tầng ứng dụng](<../Lý thuyết/[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf>) |
| T3 / LT3 | [Chương 3 — Tầng vận chuyển](<../Lý thuyết/[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf>) |
| E01 / D19 | [Đề 2019–2020](<../Giữa Kỳ/[BHT CNPM] NMMMT 2019-2020 GK1.pdf>) |
| E02 / D20 | [Đề 2020–2021](<../Giữa Kỳ/[BHT CNPM] NMMMT 2020-2021 GK1.pdf>) |
| E03 / D25 | [Đề 2025–2026](<../Giữa Kỳ/[BHT CNPM] NMMMT 2025-2026 GK1.pdf>) |
| E08 / D23 | [Đề A MMT — thư mục 2023](<../Giữa Kỳ/Nhập Môn Mạng Máy Tính/2023/Đề A MMT.pdf>) |
| E10 / D24 | [Đề 2024](<../Giữa Kỳ/Nhập Môn Mạng Máy Tính/2024/2024.pdf>) |

## Đề mẫu cô cung cấp riêng — 30/10/2026

- Người dùng cho phép chữa/đối chiếu đề mẫu15câu qua2ảnh [trang1](<C:/Users/phuoc/Downloads/drive-download-20261030T020832Z-1-001/20261030_090708.jpg>) và [trang2](<C:/Users/phuoc/Downloads/drive-download-20261030T020832Z-1-001/20261030_090713.jpg>), nêu đây là đề cô đưa. Đây là nguồn luyện bổ sung được cho phép mới, không phải nguồn đề online và không gộp vào thống kê5PDF/172lượt câu.
- Báo cáo: [chữa đề mẫu](../output/CHUA_DE_MAU_CO_20261030.md). User đã xác nhận lựa chọn cuối C2=A,C10=B,C12=A; không tự đoán từ nét sửa. C15 thuộc phần congestion đãloại/chưa thấy lựa chọn, không tự đưa lại vào lịch/tiến độ.
- Các lỗhổng được bổ sung vào bản tổng hợp và Obsidian theo yêu cầu; RFC/IANA chỉ làm rõ cổng/tên/HTTP, nguồn lý thuyết chính vẫnT1/T2/T3. Không dùng key/đáp án riêng, có3subagent ràđộc lập.

## Phạm vi hiện hành — 29/10/2026

- Người dùng cập nhật: chỉ tới hết phần TCP ban đầu, không thi TCP điều khiển tắc nghẽn. Giữ T3 đến hếttr94, gồm flow/connection; loại tr96–102, QUIC/HTTP3tr104–108 vẫn ngoài phạm vi. Fast retransmit tr84 vẫn giữ; EstimatedRTT bước24 vẫn tùy chọn.
- Có9chặng cơ sở bước14–22; bước23 bỏ khỏi lịch/tính tiến độ. NguồnT1/T2/T3 và5PDFđề/172lượt câu, kết quả phân loại và tần suất không đổi. Các mốc phạm vi/phần trăm cũ bên dưới là lịch sử trước cập nhật này.

## Bản lưu trước khi tách memory

Các mục bên dưới được giữ nguyên văn từ các tệp trước khi tách ngày 27/10/2026. Yêu cầu đọc toàn bộ nguồn để lập kế hoạch đã được thực hiện; không phải việc cần lặp lại mỗi buổi. Quy tắc cũ về subagent và cập nhật tiến độ ở hai tệp đã được thay bằng AGENTS.md. Thông tin môi trường là ghi nhận lúc đó, chỉ kiểm lại khi thực sự cần dùng.

Đường dẫn trong phần lấy từ memory.md tính từ NMMMT; đường dẫn trong bản lưu README cuối tệp giữ theo vị trí gốc tmp/study_audit/.

## Yêu cầu và phạm vi cuối

- Cập nhật 27/10/2026: Chương3 chỉ học đến hết TCP, gồm cả quản lý kết nối, điều khiển luồng và điều khiển tắc nghẽn theo ảnh outline. QUIC/HTTP3 tr104–108 ngoài phạm vi, không tự thêm lại dù các ghi chú cũ từng xếp C. Không thay đổi nguồn đề hay kết quả phân loại172câu.
- Đọc toàn bộ file đề thi trong `NMMMT`, chỉ dùng phần câu hỏi; không đọc các file đáp án riêng. Đọc tài liệu lý thuyết, phân loại trọng tâm và lập lịch học 7 ngày theo Chương 1, 2, 3 do người dùng nêu.
- Người dùng mới học, chưa nắm chắc, có 2-3 giờ/ngày (14-21 giờ/tuần).
- Người dùng đã bổ sung: không lấy nội dung từ đề thi online. Loại hoàn toàn các liên kết online, kể cả URL trong đề PDF/DOCX.
- Người dùng tiếp tục thu hẹp sang đề thi các năm, bỏ đề tự làm. Đã đồng ý dùng bản BHT sưu tập/soạn lại 2025-2026, sau đó chỉ định tính thêm hai PDF trong folder 2023 và 2024.
- Phạm vi cuối: E01 (2019-2020,30c), E02 (2020-2021,30c), E03 (2025-2026,30c), E08 (2023,40c), E10 (2024,42c), và T1/T2/T3. Không phải 170 câu: đúng là **172 lượt câu**. Có câu lặp giữa đề, không coi đây là 172 quan sát độc lập.
- Phải có subagent cho từng chương/phần phù hợp, đối chiếu bằng chứng; không tự bịa khi tài liệu thiếu hoặc không rõ.
- Tách dữ liệu tạm phục vụ extract và có `memory.md` (yêu cầu trực tiếp của người dùng).

## Tổ chức tệp

- Toàn bộ tệp liên quan được gom trong `NMMMT/` theo yêu cầu mới. Các đường dẫn tương đối bên dưới tính từ thư mục `NMMMT/`.
- Nguồn gốc: `Giữa Kỳ/` và `Lý thuyết/` (giữ nguyên).
- Script và trích xuất tạm: `tmp/study_audit/`.
- Script: `tmp/study_audit/extract_sources.py`.
- Manifest: `tmp/study_audit/manifest.json`.
- Phân loại từng câu: `tmp/study_audit/question_classification.json`.
- Giải thích dữ liệu tạm: `tmp/study_audit/README.md`.
- Kết quả: `output/KE_HOACH_ON_NMMMT_7_NGAY.md`, gồm chương/phần, A/B/C, trang lý thuyết, câu đối chiếu, lịch7ngày, lưu ý lỗi/mơ hồ và danh sách phân nhóm đủ172câu.
- Hướng dẫn thực hiện: `output/THU_TU_HOC_NMMMT.md`, tạo theo yêu cầu tiếp theo về thứ tự học cụ thể/chương/tóm tắt. Có 25 bước theo 7 ngày, trang PDF, mục tiêu tự kiểm; bước 24 EstimatedRTT là tùy chọn thêm giờ. Giữ nguyên phạm vi kế hoạch chính. Đã kiểm lại thứ tự Ch3 với subagent, trang UDP24-29/checksum30-34.

## Kiểm kê ban đầu

- Có 3 PDF lý thuyết riêng Chương 1-3 và một `slide nmm.pdf` cần nhận diện nội dung.
- Có đề thi PDF/DOCX, ngân hàng câu hỏi, tài liệu phát triển đề. File `LINK THI ONLINE 52 câu.docx` chỉ chứa URL, loại theo yêu cầu mới.
- Loại các file đáp án riêng: `ĐA 2024.pdf`, `ĐA Đề A.pdf`, `_45_cau_ đáp án .docx`.
- Chưa kết luận trọng tâm/tần suất cho tới khi đọc và đối chiếu đầy đủ. Không dùng tên file để khẳng định một tài liệu là đề chính thức.

## Môi trường

- Python bundle: `C:/Users/phuoc/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
- Có pypdf, pdfplumber, python-docx, PIL; chưa có fitz.
- Đã đọc skill PDF và tài liệu, dùng cho đọc nguồn; chưa tạo DOCX/PDF đầu ra.

## Tiến độ

- Đã trích xuất 3 PDF lý thuyết (69 + 105 + 109 trang), slide tổng hợp 238 trang, các đề PDF/DOCX. Manifest chứa đường dẫn, số trang, thống kê chữ/hình và SHA256.
- Ba agent `chuong_1`, `chuong_2`, `chuong_3` đã đọc đủ lý thuyết chương mình và toàn bộ câu hỏi của các đề giữ lại, đối chiếu ảnh, phân tích trong `ch1_analysis.md`, `ch2_analysis.md`, `ch3_analysis.md`. Đã yêu cầu các agent review bản tổng hợp theo chương độc lập.
- Đề scan E01 (2019-2020, 6 trang) và E02 (2020-2021, 7 trang) đã render bằng pypdfium2, OCR cục bộ Windows. OCR chỉ có en-US nên số liệu/hình được đối chiếu ảnh gốc. Ví dụ E01 C12 link 1 dài 3 km, OCR nhận nhầm 9 km.
- E06 DOCX và E08 PDF là cùng bộ 40 câu 2023; chỉ tính một bộ.
- E16 `Phát Triển Đề Thi...docx`: không có nút chữ hiện hành w:t, có 446 nút w:delText (Track Changes). Nội dung lịch sử được lưu riêng `E16_deleted_history.txt`, không dùng để nâng ưu tiên. Hai ảnh mail đã xem.
- E14 ngân hàng có nhiều câu ngoài Chương 1-3 (IP/subnet/routing/link/physical). Cụm đồ thị TCP P308-356 chỉ còn nhãn chữ/số, không có phần đồ thị trong gói DOCX; không suy đoán đáp án.
- Không có LibreOffice trong runtime bundle. Không dùng LibreOffice desktop của người dùng.
- Nguồn đề bị loại: E13 training, E14 ngân hàng, E15 bài tập ôn, E16 phát triển đề/lịch sử, E20 đề mẫu; E17 slide ôn không làm căn cứ cuối; E19 chỉ liên kết online. E06 trùng E08 không tính. Những nguồn từng đọc trước khi phạm vi đổi chỉ lưu ở tmp/archives, không tham gia bảng ưu tiên/luyện của bản cuối.
- Phân nhóm chính đủ172câu: Ch1=26, Ch2=75, Ch3=71. Đã kiểm chéo từng chương và tự động kiểm không thiếu/trùng chỉ số trong mỗi đề.
- Đã ghi lưu ý nội dung mơ hồ/sai trong LT2tr24, LT3tr78,88-89, D25C19,C26,C30 và D23C6/C17; không tự chấm mù bằng đáp án tham khảo.
- D20 C23 hỏi EstimatedRTT nhưng LT3 thiếu công thức chi tiết. Đã đối chiếu RFC6298 chính thức mục2.2-2.3: https://www.rfc-editor.org/rfc/rfc6298.html#section-2. Nêu rõ khởi tạo mẫu đầu, alpha của đề0.2 khác khuyến nghị1/8. Đã kiểm thêm NFS là giao thức tầng ứng dụng qua RFC2074 mục5.5.10 để đánh dấu D23 C21 có nhiều lựa chọn đúng: https://www.rfc-editor.org/rfc/rfc2074.html#section-5.5.10. Hai tham chiếu này chỉ kiểm kiến thức thiếu/mơ hồ, không lấy đề online hoặc tăng tần suất chủ đề.
- Lịch cơ sở14giờ gồm nghỉ:7ngày×(110phút học+10phút nghỉ), thêm tối đa60phút/ngày (tổngtốiđa21giờ). Quỹ khoảng Ch1=3h,Ch2=4h,Ch3=5h,tổnghợp=2h. Học nềnCh1 trước, rồiứngdụng,vậnchuyển,luyệnđề. D25 giữ cho lượt làm tổng hợp65phút ngày7.
- `tmp/study_audit/verify_final.py` đã chạy đạt: đủ172câu đúngmộtchươngchính/câu;8liênkếtnguồncục bộ hợp lệ;7ngày đúng110phúthọc;SHA256 của8nguồn được chọn giữ nguyên. Không sửa tệp nguồn.
- Đã hoàn tất review độc lập của cả ba agent: Ch1 xác nhận số câu/trang/công thức, sửa giới hạn OSI và bổ sung lỗi ký hiệu b/B; Ch2 xác nhận HTTP/DNS/mail và lịch; Ch3 xác nhận cơ chế, Seq/ACK, rwnd/cwnd và RTT, bổ sung giả thiết GBN và trang ví dụ Seq/ACK. Bản kế hoạch đã áp dụng các sửa cần thiết.
- Trạng thái: đã hoàn thành kế hoạch và các tệp người dùng yêu cầu; không còn câu hỏi phạm vi đang chờ.

## Lịch sử di chuyển thư mục

- Đã chuyển các thư mục `output/`, `tmp/` và `memory.md` từ gốc workspace vào `NMMMT/`. Đã cập nhật đường dẫn extraction trong manifest và giới hạn script extract chỉ quét hai thư mục nguồn, tránh quét nhầm dữ liệu phát sinh. Gốc workspace chỉ còn thư mục `NMMMT/`.

## Quy tắc cập nhật cũ — chỉ lưu lịch sử, đã thay thế

- Khi tiếp tục ôn, đọc `memory.md` và cập nhật mốc đã học/bài tiếp theo trong cả tệp này và `tmp/study_audit/README.md`.

## Bản lưu tiến độ từ tmp/study_audit/README.md — ngừng cập nhật

> Lưu nguyên văn để không mất thông tin. Các chỉ dẫn cập nhật cả hai tệp ở cuối bản lưu không còn áp dụng.

## Tiến độ ôn thi — cập nhật 27/10/2026

- **TẠM DỪNG theo yêu cầu — 27/10/2026:** ba câuSR đúngý chính; sửa C1receiverchờpkt2đúngđến, không biết/chờ timer sender. Đã giải thíchW củaGBN/SR rồi dừng, không thêmquiz/khôngdạyTCP. **Bước14–19 đã học/tựkiểm/chữa:6/10=60% nội dungCh3**, không phải thànhthạo. Buổi sauuser tiếp thì bắt đầu bước20TCPtr75–84, CHƯAGIẢNG. Phạmvi đến hếtTCP/tr102, loạiQUIC/HTTP3. Ch2C11–20 vẫn tạm dừng, CHƯA TRẢ LỜI.
- **Phạm vi Ch3:** đến hết TCP, gồm quản lý kết nối, điều khiển luồng và điều khiển tắc nghẽn; T3 hếttr102. Phát triển tầng vận chuyển/QUIC/HTTP3tr104–108 ngoài phạm vi. EstimatedRTT tùy chọn;10chặng cơ sở bước14–23. Ch2C11–20 vẫn chưa trả lời. Tiến độ hiện tại theo bullet đầu.
- **Lịch sử chuyển chương:** ngày27/10/2026 chuyểnCh2 sangCh3 từ0/10,sau bước14 là10%. Không dùng mốc cũ làm tiến độ hiện tại; xem bullet đầu.
- **Tiến độ Chương 2 hiện tại:** **100% = 8/8 chặng nội dung**, mỗi chặng tính trọng số bằng nhau theo bước 6–13 của `../../output/THU_TU_HOC_NMMMT.md`. Đã học và có tự kiểm/chữa theo từng phần; đây không phải tỷ lệ thành thạo. Vẫn ôn header/status, iterative, MX→A và HTTP tái sử dụng TCP. Ba câu DNS cơ bản ban đầu chưa trả lời đủ được giữ trong memory, không ép lặp lại nếu người dùng muốn chuyển bài.
- **Nội dung đã học:** bốn loại độ trễ; `d_trans=L/R`, `d_prop=d/s` và đổi đơn vị; cường độ lưu lượng `La/R`, hàng đợi và mất gói; độ trễ của một gói qua nhiều link theo store-and-forward.
- **Chương 1:** đã tổng ôn và làm 8 câu tự kiểm; đúng câu 2/3/5/7/8. Các điểm cần ôn lại là định nghĩa giao thức, tầng xử lý của switch lớp 2/router và cộng đủ độ trễ nhiều link; chi tiết giữ trong memory.
- **Chương 2 đã học:** client–server/P2P; host, process, socket; IP và port. Đã trả lời 3 câu mở đầu và được chỉnh thuật ngữ server, GET, phần file chia sẻ, IP đích.
- **Đã kiểm tra:** trả lời đúng cả 3 câu về chọn TCP cho tải file, UDP không bảo đảm độ trễ và bổ sung TLS để bảo mật theo mô hình bài học.
- **Đã trao đổi thêm:** lý do dùng UDP, minh họa bằng cuộc gọi và game; ví dụ từ tài liệu Riot/Valve không bổ sung nguồn đề thi.
- **Web/HTTP đã học:** HTML/object, URL, request/response; method, Host, version, status, Connection, Content-Length và header/body. Đã trả lời tự kiểm và giải thích toàn response khác body; Content-Length đếm byte body trong các ví dụ đã học. Chi tiết lưu trong `../../memory.md`.
- **Bài mới đã trình bày:** method GET/POST/HEAD/PUT, query sau dấu ?, mã 200/301/400/404/505 và header Location; Connection: close. Đối chiếu LT2 trang PDF 27, 29, 51 với subagent; sửa lỗi chữ POST trong mô tả PUT ở slide. Người dùng đúng câu 1–2; câu 3 nhận đúng /new.html, cần chỉnh “chuyển dữ liệu” thành chuyển vị trí vĩnh viễn và gọi tên header Location.
- **Đã làm rõ chuyển hướng:** người dùng diễn giải đúng GET nhận 301 thông báo URL mới và phân biệt với yêu cầu server di chuyển tài nguyên. Chỉnh rằng thành công có thể trả 200 hoặc mã phù hợp khác như 204; không mặc định luôn 200. Tham khảo RFC chỉ làm rõ khái niệm, không đổi phạm vi nguồn đề thi. Chặng Web/HTTP tính đã học và tự kiểm khi chuyển bài.
- **Bài cookie đã học và kiểm tra:** LT2 trang PDF 19, 31–34, đối chiếu với subagent. Người dùng trả lời đúng Set-Cookie trong response, Cookie trong request và dữ liệu mỗi bên lưu. Trong mô hình ví dụ, browser giữ cookie chứa mã phiên, server giữ ánh xạ ID và dữ liệu phiên/giỏ hàng.
- **Kết quả tổng ôn Chương 2:** câu 3/4/6/8 đúng. Câu 1 cần sửa trang web là nội dung, phần mềm web server mới đóng vai server; P2P chia sẻ phần file đã có mà peer khác cần, chưa cần đủ file. Câu 2 cần sửa IP xác định host trong mô hình bài học, port chọn dịch vụ/điểm cuối trên host. Câu 5 đúng Content-Length/body nhưng bỏ method/host (bổ sung POST, study.example). Câu 7 đúng GET/404 nhưng bỏ đường dẫn mới (bổ sung /new.html). Chi tiết giữ trong memory; chưa xác nhận nắm chắc thuật ngữ còn lặp lại.
- **Đã củng cố:** người dùng trả lời đúng host 192.0.2.10, port 80 và index.html là tài nguyên trong ví dụ đã hỏi.
- **Bài cache đã trình bày:** cache lưu bản sao object; proxy là server với browser và client với origin; cache dùng được ngay khi được phép/còn hợp lệ. Browser xác thực lại bằng GET + If-Modified-Since lấy từ Last-Modified bản cũ; chưa đổi nhận 304 không body object và dùng bản cache, đã đổi nhận 200 + body mới. 304 vẫn dùng trao đổi mạng cho request/status/header. Đã được subagent đối chiếu.
- **Tự kiểm cache:** câu 2 đúng 304 dùng ảnh cache; phần body ảnh mới trong câu 3 đúng. Ở câu củng cố, người dùng trả lời đúng proxy là server với browser và client với origin, còn nhầm If-Modified-Since với mã phản hồi. Đã sửa chỗ cuối thành 200 OK và minh họa request/response. Lưu điểm cần ôn; chuyển bài khi người dùng yêu cầu tiếp, không coi đã thành thạo toàn bộ.
- **Ưu tiên:** subagent đối chiếu kế hoạch và corpus, bài số hit-rate/lưu lượng/trễ cache thuộc B/C thêm giờ; không cần trước HTTP/RTT. Chi tiết bằng chứng giữ trong memory.
- **Bài HTTP/RTT đã học và kiểm tra:** nonpersistent tối đa một object/TCP; persistent tái sử dụng TCP cùng server. TCP mới một object: T≈2RTT+L/R; TCP đã mở, GET tuần tự: T≈RTT+L/R trong mô hình đã nêu. Người dùng trả lời đúng cả 3 câu: 4 TCP, có thể tái sử dụng 1 TCP cho 4 request, trễ truyền20ms và tổng80ms. Chưa kiểm tra bài nâng cao nhiều object/pipelining.
- **Bài Mail đã học và kiểm tra:** câu 1 đúng SMTP/SMTP/POP3 hoặc IMAP; câu 2 đúng mailbox trên server nhận; câu 3 chọn IMAP đúng, cần chỉnh lý do: IMAP vẫn tải nội dung khi đọc, quản lý thư/thư mục/trạng thái trên server giúp nhiều thiết bị. POP3 có thể giữ bản sao trên server. Cổng trọng tâm SMTP/TCP25 cho server-to-server và POP3/TCP110; nội dung được subagent đối chiếu LT2 trang 53–60/kế hoạch mục 2.3.
- **Ví dụ Gmail:** theo Google Help, Gmail hỗ trợ IMAP cho ứng dụng mail; Gmail trên browser dùng HTTPS. Không gán IMAP cho mọi cách truy cập Gmail. Nguồn Google chỉ làm rõ khái niệm, không thay đổi corpus đề. Giữ tiến độ 50% trong lượt giải thích.
- **So sánh POP3/IMAP:** IMAP thường phù hợp nhiều thiết bị nhờ quản lý hộp thư/thư mục/trạng thái trên server; POP3 chủ yếu lấy thư về từng máy, không đồng bộ đầy đủ trạng thái/thư mục. Cả hai tải nội dung; IMAP đọc offline được nếu đã tải/cache và ứng dụng hỗ trợ; POP3 không bắt buộc xóa server. Đối chiếu Mozilla/Google và subagent, chi tiết nguồn giữ trong memory; không thay đổi corpus đề. Tiến độ giữ50%.
- **Bài DNS đã trình bày:** hostname→IP, DNS tầng ứng dụng và CSDL phân tán/phân cấp; root chỉ TLD, TLD chỉ authoritative, authoritative trả dữ liệu vùng quản lý. Host hỏi local resolver trước khi cần gửi truy vấn; resolver dùng cache hoặc tra các tầng, không phải local là tầng thứ tư. Ví dụ giả định www.study.com, không tra tên thật; root không lưu mọi IP. DNS thường dùng UDP/TCP53. Đã được subagent đối chiếu LT2 trang 62–69; chờ 3 câu tự kiểm. Mail đã học và làm/chữa tự kiểm trước khi chuyển bài.
- **Giải thích lại DNS:** ví dụ giả định www.study.com→192.0.2.20, sơ đồ resolver hỏi từng DNS server rồi browser dùng kết quả lấy HTML từ web server. Người dùng đã trả lời đúng phân biệt DNS tìm IP/web server trả HTML; ba câu DNS ban đầu chưa trả lời đầy đủ. Không tự khẳng định thành thạo toàn bộ.
- **Tự kiểm DNS truy vấn/cache:** câu 1 đúng recursive; câu 2 đúng iterative nhưng nhầm root hỏi .com, sửa local resolver hỏi .com sau chỉ dẫn của root; câu 3 muốn giải thích TTL rõ hơn, chưa trả lời.
- **Đã làm rõ và kiểm tra TTL:** người dùng trả lời đúng t50 còn10s nên dùng IPcũ trong ví dụ. Đọc cache không reset TTL; hết hạn không tự truy vấn ngay; còn hạn dùng cache không bảo đảm dữ liệu gốc chưa đổi. Chi tiết timeline trong memory.
- **Bài bản ghi đã trình bày:** RR(name,value,type,ttl); A hostname→IPv4, CNAME bí danh→tên chính tắc, NS domain→tên DNS authoritative, MX domain→tên mail exchanger. Ví dụ giả định study.com: www CNAME web1, web1 A192.0.2.20; NS ns1, ns1 A192.0.2.30; MX mail, mail A192.0.2.40; TTL300s, bảng chỉ ghi đích MX. Subagent rà soát tính hợp lệ/mục tiêu; đã làm/chữa tự kiểm như mục tiếp theo.
- **Tự kiểm bản ghi:** IPweb đúng192.0.2.20; làm rõ chỉ dùng hai RR CNAME→A. Câu2 đúng study.com/MX nhưng còn thiếu A mail.study.com→192.0.2.40, đã bổ sung; câu3 đúng cần A ns1.study.com→192.0.2.30. Không coi phần thiếu là toàn câu sai; chặng đã học/chữa trước khi chuyển socket.
- **Bài socket đã học/kiểm tra:** đúng cả 3 câu: A UDP/DGRAM, B TCPclient/STREAM+connect, C server dùng conn. Chuẩn hóa listener lắng nghe/đón kết nối mới, accept trả conn để trao đổi. Không yêu cầu viết/chạy app; subagent đã đối chiếu LT2tr90–99/bước13.
- **Tổng ôn cuối Ch2 đã chữa:** đã đổi→200+body mới, chưa đổi→304 không body mới;301 là chuyểnURL. Resolver hỏiDNS.com tiếp sau referral; MX→A raIPmail.70 đúng. TCPđã mở mộtGET=RTT20+truyền10=30ms. Chưa có tự kiểm mới chứng minh đã sửa hết nhầm lẫn.
- **Ch2 tạm dừng:** bộ 80 câu tại `../../output/CAU_HOI_TONG_ON_CHUONG_2.md`; C1–10 đã trả lời/chữa, C11–20 đã đưa nhưng CHƯA TRẢ LỜI. Chỉ quay lại C11–20 khi người dùng tiếp ôn Ch2; không ép làm trước Ch3. Câu73–80 và vài bài số là mở rộng, chưa coi đã học, không đổi trọng tâm đề thi. Kết quả chi tiết giữ trong memory.
- **Mốc tiếp tục sau tạm dừng:** đã học/tựkiểm/chữa đến hếtbước19pipeline/GBN/SR,60%; không còn câu hỏi đang chờ. Đã làm rõGBNreceiverwindow1→W≤2^k−1,SRhaiwindowbằngnhau→W≤2^(k−1),k3→max7/4. Đối chiếu lý thuyết UCLouvain https://sites.uclouvain.be/CNP3/1st/html/transport/transport.html ,không dùng đềonline/đổi nguồnđề. Buổi sau bắt đầu bước20TCPtr75–84 khi người dùng quay lại, không tự tiếp TCP ngay. Chi tiết trong ../../memory.md, mục Điểm tiếp tục Chương3.

Mốc này ghi nội dung đã học, không tự xác nhận đã thành thạo toàn bộ. Khi tiếp tục buổi ôn, đọc `../../memory.md` và cập nhật mốc bài học trong cả hai tệp.
