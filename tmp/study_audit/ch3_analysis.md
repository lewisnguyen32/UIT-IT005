# Chương 3: hồ sơ phân tích theo phạm vi cuối cùng

**Cập nhật 27/10/2026:** người dùng chốt chỉ học đến hết TCP, gồm quản lý kết nối, điều khiển luồng và điều khiển tắc nghẽn theo ảnh outline. T3 đến hết trang PDF102; tr103 là mục lục chuyển phần, tr104–108 phát triển tầng vận chuyển/QUIC/HTTP3 ngoài phạm vi. Trang109 có thể dùng tổng kết các phần đã giữ. EstimatedRTT vẫn tùy chọn trong TCP. Thay đổi này không ảnh hưởng phân loại71câu Ch3 trong172lượt vì không có câu QUIC trong năm đề giữ lại.

**Nguồn dùng làm căn cứ:** E01, E02, E03, E08, E10 và T3. E06 là DOCX trùng E08, không đếm. Mọi số trang là **trang vật lý PDF**, không phải số slide in ở góc trang. Bản này thay thế các phương án phạm vi trước đó.

## 1. Nhật ký đọc và giới hạn bằng chứng

- T3 `[BHT CNPM] NMMMT_Chương 3_Tầng vận chuyển.pdf`: đọc toàn bộ 109 trang. Kiểm hình/FSM ở trang ít chữ và chỗ nghi sai. Trang 70,72 chỉ còn khung chèn web; sơ đồ tĩnh GBN/SR ở trang 69,73 đủ học cơ chế.
- E01 `[BHT CNPM] NMMMT 2019-2020 GK1.pdf`: đọc hết 30 câu/6 trang bằng OCR, đối chiếu trực tiếp hình trang 2-5 cho Ch3.
- E02 `[BHT CNPM] NMMMT 2020-2021 GK1.pdf`: đọc hết 30 câu/7 trang bằng OCR, đối chiếu trực tiếp hình trang 2-7 cho Ch3.
- E03 `[BHT CNPM] NMMMT 2025-2026 GK1.pdf`: đọc hết 30 câu/6 trang. Bản sưu tập/soạn lại sau thi được user chấp nhận. Trang 6 tự ghi đáp án tham khảo, không phải đáp án chính thức.
- E08 `2023/Đề A MMT.pdf`: đọc hết 40 câu/4 trang. E10 `2024/2024.pdf`: đọc hết 42 câu/4 trang. User bổ sung hai đề này vào phạm vi; không tự xác nhận thêm tính chính thức.
- Tổng 172 **lượt câu**, có lặp nội dung giữa các đề. Đây không phải 172 câu độc lập và không dùng làm xác suất đề tương lai.
- Theo nhiệm vụ audit ban đầu đã đọc toàn bộ câu E06,E13,E14,E15,E20; E17 phần Ch3 trang 109-160 và bài ôn 161-180; E16 lịch sử tracked deletion do root trích. Các nguồn này **không làm căn cứ xếp ưu tiên, thống kê hoặc bài luyện final**. E06/E08 cùng bộ 40 câu; E14 thiếu một đồ thị; E16 chỉ có text bị xóa theo tracked changes. Những ghi chú này chỉ phục vụ kiểm nguồn.
- Không mở các file đáp án riêng bị loại; không dùng đề online, E19 bị loại. Đáp án nhúng trong file đề không được dùng để chấm mù.

## 2. Phân loại Ch3: 71/172 lượt câu

Một câu chỉ thuộc một chương chính. Socket code/client-server, định danh endpoint IP+port gán Ch2 theo nguyên lý ứng dụng; nhận biết tầng đơn giản gán Ch1; demux và dịch vụ cụ thể tầng vận chuyển gán Ch3.

