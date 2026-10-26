# Phân tích Chương 2 - Tầng ứng dụng

Ngày phân tích: 2026-10-22. Báo cáo làm việc cho bản kế hoạch chung, không phải đáp án chính thức. Chỉ dùng tài liệu trong thư mục; không tìm hay lấy đề trực tuyến. Mọi số trang PDF dưới đây là trang vật lý (tính từ 1).

## 1. Phạm vi đã đọc và giới hạn chứng cứ

Đã đọc lần lượt toàn bộ nội dung trích xuất T2, trang 1-105, kể cả phần P2P và lập trình socket ngoài bốn nhóm nội dung người dùng nêu. Đã đọc hết Chương 2 E17, trang 51-108. Đã xem ảnh những trang E17 có bảng/sơ đồ/mã nguồn bị thiếu trong văn bản: 58, 66, 73, 86, 87, 89, 91-93, 101, 104-108. T2 là nguồn lý thuyết chính; E17 là slide tổng hợp đối chiếu, có một số lỗi cần tránh.

Đã đọc hết câu hỏi các nguồn sau, không chỉ tìm từ khóa:

| ID | Nội dung và mức độ tin cậy khi dùng |
|---|---|
| E01 | `[BHT CNPM] NMMMT 2019-2020 GK1.pdf`, 6 trang, 30 câu. Đã đọc hết E01_ocr.txt và xem trực tiếp trang 1, 3-6 cho câu Ch2; OCR có lỗi tiếng Việt nên các ví dụ dùng trong báo cáo đều được đối chiếu ảnh. Đây là bản đề được lưu/sưu tập, không có cơ sở tự khẳng định đáp án chính thức. |
| E02 | `[BHT CNPM] NMMMT 2020-2021 GK1.pdf`, 7 trang, 30 câu. Đã đọc hết E02_ocr.txt và xem trực tiếp trang 1-2, 4-7 cho câu Ch2. Phần đầu ảnh ghi năm 2020; giữ tên nguồn theo manifest, không suy diễn thêm niên khóa. |
| E03 | `[BHT CNPM] NMMMT 2025-2026 GK1.pdf`, 6 trang, 30 câu, trong đó trang 6 là đáp án tham khảo và ghi rõ đề sưu tập/soạn lại sau thi, không phải đáp án chính thức. Dùng câu hỏi làm bằng chứng dạng kiến thức; không lấy bảng đáp án làm chân lý. |
| E06 và E08 | E06 DOCX `_De_A_NMMMT_-UIT_d2afeb_03_11_2023-2.docx` và E08 PDF `Đề A MMT.pdf`, cùng 40 câu Đề A 2023. Đã đọc cả hai và nhận ra cùng bộ câu; chỉ coi là một bộ khi đánh giá sự xuất hiện. E06 chèn đáp án từng câu; không dùng các đáp án đó để quyết định lý thuyết. |
| E10 | `2024.pdf`, 4 trang, 42 câu. Đã xem ảnh trang 4 để đọc rõ sơ đồ mail C39. Có nhiều câu trùng dạng/đoạn câu với E08; không từ số bản sao suy ra xác suất thi. |
| E13 | `BHTCNPM-Trainingonline-NMMMT-GK-2023-2024.pdf`, 62 trang, đã đọc hết 30 câu đề thử và các câu bổ sung RDT. Tên nội dung là TRAINING/GIẢI ĐỀ THI THỬ, không gộp vào đề thi thật. |
| E14 | `ComputerNetwork_Quiz_Bank.docx`, đã đọc hết đoạn P1-P819. Là ngân hàng câu hỏi, có nội dung nhiều chương về sau; không coi là một đề thi hay bằng chứng về tỷ lệ ra thi. Không có số câu liên tục, nên trích dẫn bằng mã đoạn P... từ bản extract. |
| E15 | `GK Nhập Môn Mạng Máy Tính.pdf`, 28 trang, đã đọc hết Ch1 (13 câu), Ch2 (23 câu), Ch3 (52 câu). Đây là BÀI TẬP ÔN GIỮA KỲ đăng lại trên Studocu, không coi là đề thật. Đã xem ảnh trang 12 để xác nhận hình mail C23 Ch2. |
| E16 | Đã đọc hết E16_deleted_history.txt, gồm 446 đoạn w:delText. Văn bản nguồn toàn bộ là tracked deletion, không có nội dung w:t hiện hành; chỉ kiểm tra lịch sử, không coi là đề hiện hành, không dùng tăng ưu tiên hay làm căn cứ bài luyện chính. |
| E20 | `Đề Thi Mẫu.docx`, 15 câu. Đã đọc hết; xem `visuals/E20/image1.jpg` xác nhận đó là phiếu tô trắc nghiệm trống, không phải câu hỏi bị bỏ sót. Chỉ là đề mẫu theo tên văn bản. |

