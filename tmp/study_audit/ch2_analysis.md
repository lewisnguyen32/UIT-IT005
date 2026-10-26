# Chương 2 - Tầng ứng dụng: phân tích 5 đề theo phạm vi cuối

Ngày: 2026-10-22. Cập nhật sau khi người dùng bổ sung hai đề trong folder 2023 và 2024: dùng E01/E02/E03/E08/E10 và T2. Không lấy đề online. Đây là căn cứ lập kế hoạch ôn, không phải đáp án chính thức hay dự đoán xác suất ra đề.

## 1. Phạm vi đọc và nguồn được dùng

Đã đọc hết T2 `[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf`, đủ trang vật lý 1-105, kể cả phần P2P và lập trình socket nằm ngoài bốn nhóm tiêu đề Ch2 người dùng nêu. Nguồn chính cho kế hoạch là tài liệu này. Khi chỉ trang, luôn tính trang vật lý PDF từ 1.

Đã đọc hết tất cả câu hỏi của năm đề được giữ lại và kiểm hình những câu Ch2:

- **E01** `[BHT CNPM] NMMMT 2019-2020 GK1.pdf`: 6 trang/30 câu. Đã đọc toàn bộ E01_ocr.txt; đối chiếu hình trang 1,3-6 cho các câu Ch2. OCR tiếng Việt có lỗi nên không chỉ dựa OCR cho câu/sơ đồ được trích dẫn.
- **E02** `[BHT CNPM] NMMMT 2020-2021 GK1.pdf`: 7 trang/30 câu. Đã đọc toàn bộ E02_ocr.txt; đối chiếu hình trang 1-2,4-7 cho các câu Ch2.
- **E03** `[BHT CNPM] NMMMT 2025-2026 GK1.pdf`: 6 trang/30 câu. Đây là đề được BHT sưu tập/soạn lại sau thi và có đáp án tham khảo không chính thức ở trang 6, được người dùng chấp nhận dùng. Dùng câu hỏi làm bằng chứng kiến thức; không lấy bảng đáp án làm chuẩn.
- **E08** `Nhập Môn Mạng Máy Tính/2023/Đề A MMT.pdf`: 4 trang/40 câu, được người dùng yêu cầu tính thêm. E06 DOCX trùng cùng bộ câu E08 nên không đếm riêng, không lấy đáp án chèn trong E06 làm chuẩn.
- **E10** `Nhập Môn Mạng Máy Tính/2024/2024.pdf`: 4 trang/42 câu, được người dùng yêu cầu tính thêm. C42 checksum nằm cuối trang 4, đã đọc đủ. Đã xem ảnh trang 4 để đọc rõ sơ đồ mail C39.

Không mở ba file đáp án riêng. Các file E13/E14/E15/E16/E20 và slide tổng hợp E17 từng được đọc để sàng lọc trước khi người dùng thu hẹp phạm vi; **không dùng chúng làm bằng chứng ưu tiên hay bài luyện trong báo cáo này**. E19 online bị loại. Bản đọc rộng chỉ lưu tạm trong `ch2_analysis_broad_internal.md`, không đưa vào bản ôn chính.

## 2. Kiểm đếm nhất quán Ch2 trong 172 câu

Mỗi câu chỉ gán một chương chính. Câu socket code/client-server/IP+port và câu ghép giao thức liên chương được gán Ch2; câu dịch vụ TCP/UDP và demultiplexing thuộc Ch3. Nhận diện tầng đơn giản và định nghĩa RTT thuộc Ch1. Do đó E02 C10-11, E08 C10,27,28,37, E10 C21,37 không đếm vào Ch2; E08 C31 định nghĩa RTT thuộc Ch1.

| Đề | Câu Ch2 | Số câu |
|---|---|---:|
| E01 | 1,14,20,22,23,26,27,28,29,30 | 10 |
| E02 | 1,2,3,12,13,17,18,22,24,27,28,29 | 12 |
| E03 | 2,6,7,8,10,14,19,20,22,25,28 | 11 |
| E08 | 5,7,8,9,11,13,14,15,16,17,18,19,20,22,23,24,25,26,29,30,32 | 21 |
| E10 | 2,8,9,10,12,13,14,15,16,17,18,19,20,22,24,26,27,28,36,38,39 | 21 |
| **Tổng** | Đã kiểm đủ 30+30+30+40+42 câu; số theo quy tắc gán một chương | **75** |

