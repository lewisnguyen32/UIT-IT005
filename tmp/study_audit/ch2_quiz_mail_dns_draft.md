# Nháp 18 câu tự kiểm Ch2 — Mail và DNS

Các câu dưới đây do trợ giảng soạn từ T2, dùng tự kiểm, không phải câu đề thi. Đáp án là tài liệu nội bộ: tách khỏi bản hỏi người học. Trang nguồn là trang PDF trong T2. Bảng DNS rút gọn bỏ priority/TTL khi không phục vụ câu hỏi. Các địa chỉ IP chỉ dùng minh họa.

## Mail — 8 câu

### M1. Ba thành phần

**Hỏi:** Nêu ba thành phần chính của hệ thống email theo bài học. Phần mềm người dùng dùng để soạn và đọc thư thuộc thành phần nào?

**Đáp án nội bộ:** User agent (UA), mail server, SMTP. Phần mềm soạn/đọc là UA. Không gọi nội dung bức thư là server.

**Nguồn:** T2 tr.53.

### M2. Đường đi của thư

**Hỏi:** An dùng ứng dụng email gửi thư cho Bình; hai người dùng hai mail server khác nhau. Điền giao thức cho từng đoạn: `UA của An → server An → server Bình → UA của Bình`. Đoạn cuối có những lựa chọn nào trong bài học?

**Đáp án nội bộ:** Theo mô hình UA truyền thống của slide: SMTP; SMTP; POP3 hoặc IMAP. HTTP/HTTPS nếu đọc qua giao diện web. Giao thức truy xuất thư khác giao thức chuyển thư.

**Nguồn:** T2 tr.56,60.

### M3. Queue hay mailbox?

**Hỏi:** a) Server An đang giữ thư chờ chuyển ra ngoài: đó là message queue hay mailbox? b) Server Bình đã nhận và lưu thư, nhưng điện thoại Bình đang tắt: thư nằm ở đâu? Có bắt buộc còn nằm ở queue của server An không?

**Đáp án nội bộ:** a) Message queue. b) Mailbox của Bình trên server Bình. Không bắt buộc còn ở queue server An; máy người nhận tắt không ngăn server nhận đã hoạt động lưu thư.

**Nguồn:** T2 tr.53–56.

### M4. Ai là SMTP client?

**Hỏi:** Khi server An chủ động chuyển thư cho server Bình, bên nào là SMTP client, bên nào là SMTP server? Một máy mail server có thể đóng vai client trong giao dịch này và server trong giao dịch khác không?

**Đáp án nội bộ:** Server An là SMTP client; server Bình là SMTP server. Có, vai trò phụ thuộc bên khởi tạo/gửi và bên nhận trong giao dịch; từ client không luôn chỉ PC người dùng.

**Nguồn:** T2 tr.54–56.

### M5. Dịch vụ vận chuyển và kiểu trao đổi

**Hỏi:** a) Trong mô hình chuyển thư giữa hai mail server, SMTP dùng TCP hay UDP, cổng server trọng tâm là bao nhiêu? b) SMTP được xem là push hay pull? c) Tính truyền tin cậy ở tầng vận chuyển do giao thức nào cung cấp? Có thể vì dùng TCP mà kết luận nội dung thư đã được mã hóa không?

**Đáp án nội bộ:** TCP, cổng 25 trong mô hình server-to-server; push; TCP cung cấp truyền tin cậy. Không, TCP không tự mã hóa. Không khái quát mọi ứng dụng gửi thư đều dùng cổng 25.

**Nguồn:** T2 tr.15,55,58.

### M6. POP3 và IMAP

**Hỏi:** Bạn muốn thư mục và trạng thái đọc thư thống nhất khi dùng cả điện thoại lẫn máy tính: chọn POP3 hay IMAP, vì sao? Đánh giá hai nhận xét: a) “IMAP không tải nội dung thư về thiết bị khi đọc”; b) “POP3 luôn buộc xóa bản thư trên server”.

**Đáp án nội bộ:** IMAP, vì quản lý thư/thư mục/trạng thái trên server và thuận tiện truy cập nhiều thiết bị. Cả a và b đều sai: IMAP vẫn tải nội dung để đọc; POP3 có thể giữ bản trên server. Không dùng việc tải hay không tải nội dung làm khác biệt tuyệt đối.

**Nguồn:** T2 tr.60; phần làm rõ đã thống nhất trong memory.md.

### M7. Webmail

**Hỏi:** Bình mở webmail bằng trình duyệt. a) Trình duyệt trao đổi với giao diện web bằng nhóm giao thức nào? b) Hai mail server vẫn có thể chuyển thư bằng SMTP không? c) Dùng webmail có đồng nghĩa toàn bộ đường đi thư đều dùng HTTP không?

**Đáp án nội bộ:** a) HTTP/HTTPS. b) Có. c) Không; phân biệt browser↔dịch vụ web với chuyển thư server↔server.

