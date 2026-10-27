# 80 câu tự kiểm Chương 2 — Tầng ứng dụng

Bộ câu hỏi do trợ giảng soạn theo tài liệu Chương 2 trong thư mục `Lý thuyết/`, để ôn tương tác. Đây không phải bộ câu trích nguyên văn từ đề thi, và số câu mỗi nhóm không biểu thị xác suất ra thi. Không kèm đáp án để người học tự trả lời trước khi chữa.

Đề nghị trả lời từng lượt 10 câu, kèm lý do hoặc phép tính. Có thể trả lời “chưa nhớ” để được giải thích. Câu 73–80 là phần mở rộng từ lý thuyết; nội dung mới trong nhóm này sẽ được giảng khi chữa, chưa coi là đã học.

Quy ước: mọi tên miền `.example` và IP trong ví dụ là giả định. Bảng DNS là bảng khái niệm rút gọn, lược TTL và preference của MX. Khi đọc HTTP, dùng mô hình HTTP/1.x qua TCP; các bài số bỏ DNS/TLS, xử lý/hàng đợi, kích thước request/header, mất gói và truyền lại, trừ khi đề nêu khác. Các kết nối tái sử dụng đều còn hoạt động. Câu conditional GET giả sử server xử lý điều kiện đúng theo mô hình đã học, request hợp lệ và tài nguyên vẫn tồn tại.

## Câu 1–10: Củng cố những điểm vừa nhầm

1. Browser có ảnh cũ, gửi `GET /map.png` kèm `If-Modified-Since: T1`. Server có ảnh được sửa lúc `T2`, với `T2 > T1`. Server trả mã nào, có body ảnh mới không? `If-Modified-Since` là header request hay mã response?

2. Vẫn request ở câu 1, nhưng ảnh trên server chưa thay đổi kể từ `T1`. Server trả mã nào, có gửi lại body ảnh không? Browser lấy ảnh ở đâu để hiển thị?

3. Browser gửi `GET /old.html`, nhận `301 Moved Permanently` và `Location: http://study.example/new.html`. Browser đang được thông báo điều gì? Nếu đi theo chuyển hướng của GET này, nó gửi method và đường dẫn nào? Có thể kết luận từ mã 301 rằng nội dung file đã thay đổi không?

4. TCP đã mở và còn hoạt động, browser gửi một GET. RTT = 40 ms, thời gian truyền object = 6 ms. Tổng thời gian trong mô hình là bao nhiêu? Giải thích mỗi thành phần của phép cộng.

5. Giữ dữ kiện câu 4, nhưng lần này phải thiết lập TCP mới. Tổng thời gian là bao nhiêu? Phần thời gian tăng thêm dùng cho việc gì?

6. Object dài 25.000 byte, tốc độ hiệu dụng 10 Mbps, RTT = 15 ms. Tính thời gian truyền object; sau đó tính tổng thời gian lấy object với TCP mới và với TCP đã mở. Ghi rõ bước đổi byte sang bit và giây sang ms.

7. Resolver hỏi root, root trả referral đến DNS `.com`. Ai gửi truy vấn tiếp tới `.com`? Ai là bên nhận câu trả lời đó? Đoạn root–resolver này thuộc kiểu iterative hay recursive, vì sao?

8. Host yêu cầu resolver phân giải hộ đến kết quả cuối; resolver lần lượt hỏi root, TLD và authoritative, mỗi nơi trả kết quả hoặc referral. Phân loại riêng quan hệ host→resolver và cách resolver hỏi các máy chủ trong cây. Vì sao một lần phân giải có thể kết hợp hai kiểu?

9. Cho bảng rút gọn:

   ```text
   school.example          MX   inbound.school.example
   inbound.school.example  A    192.0.2.90
   school.example          NS   ns.school.example
   ns.school.example       A    192.0.2.53
   www.school.example      A    192.0.2.10
   ```

   Mail server bên gửi muốn chuyển thư tới `an@school.example`: chọn IP nào, theo những bản ghi nào? Vì sao hai IP còn lại không phải đích nhận SMTP của ví dụ?

10. Resolver cache `www.school.example → 192.0.2.10` tại giây 0, TTL = 120 giây. Authoritative đổi IP thành `192.0.2.20` tại giây 50. Tại giây 70, cache còn bao nhiêu TTL và có thể trả IP nào? Giả sử không làm mới sớm, không dùng cache hết hạn: đọc cache có reset TTL không; hết TTL có bắt buộc gửi truy vấn ngay dù chưa có ai hỏi không?

