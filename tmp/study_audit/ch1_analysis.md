# Chương 1: phân tích cuối theo 5 bộ đề được chấp nhận

Ngày kiểm: 22/10/2026. **Chỉ dùng E01, E02, E03, E08, E10 làm bằng chứng đề; T1 làm nguồn lý thuyết.** E03 là bản BHT sưu tập và soạn lại sau thi 2025–2026, đã được người dùng chấp nhận; không gọi là đề gốc hay đáp án chính thức. E08 và E10 là hai đề trong folder 2023 và 2024 người dùng yêu cầu tính thêm. E06 trùng toàn bộ 40 câu E08, không tính thành bộ thứ sáu.

Mọi số trang là **trang vật lý PDF**. Nguồn và đường dẫn đầy đủ có trong `manifest.json`:

- T1: `[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf`.
- E01/E02/E03: `[BHT CNPM] NMMMT 2019-2020 GK1.pdf`, `[BHT CNPM] NMMMT 2020-2021 GK1.pdf`, `[BHT CNPM] NMMMT 2025-2026 GK1.pdf`.
- E08: `2023/Đề A MMT.pdf`; E10: `2024/2024.pdf`.

## Phạm vi đã đọc

Đã đọc toàn bộ T1, 69/69 trang, gồm mục lục và tổng kết. Hình ở tr27–28 (routing/forwarding) và tr67 (đóng gói) đã được render và xem. Đã đọc hết E01 (6 trang, 30 câu), E02 (7 trang, 30 câu) qua OCR, sau đó đối chiếu trực tiếp toàn bộ trang có câu Ch1: E01 tr1–3, E02 tr2 và tr5. OCR sai số liệu ở E01 C12: link1 dài **3 km**, không phải 9 km. Đã đọc hết E03 (30 câu), E08 (40 câu), E10 (42 câu).

Các nguồn khác đã đọc trước khi thu hẹp phạm vi chỉ lưu trong `ch1_archive.md`; **không dùng training, ngân hàng, bài tập ôn, đề mẫu, lịch sử phát triển đề hay slide tổng hợp để xếp ưu tiên, chọn câu luyện hoặc tính tần suất**. Không mở ba file đáp án riêng và không lấy đề online. Một số đề có đáp án xen kẽ/tham khảo: không coi key đó là chuẩn; bài tính dưới đây đã kiểm lại theo dữ kiện và T1.

## Phân nhóm câu để root lập bảng 172 câu

| Bộ | Câu thuộc nhóm chính Ch1 | Số câu |
|---|---|---:|
| E01 | 2, 3, 4, 10, 12, 13 | 6 |
| E02 | 4, 5, 14, 20 | 4 |
| E03 | 12, 21, 26 | 3 |
| E08 | 1, 12, 21, 31, 33, 36 | 6 |
| E10 | 1, 3, 6, 7, 23, 25, 35 | 7 |
| Tổng | Phân nhóm phục vụ ôn, không dự báo đề tương lai | **26** |

Quy tắc: câu phân loại tầng/PDU và RTT định nghĩa chung gán Ch1; câu dịch vụ/hoạt động vận chuyển gán Ch3; chức năng giao thức ứng dụng và IP+port gán Ch2. E01 C6 và E10 C32 hỏi process–process, gán chính Ch3 dù có giao thoa T1 tr62. E08 C11, E10 C24/C26 về HTTP gán Ch2. E08 C33/C36 chỉ hỏi phân loại tầng TCP/UDP nên gán Ch1. E10 C3/C25 lặp câu; nhiều câu E08/E10 cũng trùng các bộ khác: 26 là số vị trí câu trong 5 đề, **không phải 26 dạng độc lập**. E08 C21 có lựa chọn NFS gây mơ hồ, không dùng để chấm chắc một đáp án.

## Chia phần và xếp ưu tiên

