# Tổng hợp kiến thức NMMMT — ba chương

Bản tra nhanh ngày 30/10/2026: mỗi mục 1–2 câu, riêng phần nhiều cơ chế có thể dài hơn. Chỉ tổng hợp phần đã chốt học; Chương3 dừng ở T3 trang PDF94, không gồm TCP điều khiển tắc nghẽn và QUIC/HTTP3. EstimatedRTT vẫn tùy chọn, không đưa vào phần chính.

## Chương 1 — Giới thiệu mạng máy tính

Nguồn chính: [T1 — Chương1](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf>), nhóm trang PDF3–35,46–56,58–67.

- **Internet và ISP:** Internet là mạng của các mạng, nối các thiết bị đầu cuối qua liên kết và thiết bị chuyển tiếp. ISP cung cấp kết nối và liên kết với các mạng khác để tạo khả năng liên lạc rộng hơn.
- **Giao thức:** Quy định khuôn dạng, thứ tự thông điệp và hành động khi gửi/nhận. Hai bên phải tuân cùng quy tắc để trao đổi đúng.
- **Mạng biên và host:** Host là thiết bị đầu cuối chạy ứng dụng; client thường khởi tạo yêu cầu, server cung cấp dịch vụ. Mạng biên là nơi các ứng dụng nguồn/đích hoạt động.
- **Mạng truy cập:** Nối host với router đầu tiên trên đường vào mạng; ví dụ Ethernet, Wi-Fi, DSL, cable và mạng di động. Không nhầm mạng truy cập với toàn bộ mạng lõi.
- **Môi trường truyền:** Cáp đồng/cáp quang là môi trường hữu tuyến; vô tuyến truyền tín hiệu qua không gian. Tốc độ truyền dữ liệu và tốc độ lan truyền tín hiệu là hai đại lượng khác nhau.
- **Mạng lõi/chuyển mạch gói:** Mạng lõi gồm các router liên kết với nhau; dữ liệu được chia thành gói, các luồng chia sẻ tài nguyên liên kết theo nhu cầu. Gói có thể phải chờ ở hàng đợi khi đầu ra bận.
- **Chuyển mạch kênh:** Tài nguyên được dành riêng cho kết nối; phần đã cấp có thể bị bỏ trống lúc không truyền. Không có kết luận chung rằng chuyển mạch kênh hoặc gói luôn nhanh hơn.
- **FDM và TDM:** FDM chia theo dải tần; TDM chia theo khe thời gian. Trong mô hình chuyển mạch kênh, mỗi kết nối dùng phần được cấp cho mình.
- **Forwarding và routing:** Forwarding đưa gói từ đầu vào sang đầu ra phù hợp tại một router. Routing xác định đường đi nguồn–đích và làm cơ sở cho các bảng chuyển tiếp.
- **Store-and-forward:** Router phải nhận đủ một gói rồi mới phát gói đó lên liên kết kế tiếp. Một gói qua nhiều liên kết vì thế phải chịu thời gian truyền ở từng liên kết.
- **Đổi đơn vị:** 1 byte=8 bit, 1 Mbps=10^6 bit/s, 1 km=1000 m, 1 s=1000 ms; bps khác B/s. Tốc độ truyền R tính bằng bit/s, tốc độ lan truyền s tính bằng m/s.
- **Trễ xử lý:** Thời gian nút kiểm tra/xử lý gói và xác định đầu ra. Nếu đề cho trễ xử lý tại router, cộng đúng số lần xử lý được nêu.
- **Trễ hàng đợi:** Thời gian gói chờ được phát lên liên kết, phụ thuộc tải và trạng thái hàng đợi. Với cường độ tải La/R, L là bit/gói, a là gói/s và R là bit/s; tải gần khả năng phục vụ làm trễ hàng đợi tăng mạnh trong mô hình của slide.
- **Trễ truyền:** d_trans=L/R là thời gian đẩy đủ L bit lên liên kết tốc độ R. Gói dài hơn làm trễ này tăng; R lớn hơn làm trễ này giảm.
- **Trễ lan truyền:** d_prop=d/s là thời gian tín hiệu đi qua khoảng cách d với tốc độ lan truyền s. Gói dài hơn không tự làm trễ này tăng; tăng R không tự làm trễ này giảm.
- **Tổng độ trễ:** Tại một nút, d_nodal=d_proc+d_queue+d_trans+d_prop; một gói qua nhiều liên kết store-and-forward, bỏ xử lý/hàng đợi thì d_end-to-end=Σ(L/R_i)+Σ(d_i/s_i). Không thay tổng thời gian truyền bằng L/min(R_i).
- **Hàng đợi đầy và mất gói:** Gói đến có thể bị loại khi bộ đệm không còn chỗ. Việc có phát lại hay không phụ thuộc giao thức và cơ chế bên trên.
- **Thông lượng:** Là tốc độ dữ liệu thực sự được chuyển; với một luồng qua các liên kết nối tiếp trong mô hình không cạnh tranh/bỏ overhead, T=min(R_i). Nếu n luồng chia sẻ công bằng liên kết R thì phần của mỗi luồng tại liên kết đó là R/n, vẫn chịu các nút thắt khác.
- **Số gói phát được:** Bỏ overhead, số gói nguyên vẹn L bit phát được trong t giây là floor(Rt/L). Đây là số gói phát lên liên kết, không phải số gói chắc chắn đã tới đích.
- **RTT:** Thời gian cho một lượt đi và quay về, khác trễ một chiều và thời gian tải toàn bộ tệp. Chỉ dùng RTT=2d/s khi mô hình cho phép bỏ các trễ khác và hai chiều tương ứng.