Phân nhóm chính trong riêng Ch2, không đếm trùng giữa các dòng:

| Nhóm chính | E01 | E02 | E03 | E08 | E10 | Tổng |
|---|---|---|---|---|---|---:|
| Nguyên lý ứng dụng/socket/client-server/P2P | C22,23 | C12 | C2,6,10 | C22,25,26,29 | C9 | 11 |
| Ghép giao thức, dịch vụ, transport, cổng/FTP | C14,26 | C27,28 | C8 | C14,16,18 | C13,15,18,19,20,27,28,38 | 16 |
| Web/HTTP, cache/cookie, TLS | C1,29,30 | C17,18,22,24 | C14,20,22,25 | C5,7,8,9,11,13,19,23,30 | C2,8,14,24,26,36 | 26 |
| Mail/SMTP/truy xuất thư | C27,28 | C1,2,3 | C28 | C20,24 | C10,12,22,39 | 12 |
| DNS | C20 | C13,29 | C7,19 | C15,17,32 | C16,17 | 10 |
| **Tổng** | **10** | **12** | **11** | **21** | **21** | **75** |

Số câu trên chỉ mô tả năm đề được giữ lại theo quy tắc gán chương. Không coi 75/172 là tỷ lệ chắc chắn của đề sắp thi, không coi mỗi nhóm có đúng số điểm tương ứng. Nhiều câu E08/E10 trùng nhau và trùng các đề khác; không coi số lần lặp là các quan sát độc lập về xác suất ra thi. Không dùng ngân hàng hoặc bản sao để làm tăng tần suất.

## 3. Các phần cần học và thứ tự

Mức **A**: phải hiểu và tự giải thích/làm được trong tuần; **B**: sau A, luyện mức cơ bản; **C**: đọc sau nếu còn thời gian hoặc giảng viên xác nhận có thi. Đây là quyết định học tập theo nội dung và bằng chứng hiện có, không phải khẳng định C sẽ không thi.

