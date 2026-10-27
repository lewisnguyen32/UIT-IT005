# Nháp nội bộ — 20 câu HTTP, cookie, cache, RTT

Nguồn: T2.txt trích xuất từ lý thuyết Ch2 và ch2_analysis_strict.md. Đây là câu tự kiểm do trợ giảng soạn, không phải câu đề thi được bổ sung vào corpus. Đáp án bên dưới chỉ dành cho trợ giảng.

## 1. Trang web và URL

Một HTML cơ sở tham chiếu 2 ảnh và 1 tập tin âm thanh riêng, chưa có object nào trong cache. Có bao nhiêu object cần lấy? Với `http://study.example/img/logo.png`, chỉ ra hostname và đường dẫn. DNS cần phân giải phần nào?

Đáp án: 4 object; hostname study.example, path /img/logo.png; DNS phân giải hostname, không phân giải cả URL/path. Nguồn: T2 tr.17–19,62.

## 2. Đọc request

```http
POST /search?lang=vi HTTP/1.1
Host: study.example
User-Agent: StudyBrowser/9.0
Content-Length: 5

q=net
```

Xác định method, đường dẫn, query, phiên bản HTTP, host, phần mềm client và body. `9.0` có phải phiên bản HTTP không? Dòng trống dùng để làm gì?

Đáp án: POST; /search; lang=vi; HTTP/1.1; study.example; StudyBrowser/9.0; q=net. 9.0 là phiên bản phần mềm trong ví dụ. Dòng trống phân tách header và body. Nguồn: T2 tr.25–27.

## 3. Đọc response và Content-Length

```http
HTTP/1.1 200 OK
Server: StudyServer/2.0
Content-Type: text/plain
Content-Length: 5

Hello
```

Chỉ ra status line, header và body. `Content-Length: 5` đếm những byte nào? Nếu toàn bộ phần trước body dài 120 byte thì toàn response dài bao nhiêu byte? Giả sử body chỉ có đúng 5 byte ASCII `Hello`, không thêm ký tự xuống dòng.

Đáp án: status line HTTP/1.1 200 OK; 3 header; body Hello. Content-Length đếm body 5 byte; tổng 125 byte. Nguồn: T2 tr.26,28; strict mục 4.

## 4. Date và Last-Modified

Response có `Date: Tue, 27 Oct 2026 03:00:00 GMT` và `Last-Modified: Mon, 26 Oct 2026 01:00:00 GMT`. Dòng nào cho biết thời điểm tài nguyên được chỉnh sửa? Khi xác thực lại cache bằng cơ chế đã học, client lấy mốc nào để đặt trong header nào?

Đáp án: Last-Modified; dùng mốc Last-Modified của bản cũ trong If-Modified-Since của request. Date là ngày giờ tạo message theo cách trình bày bài học, không thay cho Last-Modified. Nguồn: T2 tr.28,47; strict mục 4.

## 5. Chọn method theo tình huống

Chọn method phù hợp và giải thích: (a) lấy ảnh; (b) hỏi thông tin như GET nhưng không nhận body; (c) gửi form để server xử lý; (d) tạo hoặc thay thế toàn bộ biểu diễn tại URL đích bằng nội dung gửi lên. PUT có tự xóa tài nguyên ở một URL nguồn khác không?

Đáp án: GET, HEAD, POST, PUT; PUT không tự thực hiện thao tác di chuyển/xóa URL nguồn. Nguồn: T2 tr.27; strict mục 3 và ghi chú sửa chữ POST in nhầm trong mô tả PUT.

## 6. GET có gửi dữ liệu được không?

Trong `GET /search?q=network&page=2 HTTP/1.1`, server nhận được các tham số nào và chúng nằm ở đâu? Sửa phát biểu: “GET không thể gửi dữ liệu; POST chỉ dùng để tạo tài nguyên mới.”

Đáp án: q=network, page=2 ở query của request target. GET có thể mang dữ liệu query trong URL; POST yêu cầu xử lý dữ liệu theo ngữ nghĩa tài nguyên đích, không giới hạn vào tạo mới. Nguồn: T2 tr.27 và cách chuẩn hóa đã lưu trong memory.

## 7. Phân biệt các mã trạng thái

Ghép 200,301,304,400,404,505 với: GET thành công và trả bản mới; tài nguyên chuyển URL vĩnh viễn; bản cache vẫn cập nhật sau conditional GET; request lỗi; tài nguyên không tìm thấy; phiên bản HTTP không được hỗ trợ. 301 đi kèm header nào để chỉ URL mới? 404 có đồng nghĩa response không được có body báo lỗi không?