| Bộ | Câu Ch3 | Số lượt |
|---|---|---:|
| E01 | 5,6,7,8,9,11,15,16,17,18,19,21,24,25 | 14 |
| E02 | 6,7,8,9,10,11,15,16,19,21,23,25,26,30 | 14 |
| E03 | 1,3,4,5,9,11,13,15,16,17,18,23,24,27,29,30 | 16 |
| E08 | 2,3,4,6,10,27,28,34,35,37,38,39,40 | 13 |
| E10 | 4,5,11,21,29,30,31,32,33,34,37,40,41,42 | 14 |
| Tổng | Có câu/chủ đề lặp giữa các đề | **71** |

| Nhóm chính Ch3 | E01 | E02 | E03 | E08 | E10 | Tổng |
|---|---|---|---|---|---|---:|
| Dịch vụ/nhận diện TCP-UDP và ứng dụng chọn vận chuyển | 6,16 | - | 29 | 4,10,27,28,34,37 | 4,5,11,21,32 | 14 |
| Mux/demux, port theo hình/chức năng | - | 10,11 | - | - | 30,37 | 4 |
| UDP: tính chất/header/Length/checksum | 7,21,24 | 21,26 | 3,4,5,13 | 3,38,39,40 | 31,33,34,42 | 17 |
| RDT/FSM/mất ACK | 8,11,19 | 16,19 | 30 | 2,6 | 29,40 | 10 |
| Pipeline/GBN/SR | 18 | 9,25 | 15,24 | - | - | 5 |
| TCP byte stream, Seq/ACK, phát lại/header, MSS | 5,9,15,17,25 | 6,7,8 | 9,11,16,17 | - | 41 | 13 |
| Flow/window | - | 15 | 27 | 35 | - | 3 |
| Thiết lập/đóng kết nối | - | 30 | 1,18,23 | - | - | 4 |
| EstimatedRTT | - | 23 | - | - | - | 1 |
| Tổng | 14 | 14 | 16 | 13 | 14 | **71** |

E03 C11 có cả Seq/ACK/rwnd nhưng chọn nhóm Seq/ACK làm chính. E03 C15 ghép TCP/UDP/RDT/GBN/SR, chọn nhóm pipeline để không cộng ở nhiều hàng. E01 C23,E02 C12 (socket code) và E03 C10 (IP+port) gán Ch2; E02 C10-11 (port theo hình) gán Ch3. Các câu Ch1 E08/E10 đã đối chiếu quy ước chung root, không cộng lại Ch3.

## 3. Phần học, thứ tự và mức ưu tiên

Điều kiện trước Ch3: message/segment/datagram; vận chuyển khác tầng mạng; bit/byte; L/R; RTT hai chiều. Trật tự: **dịch vụ -> socket/port,mux/demux -> UDP/checksum -> RDT -> pipeline,GBN/SR -> TCP theo byte -> flow/quản lý kết nối -> congestion**.

A: cần vững trước luyện đề tổng hợp. B: học sau A, vẫn dành thời gian. C: nhận biết khi đã đạt A/B. Mức này dựa trên điều kiện tiên quyết, T3 và năm đề được chấp nhận; không dựa vào training/ngân hàng/mẫu.