**Năm tầng Internet và đơn vị dữ liệu:**

| Tầng | Vai trò | PDU |
|---|---|---|
| Ứng dụng | Hỗ trợ trao đổi thông điệp của ứng dụng, như HTTP/DNS/SMTP. | Message |
| Vận chuyển | Truyền thông process–process tại hai đầu cuối, bằng TCP/UDP. | Segment; UDP thường gọi datagram |
| Mạng | Chuyển dữ liệu host–host qua mạng, như IP. | Datagram/packet |
| Liên kết | Chuyển dữ liệu giữa các nút lân cận trên liên kết, như Ethernet/Wi-Fi. | Frame |
| Vật lý | Truyền các bit qua môi trường vật lý. | Bit |

- **Đóng/mở gói:** Khi gửi, dữ liệu đi theo message→segment→datagram→frame→bit; bên nhận xử lý theo chiều ngược lại. Các tầng vận chuyển/mạng/liên kết thêm thông tin điều khiển tương ứng; tầng vật lý truyền bit, không phải mọi tầng đều thêm header.
- **Host, switch và router:** Trong mô hình chuyển tiếp cơ bản, host có đủ năm tầng; switch xét đến tầng liên kết, router xét đến tầng mạng. Không gán chức năng xử lý TCP/HTTP cho switch hoặc router chỉ vì chúng chuyển tiếp gói mang những dữ liệu đó.

## Chương 2 — Tầng ứng dụng

Nguồn chính: [T2 — Chương2](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf>), nhóm trang PDF3–34,41–47,51,53–77,90–99. Sau đề mẫu cô cung cấp ngày30/10, các mục đánh dấu bổ sung và bảng cổng được đối chiếu thêm RFC/IANA ở cuối bản; đây là nguồn làm rõ, không thay T2 làm nguồn chính.

