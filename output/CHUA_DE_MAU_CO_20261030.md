# Chữa đề mẫu cô cung cấp — 30/10/2026

Đề15câu do người dùng gửi và xác nhận là đề làm mẫu của cô. Đây là nguồn luyện/chữa bổ sung được cho phép riêng, không nhập vào thống kê5PDF/172lượt câu và không thay T1/T2/T3 làm nguồn lý thuyết chính.

Nguồn ảnh: [trang1](<C:/Users/phuoc/Downloads/drive-download-20261030T020832Z-1-001/20261030_090708.jpg>), [trang2](<C:/Users/phuoc/Downloads/drive-download-20261030T020832Z-1-001/20261030_090713.jpg>). Dấu chọn mờ đã được người dùng xác nhận bằng tin nhắn: câu2=A,10=B,12=A; không tự suy đoán từ nét gạch sửa.

## Kết quả

Trong14câu đã chọn:10đúng,4sai (2,6,10,11), tính câu12A theo ý hỏi chức năng và ghi rõ lỗi tên ởD. Câu15 chưa thấy đáp án được chọn và nằm ngoài phạm vi TCP hiện hành nên không tính là một câu đã làm sai.

| Câu | Bạn chọn | Kết luận kiến thức | Kết quả |
|---:|---|---|---|
| 1 | C | C: cookie lưu phía client trong mô hình môn học. | Đúng |
| 2 | A | D:10RTT, một kết nối TCP mới,6object tải tuần tự. | Sai |
| 3 | D, ghi8ms | D:2000×8/(2×10^6)=0,008s=8ms. | Đúng |
| 4 | A | A:min(1,2,3)=1Mbps, mô hình không cạnh tranh. | Đúng |
| 5 | B | B:ACK200 xác nhận liên tục đến byte199. | Đúng |
| 6 | A | B:2lượt xem thành công,200 và304 dùngcache. | Sai |
| 7 | C | C:FTP dùngTCP/21 cho điều khiển; HTTP cơ sởTCP/80,SMTP/TCP25. | Đúng |
| 8 | B | B:SYNbit của segment đầu được bật; ISN không bắt buộc0. | Đúng |
| 9 | C | C là phát biểu sai trong mô hình client–server thuần túy ởT2tr6. | Đúng |
| 10 | B | C:UDP Length tối thiểu8byte, tính cả header+payload. | Sai |
| 11 | D | C theo mặc địnhHTTP1.1 khi không chỉ định đóng, path phải là/docs/index.html. | Sai |
| 12 | A | A sai chức năng:IMAP không dùng gửi thư đến người nhận; D cũng ghi sai tên chuẩn. | Chấp nhậnA theo ý hỏi; đề chưa chặt |
| 13 | D | D:port giúp giao dữ liệu tới đúng đầu nhận ứng dụng/process. | Đúng |
| 14 | A | A:checksum00001001 11100010. | Đúng |
| 15 | Chưa có lựa chọn rõ | B:cấp số nhân/nhân đôi mỗiRTT trong slowstart của mô hìnhT3tr98. | Chưa làm; ngoài phạm vi đã chốt |

## Chữa các câu sai

### Câu2 — Persistent without pipelining

Một HTML+5ảnh là6object. Giả sử một TCP mới, cùng server, tải tuần tự, khôngTLS/DNS/xử lý và bỏ thời gian truyền request/header:

T=1RTT mởTCP+6RTT cho6request/byte phản hồi đầu tiên+6×0,5RTT truyền object=10RTT →D.

Tổng quát mộtHTML tham chiếu mobject: T=(m+2)RTT+Σt_i trong cùng mô hình. Không dùng kết luận '1RTT cho tất cả object' của mô hình pipelining cho trường hợp without pipelining. Nguồn chính:T2tr20–24.

### Câu6 — 304 vẫn có thể xem nội dung

200 trả nội dung thành công;304 cho phép dùng lại bảncache hợp lệ mà không gửi lại body. 404/502 không phải thành công lấy nội dung yêu cầu trong mô hình này, nên200/304/404/502 có2lượt →B. Không chỉ đếm số mã2xx.

304 có ởT2tr47;502 là phần bổ sung để đọc đề mẫu, đối chiếu[RFC9110 §15.4.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.4.5) và[§15.6.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6.3).

### Câu10 — Giá trịLength và kích thước trường

UDPheader=8byte; UDP Length=8+payload, giá trị tối thiểu8byte và payload=Length−8. Bản thân trườngLength dài16bit=2byte: không phải16byte, cũng không chỉ đo payload. Vì vậy chọnC. Nguồn chính:T3tr29.