Không mở ba file đáp án riêng: `ĐA 2024.pdf`, `ĐA Đề A.pdf`, DOCX có `_45_cau_` trong tên và là đáp án. E19 là đường dẫn online, loại hẳn theo yêu cầu. Văn bản/đáp án đính kèm trong chính các nguồn có thể nằm chung trong extract; chỉ kiểm tra tính nhất quán, không dùng làm chuẩn.

Không đưa con số phần trăm/tần suất ra thi: số đề ít, nguồn sưu tập, có bản trùng và nhiều câu sao chép. A/B/C dưới đây là thứ tự học dựa vào phạm vi người dùng, quan hệ tiên quyết, độ rõ của lý thuyết và bằng chứng dạng câu hỏi trong tập nguồn.

## 2. Trật tự học hợp lý và mức ưu tiên

Định nghĩa: **A** = phải hiểu và tự giải thích được trong tuần; **B** = học sau A, nhận diện/làm được bài cơ bản; **C** = đọc sau nếu còn giờ hoặc giảng viên xác nhận nằm trong thi. Không có nghĩa C chắc chắn không thi.

| Phần học | Mức | Cần hiểu và tự làm được | Nguồn lý thuyết chính | Bằng chứng câu hỏi cụ thể |
|---|---|---|---|---|
| 2.1. Ứng dụng, tiến trình, socket; client-server và P2P; chọn TCP/UDP theo nhu cầu | A | Phân biệt host với process; IP xác định host/đầu cuối trong mô hình đơn giản, port phân biệt tiến trình; client chủ động liên lạc, server chờ; hai peer có thể vừa cung cấp vừa yêu cầu dịch vụ. TCP tin cậy không đồng nghĩa bảo đảm độ trễ/thông lượng tối thiểu hay tự mã hóa. | T2 tr.3-15; E17 tr.53-59 | E01 C22-23 tr.5; E02 C12 tr.4; E03 C2,6 tr.1 và C10 tr.2; E08 C22,25-29 tr.2-3; E10 C9 tr.1; E20 C9,13. |
| 2.2. Web/HTTP: object, URL, request/response, header, method, status | A | Ghép Host với request-target để xác định tài nguyên; phân biệt phiên bản HTTP với User-Agent; đọc GET/POST/HEAD/PUT cơ bản; status line và header; Content-Length là độ dài thân nội dung, không phải toàn bộ header+body. 200/301/304/400/404/505. | T2 tr.17-30,47,51; E17 tr.61-71 | E01 C1 tr.1, C29-30 tr.6; E02 C22,24 tr.6; E03 C20 tr.4; E08 C7,9,11,13 tr.1-2, C19,23 tr.2-3; E10 C14,24,26 tr.2-3; E20 C11. |
| 2.3. HTTP stateless, cookie, Web cache, conditional GET | A | Stateless là đặc tính giao thức; cookie giúp ứng dụng duy trì trạng thái. Cookie không phải Web cache. Proxy cache có vai trò server với browser và client với origin. If-Modified-Since/Last-Modified và 304: dùng lại bản cache, server không gửi lại body của object đó. | T2 tr.19,31-34,41-47; E17 tr.72-74 (sửa lỗi ở mục 5) | E02 C17 tr.5; E03 C14 tr.3, C22 tr.4; E10 C8 tr.1, C36 tr.4; E20 C1,6. Training E13 C15-17 tr.20-25; E15 Ch2 C1,13 tr.5,9. |
| 2.4. HTTP persistent/nonpersistent; tính RTT; kết hợp DNS | A | Vẽ timeline trước khi thế số; tách TCP setup, request/response, truyền object, DNS; phân biệt tuần tự/song song và có/không pipelining. Chỉ đếm các kết nối thực sự cần mở theo giả định đề. | T2 tr.20-24; E17 tr.63-64,82,94-95 | E02 C18 tr.5; E08 C5,8 tr.1; E10 C2 tr.1; E20 C2. E13 C13-14 tr.18-19 và C22 tr.36-38 là bài luyện mở rộng, không phải bằng chứng đề thật. |
| 2.5. Email: thành phần và đường đi thư; SMTP so với POP/IMAP; mailbox/queue | A | Vẽ UA gửi → server gửi → server nhận → UA nhận; ghi giao thức cho từng chặng theo mô hình slide; Bob tắt máy vẫn có thư trong mailbox ở server nếu server đã nhận; gửi/chuyển mail khác truy xuất thư. SMTP push, HTTP chủ yếu pull. | T2 tr.53-60; E17 tr.76-80 | E01 C26-28 tr.5-6; E02 C1-3 tr.1-2 và C28 tr.7; E03 C8 tr.2, C28 tr.5; E08 C14,20,24,27 tr.2-3; E10 C10,12,15,18,22,27,39 tr.1-4; E20 C12. |
| 2.6. DNS: dịch vụ, phân cấp, local resolver, iterative/recursive, cache/TTL, RR | A | Biết ai được host hỏi đầu tiên, vai trò root/TLD/authoritative/local; đọc sơ đồ mũi tên; đi từ CNAME tới A; phân biệt IP web server, DNS server và mail server. Phân biệt TTL DNS với TTL IP. | T2 tr.62-77; E17 tr.85-95 | E01 C20 tr.4; E02 C13 tr.4-5, C29 tr.7; E03 C7-8 tr.2, C19 tr.3 (câu chữ mơ hồ); E08 C15,17,32 tr.2-3; E10 C16-17,19-21 tr.2. E13 C20-22 tr.30-38 là bài luyện bổ sung. |
| 2.7. Bảng giao thức - vận chuyển - cổng; TLS/HTTPS | A cơ bản | HTTP/TCP/80; SMTP/TCP/25; DNS/UDP hoặc TCP/53; POP3/TCP/110; IMAP/TCP/143; HTTPS qua TLS trong mô hình đang học. Đây là cổng dịch vụ mặc định theo tài liệu/bài tập, không phải mọi kết nối thực tế bắt buộc dùng duy nhất cổng đó. | T2 tr.9,13-15,19,55,60; E17 tr.56,59,83,85 | E01 C14 tr.3; E02 C27-28 tr.6-7; E03 C25 tr.4; E08 C14,18 tr.2; E10 C15,18-20,27,38 tr.2-4; E20 C7,12. |
| Nhận diện mã socket UDP/TCP, phía client/server | B, ngoài bốn mục chi tiết người dùng nêu | SOCK_DGRAM/sendto/recvfrom; SOCK_STREAM/connect; bind/listen/accept; server TCP có socket nghe và socket kết nối. Đủ đọc/nhận diện ví dụ; không cần tự viết app hoàn chỉnh trong lịch cơ sở. | T2 tr.90-99; E17 tr.103-108 | E01 C23 tr.5; E02 C12 tr.4; E15 Ch2 C8-10 tr.7-8. Vì đã có trong đề cũ, nên có 20-30 phút mở rộng nếu phạm vi thi bao gồm phần này. |
| SMTP lệnh, DNS message fields, cache arithmetic | B | HELO → MAIL FROM → RCPT TO → DATA → QUIT; CRLF.CRLF kết thúc DATA trong ví dụ; DNS transaction ID, flags, answer/authority/additional ở mức nhận diện; hit-rate và trung bình độ trễ khi đề cung cấp đầy đủ giả định. | T2 tr.43-47,55-59,75-77 | Có lý thuyết trực tiếp; E13 C21-22 cần RR/RTT chứ chưa đủ căn cứ cho việc học thuộc cấu trúc byte của DNS. Lệnh SMTP chủ yếu xuất hiện ở lịch sử E16 đã loại khỏi căn cứ ưu tiên. |
| HTTP/2, theo dõi cookie/GDPR, DNSSEC/DDoS, DNS registrar; BitTorrent/phân phối P2P | C | Chỉ đọc tổng quan sau khi A vững; khái niệm kiến trúc P2P ở 2.1 vẫn là A. Công thức phân phối tập tin và cơ chế tracker/tit-for-tat thuộc phần P2P riêng, không tự thêm vào phạm vi bốn mục người dùng. | T2 tr.35-40,48-50,67,77-78,80-88 | Không thấy câu tính phân phối file BitTorrent/HTTP2/DNSSEC trong các đề chính E01/E02/E03/E08/E10 đã đọc. Điều này không chứng minh sẽ không thi. |