## Câu 11–20: Nguyên lý ứng dụng, kiến trúc và dịch vụ vận chuyển

11. Phân biệt host, process và socket bằng ví dụ một máy chạy đồng thời trình duyệt và ứng dụng mail. Một host có thể chạy nhiều process không? Socket nằm ở giao diện giữa những thành phần nào?

12. Trong một lần duyệt web, hãy phân loại: trình duyệt, phần mềm Apache, máy tính chạy Apache và file `index.html`. Thành phần nào là tiến trình client, tiến trình server, host và tài nguyên? Vì sao gọi trang web là “tiến trình server” chưa chính xác?

13. Vì sao địa chỉ IP đích chưa đủ để chọn đúng điểm cuối ứng dụng trên một host? Trong mô hình cơ bản, IP và port giúp xác định điều gì? Dùng ví dụ cùng một máy có dịch vụ web và SMTP.

14. Trong client–server, phía nào thường khởi tạo liên lạc, phía nào chờ phục vụ? “Client” có đồng nghĩa với máy nhỏ và “server” với máy cấu hình mạnh không? Giải thích bằng vai trò của hai mail server khi gửi thư cho nhau.

15. So sánh client–server và P2P theo: nơi cung cấp tài nguyên, khả năng vừa nhận vừa gửi của một bên, tác động khi thêm người dùng và khó khăn khi các peer vào/ra. Vì sao P2P có tính tự mở rộng nhưng không có nghĩa là vô hạn tài nguyên?

16. Một peer có 3 trong 10 khối của file. Nó có thể cung cấp dữ liệu hữu ích cho peer khác chưa? Điều kiện là gì? Có bắt buộc chờ tải đủ file rồi mới chia sẻ không?

17. Một giao thức ứng dụng cần quy định những gì về loại thông điệp, cú pháp, ngữ nghĩa và thứ tự/hành động? Cho một ví dụ phân biệt “tên trường” với “ý nghĩa của trường”. Giao thức được công bố công khai giúp hai bên triển khai độc lập như thế nào?

18. Nêu bốn nhóm nhu cầu ứng dụng: tin cậy, độ trễ, thông lượng và bảo mật. Với tải bản sao lưu, gọi thoại trực tiếp và xem video đã lưu, hãy nêu yêu cầu nào nổi bật và vì sao. Tránh kết luận mọi ứng dụng trong một nhóm đều dùng cùng giao thức vận chuyển.

19. Đánh giá và sửa từng nhận định: “TCP tự mã hóa”; “UDP bảo đảm độ trễ thấp”; “TCP bảo đảm thông lượng tối thiểu”; “UDP không tự bảo đảm giao đủ/đúng thứ tự”; “ứng dụng dùng UDP không thể bổ sung xác nhận hay truyền lại”. Phân biệt dịch vụ transport có sẵn với cơ chế ứng dụng tự bổ sung.

20. Ghép chức năng với HTTP, SMTP, DNS, POP3, IMAP và FTP. Nêu transport/cổng trọng tâm đã học: HTTP thông thường, SMTP giữa mail server, DNS, POP3 và FTP điều khiển. Giải thích vì sao TLS cần được phân biệt với tính tin cậy của TCP; không cần học thêm cổng IMAP ở câu này.

## Câu 21–30: Đọc và hiểu HTTP

21. Trang gồm một HTML cơ sở, hai ảnh và một file CSS, mỗi thành phần là một object riêng, chưa có cache. Có bao nhiêu object? Nếu tải bằng HTTP/1.x, mỗi object cần request riêng theo mô hình đã học hay chỉ cần một GET cho cả trang?

22. Với URL `http://www.study.example/course/logo.png?size=small`, hãy chỉ ra scheme, hostname, path và query. DNS cần phân giải phần nào? Trong mô hình này, TCP kết nối đến cổng mặc định nào?

23. Đọc request:

   ```http
   GET /search?q=network HTTP/1.1
   Host: study.example
   User-Agent: DemoBrowser/7.0
   Connection: close
   ```

   Xác định method, request target, path, query, phiên bản HTTP và hostname. `DemoBrowser/7.0` có phải phiên bản HTTP không? `Connection: close` mang ý nghĩa gì trong giao dịch này?