| Phần | Mức | Mục tiêu hiểu | T2 nên học | Câu làm căn cứ/luyện |
|---|---|---|---|---|
| 2.1. Tiến trình - socket - client/server - P2P | A | Host khác process; process sử dụng socket; IP+port trong mô hình định danh tiến trình. Client khởi tạo liên lạc, server chờ. Peer có thể vừa chia sẻ vừa nhận dữ liệu. | tr.3-10 | E01 C22-23 tr.5; E02 C12 tr.4; E03 C2,6 tr.1 và C10 tr.2; E08 C22,25-26,29 tr.2-3; E10 C9 tr.1. |
| 2.2. Nhu cầu ứng dụng và bảng giao thức/cổng | A | HTTP/TCP/80; SMTP/TCP/25; DNS/53 (E10 nêu UDP); POP3/110; FTP cổng điều khiển21. Biết vai trò IMAP, không cần thêm cổng IMAP vào danh sách trọng tâm khi nguồn được giữ không hỏi. TCP không tự mã hóa. Đặc tính TCP/UDP học sâu ở Ch3. | tr.9,11-15,19,55,60; cổng DNS/POP3/FTP đối chiếu câu ghép E01/E08/E10. Không nói T2 có liệt kê đủ mọi cổng. | E01 C14 tr.3,C26 tr.5; E02 C27 tr.6,C28 tr.7; E03 C8 tr.2,C25 tr.4; E08 C14,16,18 tr.2; E10 C13,15,18-20,27-28,38 tr.2-4. |
| 2.3. Web/HTTP request-response | A | Base HTML+object; URL; method GET/POST/HEAD/PUT; request line/status line/header/body; Host/Server/Connection/Content-Length; phiên bản HTTP khác User-Agent. Biết 200/301/304/400/404/505. | tr.17-30,47,51 | E01 C1 tr.1,C29-30 tr.6; E02 C22,24 tr.6; E03 C20 tr.4; E08 C7,9,11,13,19,23,30 tr.1-3; E10 C14,24,26 tr.2-3. |
| 2.4. HTTP stateless; cookie; Web cache; conditional GET | A | Stateless ở giao thức không cấm ứng dụng dùng cookie giữ phiên. Cookie không phải cache. Cache giảm traffic và độ trễ. Set-Cookie trong response, Cookie trong request tiếp theo. 304 dùng lại bản đã cache, không gửi lại body mới. | tr.19,31-34,41-47 | E02 C17 tr.5; E03 C14 tr.3,C22 tr.4; E10 C8 tr.1,C36 tr.4. |
| 2.5. HTTP persistent/nonpersistent và RTT | A cho khái niệm/công thức một object; B cho nhiều object | Nonpersistent một object/kết nối; persistent tái dùng kết nối. Một object: 1RTT TCP setup+1RTT request/first-byte+transmission. Phân biệt persistent không/có pipelining trước bài nhiều object. | tr.20-24 | E02 C18 tr.5; E08 C5,8 tr.1; E10 C2 tr.1. Năm đề giữ lại không có bài tính HTTP nhiều object/DNS+HTTP bằng số; tính nâng cao là mở rộng từ lý thuyết. |
| 2.6. Email, SMTP, POP/IMAP, mailbox/queue | A | Vẽ đường đi UA→server gửi→server nhận→UA; gán SMTP cho gửi/chuyển mail và POP/IMAP/HTTP cho đọc thư theo mô hình slide. SMTP push, HTTP chủ yếu pull; người nhận offline không cản server nhận thư vào mailbox. | tr.53-60 | E01 C26-28 tr.5-6; E02 C1-3 tr.1-2,C28 tr.7; E03 C8 tr.2,C28 tr.5; E08 C20,24 tr.2-3; E10 C10,12,22,39 tr.1-4. |
| 2.7. DNS: chức năng/phân cấp/tra cứu/cache/RR | A | Local resolver trước; vai trò root/TLD/authoritative/local; iterative khác recursive qua ai hỏi tiếp và ai trả referral/kết quả; CNAME→A; phân biệt IP DNS/mail/web. RR `(name,value,type,ttl)`: A,NS,CNAME,MX. TTL cache DNS khác TTL IP. | tr.62-77 | E01 C20 tr.4; E02 C13 tr.4-5,C29 tr.7; E03 C7 tr.2,C19 tr.3 (câu chữ cần thận trọng); E08 C15,17,32 tr.2-3; E10 C16-17 tr.2. |
| 2.8. Nhận diện mã socket đơn giản | B, nhưng nên dành 15-20 phút vì có trong đề giữ lại | SOCK_DGRAM/sendto/recvfrom là UDP; SOCK_STREAM/connect là TCP client; listen/accept là TCP server. Server TCP dùng socket nghe và socket kết nối; nhận diện vai trò, chưa cần viết ứng dụng hoàn chỉnh. | tr.90-99 | E01 C23 tr.5; E02 C12 tr.4. Đặt trong phần nguyên lý/phụ lục ngắn, dù outline người dùng không có một mục lập trình riêng. |
| SMTP commands; DNS message fields; bài hit-rate/cache và RTT nhiều object | B/C tùy giờ | Sau nền A, đọc ví dụ; không học thuộc chi tiết bằng cách suy ra từ nguồn đã loại. | tr.43-47,55-59,75-77 | Chưa có câu trực tiếp trong năm đề được giữ lại đủ để đặt lên trước nội dung A. |
| P2P phân phối file/BitTorrent, HTTP/2, tracking/GDPR, DNSSEC/DDoS/registrar | C | Kiến trúc P2P ở 2.1 vẫn A; các cơ chế/công thức sâu là phần bổ sung. | tr.35-40,48-50,67,77-78,80-88 | Không có câu trực tiếp trong E01/E02/E03/E08/E10 đã đọc. Điều này không chứng minh sẽ không thi. |

Trật tự để người mới đỡ học vẹt: sau Ch1 về tầng, delay/RTT → **2.1-2.2 → 2.3 → 2.4 → khái niệm 2.5 → 2.6 → 2.7 → nhận diện 2.8 → bài tính HTTP mở rộng nếu còn giờ**. Trước bài DNS+HTTP phải hiểu từng cơ chế riêng. Không cần học toàn bộ TCP/RDT Ch3 trước mới bắt đầu HTTP, chỉ cần biết TCP mở kết nối và cung cấp byte stream tin cậy.