Trình tự khuyến nghị: kiến thức Ch1 về tầng và delay/RTT → 2.1 → 2.2 → 2.3 → 2.5 → 2.6 → 2.4 nâng từ một object sang nhiều object và DNS+HTTP. Có thể học công thức HTTP một object ngay sau 2.2; để bài tổng hợp DNS+HTTP sau 2.6 sẽ ít học vẹt hơn. Sau đó chuyển Ch3 để hiểu sâu transport thay vì học hết cơ chế TCP ngay trong Ch2.

## 3. Các dạng bài và bẫy cần ghi vào kế hoạch ôn

### HTTP RTT: công thức có điều kiện

Ký hiệu R = RTT giữa browser và Web server; m = số object được HTML cơ sở tham chiếu, nên tổng số object là m+1; t_i = thời gian truyền object i. Những công thức dưới đây dùng mô hình đơn giản của slide: kết nối TCP mới, không TLS, bỏ qua thời gian xử lý và truyền request/header; các object cùng server trừ khi nêu khác.

- Một object, TCP mới: `2R + t_object` (T2 tr.23).
- Nonpersistent, lần lượt từng object: `2(m+1)R + Σt_i`.
- Persistent không pipelining, một kết nối mới: `(m+2)R + Σt_i` = một R khởi tạo TCP cộng một R request/first-byte cho từng object. Ví dụ đúng E20 C2/E13 C13: 1 HTML+5 ảnh, mỗi object 0,5R → `1R + 6R + 6×0,5R = 10R`.
- Persistent có pipelining, m>0, object rất nhỏ, các ảnh chỉ biết sau khi có HTML: `3R` cho một server/kết nối mới (1R setup + 1R HTML + 1R cho loạt request ảnh). Khi truyền object không thể bỏ qua phải phân tích lịch truyền; không tự bỏ Σt hoặc cho rằng mọi body truyền song song trên cùng liên kết.
- Nonpersistent, tối đa p kết nối song song, body không đáng kể: `2R + 2 ceil(m/p)R`. HTML cơ sở phải nhận trước; m ảnh chia theo đợt. Không cộng một R/TCP riêng cho từng ảnh nếu các kết nối trong một đợt thiết lập cùng lúc.
- Nếu phải tra DNS trước và đề cung cấp các RTT DNS độc lập nối tiếp: cộng thời gian DNS đúng theo sơ đồ/giả định, thường `Σ RTT_DNS_i`, rồi mới HTTP. Không tự nhân đôi các RTT đã là round trip.

