# Phân tích Chương 1 — nhật ký đọc và đề xuất ôn

Ngày kiểm: 22/10/2026. Phụ trách: subagent Chương 1. Mọi trang dưới đây là **trang vật lý của PDF**, không lấy số trang in trong tài liệu nếu khác. Nhãn E/T tra đường dẫn tuyệt đối trong `manifest.json`. Không dùng web/đề online.

## 1. Phạm vi đã đọc, cách dùng nguồn

- Đã đọc toàn bộ chữ trích xuất của **T1, 69/69 trang**, gồm cả trang mục lục, tổng kết; hình thiếu chữ ở tr27–28 và sơ đồ đóng gói tr67 đã render và xem. T1 là nguồn lý thuyết chính: `[BHT CNPM] NMMMT_Chương1_Giới thiệu.pdf`.
- Đã đọc toàn bộ **Chương 1 của E17, tr1–50**; tr51 bắt đầu Chương 2. Đã render và xem tr8,12,31–36,42–46,50 để bổ sung hình/chữ chỉ có trong ảnh. E17 là slide ôn tập, không phải đề thi.
- Đã đọc hết các câu trong E03 (30 câu, 6tr), E06 (40 câu), E08 (40 câu, 4tr), E10 (42 câu, 4tr), E13 (62tr, đề thử/training 30 câu và 6 câu RDT bổ sung), E14 (toàn bộ ngân hàng qua đoạn P1–P819), E15 (28tr, bài tập ôn theo chương), E20 (15 câu đề mẫu).
- Đã đọc hết **E01_ocr.txt (6tr,30 câu)** và **E02_ocr.txt (7tr,30 câu)**, đối chiếu trực tiếp ảnh toàn bộ các trang có câu Ch1: E01 tr1–3, E02 tr2 và tr5. OCR tiếng Anh sai dấu và một số số liệu; số liệu trong báo cáo lấy từ hình PDF, không lấy máy móc từ OCR.
- Đã đọc hết `E16_deleted_history.txt`: toàn bộ chữ nguồn nằm trong tracked deletions, là lịch sử phát triển đề. Không coi là đề hiện hành, không dùng để tăng mức ưu tiên hay thống kê số đề. E19 là liên kết online, không truy cập.
- **Không mở ba file đáp án riêng**: `ĐA 2024.pdf`, `ĐA Đề A.pdf`, `_45_cau_ đáp án .docx`. Một số file đề/bài ôn tự chứa đáp án: đã gặp trong lúc đọc cả file nhưng không dùng đáp án đó làm chuẩn đúng/sai. Các điểm sai dưới đây được đối chiếu lý thuyết và tính lại.
- **E06 và E08 trùng toàn bộ 40 câu theo cùng thứ tự**, E06 có thêm đáp án xen kẽ; chỉ coi là **một bộ câu hỏi**. Nhiều câu E08/E10/E13/E14/E15/E20 cũng lặp nguyên văn/biến thể: không lấy số file chứa câu làm tần suất độc lập. E03 tự ghi là đề do BHT sưu tập/soạn lại và đáp án tham khảo, không tự nhận nó là đề gốc chính thức. E13/E14/E15 lần lượt là training/ngân hàng/bài ôn, không gọi là các năm thi.

## 2. Kết luận ưu tiên

**A = cần làm chắc trong tuần này**; **B = phải hiểu ngắn gọn để nối kiến thức và làm câu nhận biết**; **C = đọc sau khi A/B ổn, không dành nhiều thời gian nhớ chi tiết**. Đây là thứ tự học theo bằng chứng trong bộ file và quan hệ kiến thức, **không phải dự báo xác suất ra đề**.

