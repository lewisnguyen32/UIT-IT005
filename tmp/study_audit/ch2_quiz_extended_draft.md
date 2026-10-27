# Nháp nội bộ — 16 câu mở rộng Chương 2

Nguồn: T2.txt (trang vật lý PDF); ch2_analysis_strict.md. Không dùng đề online/ngân hàng/đáp án bị loại. Các câu P2P sâu và HTTP/2 là mở rộng, không thay đổi mức ưu tiên thi. Đáp án bên dưới dành cho trợ giảng, tách khỏi bản câu hỏi giao người học.

1. **Peer chưa tải xong file có thể chia sẻ chưa?** Giả sử nó đã có những chunk mà peer khác cần. Giải thích vì sao thêm peer vừa tăng nhu cầu vừa có thể tăng năng lực phân phối; vì sao không thể kết luận càng đông thì mọi người luôn tải nhanh hơn?
   - Đáp án: Có thể upload chunk đã có. Peer mới có thêm nhu cầu download và có thể đóng góp upload. Tốc độ thực tế còn phụ thuộc upload, download, chunk đang có, các peer rời/đến; không bảo đảm đơn điệu.
   - Nguồn: T2 tr.7,80,83,85–86.

2. **Tracker và torrent khác nhau thế nào?** Theo mô hình BitTorrent trong slide, Alice vừa tham gia lấy gì từ tracker, rồi lấy chunk từ đâu? Tracker có bắt buộc là nơi truyền toàn bộ file cho Alice không?
   - Đáp án: Tracker theo dõi peer và cho danh sách peer; torrent là nhóm peer trao đổi chunk. Alice lấy chunk từ các peer; vai trò tracker trong mô hình không phải truyền toàn bộ nội dung.
   - Nguồn: T2 tr.85–86. Chỉ hỏi mô hình có tracker trong slide, không khái quát mọi triển khai BitTorrent.

3. **Rarest-first và tit-for-tat giải quyết việc gì?** Cơ chế nào giúp Alice chọn chunk cần yêu cầu, cơ chế nào giúp chọn peer để upload? Vì sao việc thỉnh thoảng mở upload cho một peer khác có ích?
   - Đáp án: Rarest-first ưu tiên chunk còn thiếu và hiếm trong các láng giềng. Tit-for-tat ưu tiên upload cho peer đang gửi dữ liệu tốt cho mình. Chọn thêm peer khác giúp tìm đối tác tốt mới, tạo cơ hội trao đổi; không cần học thuộc các mốc thời gian/top 4 để trả lời khái niệm.
   - Nguồn: T2 tr.87–88.

4. **Tính cận dưới phân phối file.** Cho `F=600 Mbit`, `N=10`, `u_s=20 Mbit/s`, mọi peer có `u_i=5 Mbit/s`, `d_min=10 Mbit/s`. Trong mô hình mạng lõi không là nút thắt, dùng hai cận dưới `max(NF/u_s, F/d_min)` và `max(F/u_s, F/d_min, NF/(u_s+Σu_i))` để tính cho client–server và P2P. Có được gọi kết quả là thời gian hoàn tất thực tế chắc chắn không?
   - Đáp án: Client–server `max(300,60)=300 s`; P2P `max(30,60,6000/70)≈85,7 s`. Là cận dưới theo mô hình, không bảo đảm ứng dụng thực đạt được; không dùng dấu bằng như kết quả đo.
   - Nguồn: T2 tr.81–84. Mbit dùng thập phân; `F` là bit; bỏ overhead và các nút thắt ngoài giả thiết.

5. **Object lớn chặn object nhỏ.** Trong ví dụ HTTP/1.1 pipelining của slide, client yêu cầu video O1 rồi ba object nhỏ O2–O4. Vì sao ba object nhỏ có thể chờ lâu? HTTP/2 chia object thành frame và xen kẽ việc gửi giúp gì?
   - Đáp án: Phản hồi HTTP/1.1 pipelining theo thứ tự khiến object nhỏ chờ phía sau object lớn. HTTP/2 có thể xen kẽ frame và ưu tiên object nhỏ để chúng hoàn tất sớm hơn; object lớn có thể hoàn tất muộn hơn.
   - Nguồn: T2 tr.48–50. Hỏi đúng ví dụ pipelining một kết nối trong slide, không khái quát mọi cách mở kết nối của trình duyệt.

6. **Persistent, pipelining và HTTP/2 có đồng nghĩa không?** Nêu riêng việc tái sử dụng TCP, gửi nhiều request chưa cần chờ từng response, và chia/xen kẽ frame giữa các object. Cải thiện cách xếp lịch có đủ bảo đảm mọi object luôn nhanh hơn hoặc không còn độ trễ mạng không?
   - Đáp án: Persistent tái dùng TCP; pipelining cho gửi nhiều request khi chưa nhận xong response trước trong mô hình HTTP/1.1; HTTP/2 dùng frame/multiplexing linh hoạt. Không đồng nghĩa nhau, không bảo đảm mọi object luôn nhanh hơn hay loại hết độ trễ.
   - Nguồn: T2 tr.20–24,48–50. Không cần mở sang HTTP/3/QUIC hay phân tích transport HOL sâu.

7. **Đọc loại socket.** Hai đoạn dùng `socket(AF_INET, SOCK_DGRAM)` và `socket(AF_INET, SOCK_STREAM)` trong mô hình của chương tương ứng UDP/TCP thế nào? Tên biến `tcpSocket` hoặc `udpSocket` có quyết định loại thật không? `AF_INET` cho biết điều gì?
   - Đáp án: DGRAM→UDP, STREAM→TCP trong ví dụ AF_INET; tên biến không đổi loại socket. AF_INET là họ địa chỉ IPv4.
   - Nguồn: T2 tr.91–99; memory đã chuẩn hóa phạm vi AF_INET.