Đáp án: theo thứ tự 200,301,304,400,404,505; Location; không, 404 có thể mang body trang báo lỗi. Nguồn: T2 tr.29,47; strict mục 4.

## 8. Theo chuyển hướng

Browser gửi `GET /old.html` tới study.example và nhận `301 Moved Permanently`, `Location: /new.html`. Trong ví dụ này browser muốn đi theo chuyển hướng thì gửi request gì tới host nào? 301 có phải yêu cầu browser di chuyển file trên ổ đĩa server không?

Đáp án: GET /new.html tới study.example; không, đây là thông báo URL mới của tài nguyên, không phải lệnh di chuyển file. Chỉ xét request GET trong đề, không khái quát cách đổi method của mọi redirect. Nguồn: T2 tr.29; memory phần đã giải thích chuyển hướng.

## 9. Conditional GET: đã đổi

Client đã cache ảnh với Last-Modified cũ, nay gửi GET có If-Modified-Since. Ảnh vẫn tồn tại và đã đổi sau mốc này. Server trả mã gì, có gửi body ảnh mới không, browser cập nhật cache ra sao? Header If-Modified-Since thuộc request hay response?

Đáp án: 200 OK + body mới; browser dùng và có thể cập nhật bản cache theo chỉ dẫn cache; If-Modified-Since thuộc request. Nguồn: T2 tr.47.

## 10. Conditional GET: chưa đổi

Vẫn tình huống câu 9 nhưng ảnh chưa đổi. Server trả mã gì? Browser lấy nội dung ảnh từ đâu? Có còn request/response qua mạng không? Phân biệt trường hợp này với 301.

Đáp án: 304 Not Modified, không body ảnh mới, dùng ảnh trong cache; vẫn có request và status/header response qua mạng. 301 báo chuyển URL, 304 báo bản cache chưa thay đổi theo điều kiện kiểm tra. Nguồn: T2 tr.29,47; strict mục 4.

## 11. Xếp header đúng hướng

Xếp các header sau vào request hoặc response trong mô hình đã học và nêu chức năng: Host, User-Agent, Server, Set-Cookie, Cookie, Last-Modified, If-Modified-Since, Location. Vì sao không thể trả lời “server trả If-Modified-Since” thay cho mã trạng thái?

Đáp án: request: Host,User-Agent,Cookie,If-Modified-Since; response: Server,Set-Cookie,Last-Modified,Location. Header và status code là các thành phần khác nhau; If-Modified-Since là điều kiện client gửi. Nguồn: T2 tr.25,28–29,32–33,47.

## 12. HTTP stateless và phiên đăng nhập

HTTP stateless nhưng website vẫn nhớ giỏ hàng của người dùng qua nhiều request. Giải thích bằng ví dụ cookie chứa session_id. Trình duyệt giữ gì, server giữ gì? Nêu bốn thành phần cookie theo slide. Cookie có nhất thiết chỉ được tạo sau đăng nhập không?

Đáp án: browser giữ cookie/session ID, server giữ ánh xạ ID với dữ liệu phiên/giỏ hàng trong mô hình này; Set-Cookie response, Cookie request tiếp theo, kho cookie browser, database website. Không bắt buộc sau đăng nhập. Nguồn: T2 tr.19,31–34.

## 13. Cookie khác cache, proxy có hai vai

Một browser lưu `session_id=abc` và một bản ảnh logo.png. Mỗi thứ phục vụ mục đích gì? Proxy cache nhận request từ browser rồi lấy ảnh từ origin khi chưa có bản dùng được: proxy đóng vai gì trong mỗi cuộc trao đổi?

Đáp án: cookie liên kết request với trạng thái/phiên; cache lưu bản sao object tái sử dụng. Proxy là server đối với browser, client đối với origin. Nguồn: T2 tr.32–34,41–42.

## 14. Cache hit, miss và xác thực lại

Giả sử chính sách cho phép cache: (a) có bản được phép dùng ngay; (b) chưa có bản; (c) có bản nhưng cần xác thực lại. Hãy mô tả cache/browser phải làm gì trong từng trường hợp. Vì sao “có object trong cache thì không bao giờ hỏi origin” là sai?

Đáp án: (a) trả bản cache; (b) lấy origin, lưu nếu được phép rồi trả; (c) conditional GET, xử lý 200/304. Có bản chưa chắc còn được dùng ngay. Nguồn: T2 tr.41–42,47; strict mục 3–4.

## 15. Bài số cache cơ bản — mở rộng B/C