| Phần của Ch1 | Mức | Cần hiểu/làm được | Lý thuyết chính | Bằng chứng câu hỏi |
|---|---|---|---|---|
| 1.1 Internet và giao thức | B, là bước mở đầu bắt buộc | Internet theo góc nhìn thành phần và dịch vụ; giao thức quy định khuôn dạng, thứ tự thông điệp và hành động; phân biệt hạ tầng/giao thức/ứng dụng | T1 tr3–7; E17 tr4–8 | E13 C1 tr3; E14 đoạn P37–41 (phát biểu sai về giao thức) |
| 1.2 Mạng biên, truy cập, vật lý | B; phần bit/byte và tốc độ nâng lên A | Host/client/server ở biên; access nối host đến edge router; phân biệt lõi. Phân loại hữu tuyến/vô tuyến, cable/DSL/Ethernet/WiFi/cellular ở mức nguyên lý. Đổi byte→bit, kbps/Mbps, km→m, s→ms | T1 tr9–23, đặc biệt tr20–23 | E03 C21 tr4; E10 C6 tr1; E13 C2 tr4; E01 C2–3 tr1; E02 C20 tr5–6 |
| 1.3 Mạng lõi | B nền tảng; store-and-forward gắn A | Router nối nhau; routing là chọn đường toàn cục, forwarding là thao tác cục bộ; nhận đủ gói rồi mới phát lên link kế tiếp; hàng đợi và loss khi buffer đầy; so sánh packet/circuit switching; hiểu FDM/TDM | T1 tr25–35; E17 tr22–29 | E13 C3 tr5, C4 tr6–7, C7 tr11; E14 P91–108; các bài delay nhiều link E01 C12 tr3, E02 C14 tr5 |
| 1.4 Hiệu suất | **A** | Phân biệt 4 loại delay; tính một gói qua 1/nhiều link; bottleneck và thông lượng khi chia sẻ; thời gian file dài theo thông lượng dưới giả định; số gói/giây; RTT hai chiều; giải thích mất gói/queue tăng | T1 tr46–56; công thức tr48,50,55–56. E17 tr39–46 nhưng có lỗi ở tr43–44 | E01 C2–3 tr1, C10,C12 tr3; E02 C14 tr5,C20 tr5–6; E03 C12 tr2; E08 C31 tr3; E10 C35 tr4; E20 C3–4 (trang1/2); bài ôn E15 Ch1 C4–8 tr2–3 |
| 1.5 Chồng giao thức | **A** | Thứ tự 5 tầng; chức năng và giao thức ví dụ; process↔process / host↔host / lân cận; message→segment→datagram/packet→frame→bit; đóng/mở gói; đọc sơ đồ host–switch–router–host. OSI chỉ thêm 2 tầng ở mức nhận biết | T1 tr58–67, đặc biệt tr62–67; E17 tr47–50 (OSI tr49) | E01 C4 tr1–2,C6 tr2,C13 tr3; E02 C4–5 tr2; E03 C26 tr4–5; E08 C1 tr1,C12,C21 tr2,C33 tr3,C36 tr4; E10 C1,C3,C7 tr1,C23,C25 tr3; E13 C5 tr8–9; E15 Ch1 C1,C3 tr2,C9 tr3–4 |

### 1.1 Internet và giao thức — B (15–20 phút)

Đầu ra: tự kể một ví dụ giao thức như chào hỏi hoặc HTTP, chỉ ra **thông điệp nào, gửi theo thứ tự nào, bên nhận làm gì**. Vẽ một đường host → mạng truy cập → router/ISP → mạng truy cập → host. Giải thích Internet là mạng của các mạng. Biết RFC/IETF ở mức nhận diện, không cần học lịch sử/tên hãng.

### 1.2 Mạng biên — B, đơn vị A (20–25 phút)

Chia hai tiểu phần: (a) host, mạng truy cập và phương tiện vật lý; (b) độ dài gói L và tốc độ link R. Ưu tiên phân biệt **R (bit/s)** với tốc độ lan truyền **s (m/s)**. Không dành thời gian học thuộc mọi con số tốc độ WiFi, DSL, 4G/5G trong slide; đây là ví dụ của slide và không phải tốc độ chung của mọi công nghệ. Biết cáp quang, đồng trục, xoắn đôi là hữu tuyến/có hướng; radio là vô tuyến/vô hướng.

### 1.3 Mạng lõi — B và nền bài tính A (25–30 phút)

Chia ba tiểu phần: (a) routing/forwarding và store-and-forward; (b) packet/circuit, FDM/TDM; (c) cấu trúc ISP/peering/IXP/content provider. Với (a), vẽ dòng thời gian gói được phát qua **hai link**, để tránh cộng thông lượng hoặc bỏ lần truyền thứ hai. Với (b), dùng bảng hai cột: dành riêng/chia sẻ, cần thiết lập kênh, tài nguyên lúc im lặng, đảm bảo tài nguyên, queue/loss; không kết luận packet switching luôn nhanh hơn hoặc không tắc nghẽn. Với (c), chỉ cần một sơ đồ kết nối; tên ISP cụ thể và phép tính xác suất nhị thức tr34 để C.