- **Client–server:** Trong mô hình slide, server cung cấp dịch vụ, hoạt động liên tục và có IP cố định; client khởi tạo yêu cầu, có thể đổi IP/kết nối không liên tục. Trong kiến trúc client–server thuần túy, client không trực tiếp cung cấp dịch vụ cho nhau như P2P.
- **P2P:** Peer vừa có thể yêu cầu vừa cung cấp dịch vụ cho peer khác. Thêm peer vừa tăng nhu cầu, vừa có thể tăng tài nguyên phục vụ.
- **Process và socket:** Process là chương trình đang chạy; socket là cửa giao tiếp giữa process và tầng vận chuyển. Trong mô hình ứng dụng, IP xác định host và port giúp xác định đầu nhận ứng dụng trên host đó.
- **Nhu cầu ứng dụng:** Ứng dụng có thể cần độ tin cậy, thông lượng, độ trễ hoặc bảo mật; TCP tin cậy không đồng nghĩa bảo đảm độ trễ/thông lượng tối thiểu. TCP/UDP không tự mã hóa; HTTPS trong mô hình đã học bổ sung TLS.
- **Web, object và URL:** Trang web thường gồm HTML cơ sở cùng các object được tham chiếu như ảnh hoặc âm thanh. URL web cơ bản có scheme, host và path; một HTML tham chiếu 5 ảnh là 6 object cần lấy.
- **HTTP request:** Có dòng yêu cầu chứa method, request-target, phiên bản; tiếp theo là header, dòng trống và body nếu có. Host chỉ máy chủ được yêu cầu; User-Agent mô tả phần mềm client.
- **Ghép URL từ request:** Trong mô hình HTTP trực tiếp, ghép scheme với Host và đúng request-target, giữ đủ các thư mục trong đường dẫn. Với GET /docs/index.html và Host: www-net.cs.umass.edu, giả sử HTTP thường thì URL là http://www-net.cs.umass.edu/docs/index.html; chỉ hostname chưa xác định đủ tài nguyên.
- **HTTP response:** Có dòng trạng thái chứa phiên bản, mã trạng thái và mô tả; tiếp theo là header và body nếu có. Content-Length là độ dài body, không phải toàn bộ response; Date khác Last-Modified.
- **GET/POST/HEAD/PUT:** GET lấy tài nguyên và có thể mang tham số trong URL; POST thường gửi dữ liệu trong body. HEAD lấy các header tương ứng GET mà không lấy body; PUT tạo/thay thế tài nguyên tại URL.
- **Mã HTTP:** 200 thành công, 301 chuyển vĩnh viễn với vị trí mới trong Location, 304 bản cache chưa thay đổi. 400 yêu cầu không hợp lệ, 404 không tìm thấy tài nguyên trên server, 505 phiên bản HTTP không được hỗ trợ.
- **502 Bad Gateway — bổ sung từ đề mẫu:** Gateway/proxy nhận phản hồi không hợp lệ từ server phía sau khi xử lý yêu cầu. Đây là lỗi lấy nội dung yêu cầu, không phải một lần nhận trang thành công theo mô hình đề.
- **HTTP stateless:** HTTP không tự ghi nhớ lịch sử các request để duy trì trạng thái ứng dụng. Ứng dụng vẫn có thể xây dựng phiên người dùng bằng cookie và dữ liệu phía server.
- **Cookie:** Server gửi Set-Cookie trong response; trình duyệt gửi Cookie trong request tiếp theo. Cookie hỗ trợ nhận diện/trạng thái phiên, khác cache lưu bản sao nội dung.
- **Web cache/proxy:** Lưu bản sao object để giảm độ trễ và lưu lượng phải đi đến server gốc. Cache không tự tăng dung lượng vật lý của đường truyền.
- **Conditional GET/304:** Client có thể gửi If-Modified-Since để kiểm tra bản đã cache; server trả 304 nếu chưa thay đổi hoặc 200 cùng nội dung mới khi cần. 304 không gửi lại body object nhưng trình duyệt dùng bản cache để hiển thị, nên chuỗi 200/304/404/502 trong đề mẫu có 2 lượt xem nội dung thành công, không chỉ đếm mã 2xx.
- **Nonpersistent và persistent:** Nonpersistent dùng tối đa một object trên một kết nối TCP; persistent tái sử dụng kết nối cho nhiều object cùng server. Persistent không tự đồng nghĩa với pipelining.
- **Phiên bản HTTP và mặc định kết nối:** HTTP/1.1 mặc định dùng persistent khi không có chỉ định đóng như Connection: close; HTTP/1.0 mặc định không persistent nhưng có thể có cơ chế keep-alive. Đây là mặc định theo phiên bản, không phải khẳng định mọi kết nối thực tế đều được tái sử dụng.
- **Pipelining:** Cho phép gửi nhiều request trước khi chờ lần lượt từng response. Khi tính nhiều object, phải phân biệt tuần tự, pipelining và nhiều kết nối song song.
- **HTTP và RTT:** Với một object qua TCP mới, không TLS, bỏ xử lý và thời gian truyền request/header, thời gian là 2RTT+t_object: một RTT mở TCP, một RTT request/byte phản hồi đầu tiên. Nhiều object phải vẽ timeline theo giả thiết, không áp một công thức chung.
- **Persistent without pipelining, nhiều object:** Với một TCP mới, cùng server, tải tuần tự, không TLS/DNS/xử lý và bỏ truyền request/header, một HTML tham chiếu m object có T=(m+2)RTT+Σt_i, trong đó tổng cộng m+1 object. Ví dụ 1 HTML + 5 ảnh, mỗi object truyền 0,5RTT: T=1RTT mở TCP+6RTT request+6×0,5RTT truyền=10RTT.
- **Thành phần mail:** User agent giúp soạn/đọc thư; mail server lưu và chuyển thư. Mailbox chứa thư của người nhận, message queue chứa thư chờ gửi.
- **SMTP:** Theo mô hình slide, thư đi UA gửi→server gửi→server nhận bằng SMTP. Người nhận offline vẫn có thể có thư trong mailbox tại server; SMTP dùng gửi/chuyển thư, không lấy thư về đọc.
- **POP3/webmail:** POP3 dùng truy xuất/tải thư, cổng cơ sở TCP/110. Webmail dùng HTTP ở chặng trình duyệt–dịch vụ webmail; các mail server vẫn có chặng chuyển thư riêng.
- **IMAP — bổ sung tên chuẩn/cổng:** IMAP là Internet Message Access Protocol, truy xuất/quản lý thư và thư mục trên server, không thay SMTP để gửi thư đến người nhận. Cặp cần nhớ là TCP/143; “Internet Mail Access Protocol” ở T2 tr60 và phương án D câu12 đề mẫu là tên ghi chưa đúng chuẩn.
- **Thông điệp mail:** Gồm header như To/From/Subject, dòng trống và body. Header của thư khác với các lệnh SMTP MAIL FROM và RCPT TO.
- **FTP — bổ sung làm rõ:** FTP (File Transfer Protocol) truyền tệp trên TCP, dùng TCP/21 cho kết nối điều khiển và một kết nối dữ liệu riêng. Cổng 20 là cổng dữ liệu phía server trong FTP active cơ bản; passive dùng cổng được thông báo/thương lượng, không học rằng mọi dữ liệu FTP luôn đi cổng 20.

