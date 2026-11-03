# Mốc ôn thi — 03/11/2026

**Tự kiểm U ngày03/11:** câu tự soạn stop-and-wait đã trả lời đúng kết quả16,67%; đã chữa phép tính (truyền8ms, chu kỳ48ms). User chưa trình bày cách tính; không suy thành thạo, không đổi9/9chặng Ch3. Không còn câu U đang chờ.

**Đề D19/E01:** đã cung cấp key tự giải30câu, kiểm đủ6ảnh và rà độc lập ngày03/11; chưa có bài làm của user, chưa chấm/đổi tiến độ. C4 hỏi không thuộcTCP/IP→A; C9A(100,120,120),C12A(4,203333ms),C20D(tuần tự),C21C(checksumB53D).

**Lịch thi đã xác nhận:** NMMMT ngày 03/11/2026, 9h30–11h. Ngày 02/11 rảnh cả ngày; ôn chính sau 12h30, buổi sáng chỉ ôn nhẹ tùy chọn. Việc lên lịch không thay đổi tiến độ học bên dưới.

Lịch gợi ý 02/11, **chưa thực hiện**: 13h–13h45 ôn trọng tâm; nghỉ 15 phút; 14h–15h05 làm D25 C1–30; 19h–19h55 chữa đề và bù kiến thức chưa kiểm. Tổng 3 giờ gồm nghỉ; chia block lớn theo yêu cầu, có làm đề riêng.

Gợi ý sáng03/11 trước thi9h30 (**chưa chốt/chưa thực hiện**, theo câu hỏi cókhoảng2giờ): tính giờdi chuyểnthựctếtrước/nhắmtới khoảng9h hoặc theo thôngbáothi. Khối45phútCh2ưu tiênHTTPnhiềuobject/persistent–pipeline/cache304,cổngvàC17cúpháp-ngữnghĩa;nghỉ10phút;khối35phút tựnhớ/tínhlỗicũCh1+TCP(đơnvị,trễtừnglink,MSS/UDPLength,rwnd,haichiềuSeq);30phútđệmcòn lạikhôngmặcđịnhđủđilại,rútônnếucần. Khônglàmđềdài/mởchủđềmới/ônlạisơđồFINdài;chưacóbằngchứngD25đãlàm. Đãcósubagentràđộclậpkhungônsáng;khôngđặtnhắclịch/đổitiếnđộ.

**Đã bổ sung tính DevRTT/TimeoutInterval vào [file riêng](output/ESTIMATED_RTT.md) theo yêu cầu ngày02/11**, có2lần tínhmẫu/quyướcrõE_cũtheoRFCbổsung vàso sánhE_mới. Slide11khôngnêurõcũ/mới,khônggánquyướccủaví dụchocô. C4–5trongfilechưađưa/chưatrảlời;userchưa xácnhậnđọc/hiểu,khôngđặtcâuhỏimớitrongchat. EstimatedRTTC1–3đãchữa2/3đúng(C1=84,C2=85,2;C3bỏmẫutruyền lạiđãsửa/chưaxácnhậnhiểu);phânbiệtE/timerđãgiảithích. TCPcơsởđãônxong/FIN10/10;giữ9/9chặng,khôngsuythànhthạo. Congestionngoàithi. Ch2C17đánhdấu/C21–30chưađưa;Ch1C13đãgiảithích/chưachọn.

- **Chương 3: 9/9 chặng = 100% nội dung đã học/tự kiểm/chữa**, bước14–22; không phải thành thạo. Phạmvi cơsởhếtT3cũtr94;congestion/QUICngoàithi. EstimatedRTTbước24tựkiểm/chữa2/3đúng,cầngiữđiểmbỏmẫutruyền lại;DevRTT/TimeoutIntervalđãcóbàihọc/ví dụtrongfile,userchưalàmtựkiểm. Khôngtínhthêmchặngcơsở.
- **Đề mẫu cô15câu:**10đúng/14đãlàm theo ý hỏiC12A; sai2,6,10,11 đãchữa. C2A/C10B/C12A được user xác nhận; C12cólỗitênởD, C15chưa chọn/ngoài phạmvi hiện hành. [Báo cáo và lỗ hổng](output/CHUA_DE_MAU_CO_20261030.md); khônggộpvào172câu.
- **Điểm cần ôn:** HTTP nhiềuobject/304/ghépURL,UDP Length; MSS/header,ACK vớiappđọc,rwnd vàhai chiềuSeqACK. Đã bổ sung IMAPTCP143/tênMessage,FTPcontrol/data vàbảngcổng; không tự coi phần mới đã thành thạo.
- **Chương 2: 8/8 chặng cơ sở = 100%**, bước6–13, không phải thành thạo. Bộ80: C1–20 đã trả lời/chữa, nhiều ý còn thiếu/đã sửa; C17 được đánh dấu ôn lại, chưa xác nhận hiểu. C21–30 chưa đưa; không tự chấm đạt toàn bộ C11–20.
- **Chương 1:** đã tổng ôn/làm8câu trước; bộ20câu ngày01/11 đúng19/19câu đã chọn,C13 chưa chọn/đã giải thích. Chưa có cách tính tự trình bày, chưa xác nhận nắm gỡ/đóng gói ở router; không suy thành thạo toàn chương. Giữ điểm yếu cũ để kiểm tra vận dụng sau.

Phần trăm tính theo các chặng nội dung có trọng số bằng nhau đã học/tự kiểm/chữa, **không phải mức thành thạo**. Chi tiết câu trả lời và điểm cần củng cố được giữ trong nhật ký chương.

## Chỉ mở phần liên quan

- [Tính năng các giao thức](output/TINH_NANG_CAC_GIAO_THUC_NMMMT.md): bảng HTTP/FTP/mail/DNS/Telnet, TCP–UDP, RDT, GBN–SR và các điểm dễ nhầm; tạo theo yêu cầu03/11, không đổi tiến độ.

- E02/D20 đã được cung cấp key tự giải, chưa có bằng chứng user làm cả đề. Đang làm rõ C19 (timeout không xác định nguyên nhân lỗi) và C9 (gói đến/chấp nhận/buffer, quy ước ACK); chi tiết ở nhật ký Ch3, không đổi tiến độ.

- [Tổng hợp kiến thức ba chương](output/TONG_HOP_KIEN_THUC_NMMMT_3_CHUONG.md): mỗi mục1–2câu, có công thức/điều kiện và phạm vi TCP đếntr94; tài liệu tra nhanh, không phải xác nhận thành thạo. Đã ghi bản Obsidian theo yêu cầu vào [MMT.md](<D:/The Great Root/Obsidian/my-notes/content/Ôn thi/MMT.md>).
- [Chương 1](memory/chuong-1.md): lịch sử học, kết quả tổng ôn và chỗ cần sửa.
- [Chương 2](memory/chuong-2.md): mốc tạm dừng, kết quả C1–10, lưu ý chấm và lịch sử từng chủ đề.
- [Chương 3](memory/chuong-3.md): mốc ôn, kết quả bước14–22, TCP/flow/connection, SR/GBN/RDT/checksum và IP/port.
- [Thứ tự học](output/THU_TU_HOC_NMMMT.md): tra bước đang học và trang lý thuyết tương ứng.
- [Nguồn và lịch sử](memory/nguon-va-lich-su.md): phạm vi đề, kiểm kê, review và bản lưu tiến độ cũ; chỉ đọc khi cần đối chiếu.

Quy tắc đọc và cập nhật: [AGENTS.md](AGENTS.md). Đây là nơi duy nhất ghi mốc hiện tại; các mốc trong nhật ký là lịch sử tại thời điểm ghi.