Bài luyện tốt để tự giải: E20 C2; E08 C8; E13 C22 tr.36-38 (DNS 5+39+48+38=130 ms; Web R=34 ms; 10 ảnh và p=5; bỏ truyền → 130+6×34=334 ms). Đây là phép kiểm tự tính từ mô hình, không phải chấp nhận lời giải đính kèm.

Chốt bẫy: 1 HTML+5 ảnh là 6 object; persistent không đồng nghĩa có pipelining; một server khác có thể cần một kết nối khác; HTTP version dùng trong thông điệp không chứng minh đó là phiên bản cao nhất server hỗ trợ; 304 là dùng lại body đã cache, không phải server gửi lại body mới.

### Đọc request/response

1. Đọc dòng đầu tiên: method + request-target + version hoặc version + status + phrase.
2. Đọc Host, Server, Connection, Content-Length, Content-Type, If-Modified-Since/Last-Modified, Cookie/Set-Cookie theo đúng hướng.
3. Dòng trống ngăn header và body; header ASCII không có nghĩa body của ảnh/audio cũng là văn bản.
4. Đừng nhầm 404 (không có tài nguyên yêu cầu) với không tìm thấy máy chủ, lỗi DNS, hay phiên bản HTTP. 301 là chuyển vị trí vĩnh viễn và Location chỉ vị trí mới.
5. Response 404 vẫn có thể kèm body trang báo lỗi và Content-Length. Không suy ra trang được yêu cầu tải thành công chỉ từ việc có body.

