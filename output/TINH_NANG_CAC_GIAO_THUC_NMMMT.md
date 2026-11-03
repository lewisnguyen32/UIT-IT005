# Tính năng các giao thức — ôn nhanh NMMMT

Tài liệu tra nhanh theo phần đã ôn và hai đề 2019–2020, 2020–2021. Nhớ chức năng trước, cổng sau. Việc có bảng này không đồng nghĩa đã thành thạo từng giao thức.

## 1. Các giao thức tầng ứng dụng

| Giao thức | Chức năng chính | Điểm cần nhớ | Cổng thường gặp trong bài học |
|---|---|---|---|
| **HTTP** | Trao đổi tài nguyên web giữa client và server | Dùng request/response. Trong mô hình đang học, HTTP chạy trên TCP; có kết nối bền vững hoặc không bền vững. | TCP **80** |
| **FTP** | Truyền, tải tập tin giữa client và server | Phân biệt kết nối điều khiển với kết nối dữ liệu. Cổng 21 là cổng điều khiển, không phải cổng truyền mọi dữ liệu của FTP. | TCP **21** cho điều khiển |
| **SMTP** | Gửi thư từ user agent lên mail server và chuyển thư giữa các mail server | Là giao thức gửi/chuyển thư; không dùng để lấy thư từ hộp thư về đọc. | TCP **25**, đặc biệt server-to-server trong mô hình đề |
| **POP3** | Truy xuất, tải thư từ mail server về mail client | Chủ yếu tải thư về để quản lý cục bộ; có thể giữ bản sao trên server tùy chế độ. Không bắt buộc tải xong là xóa. | TCP **110** |
| **IMAP** | Truy cập và quản lý thư lưu trên server | Quản lý thư, thư mục, trạng thái trên server; thuận tiện đồng bộ nhiều thiết bị. Vẫn tải nội dung thư về khi đọc. | TCP **143** |
| **DNS** | Phân giải tên miền thành địa chỉ IP | Còn hỗ trợ bí danh máy, tìm mail server và cân bằng tải; có cache. DNS thuộc tầng ứng dụng. | UDP/TCP **53** |
| **Telnet** | Đăng nhập, thao tác máy từ xa bằng dòng lệnh | Trong câu ghép cổng của đề: Telnet dùng TCP, không phải UDP. | TCP **23** |

Các cổng trên là cổng dịch vụ quen thuộc trong bài học, không phải cổng nguồn cố định của mọi client. Bảng không liệt kê các biến thể bảo mật hay mọi cách triển khai thực tế.

### Nhớ nhanh thư điện tử

**SMTP gửi — POP3 tải về — IMAP quản lý trên server.**

Theo sơ đồ mail trong đề:

1. User agent của Alice → mail server của Alice: **SMTP**.
2. Mail server của Alice → mail server của Bob: **SMTP**.
3. Mail server của Bob lưu thư trong **mailbox** của Bob.
4. Bob truy cập/đọc thư: **POP3, IMAP**, hoặc **HTTP** nếu truy cập giao diện webmail.

**Mailbox** giữ thư đã nhận cho người dùng; **message queue** giữ thư đang chờ gửi. Người nhận chưa mở ứng dụng không ngăn mail server nhận và lưu thư.

### Các điểm thường hỏi về HTTP và DNS

| Chủ đề | Ý cần nhớ |
|---|---|
| HTTP không bền vững | Trong mô hình bài học: mỗi kết nối TCP truyền một đối tượng rồi đóng. |
| HTTP bền vững | Một kết nối TCP có thể dùng cho nhiều đối tượng. |
| Web cache | Giảm thời gian đáp ứng và lưu lượng trên đường truy cập khi phục vụ được nội dung đã lưu. |
| HTTP 200 | Yêu cầu thành công; trong ví dụ GET, phản hồi mang tài nguyên được yêu cầu. |
| HTTP 301 | Tài nguyên đã chuyển sang URL mới; xem trường `Location`. |
| HTTP 304 | Bản đã lưu trong cache vẫn dùng được; phản hồi không gửi lại body của tài nguyên. |
| HTTP 404 | Không tìm thấy tài nguyên được yêu cầu; phản hồi vẫn có thể có body trang báo lỗi. |
| DNS tuần tự | DNS cục bộ lần lượt hỏi root, TLD, authoritative; máy chủ được hỏi trả referral khi chưa có kết quả cuối. |
| DNS đệ quy | Máy chủ được hỏi tiếp tục nhờ máy chủ khác phân giải thay cho bên yêu cầu. |
| DNS cache | Lưu ánh xạ để dùng lại trong thời gian TTL; thông tin có thể cũ trước khi hết TTL. |
| Bản ghi A / CNAME / MX | A: tên → IP; CNAME: bí danh → tên gốc; MX: tên miền → tên mail server. |

