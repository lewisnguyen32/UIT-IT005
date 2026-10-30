# Thứ tự học cụ thể môn Nhập môn Mạng máy tính

Dành cho người mới học, chưa chắc kiến thức, có 2-3 giờ/ngày trong 7 ngày. Đi lần lượt theo số thứ tự dưới đây. Đây là bản hướng dẫn thực hiện từ kế hoạch đã chốt, giữ nguyên phạm vi ba chương và năm bộ đề đã chọn.

Số trang là **trang PDF tính từ 1**, không phải số slide in ở góc. Khi ghi Ch1/Ch2/Ch3, mở file lý thuyết tương ứng trong `NMMMT/Lý thuyết/`.

**Phạm vi Chương 3 cập nhật ngày 29/10/2026:** chỉ học đến hết phần TCP ban đầu, gồm điều khiển luồng và thiết lập/đóng kết nối, T3 hết trang PDF94. **TCP điều khiển tắc nghẽn tr96–102 không thi**; QUIC/HTTP3 tr104–108 vẫn ngoài phạm vi. Giữ bước14–22, tổng9 chặng cơ sở; bỏ bước23. EstimatedRTT bước24 vẫn tùy chọn. Giữ số bước24/25 để không đổi các tham chiếu đã lưu.

## 1. Danh sách học theo thứ tự

