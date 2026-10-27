# Kế hoạch học Nhập môn Mạng máy tính trong 7 ngày

Kế hoạch dành cho người mới học, chưa nắm chắc, có **2-3 giờ/ngày**. Học nền Chương 1 trước, sau đó Chương 2, rồi Chương 3; dành ngày cuối làm đề và chữa lỗi. Trọng tâm là **hiệu suất và chồng tầng; HTTP, DNS, mail; UDP, RDT, GBN/SR và TCP Seq/ACK**.

Lịch có **14 giờ cơ sở**, gồm thời gian nghỉ, và tối đa **7 giờ tăng cường**. Đây là lộ trình chọn phần cần làm chắc trong một tuần; các phần mở rộng được tách rõ để không dồn toàn bộ slide vào 14 giờ.

## 1. Phạm vi và căn cứ

**Cập nhật phạm vi ngày 27/10/2026:** Chương3 chỉ đến hết TCP theo ảnh outline người dùng gửi, bao gồm quản lý kết nối, điều khiển luồng và điều khiển tắc nghẽn. Nội dung T3 đến hết trang PDF102; phần phát triển tầng vận chuyển/QUIC/HTTP3 tr104–108 ngoài phạm vi. EstimatedRTT vẫn là phần TCP tùy chọn đã có trong kế hoạch; nguồn đề và số câu phân loại không đổi.

Đã đọc đủ ba file lý thuyết, tổng **283 trang**, và toàn bộ câu hỏi trong **5 bộ đề được chốt, 172 lượt câu**. Hai đề scan đã được trích OCR và đối chiếu hình/số liệu. Ba subagent phụ trách từng chương; người điều phối kiểm tra phạm vi, trùng lặp, số câu và lịch chung.

Trong tài liệu này, mọi số trang là **trang PDF tính từ 1**, có thể khác số slide in trên trang. Ký hiệu `D19 C12` nghĩa là câu 12 trong đề D19 dưới đây.

| Mã | Tài liệu được dùng | Phạm vi |
|---|---|---|
| D19 | [[BHT CNPM] NMMMT 2019-2020 GK1.pdf](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/[BHT CNPM] NMMMT 2019-2020 GK1.pdf>) | 30 câu, 6 trang scan |
| D20 | [[BHT CNPM] NMMMT 2020-2021 GK1.pdf](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/[BHT CNPM] NMMMT 2020-2021 GK1.pdf>) | 30 câu, 7 trang scan |
| D23 | [Đề A MMT.pdf trong folder 2023](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/Nhập Môn Mạng Máy Tính/2023/Đề A MMT.pdf>) | 40 câu, 4 trang; tính thêm theo chỉ định của bạn |
| D24 | [2024.pdf trong folder 2024](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/Nhập Môn Mạng Máy Tính/2024/2024.pdf>) | **42 câu**, 4 trang; tính thêm theo chỉ định của bạn |
| D25 | [[BHT CNPM] NMMMT 2025-2026 GK1.pdf](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/[BHT CNPM] NMMMT 2025-2026 GK1.pdf>) | 30 câu ở trang 1-5; bản BHT soạn lại sau thi đã được bạn chấp nhận; trang 6 đáp án tham khảo không làm căn cứ |
| LT1 | [Lý thuyết Chương 1](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf>) | Đọc đủ 69 trang |
| LT2 | [Lý thuyết Chương 2](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf>) | Đọc đủ 105 trang |
| LT3 | [Lý thuyết Chương 3](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf>) | Đọc đủ 109 trang |

Nhãn 2023/2024 được giữ theo folder và yêu cầu của bạn; không tự suy ra thêm thông tin về nguồn phát hành. Bản DOCX 2023 trùng 40 câu D23 nên không tính thành bộ thứ sáu. Không dùng đề online, training, đề mẫu, ngân hàng câu hỏi, bài tập ôn/phát triển đề hay các file đáp án riêng để xếp trọng tâm. `slide nmm.pdf` không tham gia căn cứ bản kế hoạch cuối.

### Phân bố câu theo chương chính

Mỗi lượt câu được gán đúng một chương để tránh đếm hai lần. Câu nhận diện tầng/RTT chung thuộc Ch1; socket ở mức ứng dụng, mã client/server và bảng giao thức/cổng thuộc Ch2; dịch vụ TCP/UDP và demultiplexing thuộc Ch3. Một số câu có kiến thức giao thoa.