### 1.5 Chồng giao thức — A (35–40 phút)

Học sau tổng quan biên/lõi, trước khi sang Ch2/Ch3. Tự dựng bảng 5 hàng từ trí nhớ: tầng, nhiệm vụ, đơn vị dữ liệu, giao thức ví dụ. Dùng T1 tr67/E17 tr50 để giải thích vì sao trong mô hình chuyển tiếp cơ bản switch xét đến tầng liên kết còn router xét tầng mạng; host có đủ năm tầng. Tầng trên **sử dụng dịch vụ** tầng dưới, không đồng nghĩa tầng trên điều khiển cách cài đặt bên trong tầng dưới. OSI cần biết thứ tự 7 tầng và presentation/session không hiện thành hai tầng riêng trong chồng 5 tầng đang học; không sa vào bộ câu chức năng OSI thiếu chặt chẽ của E16.

### 1.4 Hiệu suất — A (60–75 phút gồm bài tập)

Chia bốn tiểu phần: (a) đơn vị và dtrans/dprop; (b) nhiều link/store-and-forward, thêm processing/queue nếu được cho; (c) throughput/bottleneck/chia sẻ; (d) queue/loss/RTT. Phải làm được ít nhất một bài mới mỗi nhóm (a),(b),(c), và giải thích lý do chọn công thức.

## 3. Công thức đúng phạm vi và bẫy

1. `d_trans = L/R`: L là **bit**, R là **bit/s**. Với 2000 bytes và 2 Mbps: `16000/(2×10^6)=0.008s=8ms` (E10 C35; E20 C3 chọn đáp án khác). `1 byte=8 bits`; Mbps trong các ví dụ dùng hệ thập phân 10^6, không tự đổi thành MiB.
2. `d_prop=d/s`: d là mét, s là m/s. R tăng không làm s tăng; gói dài hơn không làm thời gian lan truyền d/s tăng. E03 C12: `1500×8/(2×10^6)+2000×1000/(2×10^8)=0.016s`; lựa chọn D (khác), không phải 0.011s.
3. Một gói store-and-forward qua n link, không có queue và bỏ processing: `d_e2e = Σ(L/R_i)+Σ(d_i/s_i)`. Nếu đề cho processing ở router, cộng đúng số lần router xử lý. Không thay Σ(L/R_i) bằng L/min(R_i) cho **một gói**. E01 C12 ảnh: L=12000 bit, R=(100,10,10) Mbps, d=(3,500,2)km, s=3×10^8 ⇒ `4.203333…ms`. E02 C14 ảnh: L=16000bit, R=(100,100,10)Mbps, d=(5,500,3)km ⇒ `3.613333…ms`, xấp xỉ lựa chọn 0.0036s.
4. Thông lượng một luồng trên đường nối tiếp không có lưu lượng cạnh tranh, xét giới hạn link: `T≤min R_i`, mô hình đơn giản lấy `T=min R_i`. Cộng băng thông hay trung bình băng thông là sai. Với n luồng chia sẻ **công bằng** link R: `T=min(R_s,R_c,R/n)` trong mô hình slide. Nếu không có điều kiện công bằng/luồng giống nhau, không tự chia đều.
5. `t_file≈F/T` là cách tính file dài trong mô hình bỏ overhead và hiệu ứng khởi động/pipeline, không phải công thức độ trễ mọi tình huống; E13 C6 tr10 và E15 Ch1 C7–8 thiếu rõ packetization nên nên ghi giả định khi dùng. Không cộng thời gian truyền nguyên file lên từng link theo tuần tự nếu bài đang hỏi thông lượng file có pipeline.
6. Số gói tối đa trên một link trong t giây, bỏ overhead và chỉ tính phát lên link: `floor(Rt/L)`. E01 C2/E02 C20: 1000Kbps,1000bytes,1s ⇒ 125 gói. Không chia Mbps trực tiếp cho bytes.
7. TDM m người chia đều: tốc độ mỗi kênh `R/m`, thời gian gửi `L/(R/m)+t_setup` theo mô hình bài E13 C7 tr11. Không bỏ thời gian thiết lập.
8. `d_nodal=d_proc+d_queue+d_trans+d_prop`. Cường độ `La/R` (a gói/s) dùng so sánh tải đến/tốc độ phục vụ; queue phụ thuộc tải và biến thiên đến. Slide nói queue vô hạn là mô hình bộ đệm vô hạn/quá tải kéo dài; buffer hữu hạn ngoài thực tế gây mất gói. Không có một loại delay luôn lớn nhất trong mọi mạng.
9. RTT là **thời gian đi rồi quay lại**; không mặc định là dprop một chiều hay toàn bộ thời gian tải file. Đây là cầu nối cho HTTP/timeout TCP.
10. Encapsulation: message được bổ sung header transport→segment; network→datagram; link→frame. Hình slide lược bỏ trailer của một số giao thức liên kết. Tầng vật lý truyền bit; tránh học câu “mọi tầng đều thêm header” như một định luật tuyệt đối.