| Bước | Khi học | Chương và phần | Trang cần đọc | Tóm tắt cần hiểu và việc phải làm |
|---:|---|---|---|---|
| 1 | Ngày 1 | **Ch1 - Internet, giao thức và mạng biên** | 3-7; 9-23 | Biết host, server, liên kết, router, ISP; Internet là mạng của các mạng. Giao thức quy định thông điệp/thứ tự/hành động. Nhận diện thiết bị đầu cuối, mạng truy cập và phương tiện truyền. Vẽ host -> mạng truy cập -> router. |
| 2 | Ngày 1 | **Ch1 - Mạng lõi** | 25-35 | Phân biệt routing/forwarding, chuyển mạch gói/kênh, FDM/TDM. Hiểu store-and-forward: nhận đủ gói rồi mới phát tiếp. Giải thích vì sao có hàng đợi và mất gói. |
| 3 | Ngày 1 | **Ch1 - Chồng giao thức** | 58-67 | Học thứ tự năm tầng, chức năng, đơn vị dữ liệu và đóng/mở gói. Tự lập bảng tầng -> nhiệm vụ -> PDU; theo dõi một thông điệp qua host-switch-router-host. |
| 4 | Ngày 1 | **Ch1 - Đơn vị và các loại độ trễ** | 46-52 | Phân biệt xử lý, hàng đợi, truyền và lan truyền. Đổi byte-bit, Mbps-bit/s, km-m, s-ms. Hiểu vì sao `L/R` khác `d/s`; làm một bài một link. |
| 5 | Ngày 2 | **Ch1 - Nhiều link, thông lượng và RTT** | 46-56 | Vẽ timeline một gói qua nhiều link; cộng đúng độ trễ. Hiểu throughput bị giới hạn bởi nút thắt, RTT là đi-về. Làm một bài nhiều link và một bài bottleneck. |
| 6 | Ngày 2 | **Ch2 - Nguyên lý ứng dụng mạng** | 3-15 | Phân biệt client-server/P2P; host/process/socket; IP+port ở góc nhìn ứng dụng. Hiểu ứng dụng cần những dịch vụ gì từ TCP/UDP. Tự kể ai khởi tạo và ai chờ kết nối. |
| 7 | Ngày 2 | **Ch2 - Web/HTTP và cấu trúc thông điệp** | 17-30; 51 | Hiểu trang HTML và object, URL, request/response. Đọc method, Host, version, status, Connection, Content-Length, header/body. Tự chú thích một request và một response trong đề. |
| 8 | Ngày 3 | **Ch2 - Cookie, cache và conditional GET** | 19; 31-34; 41-47 | Phân biệt lưu trạng thái phiên với lưu bản sao nội dung. Hiểu Set-Cookie/Cookie, If-Modified-Since và 304. Tự giải thích dữ liệu nào được gửi lại và dữ liệu nào lấy từ cache. |
| 9 | Ngày 3 | **Ch2 - Kết nối HTTP và RTT** | 20-24 | Nonpersistent dùng một object/kết nối; persistent tái sử dụng kết nối. Vẽ TCP setup -> request -> response và giải thích `2RTT + thời gian truyền` cho một object trong mô hình đơn giản. Nhiều object/pipelining học thêm sau. |
| 10 | Ngày 3 | **Ch2 - Mail/SMTP/POP3/IMAP** | 53-60 | Vẽ user agent -> mail server gửi -> mail server nhận -> user agent nhận. SMTP gửi/chuyển thư; POP3/IMAP hoặc HTTP cho webmail dùng truy xuất. Phân biệt mailbox với message queue; nhận diện cổng dịch vụ theo kế hoạch. |
| 11 | Ngày 3 | **Ch2 - DNS: chức năng và phân cấp** | 62-69 | Hiểu tên miền được phân giải ra sao; lý do phân tán/phân cấp; vai trò local resolver, root, TLD, authoritative. Biết host hỏi ai trước trong mô hình bài học. |
| 12 | Ngày 4 | **Ch2 - DNS: truy vấn, cache và bản ghi** | 70-77 | Theo mũi tên để phân biệt iterative/recursive. Học TTL, A, NS, CNAME, MX. Tự lần theo CNAME -> A và phân biệt IP của web server, DNS server, mail server. |
| 13 | Ngày 4 | **Ch2 - Nhận diện mã socket** | 90-99 | Nhận diện TCP/UDP và client/server qua SOCK_STREAM, SOCK_DGRAM, connect, listen/accept, sendto/recvfrom. Mục tiêu là đọc hiểu vai trò; chưa cần tự lập trình cả ứng dụng. |
| 14 | Ngày 4 | **Ch3 - Dịch vụ vận chuyển và mux/demux** | 5-8; 10-22 | Transport phục vụ process-process. Hiểu gom dữ liệu ở gửi, giao đúng socket ở nhận; source/destination port; UDP socket và TCP connection theo quy tắc trong slide. Vẽ bảng port cho gói đi/gói về. |
| 15 | Ngày 4 | **Ch3 - UDP và header** | 24-29 | Hiểu không kết nối; những dịch vụ UDP không tự cung cấp. Tự vẽ bốn trường 16 bit, header 8 byte; phân biệt Length với payload và tính theo hai chiều. |
| 16 | Ngày 4 | **Ch3 - Checksum** | 30-34 | Cộng bù 1, cộng vòng carry, đảo bit. Tính được hai từ 16 bit; sau đó thử ba từ. Phân biệt phát hiện lỗi với sửa lỗi, và không phát hiện lỗi với chắc chắn không lỗi. |
| 17 | Ngày 5 | **Ch3 - Nguyên lý RDT, rdt1.0 đến rdt2.2** | 36-56 | Từng bước trả lời vì sao cần checksum, ACK/NAK, phát lại và sequence 0/1. rdt2.1 xử lý ACK/NAK hỏng, rdt2.2 dùng ACK thay NAK. Đọc trạng thái/điều kiện/hành động trong FSM. |
| 18 | Ngày 5 | **Ch3 - rdt3.0, timer và timeout** | 57-61 | Bổ sung tình huống mất data hoặc ACK. Hiểu timeout/phát lại, ACK đến trễ và gói trùng; giải thích vì sao không giao bản trùng lên ứng dụng. |
| 19 | Ngày 5 | **Ch3 - Stop-and-wait, pipelining, GBN/SR** | 62-73 | Hiểu chờ ACK làm giảm hiệu suất, cửa sổ cho phép nhiều gói đang chờ. So sánh ACK tích lũy/riêng, buffer, timer và gói phải phát lại. Theo đúng mô hình hủy/lưu gói sai thứ tự được đề cho. |
| 20 | Ngày 6 | **Ch3 - TCP: header, MSS, Seq/ACK, phát lại** | 75-84 | TCP đếm byte; Seq là byte đầu tiên của segment, ACK là byte kế tiếp còn chờ liên tục. Tính theo payload, không đếm số gói. Theo dõi mất ACK, timeout sớm và phát lại nhanh. |
| 21 | Ngày 6 | **Ch3 - Điều khiển luồng** | 85-89 | Bên nhận quảng bá rwnd để bảo vệ bộ đệm; bên gửi giới hạn dữ liệu chưa ACK. Phân biệt rwnd với MSS/kích thước mỗi segment và tổng dữ liệu đã gửi. |
| 22 | Ngày 6 | **Ch3 - Thiết lập và đóng TCP** | 90-94 | Vẽ SYN -> SYN+ACK -> ACK. Hiểu số thứ tự ban đầu, SYN/FIN chiếm một số thứ tự; FIN kết thúc một chiều gửi và phía đó vẫn có thể nhận chiều ngược lại. |
| 23 | Bỏ khỏi lịch | **Ngoài phạm vi thi: TCP điều khiển tắc nghẽn** | 96-102 | Loại theo yêu cầu ngày29/10/2026; không học, đặt câu tự kiểm hoặc tính vào tiến độ cơ sở. Fast retransmit tr84 vẫn thuộc bước20 đã giữ. |
| 24 | Thêm giờ ngày 6 | **Ch3 - EstimatedRTT** | Mục 7 của kế hoạch chính | LT3 thiếu công thức chi tiết. Đọc phần bổ sung đã kiểm nguồn, ghi rõ giá trị khởi tạo/hệ số rồi làm câu 23 đề 2020-2021. Đây là mục B: ưu tiên sau Seq/ACK, RDT và checksum. |
| 25 | Ngày 7 | **Tổng hợp cả ba chương** | Đề 2025-2026; xem lại trang lý thuyết của từng lỗi | Làm 30 câu trong 65 phút, sau đó chữa theo cơ chế. Phân biệt sai kiến thức, đơn vị, giả thiết và đọc hình; đánh dấu câu chưa chặt. Viết lại một tờ nhớ nhanh. |

