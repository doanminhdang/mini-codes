**Cách dùng công cụ này:

*Đặt tất cả các file dữ liệu đầu vào ở thư mục con có tên scopus_data


*Chạy file get_authors.py (trên nền tảng Python 3), nó sẽ đọc tất cả các file trong scopus_data và xuất ra file list_all_authors.csv

  Cấu trúc của list_all_authors.csv có các cột:
  
  Tên tác giả
  
  Số lượng affiliations trong các bài của tác giả này
  
  Các affiliations của tác giả này (phân cách bằng dấu chấm phẩy)

*Chạy file get_papers.py, nó sẽ đọc tất cả các file trong scopus_data và xuất ra file list_papers.csv

  Cấu trúc của list_papers.csv có các cột:
  
  ID (số thứ tự trong danh sách)
  
  Tên bài báo (nếu có nhiều bài báo trùng tên, hoặc một bài được liệt kê ở nhiều chỗ, thì chỉ lọc giữ lại một bài)
  
  Tên các tác giả (TODO: xét trường hợp một tác giả có thể được liệt kê với cách viết tên khác nhau)
  
  Tên tạp chí
  
  Tên nhà xuất bản
  
  Năm xuất bản
  
  Địa chỉ DOI
  
*Chạy file get_references.py, nó sẽ đọc một lần nữa tất cả các file trong scopus_data cùng với file list_papers.csv và xuất ra file list_references.csv.

  Cấu trúc của list_references.csv có các cột:
  
  ID (trùng với ID trong file list_papers.csv)
  
  Tổng số references của bài này
  
  Số lượng references nằm ngoài danh mục các bài đã thu thập được trong file list_papers.csv
  
  Số lượng references nằm trong danh mục các bài đã thu thập được trong file list_papers.csv
  
  Số lượng references trong danh mục ở file list_papers.csv mà có trùng ít nhất 1 tác giả với bài này (self cite)
  
  Danh sách các bài nằm trong list_papers.csv mà bài này đã cite (liệt kê chuỗi các ID, ngăn cách bằng dấu phẩy, e.g. 2, 15, 40)
  
  và các cột còn lại trong file list_papers.csv (từ Tên bài báo, đến Địa chỉ DOI)
  
*Chạy file get_citations.csv, nó sẽ đọc file list_references.csv và xuất ra file list_citations.csv

  Cấu trúc của list_citations.csv có các cột:
  
  ID (trùng với ID trong file list_papers.csv)
  
  Tổng số citations của bài này, xét trong phạm vi danh mục các bài đã thu thập được trong file list_papers.csv
  
  Danh sách các bài nằm trong list_papers.csv đã cite bài này (liệt kê chuỗi các ID, ngăn cách bằng dấu phẩy, e.g. 6, 8, 9)
  
  và các cột còn lại trong file list_papers.csv (từ Tên bài báo, đến Địa chỉ DOI)
  
*Tạo một file input_net_authors.txt để liệt kê nhóm tác giả cần phân tích references, mà mỗi dòng là tên của một tác giả.
  
*Chạy file count_references.py, nó sẽ đọc file list_references.csv và file input_net_authors.txt rồi xuất ra file references_net.csv

  Cấu trúc của references_net.csv có các cột (liệt kê theo từng tác giả):
  
  ID (ứng với số hàng ghi tên tác giả trong file input_net_authors.txt)
  
  Tên tác giả
  
  Tổng số bài của tác giả này trong danh mục đã thu thập ở file list_papers.csv
  
  Số lượng các bài của tác giả này mà có cite bài của ít nhất một người trong danh sách tác giả được liệt kê ở input_net_authors.txt
  
  Số lượng các bài của tác giả này nhận được citations từ bất kỳ tác giả nào khác trong danh sách ở input_net_authors.txt (kể cả họ là đồng tác giả với mình)
  
  Tổng số references trong các bài của tác giả này
  
  Số lượng references trong các bài của tác giả này do một trong những người ở input_net_authors.txt là đồng tác giả (self cite + ring cite)
  
  Tổng số citations mà các bài của tác giả này nhận được từ bài của những người nằm trong danh sách input_net_authors.txt
  
  Các cột cho biết số references (hay citations) mà các bài của tác giả này dành cho từng người trong danh sách tác giả ở input_net_authors.txt (khi mở trong Excel, phần các cột này tạo thành ma trận vuông).
  
