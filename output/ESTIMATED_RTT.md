# EstimatedRTT — TCP ước lượng thời gian đi–về

Nguồn: [slide TCP mới người dùng cung cấp](<D:/0_Personal/UIT/Đề thi các năm/NMMMT/Lý thuyết/Chapter_3_2023_3.6 TCP_1st.pdf>), trang PDF **9–11**, số in trên slide cũng là **9–11**. Công thức EstimatedRTT nằm ở **trang 10**.

## 1. Vì sao TCP cần ước lượng RTT?

TCP gửi dữ liệu rồi chờ ACK. Thời gian đi–về thay đổi giữa các lần gửi, nên không thể chỉ lấy một lần đo làm thời gian chờ cho mọi lần sau.

- Timeout quá ngắn: có thể gửi lại dù dữ liệu hoặc ACK chỉ đang đến chậm.
- Timeout quá dài: phản ứng chậm khi dữ liệu hoặc ACK thực sự bị mất.

TCP dùng các lần đo RTT để duy trì một giá trị ước lượng, rồi dùng giá trị này trong việc tính timeout.

## 2. SampleRTT và EstimatedRTT

| Đại lượng | Ý nghĩa |
|---|---|
| **SampleRTT** | Thời gian đi–về đo được của một lần gửi: từ khi gửi segment đến khi nhận ACK xác nhận nó. |
| **EstimatedRTT** | Giá trị RTT ước lượng được cập nhật từ ước lượng cũ và mẫu đo mới. |

Ví dụ tự soạn: gửi segment ở thời điểm 20 ms, nhận ACK lúc 140 ms thì **SampleRTT = 140 − 20 = 120 ms**.

Theo trang 9, **bỏ qua việc lấy SampleRTT từ segment đã truyền lại**. Khi có bản gửi lại, có thể khó xác định ACK đang xác nhận bản gửi đầu hay bản gửi lại.

SampleRTT không phải trễ truyền `L/R`; nó đo khoảng thời gian từ gửi đến nhận ACK.

## 3. Công thức cần nhớ — trang 10

```text
EstimatedRTT_mới = (1 − α) × EstimatedRTT_cũ + α × SampleRTT_mới
```

Để tính gọn, gọi EstimatedRTT là E:

```text
E_mới = (1 − α) × E_cũ + α × Sample_mới
```

- **α** là trọng số dành cho mẫu đo mới.
- **1 − α** là trọng số dành cho ước lượng cũ; ước lượng cũ đã chứa ảnh hưởng của lịch sử đo trước đó.
- Slide nêu giá trị tiêu biểu **α = 0,125 = 1/8**. Khi đó, ước lượng cũ chiếm 87,5%, mẫu mới chiếm 12,5%.
- **Đề cho α khác thì dùng α của đề.** Không tự đổi về 0,125.

Đây là cơ chế **EWMA**, tức trung bình trượt có trọng số theo hàm mũ. Mỗi lần cập nhật lại trộn mẫu mới vào kết quả cũ, nên ảnh hưởng của các mẫu xa hơn trong quá khứ giảm dần.

α lớn hơn làm kết quả phản ứng mạnh hơn với mẫu mới. α nhỏ hơn làm kết quả thay đổi chậm hơn. Đường EstimatedRTT vì thế có thể mượt hơn đường SampleRTT như đồ thị trang 10.

Hai chữ EstimatedRTT ở hai vế trong công thức trên slide mang hai thời điểm khác nhau: **vế trái là kết quả mới, vế phải là giá trị cũ**.

## 4. Ví dụ tính hai lần liên tiếp

Ví dụ tự soạn, đã cho:

- EstimatedRTT ban đầu: **100 ms**.
- α = **0,125**.
- Hai SampleRTT tiếp theo lần lượt là **120 ms**, rồi **80 ms**.

**Lần 1: nhận mẫu 120 ms**