**Giao thức — vận chuyển — cổng cần nhận diện:** Đây là cổng dịch vụ mặc định phía server, khác cổng nguồn tạm thời của client; ứng dụng có thể được cấu hình dùng cổng khác.

| Giao thức | Vận chuyển trong mô hình đang học | Cổng mặc định | Vai trò/lưu ý |
|---|---|---:|---|
| HTTP | TCP | 80 | Web HTTP cơ sở |
| HTTPS | TCP + TLS | 443 | Web có TLS trong mô hình TCP đang học |
| DNS | UDP hoặc TCP | 53 | Bài truy vấn cơ sở thường dùng UDP; DNS cũng hỗ trợ TCP |
| SMTP | TCP | 25 | Chuyển thư giữa mail server trong mô hình môn học |
| POP3 | TCP | 110 | Truy xuất/tải thư |
| IMAP | TCP | 143 | Truy xuất/quản lý thư trên server |
| FTP — điều khiển | TCP | 21 | Gửi lệnh/điều khiển truyền tệp |
| FTP — dữ liệu active | TCP | 20 | Cổng dữ liệu phía server ở chế độ active cơ bản; không áp cố định cho passive |

Các cặp HTTPS/443, IMAP/143 và phân biệt FTP control/data được bổ sung để làm rõ bảng; nguồn RFC/IANA ở cuối bản. Không mở rộng sang QUIC/HTTP3 hay thêm cơ chế TCP điều khiển tắc nghẽn.