8. **Địa chỉ trong gửi UDP/TCP.** Với mẫu UDP `sendto(message, (serverName, serverPort))` và mẫu TCP đã `connect` rồi gọi `send(message)`, vì sao mẫu UDP ghi đích trong lời gọi gửi còn mẫu TCP không ghi lại? Có phải UDP đã thực hiện bắt tay TCP ngầm không?
   - Đáp án: Mẫu UDP dùng đích cho từng datagram; mẫu TCP đã xác lập peer ở kết nối qua connect. UDP không cần bắt tay TCP. Chỉ so sánh hai mẫu đang học; không nói mọi UDP socket đều không dùng được connect.
   - Nguồn: T2 tr.92,94,98.

9. **Đọc UDP server.** Trong `message, clientAddress = serverSocket.recvfrom(2048)` rồi `serverSocket.sendto(reply, clientAddress)`, mỗi biến dùng để làm gì? Vì sao không gửi trả cho chính địa chỉ/cổng của server?
   - Đáp án: message là dữ liệu nhận; clientAddress chứa IP và port bên gửi. Phản hồi cần đến điểm cuối của client, nên dùng địa chỉ vừa nhận.
   - Nguồn: T2 tr.92,95.

10. **Có bind là TCP server?** Một đoạn có `s = socket(AF_INET, SOCK_DGRAM)` và `s.bind(('',12000))`. Nó dùng giao thức gì? `bind` có đủ chứng minh là TCP server không? Trong mẫu này bind làm gì?
   - Đáp án: UDP. bind gắn socket với địa chỉ/cổng cục bộ (ở ví dụ là port12000); cả UDP lẫn TCP đều có thể bind, nên không dùng riêng bind để phân loại.
   - Nguồn: T2 tr.95,99; strict phần bẫy socket.

11. **Tạo TCP socket đã kết nối chưa?** Sau `s = socket(AF_INET, SOCK_STREAM)`, chưa gọi gì khác, có được khẳng định TCP đã thiết lập với server không? Trong mẫu TCP client của chương, lời gọi nào bắt đầu thao tác kết nối, và tham số chứa gì?
   - Đáp án: Chưa. `s.connect((serverName,serverPort))`; chỉ định tên/IP server và port đích. Không học câu giản lược tr.96 thành tạo socket tự kết nối.
   - Nguồn: T2 tr.98; strict cảnh báo tr.96.

12. **Listener và conn.** Cho `listener.bind(('',12000)); listener.listen(1); conn, addr = listener.accept()`. Lời gọi nào đưa socket sang trạng thái lắng nghe? Lời gọi nào nhận kết nối đến? Muốn nhận dữ liệu của client vừa được nhận, dùng `listener.recv(...)` hay `conn.recv(...)`?
   - Đáp án: listen bật lắng nghe; accept nhận kết nối và trả socket conn cùng địa chỉ client; trao đổi qua conn. Không hỏi backlog1 đồng nghĩa chỉ có một client tổng cộng.
   - Nguồn: T2 tr.97,99.

13. **Nhiều client vào một server.** Trong mô hình TCP server của chương, A rồi B kết nối đến cùng listener. Sau hai lần accept, server có một socket kết nối dùng chung cho cả hai hay hai socket kết nối riêng? Listener tiếp tục giữ vai trò gì?
   - Đáp án: Hai socket kết nối riêng tương ứng hai lần accept; listener tiếp tục lắng nghe/đón kết nối. Không cần giải thích 4-tuple sâu Ch3.
   - Nguồn: T2 tr.96–99.

14. **Đóng conn có đóng server không?** Trong vòng lặp server ở tr.99, sau khi xử lý một client, chương trình gọi `connectionSocket.close()`. Nó có đóng luôn listener không? Client tiếp theo đi qua bước nào để có socket trao đổi riêng?
   - Đáp án: Chỉ đóng socket kết nối đó, listener vẫn mở. Server quay lại accept để nhận kết nối khác và lấy socket mới. Cần server còn chạy và tiếp tục vòng lặp theo giả thiết.
   - Nguồn: T2 tr.99.

15. **Tin cậy và bảo mật.** Ứng dụng gửi văn bản mật qua TCP socket cơ bản, chưa dùng lớp bảo mật nào. TCP bảo đảm giao dữ liệu tin cậy có tự làm dữ liệu thành bản mã không? Theo mô hình chương, TLS bổ sung ba mục tiêu nào?
   - Đáp án: Không tự mã hóa. TLS bổ sung mã hóa/bảo mật dữ liệu, toàn vẹn dữ liệu và chứng thực đầu cuối theo mô hình slide. Không suy ra tin cậy = bảo mật.
   - Nguồn: T2 tr.13,15.

16. **Ghép dịch vụ–transport–port.** Điền cho HTTP thường qua TCP, SMTP chuyển thư giữa mail server, DNS thông thường, POP3 cơ bản và kết nối điều khiển FTP. Với DNS có được nói luôn chỉ UDP, hoặc với mọi app gửi mail có được bắt buộc port25 không?
   - Đáp án: HTTP/TCP80; SMTP server-to-server/TCP25; DNS UDP hoặc TCP53; POP3/TCP110; FTP control/TCP21. Không nói DNS chỉ UDP hoặc mọi mail client gửi qua25. Không hỏi các cổng mã hóa/submission hay port IMAP ngoài trọng tâm đã thống nhất.
   - Nguồn: T2 tr.9,14,19,55,60 và ch2_analysis_strict.md mục2.2 đối chiếu câu ghép trong năm đề giữ lại (không nói T2 liệt kê đủ mọi port).