## 2. TCP và UDP — tầng vận chuyển

Cả hai cung cấp truyền thông logic **giữa các tiến trình ở các hệ thống đầu cuối**. Đừng nhầm chức năng này với truyền giữa các host của tầng mạng.

| Tính năng | **TCP** | **UDP** |
|---|---|---|
| Thiết lập kết nối | Có; bắt tay trước khi truyền trong mô hình đang học | Không thiết lập kết nối |
| Đơn vị dữ liệu | Segment; dữ liệu ứng dụng được cung cấp dưới dạng luồng byte | Datagram; mỗi thông điệp được xử lý độc lập |
| Truyền tin cậy | Có ACK, số thứ tự và phát lại khi cần | Không tự ACK/phát lại để bảo đảm tin cậy |
| Thứ tự giao dữ liệu lên ứng dụng | Đúng thứ tự, không giao trùng | Không bảo đảm thứ tự hoặc chống trùng |
| Điều khiển luồng | Có; dùng cửa sổ nhận để tránh làm tràn bộ đệm bên nhận | Không có sẵn |
| Phát hiện lỗi bit | Có checksum | Có checksum; không tự sửa lỗi/phát lại |
| Bảo đảm thông lượng tối thiểu | Không | Không |
| Bảo đảm độ trễ | Không | Không |
| Tự mã hóa dữ liệu | Không | Không |

### Các điểm dễ nhầm

- **TCP tin cậy không có nghĩa là TCP tự mã hóa.** Độ tin cậy truyền tải khác với bảo mật.
- **UDP có checksum không có nghĩa là UDP truyền tin cậy.** Phát hiện lỗi khác với khôi phục dữ liệu bị mất/hỏng.
- Ứng dụng dùng UDP có thể tự bổ sung ACK, timer và phát lại; đó không phải tính năng UDP tự cung cấp.
- UDP không bảo đảm độ trễ thấp và không phải lúc nào cũng nhanh hơn TCP.
- TCP `Seq` đếm theo **byte**; `ACK` là **byte tiếp theo đang chờ theo thứ tự**.
- ACK nằm trong segment đang đọc xác nhận dữ liệu của **chiều ngược lại**; không tự lấy ACK đó làm ACK trả lời cho payload của chính segment ấy.
- UDP header dài **8 bytes**; trường `Length` tính **cả header và payload**. Ví dụ `Length = 1000` thì payload là `992 bytes`.

## 3. RDT — các mô hình xây dựng truyền tin cậy

RDT là chuỗi mô hình trong bài học để hiểu cách xây dựng truyền tin cậy, không phải các giao thức ứng dụng như HTTP hay SMTP.

| Phiên bản | Vấn đề/giả định | Cơ chế và dấu hiệu nhận diện |
|---|---|---|
| **RDT 1.0** | Kênh hoàn toàn tin cậy | Gửi → nhận → giao dữ liệu; chưa cần cơ chế phục hồi lỗi/mất. |
| **RDT 2.0** | Có lỗi bit ở dữ liệu | Checksum + ACK/NAK + phát lại. ACK/NAK bị hỏng vẫn là lỗ hổng. |
| **RDT 2.1** | ACK/NAK có thể hỏng | Thêm Seq 0/1 để phân biệt dữ liệu mới và bản phát lại, chống giao trùng lên ứng dụng. |
| **RDT 2.2** | Thay NAK bằng ACK | Chỉ dùng ACK có số; ACK của gói đúng cuối cùng đóng vai trò phản hồi khi chưa nhận đúng gói đang chờ. |
| **RDT 3.0** | Có thể mất dữ liệu hoặc ACK | Thêm timer; hết thời gian chờ mà chưa có ACK hợp lệ thì phát lại. Vẫn stop-and-wait. |

**RDT 2.1 xử lý ACK/NAK hỏng, không tự có timer để xử lý ACK mất.**