| Bộ đề | Chương 1 | Chương 2 | Chương 3 | Tổng |
|---|---:|---:|---:|---:|
| D19 | 6 | 10 | 14 | 30 |
| D20 | 4 | 12 | 14 | 30 |
| D23 | 6 | 21 | 13 | 40 |
| D24 | 7 | 21 | 14 | 42 |
| D25 | 3 | 11 | 16 | 30 |
| **Tổng** | **26** | **75** | **71** | **172** |

Đây là số **lượt câu**, có câu trùng/biến thể giữa các đề, đặc biệt D23 và D24; không phải 172 câu độc lập hay dự báo tỷ lệ đề sắp thi. Ch2 và Ch3 đều cần ưu tiên cao. Ch3 được dành nhiều thời gian hơn vì cần tự theo dõi cơ chế, cửa sổ và Seq/ACK; Ch1 phải học trước vì cung cấp nền cho cả hai chương.

## 2. Quy ước mức ưu tiên và thứ tự học

- **A: làm chắc trong tuần.** Giải thích được bằng lời của mình và làm được câu cơ bản cùng dạng.
- **B: học sau A.** Nắm cơ chế, làm ví dụ đơn giản; dùng giờ tăng cường để luyện sâu.
- **C: đọc sau nếu còn giờ.** Có trong slide nhưng chưa có câu trực tiếp trong năm bộ đề được chọn, hoặc nằm ngoài phạm vi chi tiết bạn nêu. Không đồng nghĩa chắc chắn không thi.

Thứ tự học: **tổng quan biên/lõi -> chồng tầng -> độ trễ/RTT -> nguyên lý ứng dụng -> HTTP -> mail -> DNS -> dịch vụ vận chuyển/mux -> UDP/checksum -> RDT -> GBN/SR -> TCP -> luyện tổng hợp**. Chồng tầng được học trước phần tính hiệu suất sâu để người mới hình dung dữ liệu đang đi đâu; bài DNS+HTTP chỉ luyện sau khi hiểu cả hai giao thức.

## 3. Chương 1 Giới thiệu mạng máy tính

### 1.1 Internet và giao thức

**B nhưng phải học mở đầu.** Đọc LT1 trang 3-7. Hiểu host, liên kết, router/switch, ISP; Internet là mạng của các mạng. Giao thức quy định khuôn dạng, thứ tự thông điệp và hành động khi gửi/nhận. Phân biệt giao thức, ứng dụng và hạ tầng. Tự lấy một ví dụ trao đổi yêu cầu/phản hồi; không chỉ thuộc định nghĩa.

### 1.2 Mạng biên

**B; kỹ năng đơn vị là A.** Đọc LT1 trang 9-23. Chia thành: (a) host/client/server và mạng truy cập; (b) môi trường truyền hữu tuyến/vô tuyến; (c) độ dài dữ liệu và tốc độ truyền. Cần phân biệt **R tính bằng bit/s** với tốc độ lan truyền **s tính bằng m/s**; đổi byte-bit, Mbps-bit/s, km-m, s-ms. Chưa cần thuộc mọi con số tốc độ công nghệ trong ví dụ.

Đối chiếu D25 C21 (thiết bị ở biên), D24 C6 (đơn vị tốc độ), D19 C2-3 và D20 C20 (đổi đơn vị trước tính).

### 1.3 Mạng lõi

**B; store-and-forward là nền A cho bài độ trễ.** Đọc LT1 trang 25-35, đọc cấu trúc Internet/ISP ở mức sơ đồ trước phần hiệu suất. Chia thành: (a) routing khác forwarding; (b) chuyển mạch gói, nhận đủ gói rồi mới phát tiếp, queue/loss; (c) chuyển mạch kênh, FDM/TDM; (d) kết nối giữa các ISP ở mức tổng quan. Tự so sánh tài nguyên dành riêng với tài nguyên chia sẻ.

Vẽ một gói qua hai link trước khi làm D19 C12 và D20 C14. Chưa cần thuật toán định tuyến, chia subnet hoặc cấu hình mạng ở chương sau.

### 1.4 Hiệu suất

**A.** Đọc LT1 trang 46-56, đặc biệt trang 48, 50, 55-56. Học theo bốn khối:

1. Bốn loại trễ: processing, queueing, transmission, propagation; dữ kiện nào quyết định từng loại.
2. Một gói qua một/nhiều link: đổi đơn vị rồi cộng các thành phần cần tính.
3. Throughput: nút thắt đường truyền, trường hợp chia sẻ; không cộng tốc độ các link nối tiếp.
4. Số gói/giây, RTT, vì sao buffer đầy gây mất gói.

Phải làm được D19 C2, C3, C10, C12; D20 C14; D24 C35; sau đó D25 C12. D20 C20 cùng dạng D19 C2: dùng để tự kiểm lại, không coi là một dạng mới.

### 1.5 Mô hình chồng giao thức

**A.** Đọc LT1 trang 58-67. Chia thành: (a) thứ tự/chức năng năm tầng Internet; (b) đơn vị dữ liệu message -> segment/datagram -> packet/datagram -> frame -> bit theo cách gọi trong slide; (c) đóng/mở gói; (d) tầng xử lý tại host, switch, router trong mô hình cơ bản; (e) nhận ra Session không là một tầng riêng trong chồng năm tầng đang học. LT1 ở phần này trình bày chồng năm tầng; chưa cần tự bổ sung toàn bộ mô hình bảy tầng OSI để làm các câu nhận diện đã nêu.

Tự dựng bảng năm tầng từ trí nhớ và chú thích sơ đồ host-switch-router-host. Luyện D19 C4, C13; D20 C4-5; D23 C1, C12, C33, C36; D24 C7, C23; D25 C26 nhưng lưu ý giới hạn câu chữ ở mục 7.

**Điều kiện chuyển sang Ch2:** tự giải một bài trễ một link, một bài nhiều link, một bài bottleneck; viết đủ thứ tự năm tầng/PDU và phân biệt host với process. Nếu còn sai đơn vị, dùng phần tăng cường để sửa trước khi học HTTP RTT.

## 4. Chương 2 Tầng ứng dụng

### 2.1 Nguyên lý ứng dụng mạng

**A.** Đọc LT2 trang 3-15. Chia thành: (a) client-server và P2P; (b) host/process/socket, IP+port ở góc nhìn ứng dụng; (c) ứng dụng cần reliability, throughput, timing, security; (d) chọn dịch vụ TCP/UDP và nhận diện cổng quen thuộc. P2P ở đây là kiến trúc; chưa cần công thức phân phối file BitTorrent.

Luyện D19 C22; D23 C22, C25-29; D24 C9; D25 C2, C6, C10. Thêm **15 phút B** đọc mã socket LT2 trang 90-99 để nhận diện D19 C23, D20 C12: SOCK_STREAM/connect là dấu hiệu TCP client; listen/accept là phía TCP server; SOCK_DGRAM/sendto/recvfrom thuộc UDP. Chưa cần viết ứng dụng hoàn chỉnh.

### 2.2 Web và HTTP

Chia bốn phần, học theo thứ tự:

| Tiểu phần | Mức | Cần đạt | Nguồn và câu luyện |
|---|---|---|---|
| Object, URL, request/response | A | Phân biệt HTML cơ sở/ảnh; method, request-target, Host, version; status line, header, body; GET/POST/HEAD/PUT cơ bản | LT2 tr.17-30,51; D19 C1,C29-30; D20 C22,C24; D23 C9; D24 C24,C26 |
| Stateless, cookie, cache, conditional GET | A | Phân biệt cookie với cache; Set-Cookie/Cookie; If-Modified-Since và 304; cache giảm traffic/độ trễ | LT2 tr.19,31-34,41-47; D20 C17; D24 C8,C36; D25 C14,C22 |
| Nonpersistent/persistent, một object | A | Kết nối mới/tái sử dụng; biết vì sao mô hình một object qua TCP mới cần 2RTT + thời gian truyền | LT2 tr.20-24; D20 C18; D23 C5,C8; D24 C2 |
| Nhiều object, pipelining/song song, DNS+HTTP | B | Vẽ timeline, ghi rõ giả định rồi đếm RTT; không học một công thức cho mọi tình huống | Suy từ LT2 tr.20-24 và phần DNS; chưa thấy bài số trực tiếp nhiều object trong năm đề đã chọn |

Đọc thông điệp thật trong đề trước khi nhớ mã trạng thái. Cần nhận diện 200, 301, 304, 400, 404, 505 và đọc thêm mã xuất hiện trong câu hỏi. Phân biệt lỗi tài nguyên với lỗi DNS/không tìm thấy máy chủ. HTTP/2 và các chi tiết theo dõi người dùng để mức C.

