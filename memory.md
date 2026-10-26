# Memory

## Tiến độ học hiện tại — cập nhật 26/10/2026

- Hiện tại: Chương 2, bắt đầu Web/HTTP: đối tượng web, URL, request/response và cấu trúc thông điệp HTTP/1.1 (LT2 trang PDF 17–19, 25–26, 28 và 51).
- Tiến độ Chương 2 trước bài Web/HTTP: 1/8 chặng = 12,5%, tính mỗi chặng trọng số bằng nhau theo bước 6–13 trong `output/THU_TU_HOC_NMMMT.md`. Đã học chặng nguyên lý ứng dụng mạng; chặng Web/HTTP đang bắt đầu, chưa cộng vào số chặng hoàn thành. Đây là tỷ lệ chặng đã học, không phải tỷ lệ thành thạo hay thời gian học. Giữ cùng cách tính và báo tiến độ có % trước bài mới.
- Nội dung Chương 1 đã học: bốn loại độ trễ; trễ truyền `L/R` và trễ lan truyền `d/s`; cường độ lưu lượng `La/R`, hàng đợi và mất gói; độ trễ của một gói qua nhiều link theo store-and-forward.
- Đã học tới: thông lượng và nút thắt cổ chai (LT1 trang PDF 54–55). Người dùng trả lời đúng `min(8,3,10)=3Mbps`, nút thắt là link thứ hai; nâng liên kết 3Mbps lên6Mbps thì thông lượng mới6Mbps.
- Trong lượt tổng ôn: bổ sung chia sẻ công bằng đường truyền `min(R_s,R_c,R/n)` (LT1 trang PDF 56) và RTT là thời gian đi-về; tóm tắt Internet/giao thức, mạng biên/lõi, routing/forwarding, packet/circuit/FDM/TDM, 5 tầng/PDU/đóng gói/thiết bị, delay, queue/loss, throughput.
- Đã trả lời 8 câu tự kiểm tổng hợp. Câu2/3/5/7/8 đúng: routing/forwarding; packet/circuit và FDM/TDM; rho1.2 và quá tải/buffer đầy; chia sẻ4Mbps; RTT35ms. Câu1 nhớ đúng một phần nhưng thiếu thứ tự thông điệp; củng cố ba ý khuôn dạng–thứ tự–hành động. Câu4 nêu đúng5tầng/PDU (chấp nhận packet ở tầng mạng, slide dùng datagram), nhưng nhầm switch lớp2 và router cùng xử lý tới tầng mạng; người dùng yêu cầu giải thích lại. Câu6 trả lời6ms; sửa thành9ms:1500byte=12000bit, mỗi link d_trans=2ms và d_prop=1ms,3link tổng9ms. Không suy đoán chắc cách tính khi chưa có lời giải chi tiết.
- Nội dung Chương 1 cần ôn lại: định nghĩa giao thức (khuôn dạng–thứ tự–hành động), switch lớp 2 xử lý tới tầng liên kết/frame còn router tới tầng mạng/datagram, cộng đủ trễ lan truyền từng link. Chưa xác nhận thành thạo toàn bộ Chương 1.
- Đã học tới Chương 2: mô hình client–server và P2P; phân biệt host, process, socket; vai trò IP và port. Client khởi tạo liên lạc, server chờ; peer có thể vừa nhận vừa cung cấp tài nguyên. Socket là giao diện tiến trình với tầng vận chuyển.
- Đã trả lời 3 câu mở đầu Chương 2, nắm đúng ý chính. Cần dùng thuật ngữ chính xác: trình duyệt là client, phần mềm phục vụ web là server, trang web là nội dung; trong mô hình HTTP qua TCP, thiết lập TCP trước khi gửi GET, GET là yêu cầu HTTP. Peer có thể chia sẻ phần file đã có mà bên khác cần, chưa cần đủ file. IP xác định host đích trong mô hình, không chỉ host client; port giúp chọn điểm cuối dịch vụ trên host đó.
- Đang học tới: 4 nhu cầu ứng dụng (tin cậy, độ trễ, thông lượng, bảo mật); dịch vụ TCP/UDP cơ bản. TCP cung cấp truyền tin cậy, đúng thứ tự và có thiết lập kết nối; UDP không thiết lập kết nối và không tự bảo đảm giao đủ/đúng thứ tự. Cả hai không bảo đảm độ trễ hay thông lượng tối thiểu và không tự mã hóa; TLS bổ sung bảo mật trong mô hình bài học.
- Đã trả lời đúng cả 3 câu TCP/UDP: chọn TCP cho tải file cần đủ và đúng dữ liệu; UDP không bảo đảm độ trễ thấp, không cần thiết lập kết nối; TCP chưa tự mã hóa, cần bổ sung TLS theo mô hình bài học.
- Đang học tới câu hỏi “vì sao sinh ra UDP nếu có TCP”: TCP tự xử lý truyền lại và bảo đảm thứ tự luồng byte, có thể khiến dữ liệu sau phải chờ dữ liệu trước bị mất; ứng dụng thời gian thực có thể ưu tiên phần dữ liệu mới còn hữu ích. UDP không thiết lập kết nối ở tầng vận chuyển, không tự truyền lại hoặc giữ thứ tự; ứng dụng chủ động bổ sung cơ chế cần thiết. Ví dụ minh họa bằng mất một gói âm thanh trong cuộc gọi. Không khẳng định UDP luôn nhanh hơn hoặc bảo đảm độ trễ thấp.
- Người dùng đã liên hệ UDP với game esport và hiện tượng lag/skip khi mất gói. Đang làm rõ: nhiều game dùng UDP cho dữ liệu trận đấu, ưu tiên phản hồi kịp thời; game có thể tự bổ sung xác nhận/truyền lại cho thông điệp cần tin cậy. Nội suy và dự đoán có thể che mất ít gói; mất gói hoặc trễ/dao động trễ nặng có thể gây giật, đứng rồi nhảy hoặc hiệu chỉnh vị trí. Không suy ra mất một gói luôn nhìn thấy skip, không đồng nhất lag mạng với tụt FPS.
- Ví dụ game được đối chiếu bằng nguồn nhà phát triển: Riot, “Leveling Up Networking For A Multi-game Future” (https://www.riotgames.com/en/news/leveling-networking-multi-game-future); Valve, “Source Multiplayer Networking” (https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking) và GameNetworkingSockets (https://github.com/ValveSoftware/GameNetworkingSockets). Đây là ví dụ giải thích khái niệm, không thay đổi phạm vi nguồn đề thi.
- Đang học tới Web/HTTP phần đầu: trang web gồm HTML cơ bản và các object riêng; HTTP là giao thức tầng ứng dụng; mô hình HTTP/1.1 qua TCP dùng cổng mặc định 80. Request có method, đường dẫn, phiên bản và header Host; response có dòng trạng thái, header, dòng trống và body nếu có. Content-Length tính số byte body, không phải toàn thông điệp. Ví dụ minh họa response có body Hello gồm đúng 5 byte ASCII.
- Đang chờ 3 câu tự kiểm Web/HTTP: (1) HTML cơ bản và 3 ảnh riêng, tải đủ khi cache trống thì có bao nhiêu object; (2) đọc request `GET /logo.png HTTP/1.1` với `Host: study.example`, xác định method, đường dẫn, tên host và phiên bản; (3) `Content-Length: 2000` chỉ độ dài phần nào, đơn vị gì.
- Bài tiếp theo: các method HTTP và mã trạng thái, tiếp tục luyện đọc request/response để hoàn tất chặng Web/HTTP; sau đó cookie/cache theo lộ trình. Chưa xác nhận nắm chắc bài Web/HTTP vừa bắt đầu.
- Khi tiếp tục ôn, đọc `memory.md` và cập nhật mốc đã học/bài tiếp theo trong cả tệp này và `tmp/study_audit/README.md`.

## Yêu cầu và phạm vi cuối

- Đọc toàn bộ file đề thi trong `NMMMT`, chỉ dùng phần câu hỏi; không đọc các file đáp án riêng. Đọc tài liệu lý thuyết, phân loại trọng tâm và lập lịch học 7 ngày theo Chương 1, 2, 3 do người dùng nêu.
- Người dùng mới học, chưa nắm chắc, có 2-3 giờ/ngày (14-21 giờ/tuần).
- Người dùng đã bổ sung: không lấy nội dung từ đề thi online. Loại hoàn toàn các liên kết online, kể cả URL trong đề PDF/DOCX.
- Người dùng tiếp tục thu hẹp sang đề thi các năm, bỏ đề tự làm. Đã đồng ý dùng bản BHT sưu tập/soạn lại 2025-2026, sau đó chỉ định tính thêm hai PDF trong folder 2023 và 2024.
- Phạm vi cuối: E01 (2019-2020,30c), E02 (2020-2021,30c), E03 (2025-2026,30c), E08 (2023,40c), E10 (2024,42c), và T1/T2/T3. Không phải 170 câu: đúng là **172 lượt câu**. Có câu lặp giữa đề, không coi đây là 172 quan sát độc lập.
- Phải có subagent cho từng chương/phần phù hợp, đối chiếu bằng chứng; không tự bịa khi tài liệu thiếu hoặc không rõ.
- Tách dữ liệu tạm phục vụ extract và có `memory.md` (yêu cầu trực tiếp của người dùng).

## Tổ chức tệp

- Toàn bộ tệp liên quan được gom trong `NMMMT/` theo yêu cầu mới. Các đường dẫn tương đối bên dưới tính từ thư mục `NMMMT/`.
- Nguồn gốc: `Giữa Kỳ/` và `Lý thuyết/` (giữ nguyên).
- Script và trích xuất tạm: `tmp/study_audit/`.
- Script: `tmp/study_audit/extract_sources.py`.
- Manifest: `tmp/study_audit/manifest.json`.
- Phân loại từng câu: `tmp/study_audit/question_classification.json`.
- Giải thích dữ liệu tạm: `tmp/study_audit/README.md`.
- Kết quả: `output/KE_HOACH_ON_NMMMT_7_NGAY.md`, gồm chương/phần, A/B/C, trang lý thuyết, câu đối chiếu, lịch7ngày, lưu ý lỗi/mơ hồ và danh sách phân nhóm đủ172câu.
- Hướng dẫn thực hiện: `output/THU_TU_HOC_NMMMT.md`, tạo theo yêu cầu tiếp theo về thứ tự học cụ thể/chương/tóm tắt. Có 25 bước theo 7 ngày, trang PDF, mục tiêu tự kiểm; bước 24 EstimatedRTT là tùy chọn thêm giờ. Giữ nguyên phạm vi kế hoạch chính. Đã kiểm lại thứ tự Ch3 với subagent, trang UDP24-29/checksum30-34.

## Kiểm kê ban đầu

- Có 3 PDF lý thuyết riêng Chương 1-3 và một `slide nmm.pdf` cần nhận diện nội dung.
- Có đề thi PDF/DOCX, ngân hàng câu hỏi, tài liệu phát triển đề. File `LINK THI ONLINE 52 câu.docx` chỉ chứa URL, loại theo yêu cầu mới.
- Loại các file đáp án riêng: `ĐA 2024.pdf`, `ĐA Đề A.pdf`, `_45_cau_ đáp án .docx`.
- Chưa kết luận trọng tâm/tần suất cho tới khi đọc và đối chiếu đầy đủ. Không dùng tên file để khẳng định một tài liệu là đề chính thức.

## Môi trường

- Python bundle: `C:/Users/phuoc/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
- Có pypdf, pdfplumber, python-docx, PIL; chưa có fitz.
- Đã đọc skill PDF và tài liệu, dùng cho đọc nguồn; chưa tạo DOCX/PDF đầu ra.

## Tiến độ

- Đã trích xuất 3 PDF lý thuyết (69 + 105 + 109 trang), slide tổng hợp 238 trang, các đề PDF/DOCX. Manifest chứa đường dẫn, số trang, thống kê chữ/hình và SHA256.
- Ba agent `chuong_1`, `chuong_2`, `chuong_3` đã đọc đủ lý thuyết chương mình và toàn bộ câu hỏi của các đề giữ lại, đối chiếu ảnh, phân tích trong `ch1_analysis.md`, `ch2_analysis.md`, `ch3_analysis.md`. Đã yêu cầu các agent review bản tổng hợp theo chương độc lập.
- Đề scan E01 (2019-2020, 6 trang) và E02 (2020-2021, 7 trang) đã render bằng pypdfium2, OCR cục bộ Windows. OCR chỉ có en-US nên số liệu/hình được đối chiếu ảnh gốc. Ví dụ E01 C12 link 1 dài 3 km, OCR nhận nhầm 9 km.
- E06 DOCX và E08 PDF là cùng bộ 40 câu 2023; chỉ tính một bộ.
- E16 `Phát Triển Đề Thi...docx`: không có nút chữ hiện hành w:t, có 446 nút w:delText (Track Changes). Nội dung lịch sử được lưu riêng `E16_deleted_history.txt`, không dùng để nâng ưu tiên. Hai ảnh mail đã xem.
- E14 ngân hàng có nhiều câu ngoài Chương 1-3 (IP/subnet/routing/link/physical). Cụm đồ thị TCP P308-356 chỉ còn nhãn chữ/số, không có phần đồ thị trong gói DOCX; không suy đoán đáp án.
- Không có LibreOffice trong runtime bundle. Không dùng LibreOffice desktop của người dùng.
- Nguồn đề bị loại: E13 training, E14 ngân hàng, E15 bài tập ôn, E16 phát triển đề/lịch sử, E20 đề mẫu; E17 slide ôn không làm căn cứ cuối; E19 chỉ liên kết online. E06 trùng E08 không tính. Những nguồn từng đọc trước khi phạm vi đổi chỉ lưu ở tmp/archives, không tham gia bảng ưu tiên/luyện của bản cuối.
- Phân nhóm chính đủ172câu: Ch1=26, Ch2=75, Ch3=71. Đã kiểm chéo từng chương và tự động kiểm không thiếu/trùng chỉ số trong mỗi đề.
- Đã ghi lưu ý nội dung mơ hồ/sai trong LT2tr24, LT3tr78,88-89, D25C19,C26,C30 và D23C6/C17; không tự chấm mù bằng đáp án tham khảo.
- D20 C23 hỏi EstimatedRTT nhưng LT3 thiếu công thức chi tiết. Đã đối chiếu RFC6298 chính thức mục2.2-2.3: https://www.rfc-editor.org/rfc/rfc6298.html#section-2. Nêu rõ khởi tạo mẫu đầu, alpha của đề0.2 khác khuyến nghị1/8. Đã kiểm thêm NFS là giao thức tầng ứng dụng qua RFC2074 mục5.5.10 để đánh dấu D23 C21 có nhiều lựa chọn đúng: https://www.rfc-editor.org/rfc/rfc2074.html#section-5.5.10. Hai tham chiếu này chỉ kiểm kiến thức thiếu/mơ hồ, không lấy đề online hoặc tăng tần suất chủ đề.
- Lịch cơ sở14giờ gồm nghỉ:7ngày×(110phút học+10phút nghỉ), thêm tối đa60phút/ngày (tổngtốiđa21giờ). Quỹ khoảng Ch1=3h,Ch2=4h,Ch3=5h,tổnghợp=2h. Học nềnCh1 trước, rồiứngdụng,vậnchuyển,luyệnđề. D25 giữ cho lượt làm tổng hợp65phút ngày7.
- `tmp/study_audit/verify_final.py` đã chạy đạt: đủ172câu đúngmộtchươngchính/câu;8liênkếtnguồncục bộ hợp lệ;7ngày đúng110phúthọc;SHA256 của8nguồn được chọn giữ nguyên. Không sửa tệp nguồn.
- Đã hoàn tất review độc lập của cả ba agent: Ch1 xác nhận số câu/trang/công thức, sửa giới hạn OSI và bổ sung lỗi ký hiệu b/B; Ch2 xác nhận HTTP/DNS/mail và lịch; Ch3 xác nhận cơ chế, Seq/ACK, rwnd/cwnd và RTT, bổ sung giả thiết GBN và trang ví dụ Seq/ACK. Bản kế hoạch đã áp dụng các sửa cần thiết.
- Trạng thái: đã hoàn thành kế hoạch và các tệp người dùng yêu cầu; không còn câu hỏi phạm vi đang chờ.
- Học tương tác: người dùng đã yêu cầu bắt đầu ngày 1. Đang dạy khối đầu Ch1 (Internet/giao thức/mạng biên, LT1 tr3-7 và9-12), sau đó chờ trả lời câu tự kiểm trước khi chuyển mạng lõi. Chưa đánh dấu đã hiểu/hoàn thành ngày1; không suy ra trình độ từ việc đã gửi bài giảng. Câu tự kiểm trong hội thoại là kiểm tra hiểu khái niệm, không phải đề thi được tính vào nguồn.
- Ngày24/10/2026 người dùng yêu cầu tiếp tục từ đoạn học hiện tại. Tiếp tục Ngày1 phần2 Mạng lõi (LT1 tr25-35): routing/forwarding, chuyển mạch gói/store-and-forward, queue/loss, circuit switching và FDM/TDM. Đã kiểm nguồn/hình tr27-28 và có subagent review nội dung. Ví dụ minh họa từ LT1tr29:10kbit/100Mbps=0.1ms/link, một gói qua1router/2link cùngR,bỏpropagation/processing/queue thìbitcuốitớiđíchsau0.2ms. Chưa nhận câu trả lời tự kiểm phần1, không tự đánh dấu đã hiểu; phần2 sẽ chờ tự kiểm trước khi học chồng giao thức.
- Tự kiểm Ngày1 phần2: người dùng trả lời đúng routing/forwarding (câu1) và store-and-forward phải nhận đủ gói (câu2). Câu3 trả lời "đã bị mất" khi buffer vẫn còn chỗ, nên cần sửa nhầm lẫn queueing delay với packet loss. Đang giải thích: gói được lưu chờ truyền thì chưa mất; trong mô hình slide, bộ đệm hết chỗ khiến gói không được lưu và có thể bị drop. Chưa đánh dấu hiểu phần queue/loss hoặc hoàn thành phần2; dùng một câu phân biệt ngắn trước khi chuyển chồng tầng.
- Người dùng đã sửa câu tự kiểm: gói chờ5ms rồi được truyền thì không mất, nhưng gọi thời gian đó là "độ trễ lưu trữ". Đã xác nhận đúng ý và chỉnh tên thành "trễ hàng đợi (queueing delay)". Theo yêu cầu chuyển bài, bắt đầu Ngày1 phần3 Chồng giao thức (LT1tr58-67): thứ tự5tầng, dịch vụ, PDU, đóng/mởgói, host/switch/router trong môhìnhchuyểntiếp. Đã đọc đủ trang58-67 và xem hình67; chưa có câu trả lời tự kiểm phần3, chưa hoàn thành Ngày1. Không suy từ câu sửa này rằng đã kiểm đủ mọi nội dung FDM/TDM của phần2.
- Ngày23/10/2026, người dùng gửi `C:/Users/phuoc/Downloads/Chương 1 - Ôn tập.pdf` hỏi đủ ônCh1 chưa. Đã đọc và kiểm hình đủ7trang; dữ liệu tạm ở `tmp/review_friend_ch1/`. Kết luận: cókhung5mục nhưngchưađủ làmnguồnduy nhất. Lỗi tr6 d_queue=La/R (đúnglà cườngđộlưu lượngkhôngđơnvị); thiếuprocessing/tổngdelay, throughput/bottleneck, đóng/mởgói vàsơđồhost-switch-router; cầnđơnvị/bàitổnghợp/RTT. Báocáo `output/NHAN_XET_ON_TAP_CHUONG_1.md`. Không sửa PDF người dùng và không đổi phạmvi đề. Việc nhậnxéttàiliệukhông cónghĩa hoànthànhngày1.
- Đã chuyển các thư mục `output/`, `tmp/` và `memory.md` từ gốc workspace vào `NMMMT/`. Đã cập nhật đường dẫn extraction trong manifest và giới hạn script extract chỉ quét hai thư mục nguồn, tránh quét nhầm dữ liệu phát sinh. Gốc workspace chỉ còn thư mục `NMMMT/`.
- Ngày 24/10/2026, người dùng chỉ định tiếp tục Chương 1 từ phần 1.4 Hiệu suất (LT1 tr46-56). Bắt đầu bằng bốn loại độ trễ, tập trung phân biệt d_trans=L/R và d_prop=d/s, đổi đơn vị. Ví dụ minh họa tự soạn: L=1000 byte, R=2Mbps, khoảng cách 1000km, s=2e8 m/s; bỏ xử lý/hàng đợi thì d_trans=4ms, d_prop=5ms, tổng một chặng=9ms. Câu tự kiểm dự kiến: tăng R lên4Mbps, các dữ kiện khác giữ nguyên, tính lại hai độ trễ. Chưa nhận câu trả lời, chưa đánh dấu hiểu phần hiệu suất; còn học hàng đợi/mất gói, nhiều link, throughput/bottleneck và RTT theo tiến độ.
- Tiếp theo trong ngày 24/10/2026: người dùng yêu cầu bài tiếp theo và nhắc phải đọc memory; đã đọc lại toàn bộ memory.md trước khi tiếp tục. Chuyển sang trễ hàng đợi/mất gói và cường độ lưu lượng rho=La/R (LT1 tr46,50,53), có subagent kiểm tra. Nhấn mạnh rho không đơn vị, không phải d_queue; ví dụ L=1000byte,R=2Mbps,a=200gói/s =>rho0.8, khả năng phục vụ250gói/s. Khi a=300gói/s kéo dài, buffer hữu hạn sẽ đầy và mất gói. Chưa có câu trả lời tự kiểm về hiệu suất; không tự đánh dấu đã hiểu. Cần đọc memory.md trước các lượt tiếp tục ôn thi.
- Tự kiểm phần hàng đợi ngày24/10/2026: người dùng tính đúng rho=1.2>1 và giải thích quá tải kéo dài làm buffer hữu hạn đầy, dẫn tới packet loss. Đã xác nhận, làm rõ đây là hệ quả khi tải vượt khả năng phục vụ được duy trì. Chuyển sang một gói qua nhiều link theo store-and-forward, có subagent kiểm tra: A->R1->R2->B có3link; L1000byte,R2Mbps mỗi link, prop1ms/link, bỏprocqueue =>4ms truyền/link, nhận đủ tại R1/R2/B lần lượt5/10/15ms. Công thức tổng=sum(L/R_i+d_i/s_i) cho một gói. Tự kiểm mới: một gói1200byte qua2router, mỗi link4Mbps và prop0.5ms, bỏprocqueue; yêu cầu đếm link và tính tổng. Chưa có trả lời bài nhiều link, chưa đánh dấu hoàn tất hiệu suất; còn throughput/bottleneck và RTT.
- Tự kiểm nhiều link: người dùng trả lời 3link và1.5072ms. Đếm link đúng; thời gian sai, có vẻ lẫn giây với mili giây (chưa có lời giải chi tiết của người dùng). Đã sửa:1200byte=9600bit;9600/(4e6)=0.0024s=2.4ms/link; tổng3*(2.4+0.5)=8.7ms. Cần củng cố L/R trả về giây khi Lbit,Rbit/s và1s=1000ms; chưa xác nhận nắm chắc. Câu kiểm tra tiếp: giữ nguyên gói1200byte, tăngR lên8Mbps, hỏi d_trans mỗi link bằng bao nhiêu ms. Chưa chuyển sang throughput/RTT.
