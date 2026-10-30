# Nguồn và phạm vi ôn Hệ điều hành

## Tài liệu gốc

| Mã | Tệp trong `Lý thuyết/` | Số trang/slide | Bản đọc trong `Lý thuyết/pdf/` |
|---|---|---:|---|
| C01 | `[BHT CNPM] HDH _Chuong1.pdf` | 57 trang PDF | C01.md, C01-index.md, C01-manifest.json |
| W01 | `#Week01-Chapter0 2024.pptx` | 9 slide | W01.md |
| W02 | `#Week02-Chapter2 2024.pptx` | 57 slide | W02.md |
| W03 | `#Week03-Chapter3 2024.pptx` | 64 slide | W03.md |
| W04 | `#Week04-Chapter4-1 2024.pptx` | 74 slide | W04.md |
| W05 | `#Week05-Chapter4-2 2024.pptx` | 59 slide | W05.md |

W01 là Chương 0 giới thiệu môn, không thay Chương 1. C01 được người dùng thêm ngày 30/10/2026. Số slide theo thứ tự trình chiếu trong PPTX, số trang PDF từ 1. Số mục LMS có thể khác số đề mục in trong nguồn.

## Cấu trúc người dùng chỉ định

Ảnh giữ tại `memory/anh-cau-truc/`: `chuong-1.png`, `chuong-2.png`, `chuong-3-tong-quan.png`, `chuong-3-phan-1.png`, `chuong-3-phan-2.png`, `chuong-4.png`. Danh mục đã ghi lại ở `output/THU_TU_HOC_HDH.md` và README từng chương, không cần đọc lại ảnh mỗi lần.

Ch3 dùng ảnh chi tiết: 3.1–3.4, 3.5.1–3.5.3, 3.6 IPC, 3.7 tiểu trình; phần cộng tác nằm cùng ngữ cảnh IPC, không tự đánh thành mục 3.6 rồi đẩy số IPC/tiểu trình lên. Nhãn Done/To do trên ảnh không phải kết quả tự kiểm tại đây.

## Phạm vi

- Hiện soạn bài Ch1–2. Ch3–4 có nguồn và mục lục để dùng sau, chưa tự giảng/soạn toàn bộ.
- W05 tạm dùng slide 1–28 theo lời người dùng “hình như chỉ tới slide 28”. Slide 29 thực tế ghi “ĐỊNH THỜI THEO THỜI GIAN THỰC (ĐỌC THÊM)”. Từ 29–59 giữ cache để tra, không đưa vào học/tự kiểm/% cơ sở khi chưa đổi phạm vi. Ảnh mục lục Ch4 có thời gian thực/định thời trên một số OS không tự hủy giới hạn này.
- Ch1 1.2 mở rộng tách riêng theo LMS; chưa có xác nhận không thi.
- Chưa có bộ đề đầy đủ được chọn/thống kê. Ảnh `Giữa Kỳ/User/vi-du-tu-luan-mot-tu.png` chỉ là ví dụ định dạng: một số hoặc một từ tiếng Anh; chữ viết tay chưa là đáp án chính thức.

## Cache và đối chiếu đã có

Extraction do GPT‑6.1 Terra thực hiện. PPTX có `index.md` và `manifest.json`; PDF C01 có chỉ mục/manifest riêng. Hash SHA256, size/mtime, fingerprint script và số trang/slide giúp tái dùng bản đọc. Chạy công cụ chỉ khi thiếu/đổi nguồn hoặc lỗi cụ thể; không tự chạy mỗi phiên. Script dùng Python, PDF cần pypdf. Đường dẫn nguồn mặc định lấy theo gốc thư mục chứa `tools/`.

- PPTX: giữ chữ, bảng theo hàng/cột; đánh dấu ảnh, ô gộp, nội dung nhúng và Office Math. Toán được giữ chữ phẳng, chưa bảo toàn cấu trúc phân số/lũy thừa; phải xem công thức gốc khi tính.
- C01: có chỗ chữ dính, tiêu đề tự động đôi khi lẫn copyright. Trang 26/29/38/49/57 ít chữ; các trang nhiều chữ vẫn có thể thiếu nhãn trong hình. Dùng mục lục bài ôn để định vị thay vì nạp cả cache.
- Đã kiểm hình C01 trang 22 (tháp lưu trữ), 26 (I/O), 29 (Von Neumann/DMA), 38 (dual-core), 39 (NUMA), 52–53 (user/kernel mode, mode bit). Nhãn còn thiếu trong trích chữ đã được dùng đúng trong bài soạn; tái dùng phần đó, chỉ mở nguồn khi có nghi vấn mới.
- C01 trang 27 nói DMA “không cần CPU”; đọc cùng hình 29, không học thành CPU hoàn toàn không tham gia. C01 trang 36 mô tả SMP khái quát; bài ôn tránh hiểu mọi CPU phải chạy cùng một công việc.
- W05 slide 28 chủ yếu hình processor affinity, cần xem gốc khi học hình. W04 slide 21/47 có Office Math; W04 các bảng bài tính đã giữ hàng/cột. Bản đọc không thay được sơ đồ/mũi tên.

Đã có rà soát độc lập cache, số trang/slide, mốc28/29 và bài soạn Ch1–2. Không cần rà/trích lại toàn bộ nếu chưa có thay đổi hay nghi vấn mới.