### 2.3 Mail và SMTP

**A.** Đọc LT2 trang 53-60. Chia thành: (a) user agent, mail server, mailbox, message queue; (b) sơ đồ gửi/chuyển thư bằng SMTP; (c) truy xuất thư bằng POP3/IMAP, HTTP với webmail; (d) bảng giao thức/cổng theo mô hình môn học. Tự vẽ **UA gửi -> server gửi -> server nhận -> UA nhận**, gán giao thức từng chặng và giải thích thư nằm đâu khi người nhận offline.

Luyện D19 C26-28; D20 C1-3; D23 C14,C20,C24; D24 C10,C12,C15,C18,C22,C39; D25 C28. Lệnh SMTP và định dạng thông điệp chi tiết học mức B sau khi hiểu đường đi thư.

### 2.4 DNS

**A.** Đọc LT2 trang 62-77. Chia thành: (a) chức năng và lý do phân tán/phân cấp; (b) local resolver, root, TLD, authoritative; (c) iterative/recursive theo mũi tên; (d) cache/TTL; (e) RR A, NS, CNAME, MX và chuỗi ánh xạ.

Luyện D19 C20; D20 C13,C29; D23 C15,C17,C32; D24 C16-17,C19; D25 C7,C19. Với D23 C17 phải nhận ra ví dụ NS có value dạng IP không khớp cấu trúc chuẩn trong LT2 tr.74; không lấy dữ liệu đó làm mẫu cấu hình. Với D25 C19, đọc lưu ý mục 7.

**Điều kiện chuyển sang Ch3:** tự đọc một HTTP request/response; giải thích 2RTT cho một object; vẽ đúng đường mail và DNS; phân biệt IP web server, DNS server, mail server; nhận ra một đoạn mã TCP client/server đơn giản.

## 5. Chương 3 Tầng vận chuyển

### 3.1 Dịch vụ tầng vận chuyển

**A.** Đọc LT3 trang 5-8. Hiểu truyền thông logic process-process, chạy tại đầu cuối; transport sử dụng dịch vụ tầng mạng. Tự so sánh TCP/UDP theo kết nối, reliability, flow/congestion control và overhead. TCP tin cậy không đồng nghĩa bảo đảm độ trễ/thông lượng tối thiểu hoặc tự mã hóa. UDP không tự cung cấp reliability nhưng ứng dụng có thể bổ sung cơ chế phía trên.

Luyện D19 C6,C16; D23 C4,C10,C27-28,C34,C37; D24 C4-5,C11,C21,C32; D25 C3.

### 3.2 Multiplexing và demultiplexing

**A.** Đọc LT3 trang 10-22. Chia thành: (a) gom ở bên gửi/tách ở bên nhận; (b) source/destination port khi đi và khi trả lời; (c) UDP socket theo địa chỉ IP/cổng đích trong mô hình slide; (d) TCP connection theo bộ bốn IP nguồn, cổng nguồn, IP đích, cổng đích. Một server có thể có nhiều kết nối cùng cổng dịch vụ.

Luyện D20 C10-11; D24 C30,C33,C37. Vẽ bảng gói đi/gói về trước khi chọn port; không nhầm số port với số thứ tự segment.

### 3.3 UDP

**A.** Đọc LT3 trang 24-34. Chia thành: (a) tính chất và tình huống sử dụng; (b) header bốn trường 16 bit, tổng 8 byte; (c) Length gồm header+payload; (d) checksum bù 1, carry vòng về, đảo bit. Checksum phát hiện lỗi, không tự sửa lỗi; không phát hiện lỗi không bảo đảm dữ liệu hoàn toàn không lỗi.

Luyện theo độ khó: D23 C3,C38,C40 -> D24 C31,C33-34 -> D20 C26/D24 C42 -> D19 C21 (ba từ 16 bit). D25 C4-5,C13 để ngày cuối nếu giữ D25 làm lượt kiểm tra tổng hợp. Với “byte thứ 9”, phân biệt cách đếm từ 1 và offset 8 tính từ 0.

### 3.4 Nguyên lý truyền tin cậy

**A về cơ chế; B cho tính hiệu suất.** Đọc LT3 trang 36-73. Chia thành:

1. **rdt1.0 -> rdt2.0:** giả định kênh tin cậy rồi có lỗi bit; vì sao cần checksum, ACK/NAK và phát lại.
2. **rdt2.1 -> rdt2.2:** ACK/NAK hỏng; thêm sequence 0/1 để phân biệt bản trùng; chỉ ACK có số thay NAK. Đọc điều kiện/hành động trong FSM.
3. **rdt3.0:** mất data hoặc ACK; timer/timeout, phát lại, không giao trùng. Phân biệt mất ACK với ACK đến trễ/timeout sớm.
4. **Stop-and-wait -> pipelining:** vì sao phải chờ làm hiệu suất thấp; cửa sổ cho phép nhiều packet đang chờ ACK.
5. **GBN và SR:** ACK tích lũy/riêng, buffer out-of-order, timer, gói nào phải phát lại. Sơ đồ GBN LT3 tr.69 loại gói đến sai thứ tự; SR lưu đệm các gói hợp lệ trong cửa sổ nhận. LT3 tr.68 nhắc lựa chọn xử lý tùy triển khai: khi làm bài phải theo mô hình đề, không đồng nhất GBN với mọi cách nhận của TCP. Phân biệt ACK số packet trong sơ đồ RDT với ACK số byte của TCP.

Luyện FSM D19 C19, D20 C16; mất ACK D19 C8, D20 C19, D24 C40; lỗi rdt2.0 D19 C11; GBN D19 C18, D20 C9,C25. D23 C6 và D25 C30 có cách hỏi chưa chặt, xem mục 7. Hiệu suất stop-and-wait/pipeline tính số để B sau khi theo dõi đúng sơ đồ.

### 3.5 TCP

| Tiểu phần | Mức | Cần đạt | Nguồn/câu luyện |
|---|---|---|---|
| Byte stream, header, MSS, Seq/ACK | A | Seq là byte đầu tiên; ACK là byte kế tiếp còn chờ liên tục; hai chiều có không gian Seq riêng; phân biệt payload, header, MSS | LT3 tr.75-79; D19 C5,C15,C17,C25; D20 C6-8; D24 C41 |
| Phát lại và ACK tích lũy | A | Mất ACK giữa chưa chắc phải gửi lại; timeout sớm có thể gây bản trùng; hiểu fast retransmit | LT3 tr.79-84; D19 C9; D20 C25; D25 C16-17 |
| Điều khiển luồng | A | Bên nhận quảng bá rwnd; bên gửi giới hạn dữ liệu chưa ACK; phân biệt rwnd với kích thước mỗi gói và cwnd | LT3 tr.85-89; D20 C15; D25 C11,C27 |
| Thiết lập/đóng kết nối | A | SYN -> SYN+ACK -> ACK; ISN; FIN đóng một chiều, vẫn có thể nhận chiều kia | LT3 tr.90-94; D20 C30; D25 C1,C18,C23 |
| Ước lượng RTT/timeout | B nhưng có đề hỏi | SampleRTT, cập nhật có trọng số và giá trị khởi tạo; không đánh đồng EstimatedRTT với RTO | D20 C23; LT3 thiếu phần công thức chi tiết, xem bổ sung có nguồn tại mục 7 |
| Điều khiển tắc nghẽn | B, dành ít nhất một lượt đọc | cwnd, ssthresh, MSS; Slow Start, Congestion Avoidance, Fast Recovery; timeout khác 3 duplicate ACK | LT3 tr.96-102; chưa thấy câu trực tiếp yêu cầu tính cwnd/đọc đồ thị trong năm bộ đề |

QUIC/HTTP3 ở LT3 tr.104-108 **ngoài phạm vi Ch3**, theo yêu cầu chỉ học đến hết TCP ngày27/10/2026; không còn xếp vào mục C để học thêm. Không suy từ UDP ít cơ chế rằng mọi ứng dụng chạy trên UDP đều không thể truyền tin cậy.

**Điều kiện kết thúc Ch3:** tự tính checksum; phân biệt lý do thêm sequence với timer; mô phỏng một ca mất packet/ACK trong GBN/SR; tính Seq/ACK theo byte; giải thích rwnd và vẽ handshake. Chỉ nhớ tên phiên bản/cờ TCP chưa đủ.

## 6. Lịch học 7 ngày

**Mỗi ngày: 110 phút học + 10 phút nghỉ = 120 phút cơ sở.** Có thể chia nghỉ thành hai lần 5 phút. Cột tăng cường tối đa 60 phút/ngày đã bao gồm nghỉ ngắn, dùng khi hôm đó có 3 giờ. Mỗi khối học gồm đọc khái niệm, tự giải thích/vẽ và làm câu đã chỉ định; không dành cả khối chỉ đọc slide.