- **DNS:** Hệ thống cơ sở dữ liệu phân tán, phân cấp và giao thức ứng dụng để phân giải tên. Ngoài tên host–IP, nó còn hỗ trợ bí danh và xác định mail server.
- **Phân cấp DNS:** Root hướng đến TLD; TLD hướng đến authoritative server có dữ liệu có thẩm quyền cho vùng tên liên quan. Host thường hỏi local resolver trước; local có thể trả từ cache nên không phải mọi truy vấn đều đi qua root.
- **Iterative và recursive:** Iterative: server được hỏi trả kết quả đã biết hoặc referral để bên hỏi tiếp tục hỏi nơi khác; recursive: server được hỏi nhận trách nhiệm phân giải thay. Một lần tra cứu có thể kết hợp host–local recursive với local–các server khác iterative.
- **Cache/TTL DNS:** TTL quy định thời gian giữ thông tin trong cache, giúp giảm truy vấn và thời gian chờ. IP thay đổi có thể chưa được biết ngay vì cache cũ còn hiệu lực; TTL DNS khác TTL/hop limit của IP.

**Bản ghi tài nguyên DNS:** Dạng cơ sở là (name,value,type,ttl).

| Loại | Ý nghĩa |
|---|---|
| A | Hostname→địa chỉ IPv4. |
| NS | Tên miền→tên DNS server có thẩm quyền; value là tên, không phải IP. |
| CNAME | Bí danh→tên chính tắc; tiếp tục theo A khi cần IP. |
| MX | Tên miền mail→tên mail server nhận thư; không lấy nhầm IP web server hoặc DNS server. |

- **Socket TCP:** SOCK_STREAM/connect là dấu hiệu TCP client; bind/listen/accept là dấu hiệu server trong ví dụ slide. accept trả socket kết nối để trao đổi với client, khác socket lắng nghe.
- **Socket UDP:** SOCK_DGRAM/sendto/recvfrom là dấu hiệu UDP trong ví dụ slide. sendto chỉ địa chỉ đích; recvfrom trả dữ liệu cùng địa chỉ bên gửi.

## Chương 3 — Tầng vận chuyển

Nguồn chính: [T3 — Chương3](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf>), nhóm trang PDF5–34,36–73,75–94.