Giả sử 100 request/s, mỗi object 10.000 byte, các object có cùng kích thước. Cache hit rate 60%, cache hit phục vụ hoàn toàn nội bộ, bỏ traffic request/header và xác thực lại. Tính lưu lượng body đi qua access link trước/sau có cache. Nếu hit mất 5 ms và miss mất tổng 105 ms, trễ trung bình là bao nhiêu? Cache có làm dung lượng vật lý của link tăng không?

Đáp án: trước 8 Mbps; sau 3,2 Mbps; trung bình 0,6×5+0,4×105=45 ms; không tăng dung lượng vật lý, giảm traffic/tải. Nguồn: T2 tr.42–46; strict ghi nhận đây là mở rộng sau nền A.

## 16. Số object khác số kết nối

Một HTML tham chiếu 4 ảnh riêng, tất cả cùng server, không cache. Trong mô hình nonpersistent cần bao nhiêu kết nối TCP? Persistent có thể dùng bao nhiêu kết nối? Nếu cùng một TCP thì có chắc mọi GET được gửi pipelining không?

Đáp án: 5 object, nonpersistent 5 TCP; persistent có thể dùng 1 TCP; không, còn có thể gửi tuần tự chờ response. Nguồn: T2 tr.20–24; strict mục 4–5.

## 17. TCP mới và TCP tái sử dụng

Một object có thời gian truyền 12 ms, RTT=30 ms. Tính tổng từ lúc bắt đầu lấy object khi (a) cần mở TCP mới; (b) TCP đã mở và được tái sử dụng. Chỉ rõ từng RTT dùng làm gì. Giả sử HTTP/1.x qua TCP, bỏ DNS/TLS, xử lý/hàng đợi và kích thước request/header.

Đáp án: mới 2×30+12=72 ms, cũ 30+12=42 ms. Mới thêm 1 RTT setup; cả hai có 1 RTT request đến/first byte phản hồi về. Nguồn: T2 tr.23–24; strict mục 5.

## 18. Đổi byte sang bit trước khi tính

RTT=40 ms, object 75.000 byte, tốc độ hiệu dụng cố định 10 Mbps. Tính L/R bằng ms, rồi tính tổng lấy một object trên TCP mới và TCP tái sử dụng. Dùng cùng giả thiết câu 17.

Đáp án: 600.000 bit/10.000.000 bit/s=0,06 s=60 ms; mới 140 ms; cũ 100 ms. Nguồn: T2 tr.23–24; strict mục 5.

## 19. Nhiều object tuần tự — mở rộng B

HTML và 3 ảnh cùng server; RTT=20 ms; truyền mỗi object mất 5 ms. HTML phải lấy xong trước khi biết URL ảnh. Mỗi request sau chỉ gửi khi response trước đã nhận xong. Bắt đầu chưa có TCP, không cache. So sánh tổng thời gian nonpersistent tuần tự với persistent không pipelining trên một TCP. Bỏ DNS/TLS, xử lý/hàng đợi, request/header; tốc độ truyền hiệu dụng giữ cố định.

Đáp án: nonpersistent 4×(2×20+5)=180 ms; persistent 1×20 setup+4×20 request/first-byte+4×5 body=120 ms. Nguồn: suy ra từ T2 tr.20–24; strict mục 5. Đây là bài mở rộng, không khẳng định đã có dạng số này trong 5 đề giữ lại.

## 20. Pipelining và TCP song song — mở rộng B

HTML tham chiếu 6 ảnh cùng server; RTT=25 ms; bỏ toàn bộ thời gian truyền body và request/header, DNS/TLS, xử lý/hàng đợi. Bắt đầu chưa có kết nối, chỉ biết URL ảnh sau khi nhận HTML, không cache. So sánh: (a) persistent có pipelining, gửi cả 6 GET ngay sau HTML; (b) nonpersistent, sau HTML mở tối đa 3 TCP song song theo từng đợt. Có được dùng công thức “persistent chỉ 1 RTT cho tất cả” cho persistent không pipelining không?

Đáp án: (a) 3 RTT=75 ms (setup,HTML,loạt ảnh); (b) 2 RTT HTML+2 đợt×2 RTT=6 RTT=150 ms; không áp sang persistent không pipelining, từng GET tuần tự còn 1 RTT. Nguồn: suy ra T2 tr.20–24,48; strict mục 4–5. Kết quả song song chỉ theo giả thiết đã bỏ body, không tự coi nhiều body truyền đồng thời với đầy đủ băng thông trên một link.