```text
E1 = (1 − 0,125) × 100 + 0,125 × 120
   = 0,875 × 100 + 0,125 × 120
   = 87,5 + 15
   = 102,5 ms
```

Mẫu mới cao hơn ước lượng cũ, nên E tăng từ 100 lên 102,5 ms. Nó không nhảy thẳng lên 120 ms.

**Lần 2: nhận mẫu 80 ms**

Lúc này, giá trị cũ để tính tiếp là **102,5 ms**, không còn là 100 ms.

```text
E2 = (1 − 0,125) × 102,5 + 0,125 × 80
   = 0,875 × 102,5 + 10
   = 89,6875 + 10
   = 99,6875 ms
```

| Lần cập nhật | E trước cập nhật | SampleRTT mới | E sau cập nhật |
|---|---:|---:|---:|
| 1 | 100 ms | 120 ms | 102,5 ms |
| 2 | 102,5 ms | 80 ms | 99,6875 ms |

Khi tính nhiều lần, giữ đủ số lẻ ở các bước giữa; làm tròn kết quả cuối theo yêu cầu đề.

## 5. Các chỗ dễ nhầm khi làm bài

1. **Không cộng hai RTT rồi chia 2**, trừ khi hệ số của bài thực sự tương ứng với cách tính đó. Dùng đúng công thức có α.
2. **Không đảo trọng số:** mẫu mới đi với α, ước lượng cũ đi với `1 − α`.
3. **Cập nhật nối tiếp:** kết quả lần trước trở thành E_cũ của lần sau.
4. **Thống nhất đơn vị:** chẳng hạn cùng đổi mọi giá trị sang ms trước khi tính.
5. **Không tự lấy E ban đầu bằng 0.** Trang 9–11 không nêu chi tiết quy tắc khởi tạo. Các ví dụ trong tài liệu này đã cho E ban đầu; nếu đề chỉ cho chuỗi mẫu mà không cho giá trị khởi tạo, cần làm rõ giả thiết trước khi tính.

## 6. EstimatedRTT khác timeout và TIME_WAIT

Trang 11 đưa công thức:

```text
TimeoutInterval = EstimatedRTT + 4 × DevRTT
```

**DevRTT** phản ánh mức dao động của các mẫu RTT quanh giá trị ước lượng. Thành phần `4 × DevRTT` tạo phần dự phòng cho khoảng timeout.

| Đại lượng | Dùng để làm gì? |
|---|---|
| **EstimatedRTT** | Ước lượng thời gian đi–về. |
| **TimeoutInterval** | Khoảng thời gian chờ trước khi kích hoạt timeout phát lại. |
| **TIME_WAIT = 2 × MSL** | Khoảng chờ trong quá trình đóng kết nối TCP, đã học ở phần FIN. |

Phần đang tập trung ở đây là **cách tính EstimatedRTT**. Không lấy EstimatedRTT làm chính TimeoutInterval, và không dùng công thức EWMA này để tính TIME_WAIT.

## 7. Tự kiểm — chưa kèm đáp án

Các câu dưới đây là **tự soạn**, không phải câu trích từ đề thi.

**Câu 1.** E hiện tại bằng 80 ms, α = 0,2. Đo được SampleRTT mới 100 ms. Tính E sau cập nhật.

**Câu 2.** Tiếp câu 1: mẫu đo tiếp theo bằng 90 ms, α vẫn bằng 0,2. Tính E sau lần cập nhật này. Ghi rõ E_cũ bạn sử dụng.

**Câu 3.** Theo trang 9, có dùng thời gian đo từ một segment đã truyền lại làm SampleRTT trong mô hình này không? Giải thích lý do.

## Tra đúng trang trong slide mới

- **Trang 9:** mục đích ước lượng RTT, khái niệm SampleRTT, bỏ qua segment truyền lại.
- **Trang 10:** công thức EstimatedRTT, EWMA, α tiêu biểu 0,125 và đồ thị minh họa.
- **Trang 11:** liên hệ EstimatedRTT, DevRTT và TimeoutInterval.