24. Một request POST có `Content-Length: 8` và body ASCII chính xác là `name=Lan!`. Dữ kiện độ dài có nhất quán không? Nếu chưa, hãy tính lại. So sánh cách gửi dữ liệu form trong body POST với tham số trong URL của GET; có đúng rằng GET không thể mang thông tin người dùng gửi lên không?

25. Chọn method phù hợp trong các tình huống: lấy ảnh; lấy thông tin phản hồi như GET nhưng không nhận body; gửi dữ liệu biểu mẫu để server xử lý; tạo/thay thế toàn bộ biểu diễn tài nguyên tại URL đích. Giải thích vì sao PUT vào URL mới không tự đồng nghĩa với đổi tên rồi xóa URL cũ.

26. Đọc response:

   ```http
   HTTP/1.1 200 OK
   Server: DemoServer/2.0
   Content-Length: 5
   Connection: keep-alive

   Hello
   ```

   Coi body chỉ gồm đúng 5 byte ASCII `Hello`, không có newline cuối. Chỉ ra status line, các header, dòng trống và body. `Content-Length` có cộng các byte của status line/header không? Có thể lấy `DemoServer/2.0` làm phiên bản HTTP không?

27. Response ở câu 26 có phần ngoài body dài 120 byte. Tổng độ dài thông điệp HTTP là bao nhiêu byte? Nếu dùng cùng chuỗi ký tự hiển thị nhưng có ký tự Unicode, có thể luôn lấy số ký tự làm số byte của body không?

28. Giải thích ý nghĩa và phân biệt các mã `200`, `301`, `304`, `400`, `404`, `505`. Mã nào nói về URL mới; mã nào nói bản cache vẫn dùng được; mã nào nói không hỗ trợ phiên bản HTTP? Với `404`, response có thể chứa trang HTML báo lỗi không?

29. Một client gửi đúng cú pháp HTTP/1.1 nhưng yêu cầu `/missing.html` không tồn tại. Có nên giải thích `404` là “không tìm thấy HTTP/1.1” không? Nếu server muốn thông báo phiên bản HTTP không được hỗ trợ theo mã đã học thì khác thế nào?

30. Giải thích HTTP stateless ở mức giao thức. Vì sao server trả lời hai request không có nghĩa giao thức tự biết chúng thuộc cùng một phiên đăng nhập? Có thể xây dựng giỏ hàng/đăng nhập trên HTTP hay không; cần liên kết các request bằng cách nào trong mô hình cookie đã học?

## Câu 31–38: Cookie, proxy và cache

31. Server tạo phiên `sid=abc123`. Hãy vẽ chiều đi của `Set-Cookie` và `Cookie` qua hai request liên tiếp. Trong mô hình phiên dùng ID, browser lưu gì và server lưu gì? Có bắt buộc cookie chỉ xuất hiện sau khi đăng nhập không?

32. Theo slide, cơ chế cookie có bốn thành phần nào? Khi browser gửi lại `Cookie: sid=abc123`, server làm gì để tìm giỏ hàng? Vì sao không cần gửi toàn bộ giỏ hàng trong cookie của mô hình này?

33. Phân biệt cookie với cache bằng mục đích và loại dữ liệu lưu. Xóa cookie phiên và xóa bản ảnh cache có nhất thiết gây cùng một hiệu ứng không? Cookie có phải công cụ tự mã hóa dữ liệu trên đường truyền không?

34. Browser liên lạc với proxy cache; proxy cần lấy object từ origin. Ở mỗi quan hệ, proxy đóng vai client hay server? Vẽ các mũi tên request/response. Tại sao nói “proxy luôn chỉ là server” là thiếu?

35. Proxy đã có bản sao object còn hợp lệ và được phép tái sử dụng ngay. Nó có cần tải lại toàn bộ object từ origin cho mỗi request không? Nếu cache miss thì điều gì xảy ra? Nêu cách cache có thể giảm lưu lượng và độ trễ, đồng thời giải thích vì sao không làm tăng dung lượng vật lý của access link.

36. Phân biệt `Last-Modified` với `If-Modified-Since`: bên nào gửi, trong request hay response, và mốc ở request sau lấy từ đâu trong ví dụ đã học? Header `Date` của response có đồng nghĩa với lần tài nguyên được sửa cuối không?

