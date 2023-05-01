Code còn gà mờ ạ. Một số chỗ có thể chưa tối ưu và một số chỗ thêm vào để nghịch :v

Mong ae đóng góp hỗ trợ <3

À còn nữa, câu ở description là của Suboi ợ

***Info về cách chơi:

The Game of Life được nghĩ ra bởi nhà toán học người Anh John H. Conway. Là trò chơi không người chơi, The Game of Life là một ví dụ khởi đầu cho về một vấn đề trong lĩnh vực toán học hiện đại được gọi là cellular automaton. Mô tả về cách chơi và một số quy ước được tham khảo từ quyển "Data Structures and Algorithms Using Python" của Rance D. Necaise.
1. Mô tả:
  Trò chời sử dụng một lưới vô hạn hình chữ nhật gồm các ô được đê trống hoặc đã bị chiếm bởi một sinh vật. Các ô bị chiếm sẽ được coi là sống và sẽ được kí hiệu là 1 còn các ô trống được coi là chết và được kí hiêu là 0. 
2. Quy ước (Luật chơi):
  - Nếu một ô đang sống có 2 hoặc 3 hàng xóm, thì ô đó sẽ sống tiếp trong thế hệ tiếp theo.
  - Nếu một ô đang sống không có hàng xóm hoặc chỉ có đúng 1 hàng xóm sẽ chết tiếp trong thế hệ tiếp theo.
  - Nếu một ô đang sống có 4 hàng xóm trở lên sẽ chết tiếp trong thế hệ tiếp theo bởi dân số quá đông.
  - Nếu một ô đang sống có đúng 3 hàng xóm đang sống sẽ được được trang bị giáp thiên thần và sống lại trong thế hệ tiếp theo
 * Hàng xóm là tám ô ngay xung quanh một ô: theo chiều dọc, chiều ngang và đường chéo. Ví dụ :
![hình ảnh_2023-05-01_230046806](https://user-images.githubusercontent.com/97423916/235483352-2ebaca47-cf0b-4042-a3f7-03d9cd535adf.png)

3. Thêm:
  - Trò chơi trên sẽ được thể hiện trong code bằng một mảng 2 chiều có phần tử có thể có giá trị 0 hoặc 1.
  - Việc thiết kế game thì game đuọc chia ra hai chế dộ chơi là Auto Mode và Type in Mode
    + Auto Mode các giá trị của phần tử trong mảng sẽ hoàn toàn ngẫu nhiên và kết thúc sau khoảng thời gian do người dùng nhập vào.
    + Type in Mode thì người dùng sẽ nhập giá trị 1 cho các phần tử mong muốn, là chế độ gần nhất với yêu cầu ban đầu của game
  - Size của lưới theo yêu cầu là vô hạn nhưng sức lực có hạn nên người dùng có thể tự do nhập kích thước lưới mong muốn.