**Nguồn:** T2 tr.60.

### M8. Lệnh SMTP và header email

**Hỏi:** Trong giao dịch SMTP xuất hiện `MAIL FROM`, `RCPT TO`, rồi phần `DATA` chứa các dòng `From:`, `To:`, `Subject:`. a) Hai nhóm này có phải cùng một thứ không? b) Nhóm nào là lệnh SMTP, nhóm nào thuộc nội dung thông điệp email? c) Header và body của email được ngăn cách bởi gì?

**Đáp án nội bộ:** a) Không. b) MAIL FROM/RCPT TO là lệnh SMTP; From/To/Subject là header thông điệp, nằm trong dữ liệu truyền sau DATA. c) Một dòng trống. Chỉ cần phân biệt, không yêu cầu học toàn bộ mã phản hồi SMTP.

**Nguồn:** T2 tr.57,59. Câu chi tiết sau nền A.

## DNS — 10 câu

### D1. Chức năng và tầng

**Hỏi:** a) DNS thuộc tầng nào? b) Nêu chức năng ánh xạ thường dùng khi trình duyệt biết tên website mà chưa biết IP. c) Ngoài ánh xạ tên→IP, kể hai dịch vụ DNS khác trong slide. d) Một tên có thể liên quan nhiều IP không, và ứng dụng là gì?

**Đáp án nội bộ:** a) Tầng ứng dụng. b) Phân giải tên máy thành địa chỉ IP. c) Bí danh máy, bí danh mail server, cân bằng tải. d) Có, ví dụ nhiều bản sao web server/cân bằng tải. Không đồng nhất DNS với giao thức tải trang web.

**Nguồn:** T2 tr.62–63.

### D2. Tại sao DNS phân tán?

**Hỏi:** Nếu cả Internet chỉ dùng một máy DNS duy nhất, hệ thống có thể gặp những vấn đề nào về lỗi, tải, khoảng cách và bảo trì? Cấu trúc DNS trong bài học giải quyết bằng cách tổ chức thế nào?

**Đáp án nội bộ:** Điểm lỗi đơn, tải quá lớn, cơ sở dữ liệu xa nơi hỏi, bảo trì khó/khó mở rộng; dùng cơ sở dữ liệu phân tán, phân cấp nhiều máy chủ. Không yêu cầu nhớ số liệu truy vấn theo ngày trong slide.

**Nguồn:** T2 tr.62–65.

### D3. Vai trò bốn bên

**Hỏi:** Ghép local resolver, root, TLD `.com`, authoritative DNS của `school.com` với vai trò tương ứng. Khi máy người dùng cần IP `www.school.com`, theo mô hình đã học nó thường gửi yêu cầu cho bên nào trước? Root có phải nơi giữ sẵn bản ghi A của mọi website không?

**Đáp án nội bộ:** Host hỏi local resolver trước; root chỉ dẫn tới DNS TLD; `.com` chỉ dẫn tới authoritative của miền; authoritative quản lý và trả thông tin có thẩm quyền cho miền. Root không giữ mọi A của website. Local resolver không đơn giản là một tầng root/TLD/authoritative trong cây.

**Nguồn:** T2 tr.65,68–70.

### D4. Vẽ iterative

**Hỏi:** Giả sử local resolver chưa có thông tin cache cần thiết. Nó hỏi root; root đáp “hỏi `.com`”. a) Ai gửi câu hỏi tiếp tới `.com`? b) `.com` trả tên authoritative của `school.com`: ai hỏi authoritative tiếp? c) Vẽ chuỗi hỏi/trả từ host đến khi có IP `www.school.com`. Đây là kiểu tra cứu nào giữa resolver và các DNS được hỏi?

**Đáp án nội bộ:** Local resolver hỏi tiếp cả hai lần. Host→local; local→root→local (referral); local→TLD→local (referral); local→authoritative→local (kết quả); local→host. Giữa resolver và các DNS là iterative. Root trả referral không tự chuyển tiếp câu hỏi trong tình huống này.

**Nguồn:** T2 tr.69–71.

### D5. Recursive và quá trình hỗn hợp

**Hỏi:** Tình huống A: host yêu cầu local resolver phân giải thay, local tìm kết quả rồi trả IP cho host. Tình huống B: local hỏi root, nhận referral và tự hỏi `.com`, rồi authoritative. a) Quan hệ A là recursive hay iterative? b) Các bước ở B là kiểu nào? c) Hai kiểu có thể cùng xuất hiện trong một quá trình phân giải không? Giải thích qua bên có trách nhiệm hỏi tiếp.

**Đáp án nội bộ:** A recursive; B iterative; có thể cùng xuất hiện. Recursive: bên được hỏi nhận trách nhiệm phân giải thay; iterative: bên được hỏi trả kết quả hoặc referral để bên đang truy vấn tiếp tục hỏi. Không phân loại chỉ dựa từ “local DNS hỏi tiếp” mà bỏ ngữ cảnh.