### Câu11 — Phiên bản vàURL

GET /docs/index.html cho path/docs/index.html; Host cho www-net.cs.umass.edu. Trong mô hìnhHTTP thường, URL đầy đủ là http://www-net.cs.umass.edu/docs/index.html, không chỉ hostname.

HTTP/1.1 mặc địnhpersistent nếu không có chỉ định đóng như Connection: close; đề chỉ trích một phầnrequest nên nêu điều kiện mặc định, không khẳng định mọiHTTP1.1luônpersistent. Đáp án dự kiếnC; các lựa chọn trong đề đã bỏscheme. Nguồn chính:T2tr17/24–26; làm rõ bổ sung:[RFC9112 §9.3](https://www.rfc-editor.org/rfc/rfc9112.html#section-9.3).

## Hai câu cần ghi chú

### Câu12 — Lỗi tênIMAP trong nguồn

IMAP truy xuất/quản lý thư trên server, dùngTCP/143 trong mô hình cổng cơ sở; A nói cho phép gửi mail nên là phương án sai được dự định. Tuy nhiênD ghiInternet Mail Access Protocol, trong khi tên chuẩn làInternet Message Access Protocol; lỗi tên này cũng có ởT2tr60.

Vì vậy chấp nhận lựa chọnA của người dùng theo ý hỏi chức năng, không gọi câu này là một câu một đáp án hoàn toàn chặt. Đối chiếu bổ sung:[RFC9051, phần mở đầu và§2.1](https://www.rfc-editor.org/rfc/rfc9051.html#section-2.1).

### Câu15 — Khác phạm vi đã thông báo

Đáp án kiến thức làB:trong slowstart trước ngưỡng,cwnd tăng theo cấp số nhân, xấp xỉnhân đôi mỗiRTT của mô hìnhT3tr98. Người dùng đã loạiTCP điều khiển tắc nghẽn tr96–102 ngày29/10, nên chỉ chữa câu này theo yêu cầu, không tự thêm nó vào nội dung học bắt buộc hoặc thay đổi9chặng cơ sở. Nếu phạm vi thi được cập nhật lại thì cần chốt riêng.

## Kiểm tra checksum câu14

```text
  10101100 01010001
+ 01001001 11001100
= 11110110 00011101
Đảo16bit:
  00001001 11100010  → A
```

Không có carry thứ17 trong phép cộng này.

## Đối chiếu kiến thức đã ôn

| Nhóm | Kết luận |
|---|---|
| Cookie,trễ truyền,thông lượng,ACKbyte,SYN,port,checksum | Đã có đủ cơ chế để giảiC1,3,4,5,8,13,14. |
| UDP Length | Đã cóLength=8+payload và trường16bit, nhưng người dùng còn nhầm; bổ sung minh thịgiátrị tối thiểu8byte. |
| HTTP nhiềuobject | Đã học nguyên lý và đã có phầnBtrong kế hoạch; bản tra nhanh thiếu công thức/ ví dụ without pipelining rõ ràng. |
| HTTP304 | Đã cócache/conditionalGET; thiếu nhấn rằng304vẫn xem bảncache và không chỉ đếm2xx. |
| HTTP1.1/URL | Đã học kết nối vàrequest; cần ghi rõ mặc địnhpersistent, scheme+Host+path, giữ đủ/docs. |
| Client–server | Có nguyên lý, nhưng cần nêu rõtrong mô hìnhthuần túyclientkhôngtrực tiếp cung cấp dịch vụ cho nhau. |
| FTP | FTP/TCP21đã có trong bảng; bổ sung tênFileTransferProtocol,vai tròđiều khiển/kết nối dữ liệu riêng vàcổng20active. |
| IMAP | Đã học vai trò nhưng thiếuTCP143 và cần sửa tên đầy đủMessage thayMail. |
| 502 | Chưa có trong bản tra nhanh, bổ sung định nghĩaBadGateway. |
| SlowStart | Chưa học do đãđược loại khỏi phạm vi, không phải tự bỏ sót một nội dung vẫn thuộc phạm vi. |

Đã bổ sung các mục phù hợp vàoTONG_HOP_KIEN_THUC_NMMMT_3_CHUONG.md và đồng bộ bảnObsidianMMT.md; nguồn chính vẫn làT1/T2/T3, RFC/IANA chỉ làm rõ phần thiếu/mơ hồ. Chấm độc lập từ ảnh và lý thuyết, có3subagent rà từng nhóm; không dùng file đáp án riêng hay key online.