37. Browser xác thực lại ảnh đã cache và nhận `304 Not Modified`. Nó có nhận body ảnh mới không? Nó còn trao đổi request/status/header qua mạng không? Vì sao phát biểu “304 không dùng mạng” là sai?

38. Giả sử 40% request được phục vụ hoàn toàn từ cache cục bộ, mỗi request mất trung bình 10 ms; 60% còn lại có tổng thời gian phục vụ trung bình 200 ms. Bỏ qua tương tác hàng đợi và thay đổi tải: tính thời gian trung bình có trọng số. Vì sao không thể suy ra độ trễ trung bình giảm đúng 40% chỉ từ tỷ lệ hit? Đây là bài tính thêm sau phần cơ chế.

## Câu 39–44: Kết nối HTTP và RTT

39. Trang có một HTML và bốn ảnh, tất cả cùng server, chưa cache. Nếu dùng nonpersistent tuần tự thì cần bao nhiêu kết nối TCP? Với persistent, có thể dùng bao nhiêu kết nối cho cả năm object? Persistent có tự đồng nghĩa với gửi các GET bằng pipelining không?

40. Với một object qua TCP mới, giải thích vì sao có hai RTT trong công thức `2RTT + L/R`. Với TCP đã mở, GET tuần tự, phần nào được bỏ? Vì sao RTT không phải chỉ thời gian một chiều, và vì sao không cộng lại propagation của cùng hành trình vào mô hình này?

41. HTML tham chiếu ba ảnh: tổng bốn object, cùng server, chưa cache; RTT = 25 ms. Bỏ qua thời gian truyền mọi object, tải nonpersistent hoàn toàn tuần tự. Tổng thời gian là bao nhiêu? Viết phép tính theo số object và số RTT mỗi object.

42. Giữ dữ kiện câu 41, chuyển sang một TCP persistent mới, không pipelining, request sau chỉ gửi khi object trước đã nhận đủ. Tổng thời gian là bao nhiêu? Nếu TCP đã mở từ trước khi bắt đầu lấy HTML thì giảm bao nhiêu?

43. Vẫn một HTML và ba ảnh cùng server, RTT = 25 ms, bỏ qua mọi thời gian truyền. Một TCP persistent mới: lấy xong HTML rồi gửi cả ba GET ảnh bằng pipelining. Trong mô hình đơn giản, tổng bao nhiêu RTT? Vì sao không được áp đáp số này vào câu 42?

44. Trước khi lấy một object qua TCP mới, DNS cần hoàn thành ba trao đổi nối tiếp có thời gian đi-về lần lượt 4, 8, 12 ms; đây là tổng thời gian DNS cần cộng, không có bước DNS khác. RTT tới web server = 20 ms, truyền object = 6 ms. Tính tổng DNS + HTTP. Sau đó xét nếu DNS đã cache hợp lệ nhưng TCP vẫn phải mở mới. Đây là bài mở rộng từ mô hình.

## Câu 45–54: Email, SMTP và truy xuất thư

45. Vẽ đường đi của một thư giữa hai người có hai mail server khác nhau: UA gửi → server gửi → server nhận → UA nhận. Trong mô hình slide, chú thích giao thức ở từng chặng và nơi thư được đưa vào mailbox.

46. Phân biệt mailbox và message queue. Thư đã được server nhận chấp nhận và lưu, nhưng người nhận tắt laptop: thư nằm ở đâu? Người nhận offline có đồng nghĩa server gửi vẫn phải giữ thư trong queue không?

47. Khi server A chủ động mở kết nối SMTP tới server B, ai là SMTP client và ai là SMTP server? Nếu sau đó B gửi một thư khác tới A, vai trò có thể đổi thế nào? Có thể xác định vai trò chỉ bằng tên máy “mail server” không?

48. Vì sao SMTP dùng TCP trong mô hình bài học? “TCP tin cậy” bảo đảm điều gì ở mức truyền dữ liệu; có tự bảo đảm rằng người nhận đã mở và đọc thư hay không? Cổng 25 trọng tâm ở đây gắn với giao dịch giữa những thành phần nào?

49. POP3 và IMAP dùng để gửi thư đi hay truy xuất thư? Vì sao IMAP thường phù hợp nhiều thiết bị? Sửa hai nhận định: “IMAP không tải nội dung về thiết bị” và “POP3 luôn xóa bản trên server”.

