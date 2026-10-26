# Nhận xét bản ôn tập Chương 1

Đánh giá ngày 23/10/2026. Đã đọc đủ 7 trang và kiểm hình của bản người dùng gửi; đối chiếu lý thuyết Chương 1 và phạm vi đề đã chốt. Số trang dưới đây là trang PDF tính từ 1.

**Kết luận: dùng được làm khung tóm tắt, chưa đủ làm tài liệu duy nhất để ôn thi**, nhất là với người mới học chưa nắm chắc. Hai phần cần bổ sung trước là hiệu suất và đóng/mở gói. Không cần viết lại toàn bộ phần mạng truy cập.

## 1. Độ phủ năm phần

| Phần | Đánh giá | Nhận xét cụ thể |
|---|---|---|
| Internet và giao thức | Khá đủ phần nền | Trang1-2 có góc nhìn thành phần/dịch vụ và định nghĩa giao thức. Sửa IETF viết nhầm IEFT. |
| Mạng biên | Khá đủ phần mô tả | Trang2-4 có host, mạng truy cập, môi trường truyền và L/R. Các con số tốc độ là ví dụ theo tài liệu, không phải thông số chung bắt buộc cho mọi mạng. |
| Mạng lõi | Có kiến thức cơ bản | Trang5-6 có forwarding/routing, store-and-forward, queue/loss, circuit switching, FDM/TDM. Nên thêm bảng so sánh packet/circuit và một timeline gói qua hai link. |
| Hiệu suất | Thiếu trọng tâm và có lỗi công thức | Trang6 thiếu processing delay, tổng nodal delay và toàn bộ throughput/bottleneck. Công thức d_queue=La/R sai ý nghĩa đại lượng. |
| Chồng giao thức | Mới ở mức liệt kê | Trang7 có năm tầng, chức năng/giao thức/PDU nhưng chưa có quy trình đóng/mở gói, quan hệ dịch vụ giữa tầng và sơ đồ host-switch-router-host. |

## 2. Phải sửa trước khi học thuộc

### Trang6: La/R là cường độ lưu lượng

Bản ghi `d_queue=La/R`. Cách viết đúng cho đại lượng này là:

`rho = La/R` — cường độ lưu lượng.

Nếu L là bit/gói, a là gói/s và R là bit/s thì La/R không có đơn vị. Nó không thể là một thời gian chờ tính bằng giây. Cần ghi xu hướng: tải thấp thường ít chờ; khi tải tiến gần khả năng phục vụ, trễ hàng đợi trung bình có thể tăng mạnh. Muốn tính chính xác trễ hàng đợi cần thêm mô hình/giả thiết; không tự thay bằng một công thức hàng đợi ngoài phạm vi môn.

Đối chiếu lý thuyết trang50. Với bộ đệm hữu hạn, quá tải còn gây mất gói khi bộ đệm đầy.

### Trang6: thiếu loại trễ thứ tư

Tiêu đề ghi bốn nguyên nhân nhưng chỉ liệt kê transmission, propagation và queueing. Cần thêm **processing delay**: xử lý tại nút, chẳng hạn kiểm tra lỗi và xác định liên kết đầu ra, cùng công thức:

`d_nodal = d_proc + d_queue + d_trans + d_prop`.

Đối chiếu lý thuyết trang48. Trong d_prop=d/s, tốc độ s dùng theo dữ kiện/giả thiết của bài; khoảng2x10^8m/s là giá trị minh họa, không phải hằng số áp mọi môi trường.

### Chỗ dùng thuật ngữ cần sửa

- Trang1: `IEFT` thành `IETF`, tên là Internet Engineering Task Force.
- Trang7: PDU tầng mạng nên ghi `packet/datagram`, thay từ `package`. Giữ rõ chuỗi message -> segment -> datagram/packet -> frame -> bit theo mô hình slide.
- Trang5: diễn đạt routing nên là thuật toán xác định đường từ nguồn tới đích; gói được chuyển tiếp theo kết quả/bảng tương ứng. Tránh hiểu câu “được thực hiện bởi các gói tin” thành gói tin tự chạy thuật toán chọn đường.
- Trang4: `Vệ sinh (satellite)` là lỗi chữ, cần sửa thành `Vệ tinh`.

## 3. Bổ sung tối thiểu để dùng ôn thi

### A. Thông lượng và nút thắt

Hiện chỉ có chữ “thông lượng” ở tiêu đề, chưa có phần giải thích. Thêm:

- Throughput là tốc độ dữ liệu truyền từ nguồn tới đích, đơn vị bit/s.
- Một luồng qua các link nối tiếp, không có lưu lượng cạnh tranh trong mô hình đơn giản: `T=min(R1,R2,...,Rn)`.
- Khi n luồng chia sẻ công bằng một link R, mô hình slide cho mỗi luồng `T=min(R_s,R_c,R/n)`; phải nêu điều kiện chia sẻ công bằng.
- Phân biệt thông lượng với tốc độ danh định của một link và với thời gian trễ.

Đọc lý thuyết trang54-56. Đề2019-2020 câu10, trang3 hỏi đúng dạng nút thắt; đọc riêng bản7trang hiện tại chưa có phần kiến thức này.

### B. Cách làm bài độ trễ

Có công thức thành phần chưa thay cho việc biết ghép thành bài. Thêm checklist:

1. Đổi byte -> bit, Mbps -> bit/s, km -> m, giây -> ms khi cần.
2. Một gói store-and-forward qua nhiều link, bỏ processing và queueing: `d_e2e=Σ(L/R_i)+Σ(d_i/s_i)`.
3. Nói rõ đang tính từ bit đầu tiên bắt đầu được phát tới bit cuối cùng đến đích; không nhầm với chỉ tính lúc bit đầu tiên tới.
4. Số gói tối đa phát trong t giây: `floor(Rt/L)` trong mô hình bỏ overhead, chỉ xét phát trên một link.
5. RTT là thời gian đi-về, cần phân biệt với propagation một chiều.

Luyện các dạng từ đề đã chọn: đề2019-2020 C2/C3/C12; đề2020-2021 C14/C20. C12 và C14 cần sơ đồ/timeline nhiều link, không chỉ thế L/R một lần. Không cần thêm bài từ ngân hàng/đề tự làm.

### C. Đóng gói và thiết bị xử lý đến tầng nào

Thêm một hình gồm host gửi -> switch -> router -> host nhận, cùng các bước:

- Tại host gửi: message -> segment -> datagram -> frame -> bit; các tầng tương ứng bổ sung thông tin điều khiển để triển khai dịch vụ.
- Tại bên nhận: giải đóng gói theo chiều ngược lại.
- Trong mô hình chuyển tiếp cơ bản: host có đủ5tầng; switch lớp2 xử lý tới tầng liên kết; router xử lý tới tầng mạng.
- Tầng trên sử dụng dịch vụ tầng dưới. Physical truyền bit; không học “mọi tầng đều thêm header” như quy tắc tuyệt đối.

Đọc lý thuyết trang62-67, đặc biệt hình trang67. Đề2020-2021 C4-5 trang2 hỏi đọc vị trí tầng/PDU trực tiếp trên sơ đồ; chỉ thuộc danh sách năm tầng chưa thay cho việc đọc được hình.

### D. Bảng so sánh ngắn và bài tự kiểm

Thêm bảng packet/circuit theo các tiêu chí: tài nguyên dành riêng/chia sẻ, cần thiết lập kênh, tài nguyên khi không gửi, khả năng queue/loss. Sau khi bổ sung, cần tự làm được một câu PDU/sơ đồ, một bài độ trễ nhiều link và một bài bottleneck bằng cách giải thích cơ chế.

## 4. Cách dùng phù hợp với tuần ôn

Giữ bản7trang làm khung đọc nhanh. Ưu tiên sửa La/R, bổ sung trễ xử lý/tổng trễ, throughput và đóng/mở gói; sau đó luyện các dạng trên. Với quỹ2-3giờ/ngày, chưa cần dành nhiều thời gian thuộc mọi con số WiFi/DSL/cáp trong trang2-4. Các ví dụ này giúp nhận diện công nghệ nhưng không bù được phần bài tính và sơ đồ còn thiếu.

## Nguồn đối chiếu

- [Bản7trang được nhận xét](<C:/Users/phuoc/Downloads/Chương 1 - Ôn tập.pdf>)
- [Lý thuyết Chương1](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf>)
- [Đề2019-2020](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/[BHT CNPM] NMMMT 2019-2020 GK1.pdf>)
- [Đề2020-2021](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Giữa Kỳ/[BHT CNPM] NMMMT 2020-2021 GK1.pdf>)
- [Kế hoạch ôn7ngày đã chốt](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/output/KE_HOACH_ON_NMMMT_7_NGAY.md>)

Đây là nhận xét và checklist bổ sung; chưa sửa nội dung PDF gốc và không thay đổi phạm vi nguồn đề.