| Ngày | 110 phút học cơ sở | Nếu có thêm tối đa 60 phút | Kết quả cuối ngày |
|---|---|---|---|
| **1** | 15' Internet/biên + 20' lõi/store-and-forward + 30' chồng tầng + 30' trễ/đơn vị + 15' làm và chữa D19 C2,C3,C4,C13 | Luyện D20 C4-5; tự vẽ sơ đồ tầng; thêm bài một/nhiều link D19 C12 | Một bảng 5 tầng/PDU và phân biệt được transmission với propagation |
| **2** | 35' trễ nhiều link/throughput + 20' chữa D19 C10,C12 và D20 C14; 25' nguyên lý ứng dụng + 30' HTTP request/response | Làm D24 C35, D23 C31; đọc HTTP D19 C1,C29-30; ưu tiên sửa lỗi đơn vị nếu còn | Tính được ba dạng Ch1; đọc được các trường chính của một thông điệp HTTP |
| **3** | 30' cookie/cache/status + 20' nonpersistent/persistent và 2RTT + 30' mail + 30' DNS chức năng/phân cấp | Chữa D24 C8,C36, D23 C8, D19 C27-28; vẽ lại sơ đồ DNS/mail | Phân biệt cookie/cache và gửi/đọc mail; giải thích được 2RTT cho một object |
| **4** | 25' DNS RR/iterative/recursive + 15' mã socket + 15' truy hồi Ch2; 10' dịch vụ transport + 15' mux/demux + 10' UDP header + 20' checksum | Luyện D20 C10-11,C26 và D24 C30-34,C42; nếu DNS còn yếu, dùng nửa phần thêm giờ để chữa D20 C29 | Vẽ đúng DNS; phân biệt socket UDP/TCP; tính Length/payload và checksum hai từ |
| **5** | 55' rdt1.0-3.0/FSM + 40' GBN/SR/mất ACK + 15' tự mô phỏng và chữa lỗi | Làm D19 C8,C11,C18,C19, D20 C9,C16,C19,C25; khi cơ chế chắc mới đọc phép tính utilization | Tái tạo bảng RDT và mô phỏng một trường hợp mất gói/ACK mà không nhìn mẫu |
| **6** | 40' TCP Seq/ACK/MSS/phát lại + 30' rwnd/handshake/FIN + 15' congestion cơ bản + 25' làm/chữa D19 C5,C9,C15 và D20 C6-8,C15,C30 | Khoảng 25' EstimatedRTT D20 C23; 20' thêm Seq/ACK; phần còn lại đọc LT3 tr.96-102 | Theo dõi đúng Seq/ACK theo byte; phân biệt rwnd/cwnd và thiết lập/đóng kết nối |
| **7** | 65' làm D25 C1-30 + 35' chữa theo cơ chế, ghi câu thiếu giả thiết + 10' viết lại tờ nhớ nhanh | Chữa hai nhóm yếu nhất, làm lại câu từ D23/D24 chưa dùng; tránh mở thêm chủ đề C | Một đề tổng hợp đã chữa và danh sách lỗi cụ thể cần xem trước ngày thi |

Quỹ giờ cơ sở chia gần đúng: **Ch1 3 giờ, Ch2 4 giờ, Ch3 5 giờ, tổng hợp 2 giờ**, có tính nghỉ. Bản 14 giờ ưu tiên kỹ năng A; giờ thứ ba dùng để luyện/sửa chỗ chưa hiểu và các mục B. Nếu một ngày thiếu giờ, giữ phần học cơ chế và chữa lỗi; giảm số câu lặp cùng dạng trước.

D25 giữ làm lượt kiểm tra tổng hợp; chưa cần mở bảng đáp án trang 6. Các câu chưa chặt không dùng làm thước đo “mình sai kiến thức”; đánh dấu và kiểm bằng lý thuyết. Nếu đã xem D25 trước đó, vẫn làm lại và ghi rõ câu nào trả lời nhờ nhớ chữ, câu nào tự suy được.

### Cách học trong từng khối

Đọc một nhóm khái niệm, đóng slide rồi giải thích/vẽ lại, sau đó làm một vài câu và chữa từng lý do sai. Với câu tính, ghi **đơn vị -> giả thiết -> công thức/cơ chế -> kết quả**. Với RDT/TCP, vẽ hai đầu và xử lý sự kiện theo thời gian; không cộng Seq/ACK theo cảm giác.