### DNS/RR và sơ đồ truy vấn

- RR dạng `(name, value, type, ttl)`; A: hostname → IPv4; NS: domain → tên authoritative server; CNAME: alias → canonical name; MX: tên miền mail → tên mail exchanger. Giá trị NS/MX là tên, cần bản ghi địa chỉ để tìm IP khi cần. T2 tr.74 và E17 tr.91 là nơi đối chiếu.
- Ví dụ E02 C29 tr.7: theo `www.enterprise.com → west1.enterprise.com → 142.81.17.206` cho web. Địa chỉ trong bản ghi dns.enterprise.com là DNS server; địa chỉ mail.enterprise.com là mail server, không dùng thay IP web.
- Iterative: server được hỏi trả referral; resolver đang tra tự đi hỏi server tiếp theo. Recursive: server được hỏi chịu trách nhiệm tìm/trả lời cho bên đã hỏi. Một quá trình phổ biến có thể chứa host→local kiểu recursive và local→các server khác kiểu iterative; không gán một nhãn chỉ vì thấy local DNS đang làm việc.
- Host thường hỏi local DNS/resolver trước trong mô hình học; cache hit có thể tránh hỏi root/TLD. Root không lưu toàn bộ bản ghi A của mọi web trên Internet. Local DNS không phải tầng thứ tư chính thức trong cây root/TLD/authoritative (T2 tr.69).
- TTL DNS là thời hạn cache; đổi IP có thể còn dữ liệu cache cũ tới khi TTL hết. Không lẫn TTL này với số hop tối đa trong IP.

### Email, socket và port

- Theo sơ đồ slide: bước 2 UA gửi→server gửi và bước 4 server gửi→server nhận dùng SMTP; bước 5 server nhận đặt vào mailbox; bước 6 đọc thư dùng POP3/IMAP hoặc HTTP với webmail. Không dùng SMTP để lấy mail về đọc. T2 tr.56,60; E01 C27-28; E02 C1-3; E10 C39.
- Mailbox là thư đã đến người nhận; message queue ở server gửi là thư chờ gửi. Người nhận offline không đồng nghĩa mail nằm vĩnh viễn trong queue ở server gửi: nếu server người nhận hoạt động và đã nhận thư thì nằm mailbox ở đó.
- SMTP client có thể là mail server đang gửi, không phải cứ gọi client là PC người dùng. Server trong một giao dịch SMTP khác có thể đóng vai client.
- Định danh tiến trình theo T2 tr.9 là IP+port. Khi làm demultiplexing Ch3 phải dùng quy tắc UDP/TCP tương ứng; không áp IP+port một cách máy móc cho mọi kết nối TCP (socket kết nối TCP phân biệt theo 4-tuple).
- Chỉ đọc ví dụ socket: UDP mỗi lần sendto chỉ rõ đích và recvfrom có địa chỉ bên gửi; TCP client connect; TCP server listen/accept và dùng connectionSocket cho dữ liệu, đóng connectionSocket không đồng nghĩa đóng socket nghe.

## 4. Phân bổ thời gian phù hợp người mới, 2-3 giờ/ngày trong 7 ngày

Đề nghị dành **khoảng 5 giờ cho Ch2 trong lịch cơ sở**, sau nền Ch1, rồi còn thời gian Ch3 và luyện tổng hợp. Đây là đề xuất sư phạm, không phải khối lượng học chắc chắn đủ với mọi người.

| Khối | Số phút cơ sở | Sản phẩm tự kiểm cuối khối |
|---|---:|---|
| 2.1 nền ứng dụng + bảng protocol/transport/port | 25 | Tự phân biệt host/process/socket, client-server/P2P; viết bảng cổng từ trí nhớ. |
| 2.2 request/response + method/status | 45 | Tự gạch từng phần của một request và response; làm E01 C1,29-30 hoặc E02 C22,24, giải thích từng lựa chọn sai. |
| 2.3 cookie/cache/conditional GET | 30 | Vẽ hai luồng Set-Cookie/Cookie và If-Modified-Since/304; giải thích vì sao 304 vẫn xem trang thành công khi có cache. |
| 2.5 mail | 35 | Vẽ UA→server→server→UA và chú thích queue/mailbox, SMTP/POP/IMAP/HTTP. |
| 2.6 DNS | 55 | Tự vẽ iterative và recursive; đọc A/NS/CNAME/MX; làm E01 C20/E02 C13,29 không nhìn mẫu. |
| 2.4 bài HTTP/RTT và DNS+HTTP | 55 | Tự vẽ timeline cho 1 object, 1HTML+5 ảnh; làm E20 C2; nếu vững thì E13 C22. |
| Luyện xen kẽ và sửa lỗi | 40 | Làm 15-20 câu Ch2 đã chỉ định, ghi lý do sai chứ không chỉ chữ đáp án. |
| Nhắc lại chủ động hôm sau | 15 | Không xem tài liệu vẫn giải thích được bốn trụ: HTTP/cache, email, DNS, socket/port. |
| **Tổng** | **300 phút** | **5 giờ** |