| Phần | Mục tiêu | Mức | T3 cần đọc | Bằng chứng tiêu biểu |
|---|---|---|---|---|
| 3.1 Dịch vụ vận chuyển | Truyền thông logic giữa tiến trình ở hai host; chạy tại đầu cuối; hoạt động gửi/nhận; TCP/UDP cung cấp gì, không bảo đảm gì | A | tr.5-8 | E01 C6 tr.2,C16 tr.3; E08 C4 tr.1; E10 C32 tr.3 |
| 3.2 Mux/demux | Mux tại gửi, demux tại nhận; source/destination port đổi vai khi trả lời; UDP socket (IP đích,port đích), TCP connection socket bộ 4; nhiều kết nối cùng port server | A nền tảng | tr.10-22 | E02 C10-11 tr.4; E10 C30 tr.3,C37 tr.4 |
| 3.3 UDP/checksum | Best effort, connectionless; không ACK/phát lại/flow/congestion sẵn; 4 trường 16 bit, header 8 byte; Length; checksum phát hiện lỗi | A | tr.24-34 | E01 C7,C21,C24; E02 C21,C26; E03 C3-5,C13; E08 C3,C38-40; E10 C31,33-34,C42 |
| 3.4 RDT | Mỗi phiên bản giải quyết vấn đề gì; checksum/ACK/NAK/seq/timer; đọc FSM và sơ đồ mất gói/mất ACK/timeout sớm, chống giao trùng | A | tr.36-61 | E01 C8,C11,C19; E02 C16,C19; E03 C30; E08 C2,C6; E10 C29,C40 |
| 3.5 Pipeline,GBN/SR | Cửa sổ, ACK tích lũy/riêng; timer,buffer,out-of-order; gói gửi lại khi timeout; ACK mất chưa chắc phải gửi lại dữ liệu | A cơ chế; B tính utilization | tr.62-73 | E01 C18; E02 C9,C25; E03 C15-17,C24 |
| 3.6 TCP theo byte,header,Seq/ACK | Seq byte đầu; ACK byte kế tiếp còn chờ theo thứ tự; hai chiều riêng; ACK tích lũy; MSS; timeout/fast retransmit; đọc Wireshark | A, dành nhiều bài nhất | tr.75-84 | E01 C5,C9,C15,C17,C25; E02 C6-8; E03 C9,C11,C16-17; E10 C41 |
| 3.7 Flow control | rwnd bảo vệ buffer bên nhận; lượng outstanding; khác cwnd; Window Size khác độ dài từng segment | A | tr.85-89 | E02 C15; E03 C11,C27; E08 C35 diễn đạt rất chung |
| 3.8 Kết nối TCP | SYN/SYN+ACK/ACK, ISN; SYN/FIN tiêu thụ 1 số thứ tự; FIN đóng một chiều gửi, còn nhận chiều ngược; FIN+ACK có thể ghép | A | tr.90-94 | E02 C30; E03 C1,C18,C23 |
| 3.9 EstimatedRTT | SampleRTT/EstimatedRTT, cập nhật trọng số, nêu khởi tạo | B, có đề hỏi nên không bỏ | T3 **thiếu công thức**, cần bổ sung minh bạch | E02 C23 tr.6 |
| 3.10 Congestion TCP | cwnd/ssthresh/MSS; SS/CA/Fast Recovery; timeout khác 3 dupACK; mỗi ACK khác mỗi RTT | B nền lý thuyết | tr.96-102 | Không có câu trực tiếp về cwnd/đồ thị trong 172 lượt; E03 C15 chỉ nhắc tính năng TCP |
| 3.11 QUIC/HTTP3 | Ngoài phạm vi theo yêu cầu chỉ học đến hết TCP ngày27/10/2026 | Loại khỏi lộ trình Ch3 | tr.104-108 | Không có câu trực tiếp trong 5 bộ; không thay đổi kiểm đếm |

## 4. Cơ chế và bẫy phải hiểu

### UDP/checksum

Tự vẽ bốn trường Source port,Destination port,Length,Checksum, mỗi trường 16 bit. Header=64 bit=8 byte. Payload M byte => Length=M+8; Length N byte => payload=N-8. Độ rộng trường Length 2 byte khác giá trị lưu trong đó. Byte thứ 9 nếu đếm từ 1 tương đương offset 8 nếu đếm từ 0 (E08 C38/E10 C34). E02 C21 hỏi giới hạn biểu diễn trường 16 bit, không lẫn với payload tối đa sau IP header.

Checksum: cộng bù 1 các từ 16 bit, cộng vòng carry về 16 bit thấp, rồi đảo bit. Không bỏ carry, không dùng bù 2. Khớp chỉ có nghĩa **không phát hiện lỗi**, vẫn có thể lọt lỗi (T3 tr.33); không sửa lỗi, không sắp thứ tự gói.