**Timeout chỉ cho biết chưa nhận ACK hợp lệ đúng hạn.** Bên gửi không xác định được dữ liệu mất, ACK mất/hỏng hay gói/ACK chỉ đến chậm. Phát lại giữ nguyên số thứ tự; bên nhận dùng số thứ tự để tránh giao dữ liệu trùng.

## 4. Go-Back-N và Selective Repeat

Cả hai cho phép **pipeline**: gửi nhiều gói liên tiếp khi các gói trước chưa được ACK.

| Đặc điểm | **Go-Back-N — GBN** | **Selective Repeat — SR** |
|---|---|---|
| ACK | Tích lũy | Riêng từng gói nhận đúng |
| Timer | Cho gói chưa được xác nhận sớm nhất | Riêng từng gói chưa được xác nhận |
| Khi timeout | Gửi lại từ gói hết hạn và các gói sau nó còn đang chờ ACK | Chỉ phát lại gói hết hạn tương ứng |
| Gói ngoài thứ tự | Theo giả thiết/cách triển khai; bản bài tập thường bỏ gói ngoài thứ tự | Lưu gói hợp lệ trong cửa sổ nhận để chờ lấp chỗ thiếu |
| Giao lên ứng dụng | Theo đúng thứ tự | Theo đúng thứ tự; có thể giao liên tiếp các gói đã lưu sau khi lấp chỗ thiếu |

### Hai lưu ý quan trọng

1. **GBN không nhất thiết phát lại chỉ vì mất một ACK.** ACK tích lũy cao hơn có thể đã xác nhận cả các gói trước đó.
2. T3 trang PDF 68 cho phép GBN **hủy hoặc lưu buffer gói sai thứ tự tùy cách triển khai**. Khi giải bài, theo giả thiết và hình cụ thể; không khẳng định mọi GBN đều không có buffer.

### Đừng trộn hai quy ước ACK

- **GBN trong slide:** `ACK(n)` xác nhận đã nhận liên tục đến **gói n**.
- **TCP:** `ACK(n)` nghĩa là đang chờ **byte n**, đã nhận liên tục hết đến byte `n−1`.
- Gói đã **đến bên nhận** chưa chắc đã được **chấp nhận, lưu buffer hoặc giao lên ứng dụng**.

## 5. Các cặp ghép cần thuộc

| Cụm trong câu hỏi | Giao thức/cơ chế |
|---|---|
| Truyền tập tin | FTP |
| Trao đổi tài nguyên web | HTTP |
| Gửi email giữa các server | SMTP |
| Tải email từ server về client | POP3 |
| Quản lý thư/thư mục/trạng thái trên server | IMAP |
| Phân giải tên thành địa chỉ IP | DNS |
| Dịch vụ hướng kết nối, truyền tin cậy | TCP |
| Dịch vụ không kết nối | UDP |
| ACK tích lũy, timeout phát lại một nhóm gói còn chờ | GBN |
| ACK riêng, timeout phát lại riêng gói tương ứng | SR |

## Nguồn và phạm vi

- Nguồn lý thuyết chính: [T2 — Tầng ứng dụng](<../Lý thuyết/[BHT CNPM] NMMMT_Chương 2 _Tầng ứng dụng.pdf>), đặc biệt trang PDF 6, 9–15, 17–30, 41–47, 53–60, 62–77, 90–99; [T3 — Tầng vận chuyển](<../Lý thuyết/[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf>), các mục dịch vụ vận chuyển, UDP, RDT, pipeline/GBN/SR và TCP cơ sở, đến trang PDF 94.
- Cổng và các kiểu câu được đối chiếu từ phần câu hỏi [đề 2019–2020](<../Giữa Kỳ/[BHT CNPM] NMMMT 2019-2020 GK1.pdf>) và [đề 2020–2021](<../Giữa Kỳ/[BHT CNPM] NMMMT 2020-2021 GK1.pdf>). IMAP/TCP 143 và một số phân biệt về truy xuất thư là phần bổ sung đã kiểm, được ghi nhận trong nhật ký Chương 2; không khẳng định slide có liệt kê đủ mọi cổng trong bảng.
- Đây là bản tra cứu phần đã ôn; không thêm cơ chế TCP điều khiển tắc nghẽn hay QUIC/HTTP3 vào phạm vi thi đã chốt.