Nếu chỉ có 2 giờ/ngày: giữ 5 giờ Ch2 cơ sở nhưng chia hai buổi chính khoảng 2 giờ và các khối nhắc lại 15-30 phút; không thêm BitTorrent, chi tiết HTTP/2 hay viết socket hoàn chỉnh. Nếu có thêm 1 giờ: nhận diện mã socket 20-30 phút (do E01/E02 có hỏi), thêm 2-3 bài HTTP với số object khác và chỉnh lỗi DNS 20-30 phút. Nếu người học chưa phân biệt RTT với propagation, quay lại Ch1 trước bài HTTP; không học công thức nhiều object khi còn nhầm hai khái niệm.

Tiêu chí qua Ch2: giải thích được từ đầu một lần truy cập web có DNS, TCP, HTTP, cache; vẽ đúng đường đi email; đọc được RR và sơ đồ truy vấn; làm đúng bài một object và persistent không pipelining kèm lý do. Chỉ tốc độ trắc nghiệm chưa đủ chứng minh đã hiểu.

## 5. Điểm sai, mơ hồ hoặc giản lược cần ghi chú

Các mục sau dùng để tránh học sai, không nhằm thay toàn bộ tài liệu bằng nguồn bên ngoài. Không dựa trên đáp án riêng.