Luyện tăng dần: E10 C31 (Length->payload), E03 C4 (payload->Length), E02 C21 (giới hạn trường), E03 C5 hoặc E02 C26 (hai từ), E01 C21 (ba từ, có carry). E01 C21 nằm qua trang 4-5; đã đọc đủ ba số trực tiếp từ scan, không dùng OCR rớt số.

### Chuỗi RDT

| Phiên bản | Giả định/vấn đề mới | Cơ chế |
|---|---|---|
| 1.0 | Kênh hoàn toàn tin cậy | Không cần phục hồi lỗi/mất |
| 2.0 | Dữ liệu có lỗi bit | Checksum+ACK/NAK+phát lại; ACK/NAK hỏng còn là lỗ hổng |
| 2.1 | ACK/NAK có thể hỏng | Seq 0/1 phân biệt bản mới/bản gửi lại, chống giao trùng |
| 2.2 | Thay NAK | Chỉ ACK có số thứ tự; ACK gói đúng cuối cùng đóng vai trò phản hồi lỗi |
| 3.0 | Có thể mất dữ liệu hoặc ACK | Timer, timeout/phát lại; seq vẫn xử lý trùng; stop-and-wait |

rdt2.1 xử lý ACK/NAK **hỏng**, không tự có timer xử lý ACK **mất**. Không thấy ACK đúng lúc chưa chắc dữ liệu mất: ACK có thể mất hoặc trễ. Timeout sớm có thể gửi trùng nhưng không được giao trùng lên ứng dụng.

FSM: điều kiện trên vạch, hành động dưới vạch; phân biệt chờ tầng trên/chờ ACK; nhận biết NAK/seq0-1/timer. E02 C16 là FSM1.0, E01 C19 là FSM2.0, E01 C8 là mất ACK của rdt3.0 (đã xem hình). Phải đọc hình bằng cơ chế.

### GBN/SR và hiệu suất

GBN mô hình bài tập: ACK(n) xác nhận packet đúng thứ tự tới n; timer cho outstanding sớm nhất; timeout gửi lại nó cùng các packet sau còn outstanding. T3 tr.69 dùng discard out-of-order; tr.68 nói có thể hủy hoặc buffer tùy triển khai. Tuân theo giả thiết/hình đề; E03 C24 kiểm biến thể discard.

SR ACK từng gói nhận đúng, buffer out-of-order trong cửa sổ nhận, timer riêng; timeout chỉ gửi lại gói thiếu ACK tương ứng. Lấp lỗ hổng có thể giao nhiều gói buffer lên ứng dụng. "Đã ACK" khác "cửa sổ đã trượt".

E02 C25: mất ACK trung gian không buộc phát lại nếu ACK tích lũy cao hơn đã xác nhận dữ liệu ấy. E02 C9: phân biệt gói đã tới vật lý và dữ liệu chấp nhận đúng thứ tự. Một số câu nói "TCP dùng Go-back-N" để đặt mô hình; không đồng nhất TCP thực tế với GBN thuần túy. Seq/ACK TCP đếm byte; ACK(n) trong RDT packet-based có thể là chỉ số packet cuối nhận đúng.

Utilization stop-and-wait (bỏ qua thời gian ACK/xử lý): U=(L/R)/(RTT+L/R), L bit,R bit/s. Pipeline N gói lý tưởng: U=min(1,N(L/R)/(RTT+L/R)). Độ trễ lan truyền một chiều không phải RTT. Có trong T3 nhưng chưa thấy câu tính trực tiếp ở năm đề; không dành nhiều thời gian hơn checksum/SeqACK.

### TCP Seq/ACK,flow và kết nối

Segment chỉ có dữ liệu: Seq=s,payload L byte => các byte s..s+L-1, byte tiếp theo s+L. Nhận thành công liên tiếp và không có lỗ hổng trước đó => ACK=s+L. ACK=a xác nhận liên tiếp tới a-1 và chờ a; vẫn có thể đã buffer byte lớn hơn a. Hai chiều có Seq riêng. ACK thuần không tiêu thụ byte sequence; SYN/FIN mỗi cờ tiêu thụ 1.