50. Người dùng mở giao diện webmail trong browser. Giao thức giữa browser và dịch vụ web là gì? Giữa hai mail server còn cần SMTP không? Vì sao không thể nói “mọi cách đọc webmail đều là browser trực tiếp dùng IMAP”?

51. Phân biệt lệnh SMTP `MAIL FROM`, `RCPT TO` với các header email `From:`, `To:`, `Subject:` trong phần DATA. Hai nhóm nằm ở đâu trong cuộc trao đổi? Không cần phân tích chống giả mạo địa chỉ ở câu này.

52. Trong hội thoại SMTP mẫu, `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, dòng chỉ có dấu chấm và `QUIT` làm gì? Sau `DATA`, vì sao cần cơ chế đánh dấu kết thúc nội dung? Đây là phần đọc sâu hơn của slide, không cần học thuộc mọi mã trạng thái.

53. Theo so sánh cơ bản trong slide, vì sao SMTP được gọi là push còn HTTP lấy tài nguyên thường được gọi là pull? So sánh bên chủ động truyền thư với bên chủ động yêu cầu object; không biến “HTTP chủ yếu pull” thành kết luận HTTP không gửi dữ liệu lên được.

54. Server SMTP nhận xong một thư và trả mã chấp nhận theo hội thoại mẫu. Có thể suy ra người dùng cuối đã đọc thư không? Nếu browser người nhận tải một ảnh trong thư, dữ liệu ảnh có nhất thiết được truyền bằng SMTP ở lần xem đó không? Phân biệt chuyển thư với truy cập tài nguyên web được tham chiếu.

## Câu 55–64: DNS — chức năng, phân cấp, cache và bản ghi

55. DNS thuộc tầng nào và cung cấp những chức năng nào ngoài ánh xạ hostname→IP? Với `http://www.lab.example/course/a.html`, DNS xử lý hostname nào; path có thuộc tên cần tra ở đây không? DNS server hay web server gửi nội dung HTML?

56. Giải thích vì sao DNS là cơ sở dữ liệu phân tán, phân cấp. Một máy tập trung chứa mọi ánh xạ gây khó khăn gì về tải, độ trễ, chịu lỗi và quản trị? Không cần nhớ số lượng máy chủ hoặc số truy vấn theo thời điểm trong slide.

57. Phân biệt root, TLD, authoritative và local resolver. Local resolver có phải tầng thứ tư bắt buộc của cây không? Root có phải nơi chứa mọi bản ghi A của Internet không? “Local” có bắt buộc cùng LAN với host không?

58. Giả sử chưa có cache hữu dụng, không CNAME hay delegation phức tạp. Vẽ một lần host cần IP của `www.lab.example`: host hỏi resolver; resolver hỏi lần lượt root, TLD thích hợp và authoritative theo iterative. Ghi bên nào gửi từng truy vấn, bên nào trả referral và bên nào trả IP cuối.

59. Resolver đã cache hợp lệ kết quả A cần dùng. Lần hỏi tiếp theo có bắt buộc chạm root/TLD/authoritative không? Nếu chỉ cache thông tin máy chủ TLD thì có thể bỏ qua chặng nào nhưng còn phải làm gì? Phân biệt cache kết quả cuối với cache chỉ dẫn.

60. Đọc các bản ghi rút gọn sau và chỉ ra đường cần dùng để truy cập `www.lab.example`:

   ```text
   www.lab.example    CNAME   web1.lab.example
   web1.lab.example   A       192.0.2.11
   lab.example        NS      ns1.lab.example
   ns1.lab.example    A       192.0.2.12
   lab.example        MX      mail.lab.example
   mail.lab.example   A       192.0.2.13
   ```

   IP web, DNS và mail khác nhau thế nào? Có phải lần theo cả sáu bản ghi để lấy IP web không?

61. Với mỗi RR loại A, NS, CNAME và MX, giải thích ý nghĩa của name và value. Value của NS/MX là tên máy hay trực tiếp IP trong mô hình? CNAME có phải thao tác cắt ngắn một chuỗi tên không?

62. Đánh giá bảng giả định `lab.example NS 192.0.2.12`. Nó có đúng kiểu value của NS theo bài học không? Hãy biểu diễn lại bằng một NS trỏ tới tên DNS server và bản ghi A tương ứng. Tránh đặt CNAME cùng owner với các dữ liệu khác trong mẫu bảng đang luyện.