A: phải hiểu và làm chắc trong tuần. B: phải hiểu để tạo nền và nối kiến thức. C: học sau khi A/B ổn. Không suy tỷ lệ câu hỏi thành xác suất ra đề mới.

| Phần | Mức | Cần đạt | Trang T1 | Bằng chứng đề |
|---|---|---|---|---|
| 1.1 Internet, giao thức | B, nền bắt buộc | Thành phần và dịch vụ; mạng của các mạng; khuôn dạng, thứ tự thông điệp và hành động gửi/nhận | 3–7 | Không thấy câu riêng trong nhóm Ch1; cần để hiểu Ch2/3 |
| 1.2 Mạng biên | B; đơn vị/tốc độ là A | Host/client/server, mạng truy cập, edge router; wired/wireless; L bit và R bit/s | 9–23, nhất là 20–23 | E03 C21 tr4; E10 C6 tr1; E01 C2–3 tr1; E02 C20 tr5–6 |
| 1.3 Mạng lõi | B; store-and-forward là nền bài A | Routing/forwarding; nhận đủ gói rồi phát link kế; packet/circuit; queue/loss; FDM/TDM; ISP ở mức nguyên lý | 25–44, nhất là 26, 29–35 | Nền bài 3 link: E01 C12 tr3, E02 C14 tr5; không thấy yêu cầu sâu về IXP/FDM/TDM |
| 1.4 Hiệu suất | **A** | Đơn vị; 4 loại delay; L/R khác d/s; tổng delay nhiều link; bottleneck, số gói/s, RTT; chia sẻ có giả định | 46–56; thêm 20, 29 | E01 C2–3 tr1, C10/C12 tr3; E02 C14 tr5, C20 tr5–6; E03 C12 tr2; E08 C31 tr3; E10 C35 tr4 |
| 1.5 Chồng giao thức | **A** | 5 tầng, chức năng, giao thức ví dụ, PDU; đóng/mở gói; sơ đồ host–switch–router–host | 58–67, nhất là 62–67 | E01 C4 tr1–2, C13 tr3; E02 C4–5 tr2; E03 C26 tr4–5; E08 C1 tr1, C12/C21 tr2, C33 tr3, C36 tr4; E10 C1/C3/C7 tr1, C23/C25 tr3 |

### 1.1 Internet và giao thức

Chia thành (a) thành phần Internet và (b) dịch vụ/giao thức. Vẽ host → access → router/ISP → access → host. Kể một ví dụ giao thức: gửi gì, theo thứ tự nào, bên nhận làm gì. RFC/IETF chỉ cần nhận diện từ slide; không dành nhiều giờ nhớ lịch sử/tên tổ chức.

### 1.2 Mạng biên

Chia thành (a) host, mạng truy cập và phương tiện vật lý; (b) host phát dữ liệu lên link. Phải phân biệt **R đo bit/s** với **s đo m/s** trước khi học delay. Biết cable/DSL/Ethernet/WiFi/cellular theo nguyên lý và guided/unguided theo môi trường truyền. Con số tốc độ/độ phủ trên slide là ví dụ, không phải thông số chung bất biến của công nghệ.

### 1.3 Mạng lõi

Chia thành (a) routing/forwarding và store-and-forward; (b) chia sẻ packet/circuit; (c) ISP/peering/IXP ở mức sơ đồ. Vẽ timeline **một gói qua hai link** để thấy hai lần L/R. Lập bảng packet/circuit: dành riêng/chia sẻ, thiết lập kênh, tài nguyên khi im lặng, trễ/mất gói. Không kết luận packet switching luôn nhanh hơn hoặc không tắc nghẽn. Hiểu các mạng nối nhau để host liên lạc, không cần thuộc tên ISP.

### 1.5 Chồng giao thức