**Nguồn:** T2 tr.69–72; giải thích strict mục DNS.

### D6. Cache có thể bỏ qua những bước nào?

**Hỏi:** a) Local resolver đã có bản ghi A còn hiệu lực cho tên cần tìm: có bắt buộc hỏi root/TLD/authoritative không? b) Chưa có A cần tìm nhưng đã có thông tin hợp lệ để liên hệ authoritative của miền: có bắt buộc bắt đầu lại từ root không? c) Cache DNS có phải lưu bản HTML/ảnh để trình duyệt dùng lại không?

**Đáp án nội bộ:** a) Không, có thể trả từ cache. b) Không, dùng thông tin đã cache để tiếp tục ở nơi phù hợp. c) Không; DNS cache lưu thông tin DNS như RR/ánh xạ, web cache lưu nội dung HTTP.

**Nguồn:** T2 tr.69,73; phân biệt web cache tr.41–42.

### D7. Ý nghĩa A, NS, CNAME, MX

**Hỏi:** Với bốn loại RR A, NS, CNAME, MX: a) mô tả chiều ánh xạ name→value; b) loại nào cho IPv4 trực tiếp trong mô hình đang học? c) Value của NS và MX là tên máy hay địa chỉ IP? d) CNAME có nghĩa “cắt ngắn chuỗi tên” không?

**Đáp án nội bộ:** A hostname→IPv4; NS miền→tên authoritative server; CNAME bí danh→tên chính tắc; MX miền nhận thư→tên mail exchanger. A cho IPv4 trực tiếp; NS/MX value là tên; CNAME không phải thao tác rút gọn chuỗi.

**Nguồn:** T2 tr.74.

### D8. Phân biệt IP web, mail, DNS

**Hỏi:** Cho bảng RR giả định rút gọn:

```text
www.class.example   CNAME  web1.class.example
web1.class.example  A      192.0.2.20
class.example       MX     mail.class.example
mail.class.example  A      192.0.2.70
class.example       NS     ns.class.example
ns.class.example    A      192.0.2.80
```

a) Trình duyệt cần kết nối web server của `www.class.example`: chọn IP nào, lần theo những RR nào? b) Mail server bên gửi chuyển thư tới `lan@class.example`: chọn IP nào, qua RR nào? c) Muốn liên hệ authoritative DNS được bảng chỉ ra: cần tên và IP nào? d) Có cần lần theo cả sáu dòng cho từng tác vụ không?

**Đáp án nội bộ:** a) `.20`, CNAME→A. b) `.70`, MX→A. c) `ns.class.example`, `.80`, NS→A. d) Không, dùng chuỗi phù hợp tác vụ. Không nhầm câu b với UA gửi thư tới server đã cấu hình.

**Nguồn:** T2 tr.54–56,74,77.

### D9. TTL và thay đổi IP

**Hỏi:** Lúc t=0, resolver cache `web.class.example A 192.0.2.10`, TTL=300 giây. Tại t=100, authoritative đổi bản ghi sang `.99`. Giả sử không có cơ chế cập nhật/xóa cache sớm. a) Tại t=200, cache cũ còn hiệu lực bao lâu và resolver có thể vẫn trả IP nào? b) Tại t=301 có được tiếp tục coi cache cũ còn hiệu lực không; cần làm gì trước khi trả kết quả mới hợp lệ? c) TTL DNS có phải số router tối đa gói IP được đi qua không?

**Đáp án nội bộ:** a) 100 giây, có thể vẫn trả `.10`. b) Cache đã hết hạn, phải phân giải/lấy thông tin hợp lệ lại nếu cần trả lời, không tự biết `.99` chỉ do bộ đếm hết. c) Không; đây là thời hạn cache DNS, khác TTL IP. Không kết luận mọi cache trên Internet đồng thời cập nhật ngay t=100.

**Nguồn:** T2 tr.73–74; số liệu tự soạn để kiểm ý nghĩa TTL.

### D10. Đọc cấu trúc thông điệp DNS — thêm sau nền A

**Hỏi:** Trong thông điệp DNS, a) trường identification giúp ghép truy vấn với trả lời thế nào? b) Trường mang cờ query/reply có vai trò gì? c) Ghép questions, answers, authority, additional với bốn nội dung: tên/loại cần hỏi; RR trả lời; RR về máy chủ có thẩm quyền; thông tin bổ sung hữu ích. Query và reply có dùng cùng cấu trúc tổng quát không?

**Đáp án nội bộ:** a) Reply dùng identification tương ứng query (16 bit trong slide). b) Phân biệt thông điệp hỏi/trả lời. c) Ghép đúng như thứ tự liệt kê. Có, query/reply cùng cấu trúc tổng quát. Không suy ra ID đơn lẻ bảo đảm xác thực/bảo mật.

**Nguồn:** T2 tr.75–76. Câu chi tiết sau nền A, không tự nâng lên trọng tâm đề thi.