## 4. Nội dung hoãn/ngoài phạm vi

- **C trong Ch1**: nhớ toàn bộ con số tốc độ/độ phủ của access media; tên từng nhà cung cấp ISP, lịch sử; tự suy ra xác suất nhị thức 35 user ở T1tr34; phân tích sâu kết quả traceroute (tr51–52). Vẫn biết traceroute/ping liên quan đo RTT/đường đi ở mức nhận diện (E13 C9 tr14).
- **Ngoài ba chương người dùng đã nêu**: E14 từ P386 trở đi có nhiều bài IPv4/subnet/VLSM, địa chỉ mạng/host/multicast, longest prefix, chi tiết IP/TTL/NAT/fragmentation, distance vector/link state, RIP/OSPF/BGP, rồi MAC/ARP/switch learning/CSMA/Aloha/token/CRC/Manchester. Một số từ như IP, Ethernet, router chỉ cần nhận diện trong Ch1; không vì thấy chữ đó mà kéo toàn bộ thuật toán/chia subnet vào lịch một tuần. E14 phần P799–819 mã hóa vật lý cũng ngoài phạm vi. Chương 1 không yêu cầu học các bài này.
- E15 Ch1 C13 (đổi nhị phân–thập phân) là kỹ năng hỗ trợ, làm ngắn; E15 các chương 2–3 chủ yếu thuộc phạm vi nhưng socket code/P2P chuyên sâu cần root xác định theo đề cương. Không tự gọi mọi phần của ngân hàng là nội dung giữa kỳ hiện tại.

## 5. Điểm sai hoặc mơ hồ phải ghi chú, không học vẹt đáp án

1. **E17 tr43, lỗi số học xác nhận bằng hình**: `8000/(10×10^6)=8×10^-4s`, slide ghi `10^-4s`. Với R=(100,1000,10)Mbps,d=(3,500,3)km,s=3×10^8, tổng đúng `0.0025746667s≈2.575ms`; slide ghi1.875ms. Tr42 gọi “độ trễ truyền:100Mbps” cũng sai loại đại lượng: Mbps là tốc độ truyền.
2. **E17 tr44, định nghĩa/cách tính throughput quá rộng**: min capacity chỉ đúng mô hình không cạnh tranh tương ứng; câu “link nào hiệu suất cao nhất thì tốc độ truyền link là thông lượng” không đủ điều kiện để dùng. Dùng T1 tr54–56 và nêu giả định. E17 tr46 `H2=T/(R/4)=2/3` là tỷ lệ sử dụng **phần chia của một luồng**, còn tổng tải trên link dùng bốn luồng phải viết `4T/R=2/3`; không lẫn với tải một luồng/TổngR=1/6.
3. **E15 Ch1 C12/PDFtr4**: từ đúng số liệu, `dprop=420000/(2.9×10^8)=1.44827586ms`, `R=6000/(1.47ms−dprop)≈276.190476Mbps`, không khớp bốn lựa chọn. Lời giải làm tròn1.448… thành1.44ms trước phép trừ nhỏ rồi ra200Mbps gây sai lệch lớn. Đã kiểm bằng hình; loại câu này khỏi bài chấm đúng/sai.
4. **E15 Ch1 C10/PDFtr4**: cả Byte/s,bit/s,Byte/phút,bit/phút đều là đơn vị lượng dữ liệu/thời gian; bit/s là đơn vị thường dùng của môn. Không lấy câu này để kết luận những đơn vị còn lại không đo được throughput.
5. **E15 Ch1 C2/PDFtr2** hỏi nguyên nhân phổ biến nhất gây chậm trễ mà chỉ có hình minh họa bốn nguồn, thiếu thông số/ngữ cảnh; không có cơ sở chắc chọn loại delay luôn lớn nhất. Đáp án xen kẽ không dùng làm chuẩn.
6. **E03 C26 tr4–5/E13 C5 tr8** nói “mỗi tầng thêm header” giản lược. T1tr62 nói physical truyền bit; các hình đóng gói tr63–67 vẽ header cụ thể cho transport/network/link. Học cơ chế và giới hạn câu chữ.
7. **T1tr34** ghi xác suất >10 người hoạt động “nhỏ hơn0.0004” khi35 người độc lập,p=0.1. Tính nhị thức ra `0.0004242976`, gần0.0004 nhưng không nhỏ hơn nó. Chi tiết này để C; không dùng con số bất đẳng thức đó làm bài học chuẩn.
8. T1tr54 ghi thông lượng là sốbit trong khoảngthời gian; cần diễn đạt rõ **tốc độ sốbit/đơn vịthời gian**, theo đơn vịbit/s của hình minh họa.
9. Một số câu ngân hàng có số lựa chọn không đủ chặt (ví dụ “độc lập giao thức” và môđun hóa phụ thuộc nghĩa của independent). Học rằng tầng trên dùng dịch vụ tầng dưới nhưng việc thay triển khai có thể trong suốt khi giao diện/dịch vụ được giữ; không biến thành khẩu hiệu mọi giao thức độc lập hay hoàn toàn không độc lập.