## 4. Các bẫy đúng phạm vi tài liệu và đề giữ lại

### Đọc HTTP

- E01 C1: `301 Moved Permanently` và `Location` là tài nguyên chuyển vị trí; không phải 404/xóa tài nguyên hay lỗi phiên bản HTTP.
- E01 C29-30: `HTTP/1.1` và `Connection: keep-alive` phải đọc đúng; status 404 không đồng nghĩa đối tượng được yêu cầu đã được trả thành công. Response vẫn có thể chứa body trang báo lỗi.
- E02 C24: `Content-Length: 600` là độ dài nội dung, khác toàn bộ response; `Date` không phải `Last-Modified`; 404 không có nghĩa phiên bản HTTP1.1 không tìm thấy.
- E02 C22 và T2 tr.27: GET có thể mang dữ liệu trong URL sau dấu `?`; POST thường mang dữ liệu form trong body. Không học “GET không bao giờ gửi dữ liệu”.
- Nonpersistent đóng kết nối sau một object; persistent tái sử dụng một TCP connection cho nhiều object với cùng server. Persistent không tự đồng nghĩa pipelining.
- T2 tr.24 “1RTT cho tất cả object tham chiếu” cần điều kiện pipelining/giả định đơn giản. Không áp vào persistent **without pipelining**; mỗi request tuần tự tiếp theo vẫn cần một RTT request/first-byte.
- E03 C22 dùng cụm “tăng băng thông”. Cache giảm traffic/độ trễ và giảm tải access link; không tự tăng dung lượng vật lý của đường truyền.
- E10 C8 liên quan Last-Modified/If-Modified-Since; E10 C36 cần hiểu 304 dùng bản đã cache. Không diễn giải 304 như một response chứa body mới hoặc coi có status 3xx thì luôn thất bại khi xem nội dung.

### Email

- Theo sơ đồ T2 tr.56,60: bước 2 UA gửi→server gửi và bước 4 server gửi→server nhận là SMTP; bước 5 đặt vào mailbox; bước 6 truy xuất/đọc thư dùng POP3, IMAP hoặc HTTP cho webmail. E01 C27-28/E02 C1-3 chính là các bước này.
- Mailbox: thư đến người nhận; message queue: thư chờ gửi. Người nhận tắt máy không có nghĩa thư phải ở queue server gửi nếu server nhận đã nhận thư.
- SMTP client có thể là mail server đang gửi. Đừng đồng nhất từ client với PC của người dùng trong mọi giao dịch.
- E03 C28: SMTP không phải giao thức lấy thư về đọc; IMAP không phải giao thức gửi thư. Khả năng truyền tin cậy đến từ TCP trong mô hình này; không lẫn chức năng ứng dụng và dịch vụ transport.
- T2 tr.58 mô tả SMTP cơ sở với ASCII7-bit; không suy ra email không thể có hình/attachment. Phần encoding/mở rộng không cần đưa vào lịch cơ sở.

### DNS

- E01 C20/E02 C13: xem mũi tên. Local DNS hỏi lần lượt root, TLD, authoritative và nhận referral ở mỗi bước là mô hình iterative trong hình. Không chỉ đọc một từ khóa.
- E03 C19 “local DNS tự truy vấn tiếp các máy chủ khác” chưa đủ tự thân để phân biệt mọi trường hợp recursive/iterative. Recursive: server được hỏi nhận trách nhiệm phân giải thay và trả kết quả; iterative: server được hỏi trả referral rồi resolver hỏi tiếp. Một quá trình có thể gồm host→local kiểu recursive và local→các server khác kiểu iterative. Không luyện câu này bằng cách nhớ một chữ đáp án.
- Host thường gửi đến local DNS/resolver trước theo T2 tr.69; cache hit có thể bỏ qua root/TLD. Root không lưu mọi bản ghi A của Internet; local DNS không hẳn thuộc cây root/TLD/authoritative.
- RR A hostname→IPv4; NS domain→tên authoritative server; CNAME alias→canonical; MX domain mail→tên mail exchanger. Value của NS/MX là tên, không phải IP. E02 C29: `www.enterprise.com → west1.enterprise.com → 142.81.17.206` cho web; không chọn IP dns.enterprise.com hay mail.enterprise.com.
- RR minh họa E02 C29 còn đặt CNAME và MX dưới cùng owner www.enterprise.com. Chỉ dùng phần CNAME→A để luyện đọc ánh xạ, không sao chép toàn bộ danh sách làm cấu hình DNS thực tế đúng.
- E08 C17 in RR `(alpha.com,123.4.5.7,NS)`, trong khi T2 tr.74 mô tả NS value là tên server. Không học RR này thành mẫu cấu hình đúng; tập phân biệt ý nghĩa name/value theo T2. E08 C15 dùng từ “tên viết tắt”, nên diễn đạt chính xác là bí danh→tên chính tắc chứ không phải thao tác rút gọn chuỗi.
- TTL DNS là thời hạn cache, không phải số hop IP. Đổi IP có thể còn cache cũ tới khi TTL hết; T2 tr.73.