Nhật ký lỗi nên ghi: câu/nguồn; sai vì khái niệm, đơn vị, giả thiết hay đọc hình; nguyên tắc đúng; trang lý thuyết; kết quả làm lại hôm sau. Mỗi ngày nhắc lại ít nhất một nội dung hôm trước trong các khối truy hồi/chữa bài.

## 7. Công thức và chỗ cần tránh học nhầm

### Công thức cơ sở có điều kiện

| Dạng | Cách dùng |
|---|---|
| Trễ truyền | `d_trans = L/R`, L theo bit, R theo bit/s |
| Trễ lan truyền | `d_prop = d/s`, d theo m, s theo m/s |
| Trễ tại nút | `d_proc + d_queue + d_trans + d_prop` |
| Một gói qua nhiều link store-and-forward | `Σ(L/R_i) + Σ(d_i/s_i)` nếu bỏ processing và queue; nếu có thì cộng đúng số lần |
| Thông lượng đường nối tiếp | Mô hình một luồng không cạnh tranh: nút thắt `min(R_i)`; khi chia sẻ cần thêm giả thiết |
| Số gói phát được trong t | `floor(Rt/L)` nếu bỏ overhead và chỉ xét thời gian phát trên link |
| HTTP một object, TCP mới | `2RTT + t_object` trong mô hình không TLS, bỏ xử lý và thời gian truyền request/header |
| UDP Length | `payload + 8 byte`; chiều ngược lại lấy Length trừ 8 |
| TCP dữ liệu liên tục | Segment Seq=s, payload=L byte: byte kế tiếp là `s+L`; ACK bằng giá trị đó chỉ khi không còn lỗ hổng trước nó |

Nguồn các công thức: LT1 tr.48,50,55-56; LT2 tr.20-24; LT3 tr.28-34,76-84. Không thay tổng trễ truyền của một gói bằng `L/min(R_i)`; thông lượng và độ trễ là hai câu hỏi khác nhau. Trong TCP, ACK thuần không chiếm một byte Seq; SYN/FIN chiếm một số thứ tự.

### Những điểm trong nguồn cần ghi chú