63. Resolver nhận bản ghi TTL = 90 giây tại t=10; có người hỏi lại ở t=40 và t=85. Không làm mới sớm: mỗi thời điểm còn bao nhiêu TTL? Bản cache hết hạn tại t nào? Nếu authoritative đổi IP ở t=50, việc đổi đó có làm mọi cache lập tức biết không? TTL DNS khác TTL dùng giới hạn số hop của gói IP ở ý nghĩa nào?

64. Một hostname có hai bản ghi A trỏ tới hai IP khác nhau. Đây có thể phục vụ mục đích gì? Có được kết luận hai kết quả khác nhau luôn là lỗi DNS không? Nếu DNS đã tìm ra IP nhưng browser chưa nhận được HTML, giả sử chưa có kết nối TCP tới web server, hãy nêu hai loại công việc còn phải hoàn thành trong mô hình DNS rồi TCP/HTTP.

## Câu 65–72: Nhận diện và đọc mã socket

65. Giải thích `AF_INET`, `SOCK_DGRAM`, `SOCK_STREAM` trong các mẫu đang học. Chỉ nhìn tên biến `clientSocket`/`serverSocket` có đủ biết giao thức và vai trò không? Cần đọc thêm những dấu hiệu nào?

66. Đọc mẫu rút gọn sau, coi `host` là IP server:

   ```python
   s = socket(AF_INET, SOCK_DGRAM)
   s.sendto(b'hello', (host, 12000))
   data, addr = s.recvfrom(2048)
   ```

   Đây là UDP hay TCP? Lệnh gửi chỉ rõ thông tin đích nào? `addr` của lệnh nhận biểu diễn bên nào? Có bước bắt tay TCP trong mẫu này không?

67. UDP server nhận `data, client_addr = s.recvfrom(2048)` rồi trả lời bằng `s.sendto(reply, client_addr)`. Vì sao dùng địa chỉ trả về thay vì mặc định gửi về cổng 12000 của client? Cổng dịch vụ của server có bắt buộc bằng cổng nguồn của client không?

68. Đọc mẫu:

   ```python
   s = socket(AF_INET, SOCK_STREAM)
   s.connect((host, 12000))
   s.sendall(b'hello')
   data = s.recv(1024)
   ```

   Giao thức và vai trò là gì? Lệnh nào bắt đầu thiết lập kết nối trong mẫu? Chỉ tạo `SOCK_STREAM` đã đủ thiết lập TCP chưa? Vì sao lần gửi này không truyền lại bộ `(host, port)` trong tham số gửi?

69. Đọc mẫu server:

   ```python
   listener = socket(AF_INET, SOCK_STREAM)
   listener.bind(('', 12000))
   listener.listen()
   conn, addr = listener.accept()
   data = conn.recv(1024)
   conn.sendall(data.upper())
   conn.close()
   ```

   Giải thích `bind`, `listen`, `accept`; vai trò của `listener` và `conn`. Đóng `conn` có tự đóng `listener` không? Muốn tiếp nhận client khác thì cần tiếp tục công việc nào?

70. Vì sao chỉ thấy `bind()` chưa đủ kết luận đây là TCP server? UDP server mẫu có dùng bind không? Vì sao chỉ thấy tên hàm `connect()` cũng chưa nên kết luận chung cho mọi API mà cần đọc loại socket và ngữ cảnh?

71. TCP cung cấp luồng byte. Một lần gửi ở bên gửi có bắt buộc tương ứng đúng một lần `recv` trả toàn bộ dữ liệu ở bên nhận không? Nếu muốn xử lý từng thông điệp ứng dụng, vì sao cần có cách xác định ranh giới như độ dài hoặc dấu phân cách? Đây là điểm đọc sâu hơn so với bài nhận diện mẫu.

72. So sánh ba thao tác: tạo socket, thiết lập TCP và gửi request HTTP. Chúng diễn ra theo thứ tự nào ở một TCP client mới? Một GET có phải chính là bước bắt tay TCP không? Nếu ứng dụng dùng TLS trong mô hình đang học, TLS bổ sung thuộc tính bảo mật nào mà TCP cơ bản chưa có?

## Câu 73–80: Mở rộng theo lý thuyết Chương 2