## 6. Phân bổ cho người mới 2–3h/ngày trong7ngày

Đề xuất **khoảng3–3.5 giờ tổng cho Ch1**, tách buổi để không đọc dồn toàn bộ slide. Ch1 ngắn hơn Ch2/3 nhưng phải đứng đầu vì tạo nền socket, TCP/IP và RTT.

- Ngày1: 150phút học thực: 20phút Internet+biên;25phút core;35phút chồng tầng;50phút hiệu suất và3bài;20phút tự nhớ lại/làm6–8câu. Nếu chỉ120phút, chuyển30phút bài hiệu suất sang đầuNgày2; nếu180phút thêm30phút sửa bài. Nghỉ ngắn nằm ngoài thời gian học hoặc được root cộng rõ trong lịch tổng.
- ĐầuNgày2:20–30phút làm lại một bài delay3link và một bài throughput, tự dựng bảng5tầng. Khi tính còn sai đơn vị, làm thêm ví dụ ngắn trước khi chuyển sang HTTP.
- Ngày4/Ngày6: mỗi ngày10–15phút truy hồi8khái niệm/công thức, sửa nhật ký lỗi; không đọc lại cả69slide.
- Ngày7: lấy các câu Ch1 của một bộ đề trong lượt thi thử chung (không thêm bộ trùng); xem lại câu sai bằng trang lý thuyết.

Ngưỡng chuyển chương: không cần thuộc hết C. Cần tự giải đúng ít nhất một bài dtrans+dprop một link, một bài ba link, một bài bottleneck; viết đủ5tầng và PDU; phân biệt host/process/lân cận; kể được routing/forwarding và packet/circuit. Khi chưa đạt phần nào, dành phần thời gian tùy chọn ngày tiếp theo để vá đúng phần đó.

## 7. Bộ câu gợi ý có kiểm tra được

- Cơ bản, không trùng: E01 C2,C3,C10,C12,C13; E02 C4,C5,C14 (C20 trùng dạng E01C2); E03 C12,C21,C26; E10 C35; E20 C4. Các câu này đủ cả sơ đồ, định nghĩa, tính toán, tránh chỉ nhớ chữ.
- Bổ sung khái niệm: E13 C1–5,C7–9 (phân biệt đây là training). E08 C1,C12,C21,C33,C36 để nhớ tầng/giao thức; E06 là bản trùng nên không làm thêm để đếm thành tiến bộ mới.
- Chưa chắc/không chấm đáp án: E15 Ch1 C2,C10,C12 như mục5; E14 không có số câu, trích theo câu dẫn và đoạnP để không bịa số câu. Bài E13C6/E15C7–8 phải nói giả định file dài và pipeline.

Ảnh render phục vụ kiểm tra nằm riêng trong `tmp/study_audit`; nguồn không bị sửa. Script đọc/render riêng: `ch1_render.py`.