1. **LT2 tr.24:** persistent không tự đồng nghĩa pipelining. Mệnh đề “1 RTT cho tất cả object tham chiếu” chỉ áp được theo giả định tương ứng, không áp cho mọi kiểu lấy object.
2. **LT3 tr.78:** ví dụ ghi 9000 byte nhưng có chú thích `#0..#9999`/năm đoạn 2000 byte. Hình/bảng cho đoạn cuối 1000 byte và ACK cuối 9000: học theo tổng 9000 byte, không chép số mâu thuẫn.
3. **LT3 tr.88-89:** rwnd là **bên nhận** quảng bá phần trống bộ đệm; bên gửi tuân theo. Có dòng chữ trong slide nhầm vai trò bên gửi.
4. **D25 C30:** rdt2.1 xử lý sự mơ hồ khi ACK/NAK **hỏng** bằng sequence number; xử lý **mất** gói cần timer của rdt3.0. Không học rằng rdt2.1 đã giải quyết mất ACK chỉ nhờ số thứ tự.
5. **D25 C19:** phải phân biệt host->local và local->các DNS khác. Việc local tiếp tục đi hỏi không đủ một mình để kết luận toàn bộ quá trình là recursive hay iterative; xem vai trò truy vấn/referral và mũi tên LT2 tr.70-72.
6. **D23 C6:** hỏi phiên bản nào “truyền tin cậy” mà không nêu loại kênh; mỗi phiên bản có giả định riêng. Dùng để thảo luận giả định, không ghi nhớ một đáp án làm định nghĩa duy nhất.
7. **D25 C26:** đóng gói là thêm thông tin điều khiển theo tầng/giao thức tương ứng; tầng vật lý truyền bit. Cách nói “mọi tầng đều thêm header” là giản lược, không phải quy tắc tuyệt đối.
8. **D25 C3/C22:** UDP ít overhead không bảo đảm luôn nhanh hơn TCP trong mọi hoàn cảnh; cache giảm tải/độ trễ, không tự làm tăng dung lượng vật lý đường truyền.
9. **D24 C6:** có lựa chọn viết `Bps (bit per second)` lẫn ký hiệu b/B. Nhớ `bps` là bit/s; `B/s` là byte/s, một byte bằng tám bit.
10. **D23 C21:** HTTP và NFS đều là giao thức tầng ứng dụng theo cách phân loại Internet, nên câu hỏi chọn một đáp án chưa chặt. NFS cũng được đặt trong nhóm application-layer protocols tại [RFC 2074 mục 5.5.10](https://www.rfc-editor.org/rfc/rfc2074.html#section-5.5.10). Chỉ dùng câu này để nhận diện chủ đề, không lấy một key làm chuẩn duy nhất. Việc kiểm bổ sung này không đưa NFS vào trọng tâm tuần học.

### Phần RTT thiếu trong file lý thuyết

D20 C23 hỏi EstimatedRTT nhưng LT3 không có phần công thức chi tiết. Để không suy từ đáp án, đã đối chiếu quy tắc khởi tạo/cập nhật tại [RFC 6298 mục 2.2-2.3](https://www.rfc-editor.org/rfc/rfc6298.html#section-2): mẫu đầu dùng để khởi tạo giá trị RTT làm trơn, các mẫu sau cập nhật `E_mới=(1-alpha)E_cũ+alpha*SampleRTT_mới`. Chuẩn khuyến nghị alpha=1/8; bài D20 cho alpha=0.2 thì dùng **hệ số của đề**. Nếu coi ba mẫu trong câu là từ đầu kết nối, khởi tạo E1=80 ms, sau đó E2=84 ms và E3=79.2 ms. Đây là phép tính theo giả thiết khởi tạo đã nêu; nếu có E ban đầu khác thì cần dùng giá trị đó. EstimatedRTT không đồng nhất với toàn bộ thuật toán RTO. Nguồn này chỉ kiểm công thức còn thiếu, không bổ sung đề online hay ảnh hưởng thống kê đề.

## 8. Phần hoãn sau tuần này

Giữ thời gian cho A trước khi đọc sâu: tốc độ/tên công nghệ truy cập, cấu trúc ISP chi tiết và xác suất trong LT1; phân phối file BitTorrent, HTTP/2, chi tiết message DNS, tracking/GDPR và tự viết socket app hoàn chỉnh trong LT2; tính đồ thị congestion phức tạp trong LT3. Congestion cơ bản vẫn có một lượt đọc ở ngày6 và thuộc phạm vi TCP đã chốt. QUIC/HTTP3 nằm ngoài phạm vi Ch3.

Không đưa các bài subnet/VLSM, NAT/phân mảnh IP, thuật toán routing, ARP/MAC/CSMA/CRC từ các bộ ngân hàng/bài ôn đã loại vào lịch ba chương này.

## 9. Đối chiếu đầy đủ 172 lượt câu

Các danh sách dưới đây là nhóm chương chính để kiểm đủ câu, không phải tất cả câu giao thoa đều chỉ liên quan duy nhất một chương.

| Đề | Chương 1 | Chương 2 | Chương 3 |
|---|---|---|---|
| D19 | 2,3,4,10,12,13 | 1,14,20,22,23,26,27,28,29,30 | 5,6,7,8,9,11,15,16,17,18,19,21,24,25 |
| D20 | 4,5,14,20 | 1,2,3,12,13,17,18,22,24,27,28,29 | 6,7,8,9,10,11,15,16,19,21,23,25,26,30 |
| D23 | 1,12,21,31,33,36 | 5,7,8,9,11,13,14,15,16,17,18,19,20,22,23,24,25,26,29,30,32 | 2,3,4,6,10,27,28,34,35,37,38,39,40 |
| D24 | 1,3,6,7,23,25,35 | 2,8,9,10,12,13,14,15,16,17,18,19,20,22,24,26,27,28,36,38,39 | 4,5,11,21,29,30,31,32,33,34,37,40,41,42 |
| D25 | 12,21,26 | 2,6,7,8,10,14,19,20,22,25,28 | 1,3,4,5,9,11,13,15,16,17,18,23,24,27,29,30 |

Các đường dẫn nội bộ sau tính từ thư mục `NMMMT/`: tệp dữ liệu để kiểm lại là `tmp/study_audit/question_classification.json`; `memory.md` ghi phạm vi và quyết định; toàn bộ dữ liệu extract/OCR ở `tmp/study_audit/`. Bảng phân bố, câu minh họa và lịch luyện trong bản này chỉ dùng năm bộ đề đã chốt.