## 2. Khi nào chuyển sang phần tiếp theo

- **Sau bước 3:** viết đủ năm tầng và giải thích được dữ liệu được đóng gói ra sao.
- **Sau bước 5:** tự giải được trễ một link, trễ nhiều link và bottleneck; giải thích RTT khác trễ lan truyền một chiều.
- **Sau bước 9:** đọc được một HTTP request/response, phân biệt cookie/cache và giải thích được hai RTT của một object.
- **Sau bước 13:** vẽ được đường gửi/đọc mail, sơ đồ DNS và lần theo các bản ghi; nhận diện được mã socket cơ bản.
- **Sau bước 16:** tự vẽ UDP header, tính Length/payload và checksum hai từ 16 bit.
- **Sau bước 19:** nói được lỗi nào khiến RDT thêm cơ chế nào; mô phỏng được một trường hợp mất packet/ACK trong GBN/SR.
- **Sau bước 22:** tính Seq/ACK theo byte, giải thích rwnd và vẽ đúng handshake/đóng một chiều.

Chỗ nào chưa đạt, dùng giờ tăng cường để học lại chính phần đó trước khi tăng độ khó. Các mốc này là tự kiểm học tập, không phải yêu cầu làm đúng toàn bộ mọi câu trong đề.

## 3. Nhịp học trong tuần

| Ngày | Bước theo thứ tự | Quỹ cơ sở |
|---|---|---|
| 1 | 1-4 và luyện ngắn Ch1 | 110 phút học + 10 phút nghỉ |
| 2 | 5-7 | 110 phút học + 10 phút nghỉ |
| 3 | 8-11 | 110 phút học + 10 phút nghỉ |
| 4 | 12-16 và truy hồi Ch2 | 110 phút học + 10 phút nghỉ |
| 5 | 17-19 và chữa sơ đồ | 110 phút học + 10 phút nghỉ |
| 6 | 20-22 và luyện TCP; bước 24 nếu có thêm giờ | 110 phút học + 10 phút nghỉ |
| 7 | 25: 65 phút làm đề + 35 phút chữa + 10 phút nhớ lại | 110 phút học + 10 phút nghỉ |

Ngày có ba giờ: thêm tối đa 60 phút gồm nghỉ ngắn, ưu tiên chữa phần A còn yếu. BitTorrent và HTTP/2 để sau nền cơ bản theo kế hoạch. TCP điều khiển tắc nghẽn và QUIC/HTTP3 ngoài phạm vi thi, không dùng giờ thêm để tự đưa lại vào lịch. Phần mở rộng còn giữ, câu luyện và các giả thiết công thức theo kế hoạch chính.

## 4. Lưu ý khi đọc tài liệu

1. LT2 tr.24: persistent không tự đồng nghĩa pipelining; không dùng “1RTT cho tất cả object” cho mọi tình huống.
2. LT3 tr.78: ví dụ 9000 byte có chú thích không nhất quán; xem bảng/hình và lưu ý trong kế hoạch trước khi tính.
3. LT3 tr.88-89: rwnd là bên nhận quảng bá; có dòng chữ nhầm vai trò bên gửi.
4. ACK/NAK hỏng trong rdt2.1 khác mất ACK trong rdt3.0; cần phân biệt sequence number với timer.
5. TCP chỉ dùng ACK=Seq+payload khi dữ liệu tới liên tục và không có lỗ hổng trước đó; SYN/FIN có quy tắc số thứ tự riêng.

## 5. Tài liệu liên quan

- [Kế hoạch chính và câu đề đối chiếu](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/output/KE_HOACH_ON_NMMMT_7_NGAY.md>)
- [Lý thuyết Chương1](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf>)
- [Lý thuyết Chương2](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf>)
- [Lý thuyết Chương3](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf>)

Tóm tắt trong bản này bám theo kế hoạch đã đối chiếu nguồn. Không thêm đề online, đề mẫu, training hoặc ngân hàng câu hỏi.