E01 C15: Seq120,payload1000 => Seq dữ liệu kế1120; không cộng 1 vô điều kiện. E01 C5 Wireshark có Seq1,payload305,NextSeq306; ACK249 trên chính gói đang đọc thuộc chiều ngược, không phải ACK trả lời 305 byte đó. Đọc hình theo thứ tự sự kiện tới nhận; ACK chưa tới thì bên gửi chưa biết gói đã nhận. E01 C9 cho timeout sớm; ACK tích lũy không quay lùi khi nhận lại gói cũ. E03 C17 kiểm tránh gửi lại chỉ vì mất ACK1.

Flow: **bên nhận** quảng bá rwnd phần trống bộ đệm, bên gửi giới hạn outstanding. E02 C15 rwnd1000,payload100 => 10 segment nếu chưa có outstanding và cwnd không chặt hơn (giả định bài). Có outstanding phải trừ, không luôn chia rwnd/MSS. Có cả cwnd/rwnd thì giới hạn outstanding=min(cwnd,rwnd), lượng gửi thêm còn tùy outstanding hiện tại. E03 C11 ACK2000,rwnd4000 mô tả miền B sẵn sàng nhận; Seq1000 chiều B->A không phải điểm A gửi tiếp.

Bắt tay: SYN Seq=x -> SYN+ACK Seq=y,ACK=x+1 -> ACK=y+1. Không mặc định ISN=0 vì Wireshark dùng relative sequence. TCP handshake không tự mã hóa. FIN kết thúc một chiều gửi nhưng phía đó còn nhận được chiều kia; đóng có thể 4 segment hoặc ghép FIN+ACK thành 3. Fast retransmit cần 3 duplicate ACK ngoài ACK gốc; cách nói "3 ACK cùng giá trị" dễ mơ hồ. Phân biệt phục hồi lỗi,flow và congestion.

### EstimatedRTT: đề có,T3 thiếu

E02 C23 tr.6 yêu cầu SampleRTT 80,100,60 ms, alpha=0.2. T3 không có công thức EWMA; bản PDF đã lược một số slide so với số in. Ghi rõ **kiến thức bổ sung phục vụ câu đề, không gán một trang T3 không có**.