73. Trong ví dụ HTTP/1.1 có pipelining, server phải gửi các response theo thứ tự; object đầu là video lớn, ba object sau là ảnh nhỏ. Các ảnh có thể phải đợi như thế nào? HTTP/2 chia dữ liệu thành frame và truyền xen kẽ giúp cải thiện tình huống này ra sao? Đừng đồng nhất HTTP/2 với việc tạo nhiều kết nối TCP.

74. HTTP/2 vẫn dùng TCP trong mô hình slide. Nếu mất một TCP segment, TCP phải khôi phục byte bị thiếu trước khi chuyển tiếp đầy đủ luồng byte theo thứ tự. Vì sao ghép kênh ở HTTP/2 không tự xóa mọi ảnh hưởng của mất gói ở tầng TCP? Phân biệt chờ thứ tự response HTTP/1.1 với chờ byte bị thiếu của TCP.

75. Phân biệt torrent, peer và tracker trong mô hình BitTorrent ở slide. Tracker chủ yếu cung cấp loại thông tin nào? Có cần mọi byte của file đều đi qua tracker không? Một peer đã tải đủ file có thể làm gì tiếp theo?

76. Một peer thiếu các khối A, B, C; trong nhóm láng giềng, A có 5 bản sao, B có 1, C có 3. Theo rarest-first, nên ưu tiên khối nào và vì sao? Khi peer mới chưa có khối nào, trao đổi thông tin về các khối đang có giúp nó làm gì?

77. Giải thích ý tưởng tit-for-tat và việc định kỳ thử gửi cho một peer khác trong mô hình slide. Vì sao chỉ giữ cố định các đối tác hiện có có thể bỏ lỡ đối tác tốt hơn? Có cần học thuộc các con số chu kỳ mới hiểu mục đích của cơ chế không?

78. Bài cận dưới phân phối file: F = 120 Mbit, N = 4 máy nhận, upload server `u_s = 12 Mbps`, mỗi máy nhận download `d_i = 6 Mbps`, mỗi peer có upload `u_i = 2 Mbps`; bỏ giới hạn trong lõi mạng. Với client–server, xét các ràng buộc server phải gửi tổng `NF` và máy nhận chậm nhất cần tải `F`. Với P2P, xét server cần đưa ra ít nhất một bản `F`, máy chậm nhất cần tải `F`, và tổng upload tối đa `u_s + Σu_i` phải đáp ứng `NF`. Hãy viết và tính các cận dưới tương ứng bằng cách lấy max của các thời gian ràng buộc. Các cận này có tự chứng minh một triển khai thực tế chắc chắn hoàn tất đúng từng ấy giây không?

79. Trong thông điệp DNS theo slide, identification giúp ghép query với reply thế nào? Các cờ “query/reply”, “recursion desired”, “recursion available”, “authoritative answer” mô tả những khía cạnh gì? Phân biệt phần question, answer, authority và additional; một câu trả lời có referral có thể kèm thông tin IP bổ sung hữu ích ra sao?

80. Phân biệt hai vấn đề DNS trong slide: làm máy chủ bận/không phục vụ được do DDoS và đưa ánh xạ sai vào cache do giả mạo phản hồi/cache poisoning. Cache và kiến trúc phân tán hỗ trợ tính sẵn sàng như thế nào? Xác thực nguồn gốc và tính toàn vẹn của dữ liệu DNS giải quyết mối lo nào; có đồng nghĩa với mã hóa nội dung HTTP không?

## Trang lý thuyết để tra sau khi tự trả lời

- Nguyên lý ứng dụng, socket, yêu cầu dịch vụ, TCP/UDP/TLS: trang PDF 3–15.
- HTTP, kết nối, thông điệp, cookie/cache: trang PDF 17–47, 51.
- HTTP/2: trang PDF 48–50.
- Email: trang PDF 53–60.
- DNS: trang PDF 62–78.
- P2P/BitTorrent/phân phối file: trang PDF 80–88.
- Socket UDP/TCP: trang PDF 90–99.

Câu 38, 41–44, 71 và 73–80 có suy luận/bài số mở rộng từ mô hình. Giả thiết được ghi trong câu; phần chưa học sẽ được giải thích khi chữa. Không dùng số lượng câu mở rộng để thay đổi mức ưu tiên của kế hoạch ôn thi đã thống nhất.