- **Vai trò vận chuyển:** Tầng mạng phục vụ host–host; tầng vận chuyển phục vụ process–process tại hai đầu cuối. TCP/UDP dùng dịch vụ tầng mạng để chuyển dữ liệu.
- **Multiplexing/demultiplexing:** Bên gửi nhận dữ liệu từ các socket và thêm header; bên nhận dùng thông tin để giao đúng socket. Port nằm trong header TCP/UDP, địa chỉ IP nằm trong header IP.
- **UDP demultiplexing:** Trong mô hình socket UDP chưa connect của slide, nhiều nguồn có thể gửi vào cùng socket bind tại IP/cổng đích. Không tự tạo socket mới chỉ vì thêm một client gửi tới.
- **TCP demultiplexing:** Một kết nối được phân biệt bằng bộ bốn IP nguồn, port nguồn, IP đích, port đích. Nhiều kết nối server có thể cùng dùng một port dịch vụ.
- **UDP:** Không bắt tay thiết lập kết nối, không tự ACK/phát lại và có thể mất/sai thứ tự; ứng dụng có thể bổ sung cơ chế cần thiết. Ít overhead không bảo đảm luôn nhanh hơn hoặc bảo đảm độ trễ.
- **UDP header/Length:** Có bốn trường source port, destination port, Length, checksum, mỗi trường 16 bit và tổng header 8 byte. Length=8+payload nên giá trị tối thiểu 8 byte và payload=Length−8; bản thân trường Length chỉ dài 16 bit=2 byte, không phải 16 byte và không chỉ đo payload.
- **Checksum:** Trong bài tính, chia thành các từ 16 bit, cộng có carry vòng về rồi đảo bit để tạo checksum; bên nhận cộng cả checksum, tổng toàn bit 1 là không phát hiện lỗi. Checksum không sửa lỗi, và không phát hiện lỗi chưa chứng minh dữ liệu chắc chắn nguyên vẹn.
- **FSM:** Đọc theo trạng thái hiện tại→sự kiện/điều kiện→hành động/trạng thái mới. Receiver đổi trạng thái theo packet mình nhận/xử lý, không biết hay chờ ACK của mình tới sender.

**Các phiên bản RDT:**

| Phiên bản | Kiến thức cần nhớ |
|---|---|
| rdt1.0 | Kênh giả định hoàn toàn tin cậy, không lỗi/mất; gửi và nhận chưa cần cơ chế khôi phục lỗi. |
| rdt2.0 | Thêm checksum và ACK/NAK để xử lý lỗi bit; khi ACK/NAK hỏng, sender không biết receiver đã nhận dữ liệu hay chưa. |
| rdt2.1 | Thêm số thứ tự0/1 để phân biệt dữ liệu mới với bản phát lại; receiver không giao bản trùng lần hai. |
| rdt2.2 | Chỉ dùng ACK có số, thay NAK bằng ACK cho packet cuối đã nhận thành công. ACK0/ACK1 ở đây xác nhận packet0/1, khác quy tắc ACK byte của TCP. |
| rdt3.0 | Thêm timer/timeout để xử lý mất data/ACK; timeout thì phát lại packet đang chờ và tính thời gian lại. Timeout chỉ chứng tỏ chưa nhận ACK phù hợp đúng hạn, không chứng minh data đã mất. |