1. **T2 tr.24 và E17 tr.64: “chỉ cần một RTT cho tất cả đối tượng được tham chiếu”.** Phải kèm điều kiện pipelining/giả định đơn giản và bỏ qua hoặc xử lý riêng thời gian truyền. Với persistent **without pipelining**, mỗi object tiếp theo cần một R request/first-byte. E20 C2 và E17 tr.82 tự cho ví dụ 10R, khác với cách hiểu máy móc từ câu này.
2. **E17 tr.54 ghi peer “không thay đổi địa chỉ IP”.** Trái T2 tr.7/80: peer có thể kết nối không liên tục và thay đổi IP, khiến quản lý phức tạp. Dùng T2.
3. **E17 tr.55 định nghĩa “Socket là tiến trình gửi/nhận...”** Diễn đạt làm lẫn process/socket. T2 tr.8/90 mô tả socket như giao diện/cánh cửa giữa process và transport; process sử dụng socket, không đồng nhất hai khái niệm.
4. **E17 tr.72: dòng cookie trong “thông điệp đáp ứng HTTP kế tiếp”.** Hướng đúng trong T2 tr.32-33 và hình E17 tr.73: response mang Set-Cookie; request tiếp theo mang Cookie.
5. **E17 tr.91: dòng MX name = “Tên host”.** Dạy theo T2 tr.74 và ví dụ tr.77: MX gắn tên miền cần nhận thư với tên mail server; không học mẹo “MX cho IP” hay lấy IP DNS server làm IP mail.
6. **E08/E06 C17:** RR `(alpha.com, 123.4.5.7, NS)` dùng một chuỗi IP làm value trong khi NS phải trỏ tên server theo T2 tr.74. Dùng câu này để nhận ra tên miền ở name, nhưng không xem RR đó là mẫu cấu hình DNS đúng. C21 còn có lựa chọn NFS cũng là ứng dụng; vì vậy không lấy dạng “chỉ HTTP thuộc application” làm quy tắc.
7. **E15 Ch2 C21 tr.11-12:** cho RTT=0,00041s cùng khoảng cách 1000km, propagation 2,7×10^8m/s; riêng một chiều d/s≈3,70ms đã lớn hơn RTT đó. Hướng dẫn lại cộng `2RTT + L/R + d/s`, dễ đếm propagation thêm vào RTT đã là round trip. Dữ kiện không nhất quán; không lấy bài này làm bài chuẩn và không ép ra đáp án 5ms. Dùng E20 C2/E13 C22 thay.
8. **E15 Ch2 C18 tr.11:** response Content-Length=8347 nhưng lựa chọn A ghi tổng 8327 bytes, lựa chọn D suy diễn HTTP1.1 là phiên bản cao nhất server hỗ trợ; có nhiều phát biểu không bảo đảm. Không dùng làm câu một đáp án chắc chắn. Content-Length còn không phải tổng số byte toàn bộ response.
9. **E03 C19 tr.3:** “local DNS tự truy vấn tiếp các máy chủ khác” chưa tự nó phân biệt iterative với recursive; cần xem server trả referral hay nhận trách nhiệm phân giải thay. Khi luyện phải vẽ luồng; không học một từ khóa “tự truy vấn” = nhãn cố định.
10. **E03 C22 tr.4:** cache giúp giảm traffic/độ trễ và tải access link, không tự nâng băng thông vật lý đường truyền. Câu dùng chữ “tăng băng thông” nên hiểu thận trọng như khả năng phục vụ hiệu dụng, không học thành định luật.
11. **E13 tr.31 giải thích load distribution bằng “dùng nhiều DNS server”.** Dịch vụ load distribution ở T2 tr.63 là một tên có nhiều IP ứng với các server nội dung bản sao; đừng lẫn cơ sở dữ liệu DNS phân tán với cân bằng tải của dịch vụ web.
12. **E13 tr.27 nói SMTP chỉ text/plain.** T2 tr.58 nói mô hình SMTP cơ sở 7-bit; không suy ra email chỉ có plain text và không có ảnh/tệp đính kèm. Chỉ học cơ chế ở phạm vi slide; phần encoding/mở rộng không cần thêm vào lịch một tuần.
13. **T2 tr.9/62 và E17 tr.56 “mỗi host một IP32-bit duy nhất” là mô hình IPv4 giản lược.** Không biến nó thành khẳng định mọi thiết bị Internet chỉ có một IP hoặc Internet chỉ có IPv4; không cần mở rộng IPv6/NAT ngoài phạm vi để giải các câu Ch2 này.
14. **T2 tr.39,67-68 có số liệu/chính sách theo thời điểm soạn.** Câu dự báo Chrome bỏ third-party cookie vào 2023, số bản sao root, nhà quản lý TLD là thông tin theo thời gian, không dùng làm trọng tâm hay khẳng định hiện trạng 2026 từ slide cũ. Không cần tra bên ngoài vì người dùng yêu cầu chỉ dùng đề/tài liệu hiện có.

## 6. Phần ngoài phạm vi ba chương đang ôn

E14 từ khoảng P386 trở đi đi sang subnet/IPv4 chi tiết, NAT, phân mảnh, định tuyến vector khoảng cách/trạng thái liên kết, RIP/OSPF/BGP, MAC/ARP/switch, Aloha/CSMA/Token Passing, Ethernet và mã vật lý. Đã đọc để kiểm phạm vi, nhưng không thêm vào lịch Ch1-3 chỉ vì chúng có trong ngân hàng.

Trong Ch2 T2, kiến trúc P2P ở phần nguyên lý vẫn cần biết; **công thức phân phối file/BitTorrent** (tr.81-88) và **lập trình socket chi tiết** (tr.90-99) là hai mục riêng ngoài bốn nhóm chi tiết người dùng liệt kê. Lịch cơ sở ưu tiên bốn nhóm; socket nhận diện được đánh dấu mở rộng vì E01/E02 có hỏi. FTP chỉ cần biết tên/vai trò/cổng khi ghép giao thức trong đề; không tự đưa toàn bộ hoạt động FTP vào trọng tâm Ch2 khi outline người dùng không liệt kê.

## 7. Tệp trung gian do agent này tạo

- `ch2_analysis.md`: báo cáo này.
- `ch2_render.py` và `ch2_figures_1.png` đến `ch2_figures_6.png`: render/contact sheet đọc sơ đồ E17 và hình mail E10/E15; không sửa file nguồn.

Phạm vi kiểm tra này đã hoàn tất đối với Chương 2. Quyết định lịch chung 7 ngày, nguồn còn lại và memory.md thuộc agent điều phối.