Học sau tổng quan biên/lõi, trước Ch2/3. Dựng bảng 5 hàng: tầng → nhiệm vụ → PDU → giao thức ví dụ. T1 tr62–67: ứng dụng/message; vận chuyển/segment; mạng/datagram; liên kết/frame; vật lý/bit. Network: host–host; transport: process–process; link: lân cận. Hình tr67: switch xét tầng liên kết, router xét tầng mạng trong mô hình chuyển tiếp cơ bản; host có đủ 5 tầng. Tầng trên dùng dịch vụ tầng dưới. Session không là tầng riêng trong **chồng 5 tầng đang học**; không mở rộng sang chi tiết OSI ngoài T1.

### 1.4 Hiệu suất

Chia thành (a) đơn vị, transmission/propagation; (b) tổng delay một gói qua nhiều link, có/không processing và queue; (c) throughput/bottleneck; (d) queue/loss/RTT. Phải giải được bài mới của (a), (b), (c) và giải thích lý do chọn công thức. Luyện bằng giấy, không chỉ đọc slide.

## Công thức và bẫy đã kiểm

1. `d_trans=L/R`: L là bit, R là bit/s; `1 byte=8 bits`. Mbps trong các bài dùng `10^6 bit/s`; đổi km→m và s→ms. E01 C3: `1000×8/(2×10^6)=4ms`. E10 C35: `2000×8/(2×10^6)=8ms`.
2. `d_prop=d/s`: d là mét, s là m/s. Tăng R không làm d/s giảm; gói dài hơn không làm d/s tăng. E03 C12: `1500×8/(2×10^6)+2000×1000/(2×10^8)=0.016s`, chọn “Khác”, không phải 0.011s.
3. Một gói store-and-forward qua n link, bỏ queue/processing: `d_e2e=Σ(L/R_i)+Σ(d_i/s_i)`. Nếu đề cho processing ở router, cộng đúng số lần xử lý; không dùng L/minR thay tổng L/R của một gói.
4. E01 C12, đối chiếu hình: `L=12000bit; R=(100,10,10)Mbps; d=(3,500,2)km; s=3×10^8m/s` ⇒ `4.203333…ms` (A). OCR sai 3km thành 9km.
5. E02 C14, đối chiếu hình: `L=16000bit; R=(100,100,10)Mbps; d=(5,500,3)km; s=3×10^8m/s` ⇒ `3.613333…ms≈0.0036s` (D). Không bỏ lần phát lên link2/link3.
6. Một luồng qua link nối tiếp, không cạnh tranh, theo mô hình giới hạn link: `T=min R_i`. Không cộng/trung bình R. E01 C10: `min(300Kbps,3Mbps,1Mbps)=300Kbps`. Với n luồng chia sẻ **công bằng** link R, T1 tr56 dùng `min(R_s,R_c,R/n)`; không tự chia đều nếu thiếu giả định.
7. Số gói tối đa phát lên link trong t giây, bỏ overhead: `floor(Rt/L)`. E01 C2/E02 C20: `10^6/(1000×8)=125 gói/giây`.
8. `d_nodal=d_proc+d_queue+d_trans+d_prop`. Cường độ `La/R`, a đo gói/s. Queue phụ thuộc tải và biến thiên gói đến; buffer hữu hạn đầy dẫn đến loss. Delay vô hạn ở T1 tr50 thuộc mô hình quá tải kéo dài/buffer vô hạn, không phải mọi buffer thực tế tăng mãi.
9. RTT là thời gian gói nhỏ đi rồi quay lại, khác lan truyền một chiều và thời gian tải file; nối sang HTTP/timeout TCP. E08 C31 kiểm khái niệm này.
10. Transport/network/link thêm header như T1 tr63–67; link có thể có trailer theo giao thức. **Physical truyền bit**. Không học “mọi tầng đều thêm header” như định luật tuyệt đối. E03 C26 dùng cách nói giản lược, cần hiểu theo hình T1.

## Điểm mơ hồ và phần C