- **Stop-and-wait:** Gửi một packet rồi chờ ACK mới gửi packet tiếp theo. Khi RTT lớn so với thời gian truyền packet, liên kết có thể rảnh phần lớn thời gian.
- **Pipelining/cửa sổ:** Cho phép nhiều packet đã gửi nhưng còn chờ ACK để tận dụng liên kết. Cửa sổ là dải số thứ tự được phép dùng; base tiến theo ý nghĩa ACK của từng giao thức.
- **Go-Back-N:** ACK(n) xác nhận tích lũy packet đến n; mô hình học ở T3tr69 hủy packet đến sai thứ tự và ACK lại packet cuối đã nhận liên tục. Sender dùng timer cho packet cũ nhất chưaACK; timeout phát lại các packet đã gửi còn chưaACK từ base trở đi.
- **Selective Repeat:** Receiver buffer packet hợp lệ trong cửa sổ và ACK riêng từng packet, nhưng chỉ giao dữ liệu liên tục lên ứng dụng. Sender ghi từng ACK, dùng timer logic riêng và chỉ phát lại packet bị timeout; base vẫn chờ ACK của packet đầu cửa sổ.
- **Dịch vụ TCP:** Cung cấp luồng byte tin cậy, đúng thứ tự, hai chiều trong một kết nối. TCP segment gồm header và payload; các trường cần nhận diện là port, Seq, ACK, receive window và các cờ.
- **MSS:** Là payload tối đa, không gồm TCP header. MSS 1000B với header 20B cho phép payload 1000B, tổng segment 1020B; không phải payload 1020B.
- **Seq theo byte:** Seq=s, payload L byte thì dữ liệu mang số s…s+L−1; dữ liệu mới nối tiếp bắt đầu ở s+L. Header không tính vào dãy byte này; bản phát lại giữ Seq của dữ liệu cũ.
- **Hai chiều Seq/ACK:** Seq nói về dữ liệu mình gửi; ACK nói về dữ liệu nhận từ bên kia. Nhận dữ liệu không làm Seq gửi chuyển sang dãy số của bên kia; ACK thuần không mang dữ liệu không tiêu thụ thêm Seq.
- **ACK TCP:** ACK=n nghĩa đã nhận liên tục đến byte n−1 và đang chờ n. Chỉ dùng ACK=Seq+payload khi dữ liệu đến nối tiếp, không còn lỗ hổng trước đó và không có SYN/FIN cần tính riêng.
- **Lỗ hổng và buffer:** Dữ liệu đến sau có thể được lưu nhưng chưa làm ACK vượt phần thiếu hoặc giao vượt thứ tự lên ứng dụng. Khi phần thiếu tới, ghép với phần đã buffer rồi tìm byte đầu tiên còn thiếu, nên ACK có thể nhảy xa.
- **Mất ACK và timeout:** ACK sau có thể xác nhận tích lũy cả phần mà ACK trước bị mất, giúp tránh phát lại nếu tới trước timeout. Nếu phát lại dữ liệu receiver đã có, receiver không giao trùng và ACK theo mốc liên tục hiện tại.
- **Fast retransmit:** Khi còn dữ liệu chưa ACK, nhận 3 duplicate ACK sau ACK gốc có thể kích hoạt phát lại phần thiếu trước timeout; đếm ACK sender thực sự nhận. Trong trace cơ sở, đó là 1 ACK gốc + 3 ACK trùng, cùng số ACK và cửa sổ không đổi.
- **Flow control/rwnd:** Bên nhận quảng bá rwnd để bảo vệ bộ đệm; trong mô hình đơn giản rwnd=RcvBuffer−dữ liệu đang chiếm buffer. T3tr88–89 ghi nhầm bên thông báo; đúng là bên nhận dữ liệu quảng bá cho bên gửi.
- **Ngân sách gửi theo rwnd:** Chỉ xét flow control, cùng một quảng bá hiện tại, lượng gửi mới tối đa=max(0,rwnd−byte đã gửi chưa ACK). Sau khi A xử lý rwnd 5000 với outstanding 0 rồi gửi 1200B chưa ACK, chưa có cập nhật khác, A còn gửi 3800B.
- **ACK và ứng dụng đọc:** TCP đã ACK không bảo đảm ứng dụng đã đọc dữ liệu khỏi socket buffer. Vì thế dữ liệu đã ACK vẫn có thể chiếm buffer; ứng dụng đọc bớt có thể làm rwnd tăng dù ACK chưa tiến lên.
- **Cờ và số:** SYN/ACK/FIN là các cờ điều khiển; Seq và ACK number là các giá trị số trong header. Cờ ACK=1 không có nghĩa ACK number=1.
- **Bắt tay TCP:** Không kèm data: SYN Seq=x→SYN+ACK Seq=y,ACK=x+1→ACK Seq=x+1,ACK=y+1. Hai đầu chọn ISN riêng; SYN tiêu thụ 1 số Seq, ACK thuần không tiêu thụ Seq, còn ACK thứ ba có thể kèm dữ liệu nếu tình huống cho.
- **FIN/đóng một chiều:** FIN kết thúc chiều gửi dữ liệu ứng dụng của bên gửi FIN; bên đó vẫn có thể nhận và gửi ACK chiều ngược. FIN Seq=f không payload được xác nhận bằng ACK=f+1; ACK có thể gộp FIN nên không phải luôn đúng 4 segment.
- **Chờ sau khi đóng:** Trong sơ đồ client chủ động đóng ở T3 tr94, sau khi nhận FIN/gửi ACK cuối, client còn chờ 2MSL trước khi đóng hẳn. MSL là thời gian sống tối đa của một segment.