### Socket/TCP-UDP/TLS

- IP+port là cách định danh process/đầu socket trong cách trình bày ứng dụng T2 tr.9. Khi học demultiplexing Ch3, socket TCP kết nối còn phân biệt bằng 4-tuple; không đem IP+port áp máy móc cho mọi kết nối.
- T2 tr.15 và E03 C25: TCP/UDP tự nó không mã hóa; HTTPS trong mô hình đang học thêm TLS. Không nói TCP tin cậy nghĩa là an toàn/mã hóa.
- T2 tr.9/62 nói IP32-bit và một host một địa chỉ là mô hình IPv4 giản lược; không biến thành kết luận mọi thiết bị chỉ có một IP hoặc Internet chỉ có IPv4.
- Nhận diện mã theo SOCK_STREAM/SOCK_DGRAM và API, không chỉ tên biến. E02 C12 có cú pháp connect được in theo dạng giản lược/thiếu tuple; đó là câu nhận diện TCP, không dùng nguyên đoạn làm chương trình mẫu chạy được.

## 5. Công thức HTTP để ôn mức B, ghi điều kiện trước khi dùng

R = RTT browser-Web server; m là số object được HTML cơ sở tham chiếu, tổng object là m+1; t_i là thời gian truyền object. Mô hình: kết nối TCP mới, không TLS, cùng server, bỏ thời gian xử lý và truyền request/header.

| Trường hợp | Biểu thức trong mô hình đơn giản |
|---|---|
| Một object qua TCP mới | `2R + t_object` |
| Nonpersistent, các object lấy tuần tự | `2(m+1)R + Σt_i` |
| Persistent không pipelining, một kết nối mới | `(m+2)R + Σt_i` |
| Persistent có pipelining, m>0, body rất nhỏ | `3R` = setup+HTML+loạt ảnh |
| Nonpersistent, tối đa p TCP song song, body rất nhỏ | `2R + 2 ceil(m/p)R` |

Nếu không có giả định body rất nhỏ/bỏ qua truyền body, phải giữ thời gian truyền và xét chia sẻ link/lịch truyền; không tự cho mọi body truyền đồng thời trên một liên kết. Nếu đề nêu DNS nối tiếp trước HTTP, cộng thời gian DNS đúng theo sơ đồ. RTT đã gồm đi-về, không cộng lại propagation cho cùng hành trình. Một object là dạng A có E08C8/E10C2; các biến thể nhiều object/DNS+HTTP là B suy ra từ T2, không phải dạng đã thấy ở năm đề giữ lại. Không dùng câu bị loại làm bài chuẩn.

## 6. Khối thời gian Ch2 trong tuần, 2-3 giờ/ngày và người mới

Đề xuất **4 giờ Ch2 cơ sở, gồm cả nghỉ**, trong lịch 14 giờ tối thiểu; có thể thêm 60 phút nếu dùng quỹ tăng cường 2-3 giờ/ngày. Agent điều phối sẽ đặt vào lịch chung để dành đủ Ch1, Ch3 và làm đề. Mục tiêu cơ sở là đạt các kỹ năng A ở mức giải thích được/làm được câu cơ bản, không cam kết nắm chuyên sâu toàn bộ 105 trang trong bốn giờ.