Công thức bổ sung: EstimatedRTT_mới=(1-alpha)EstimatedRTT_cũ+alpha*SampleRTT_mới. Đề không cho ước lượng trước mẫu đầu; phải ghi **giả sử EstimatedRTT_1=SampleRTT_1**:80->84->79.2 ms. Khởi tạo khác cho kết quả khác; không âm thầm gán 0 hoặc lấy trung bình cộng. Root đã đối chiếu quy tắc khởi tạo/cập nhật ở [RFC 6298 mục 2.2-2.3](https://www.rfc-editor.org/rfc/rfc6298.html#section-2): chuẩn khuyến nghị alpha=1/8, còn bài dùng alpha=0.2 do đề cho. Đây là kiểm công thức lý thuyết còn thiếu, không dùng đề online hay thêm vào thống kê.

### Congestion: nền slide,không tuyên bố đề ra nhiều

rwnd bảo vệ máy nhận,cwnd giới hạn do mạng. Mô hình T3: SS tăng xấp xỉ gấp đôi/RTT nếu mọi segment được ACK; CA khoảng 1 MSS/RTT. Tr.102 cập nhật mỗi ACK, khác tóm tắt theo round tr.100. Timeout:ssthresh=cwnd/2,cwnd=1 MSS, quay về SS. Ba dupACK:ssthresh=cwnd/2,cwnd=ssthresh+3 MSS vào Fast Recovery; ACK mới thoát recovery đưa cwnd=ssthresh. Giá trị "cắt một nửa" sau recovery khác thời điểm mới vào recovery.

Không có câu trực tiếp cwnd/đồ thị trong năm đề. Dành 25-35 phút hiểu T3 tr.96-102; không viện ngân hàng/mẫu để nâng ưu tiên. Không tự mở rộng Tahoe/CUBIC/BBR khi nguồn được dùng chưa yêu cầu.

## 5. Lỗi/mơ hồ ở nguồn được dùng

1. **T3 tr.78 (slide86):**9000 byte nhưng chú thích #0..#9999 và 5x2000 byte. Hình/bảng cuối1000 byte,ACK9000; nhất quán phải #0..#8999,bốn đoạn2000+một đoạn1000.
2. **T3 tr.88-89:**"bên gửi thông báo bộ đệm trống bằng rwnd"; đúng là **bên nhận quảng bá rwnd**,bên gửi tuân theo. Sơ đồ và tr.85-87 thể hiện đúng.
3. **T3 tr.66:**L/R=.008 ms => 3L/R=.024 ms; bản in .0024 nhưng kết quả .00081 tương ứng .024/30.008.
4. **T3 tr.19:**ví dụ connectionless nhưng hai client ghi SOCK_STREAM trong khi server SOCK_DGRAM. Code không nhất quán; không học UDP với SOCK_STREAM, dùng kết luận mux tr.22.
5. **E03 C30 tr.5:**rdt2.1 nói ACK/NAK "bị mất hoặc trùng"; động cơ chuẩn là ACK/NAK **hỏng**, mất cần timer3.0.
6. **E03 C3/E08 C10,C37:**UDP ít overhead/không handshake không có nghĩa nhanh hơn trong mọi điều kiện. T3 tr.25 có tin cậy bổ sung trên UDP/HTTP3; đừng học "không bao giờ truyền tin cậy qua UDP". Câu chọn ứng dụng xét mô hình truyền thống/best fit.
7. **E03 C1 và bảng tr.6:**bảng ghi C "server tự gửi ACK thay client", mâu thuẫn logic TCP/T3 tr.91. Theo cơ chế server chưa nhận ACK cuối, còn chờ/timeout. Không chấm mù theo bảng tham khảo.
8. **E02 C23:**thiếu khởi tạo EstimatedRTT. **E02 C15/E03 C11:**giản lược outstanding/cwnd. Nêu các giả định trong lời giải.
9. **E08 C6:**"RDT nào cung cấp dịch vụ giao hàng tin cậy?" không nêu loại kênh; từng phiên bản tin cậy trong giả thiết của nó. Không suy ra chỉ rdt3.0 là reliable.
10. **E08 C35:**"kỹ thuật sử dụng băng thông hiệu quả"/cửa sổ động rất chung, thiếu mô hình/thước đo. Học window/flow từ T3, không biến câu này thành định luật hiệu suất.
11. **T3 tr.68/69 và E03 C24:**GBN discard/buffer phải theo câu. **T3 tr.71:**chú thích buffer bên gửi không có nghĩa SR không buffer phía nhận; tr.73 vẽ receiver buffer rõ.
12. **E01 C25:**6 cờ cơ bản của đề cũ; T3 tr.76 còn ECE/CWR. Không khẳng định TCP header chỉ có 6 cờ. **E08 C38/E10 C34:**byte thứ9 đếm từ1,offset8 đếm từ0.

Không đưa lỗi E17/training/bank vào lý thuyết final vì chúng ngoài scope. Các lỗi nguồn được ghi để người mới không học thuộc nhầm.

## 6. Ghép Ch3 vào tuần2-3h/ngày

Đề xuất **5 giờ30 phút Ch3 trong khung tổng14 giờ**; nâng7-8 giờ nếu tổng21 giờ bằng luyện, truy hồi và chữa lỗi. Không hứa nắm hết109 slide chỉ trong khoảng đó. Không tính lại giờ socket/app-port đã học ở Ch2.

| Phiên | Phút | Học và đầu ra |
|---|---:|---|
| A:dịch vụ,mux,UDP | 60 | 15 dịch vụ/mux,15 header,20 checksum,10 tự giải3-4 câu. Vẽ header,làm Length,phân biệt demux |
| B:RDT,GBN/SR | 90 | 40 chuỗi RDT+hình mất ACK,30 GBN/SR,20 câu gói gửi lại/ACK tích lũy. Tự tạo bảng và trace1 mất gói+1 mất ACK |
| C:TCP bytes,flow,kết nối | 120 | 45 Seq/ACK+Wireshark,20 timeout/fast retransmit,20 rwnd,20 SYN/FIN,15 EstimatedRTT. Giải4-6 câu có giả định/lập luận |
| D:congestion nền,tự kiểm | 60 | 30 T3 cwnd/ssthresh,20 bộ câu Ch3 từ5 đề,10 sổ lỗi/truy hồi. Không dùng mẫu/bank |
| Tổng | 330=5.5 giờ | Học cơ chế trước,tập trung A; không làm hết mọi biến thể |

Có thể ghép A cuối ngày3,B ngày4,C ngày5,D ngày6; giờ còn lại dành Ch1/2 và ôn cách quãng. Ngày7 làm đề hỗn hợp/chữa lỗi, không bắt đầu học mới congestion. Đây là mô-đun để root ghép lịch tổng, không chiếm hết7 ngày.

Nếu có3h/ngày, thêm120-150 phút Ch3:30 trace RDT/GBN/SR,40 Seq/ACK/hình TCP,20 buffer/window,15 EstimatedRTT/utilization,10 QUIC,5-35 kiểm lại sau một ngày. Không thêm subnetting/định tuyến/link layer từ ngân hàng đã loại.

Đạt khi tự giải thích dịch vụ TCP/UDP; vẽ UDP header và checksum3 từ có carry; dựng bảng RDT; trace GBN/SR mất gói/ACK; Seq/ACK đúng byte,đọc rwnd,vẽ SYN/FIN; EstimatedRTT ghi khởi tạo; phân biệt rwnd/cwnd,SS/CA. Sai A thì dùng giờ mở rộng sửa. QUIC nằm ngoài phạm vi đã chốt.

## 7. Bài luyện chỉ từ năm đề được chấp nhận

1. UDP/header:E08 C3,C38-40;E10 C30-34;E01 C7,C24;E03 C4,C13;E02 C21. Chọn mỗi khái niệm một câu đầu, lặp lại ngày sau để truy hồi.
2. Checksum:E03 C5 -> E02 C26/E10 C42 (cùng hai chuỗi,không phải biến thể độc lập) -> E01 C21 (ba từ).
3. Dịch vụ/mux:E01 C6,C16;E02 C10-11;E08 C4,C27-28,C34,C37;E10 C4-5,C11,C21,C32,C37. Thẻ nhớ ngắn cho tên TCP ở E03 C29.
4. RDT/FSM:E02 C16 -> E01 C11,C19 -> E01 C8 -> E02 C19 -> E08 C2 -> E10 C29,C40 -> E03 C30 (cảnh báo mất/hỏng). E08 C6 mơ hồ,không dùng chấm cứng.
5. GBN/SR:E01 C18 -> E02 C25 -> E03 C24,C15 -> E02 C9. Trả lời bằng trace/giả thiết.
6. TCP SeqACK:E01 C15 -> E02 C6-8 -> E01 C5 -> E03 C9,C16-17 -> E01 C9,C17 -> E03 C11. MSS:E10 C41. Phân biệt ACK gói đang đọc với ACK trả lời payload.
7. Flow/kết nối/header:E02 C15,C30;E03 C1,C18,C23,C27;E01 C25. Đối chiếu T3 khi bảng tham khảo E03 C1 sai.
8. B sau A:E02 C23 EstimatedRTT,ghi khởi tạo; congestion tự kiểm T3 tr.96-102 vì năm đề chưa có câu trực tiếp.

Mỗi câu tự giải cần có cơ chế và giả định. Chỉ nhận ra đáp án từng nhìn thấy chưa được tính là nắm chắc.