## Hai công thức bổ sung đã học

- **Hiệu suất stop-and-wait:** U=(L/R)/(RTT+L/R), bỏ thời gian truyền ACK, xử lý và mất gói; RTT trong mô hình không gồm thời gian phát data L/R. Các đại lượng thời gian phải cùng đơn vị.
- **Giới hạn cửa sổ GBN/SR:** Với k bit số thứ tự, GBN chuẩn có cửa sổ nhận1 dùng W≤2^k−1; SR chuẩn có cửa sổ gửi/nhận bằng W dùng W≤2^(k−1). Công thức giới hạn này là phần bổ sung đã đối chiếu trước, không in trực tiếp ở T3tr67–73: [nguồn lý thuyết đã kiểm](https://sites.uclouvain.be/CNP3/1st/html/transport/transport.html).

## Bổ sung sau đề mẫu cô cung cấp ngày30/10/2026

Đối chiếu15câu cho thấy cần ghi rõ hơn RTT nhiều object, HTTP/1.1 mặc định persistent, URL từ Host+path,304 vẫn xem cache,UDP Length tối thiểu8B; bổ sung IMAP/TCP143,tên Message,FTP control/data và502. Các mục đã có như HTTP/TCP80,FTP/TCP21,DNS53 không bị tính nhầm là hoàn toàn chưa học.

Nguồn sau đây chỉ bổ sung/làm rõ cho T1/T2/T3; không phải nguồn đề online và không thay đổi thống kê5PDF/172lượt câu:

- [RFC9112 §9.3](https://www.rfc-editor.org/rfc/rfc9112.html#section-9.3): mặc định kết nối HTTP/1.1; [§3.3](https://www.rfc-editor.org/rfc/rfc9112.html#section-3.3): dựng URI từ request.
- [RFC9110 §15.4.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.4.5):304; [§15.6.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.3):502; [§4.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2):HTTPS/443.
- [RFC9051 §2.1](https://www.rfc-editor.org/rfc/rfc9051.html#section-2.1):IMAP/TCP143; phần mở đầu xác nhận tên Internet Message Access Protocol và chức năng truy xuất/quản lý thư.
- [RFC959](https://www.rfc-editor.org/rfc/rfc959.html):FTP/control/data; [IANA — FTP](https://www.iana.org/assignments/service-names-port-numbers?search=ftp):cổng20/21; [IANA — IMAP](https://www.iana.org/assignments/service-names-port-numbers?search=imap):cổng143.
- [RFC1035 §4.2](https://www.rfc-editor.org/rfc/rfc1035.html#section-4.2):DNS dùngUDP/TCP53.

Câu15 của đề mẫu hỏi Slow Start, thuộcT3tr98/điều khiển tắc nghẽn đã loại khỏi phạm vi hiện hành; chỉ được chữa trong báo cáo riêng, không tự đưa thành phần học bắt buộc trong bản này.

## Lưu ý nguồn

- T2tr24: persistent không tự có pipelining; câu một RTT cho mọi object cần giả thiết phù hợp. T2tr27 có lỗi gõ POST trong phần mô tả PUT; dùng đúng ý PUT tạo/thay thế tài nguyên.
- T3tr78: 9000B tương ứng byte0–8999; MSS2000B chia thành4đoạn2000B+1đoạn1000B. Không chép chú thích0–9999 hoặc5đoạn đều2000B.
- T3tr91 đặt nhãn LISTEN sai ở client chủ động connect; ví dụ chuẩn ở đây là client chủ động gửi SYN, server chờ kết nối. Không lấy nhãn sai này làm mẫu học trạng thái.

Bản này là tài liệu tra nhanh, không thay thế việc tự làm bài và không làm thay đổi đánh giá thành thạo hay trạng thái các câu chưa trả lời.