| Khối | Phút cơ sở | Đầu ra tự kiểm |
|---|---:|---|
| Nguyên lý ứng dụng + bảng giao thức/cổng + nhận diện socket | 35 | Phân biệt host/process/socket; giải thích client-server/P2P; nhận ra TCP server/client trong E01C23/E02C12. |
| HTTP request/response, method/status/header | 35 | Chỉ đúng từng trường; làm E01C1,29-30/E02C22,24 và giải thích lựa chọn sai. |
| Cookie/cache/conditional GET | 20 | Tự vẽ Set-Cookie/Cookie và If-Modified-Since/304; giải thích cache giảm traffic. |
| Mail | 25 | Vẽ UA→server→server→UA; chú thích SMTP/POP/IMAP/HTTP, queue/mailbox; làm E01C27-28/E02C1-3. |
| DNS | 40 | Vẽ iterative/recursive; làm E01C20/E02C13,29; phân biệt A/NS/CNAME/MX. |
| Nonpersistent/persistent, RTT một object | 20 | Hiểu 2RTT+transmission; làm E08C5,8/E10C2 và giải thích vì sao có hai RTT. |
| Luyện câu giữ lại và chữa lý do sai | 35 | Chọn 15-20 câu Ch2 rải trong năm đề; phần làm nguyên đề nằm quỹ luyện tổng hợp của kế hoạch chung. Không dùng đáp án tham khảo che chỗ chưa hiểu. |
| Nhắc lại chủ động hôm sau | 10 | Tự kể một lần mở web cần DNS/HTTP/cache và một lần gửi/đọc mail. |
| Nghỉ ngắn xen kẽ | 20 | Chia thành các lần nghỉ, không gộp vào số phút học hiệu dụng. |
| **Tổng cơ sở** | **240** | **4 giờ, gồm 20 phút nghỉ** |

Nếu người học chưa phân biệt RTT/transmission/propagation, dành khối RTT quay lại Ch1 thay vì tăng độ khó. Nếu chỉ đủ thời gian tối thiểu: giữ các khối A và nhận diện hai câu socket cũ; chuyển tính HTTP nhiều object, HTTP2/BitTorrent/chi tiết message DNS ra phần thêm giờ. Nếu có thêm 60 phút, dành khoảng 35 phút chữa/làm thêm câu Ch2 chưa làm trong năm đề, 15 phút đọc sâu điểm A còn yếu ở T2 và 10 phút nghỉ. Như vậy mức tăng cường là **300 phút/5 giờ gồm nghỉ**. Không cần tự tạo bài mới và không dùng bài tập/training bị loại.

## 7. Phần không tự đưa vào trọng tâm

- P2P architecture thuộc nguyên lý: vẫn học. Công thức phân phối file, tracker/tit-for-tat BitTorrent (T2 tr.81-88) và tự viết socket app hoàn chỉnh (tr.90-99) không được tự nâng lên trọng tâm chỉ vì có trong slide.
- HTTP2, chi tiết theo dõi cookie/GDPR, DNSSEC/DDoS/registrar: đọc thêm sau nền A. Những số liệu/chính sách theo thời điểm ở T2 tr.39,67-68 không được dùng làm khẳng định hiện trạng 2026.
- FTP: trong E01/E02/E08/E10 có ghép tên/vai trò/cổng, nên chỉ nhận diện FTP và cổng điều khiển 21 đủ cho những câu đã giữ. Không thêm một mục cơ chế FTP dài vào outline bốn phần Ch2.
- Không đưa subnet, NAT/phân mảnh, routing chi tiết, ARP/MAC/switch, Aloha/CSMA/Ethernet từ ngân hàng bị loại vào lịch ba chương.

Tệp tạm phục vụ xem hình do agent tạo: ch2_render.py và ch2_figures_1.png đến ch2_figures_6.png. Hình của nguồn bị loại chỉ là vết đọc nội bộ trước khi thu hẹp, không là bằng chứng bản ôn chính. File nguồn được giữ nguyên. Báo cáo Ch2 strict đã hoàn tất; lịch chung, output chính và memory.md do agent điều phối quản lý.