- E08 C21 hỏi giao thức thuộc Application, có HTTP và NFS. HTTP có trong T1 tr62; T1 không giới thiệu NFS. Theo phân loại thông thường NFS cũng thuộc tầng ứng dụng, nên câu một đáp án thiếu chặt. Dùng câu này để nhận diện chủ đề, không chấm key chắc một lựa chọn.
- E10 C6 viết “Bps (bit per second)”, lẫn B/b. Học bps cho bit/s và B/s cho byte/s; đọc đầy đủ đơn vị trước khi tính.
- Phần C: mọi con số access speed/độ phủ, tên từng ISP, bài xác suất 35 user T1 tr34, phân tích traceroute từng hop tr51–52. Không thấy yêu cầu trực tiếp sâu các phần này trong 5 bộ.
- T1 tr34 ghi xác suất hơn 10 user hoạt động “nhỏ hơn 0.0004”. Nếu 35 user độc lập, p=0.1 thì nhị thức cho `0.0004242976`: gần 0.0004 nhưng không nhỏ hơn. Không học thuộc bất đẳng thức sai này.
- Không kéo subnet/VLSM, NAT/fragmentation chi tiết, RIP/OSPF/BGP, ARP/MAC access/CRC/Manchester vào Ch1 từ các nguồn bị loại. T1 chỉ cần nhận diện vai trò IP/Ethernet/router trong mô hình.

## Thời lượng trong tuần 2–3 giờ/ngày

Ch1 khoảng **3–3.5 giờ tổng**, có truy hồi cách ngày, không đọc dồn 69 slide. Thứ tự: **1.1 → 1.2 → 1.3 → 1.5 → 1.4**, rồi sang Ch2. Chồng tầng tạo nền; hiệu suất cần giải bài trước HTTP RTT.

- Ngày1, 150 phút học thực: 20 phút Internet+biên; 25 phút core; 35 phút chồng tầng; 50 phút hiệu suất kèm 3 bài; 20 phút tự nhớ/luyện 6–8 câu. Nếu chỉ 120 phút, chuyển 30 phút bài tính sang Ngày2. Nếu 180 phút, thêm 30 phút sửa lỗi. Root cần quy định giờ nghỉ rõ trong lịch tổng.
- Đầu Ngày2, 20–30 phút: dựng 5 tầng/PDU; làm 1 bài 3 link và 1 bài throughput không nhìn lời giải.
- Ngày4 và Ngày6: mỗi ngày 10–15 phút nhớ công thức/khái niệm và làm lại câu sai; không đọc lại cả chương.
- Ngày7: câu Ch1 nằm trong lượt thi thử chung, rồi sửa bằng trang T1 liên quan.

Ngưỡng chuyển chương: viết đủ 5 tầng/PDU; phân biệt host/process/lân cận; giải thích routing/forwarding và packet/circuit; giải đúng một bài 1 link, một bài 3 link, một bài bottleneck có đơn vị. Không cần thuộc tất cả phần C.

## Câu luyện chỉ từ 5 đề được chấp nhận

- Chồng tầng: E01 C4/C13; E02 C4–5; E03 C26; E08 C1/C12/C33/C36; E10 C1/C3/C7/C23/C25. E10 C3/C25 trùng nên dùng kiểm nhớ, không tính dạng mới. E08 C21 chỉ thảo luận mơ hồ.
- Đơn vị, tốc độ, delay: E01 C2–3/C12; E02 C14/C20; E03 C12; E10 C6/C35. E02 C20 trùng dạng/số liệu E01 C2, dùng kiểm nhớ cách ngày.
- Thông lượng: E01 C10. RTT: E08 C31. Mạng biên: E03 C21.
- Có thể tự thay số bài bottleneck để kiểm hiểu, nhưng ghi “bài tự luyện biến thể”, không gọi là câu của đề.

Ảnh/script tạm giữ riêng trong `tmp/study_audit`; không sửa nguồn. Bản này thay phân tích mở rộng cũ cho kế hoạch cuối.
