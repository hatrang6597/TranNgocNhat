# Xây dựng ứng dụng chatbox trên nền tảng ứng dụng web

Chatbot không còn là xa lạ với thời đại ngày nay, sơ khai là một chương trình
nhỏ lưu trữ các mẫu cụ thể và xuất thông tin lại với người dùng những mẫu
cụ thể đó dựa trên những đầu vào và kết quả phân tích của lập trình viên
để đưa ra một câu trả lời hợp lý.

Ngày nay với nhiều ứng dụng như hỗ trợ khách hàng, tự động trả lời những
vấn đề trong việc học tập hay làm việc chúng ta có nhưng Chatbot hỗ trợ khách
hàng, Chatbot hỗ trợ học tập, Chatbot hỗ trợ việc tìm kiếm thông tin...

Trong quy mô ứng dụng Chatbot này chúng ta sẽ xây dựng một Chatbot từ cơ
bản đến nâng cao để hoàn thiện một Chatbot cơ bản phục vụ cho mục đích học
tập và nghiên cứu về sau để tùy biến dữ liệu tương thích với yêu cầu đặt
ra khi một yêu cầu nào đó muốn thỏa mãn điều người ta mong muốn

## Yêu cầu

Để có thể được đơn giản hóa tránh bị thông tin bị ngộp trong quá trình học
tập và nghiên cứu ứng dụng này chỉ cần nắm cơ bản về `python`, `HTML`,
`Javacscript`, `CSS` (*có thể không cần thiết vì nó chỉ hỗ trợ cho việc
giao diện dễ nhìn*)

Trong phần đầu tiên chúng ta sẽ sử dụng một Framework đơn giản và thịnh hành
là `Flask` để viết các điều khiển, `HTML` dùng để hiển thị cho người dùng
nhập dữ liệu vào cho Chatbot có dữ liệu để hoạt động.

## Cài đặt cơ bản

Như chúng ta đã đề cập ở trên thì chúng ta phải có tối thiểu là `python`
đã được cài đặt vì nó là một nền tảng để chạy những cái chúng ta sẽ làm.
Ngoài ra cũng nên yêu cầu phiên bản của `python` là từ phiên bản `3x` trở
lên. Tiếp đến là cài đặt Framework `Flask` dùng lệnh như sau

```bash
pip3 install Flask
```

## Bắt đầu nền tảng

Sau khi chúng ta cài đặt xong những thứ cơ bản thì chúng ta sẽ bắt đầu để
xây dựng hệ thống Chatbot giả sử chúng ta tạo một thư mục `Chatbot` nếu dùng
hệ điều hành `Windows` thì chúng ta có thể làm trực tiếp với giao diện, còn 
với hệ điều hành mã nguồn mở thì chúng ta sử dụng lệnh `mkdir Chatbot`
như vậy là chúng ta đã xong phần tạo thư mục chứa mã nguồn dự án `Chatbot`
của chúng ta.

Chúng ta sẽ bắt đầu tạo một tập tin `chatbot.py` đây là tập tin sẽ lưu trữ
mã nguồn chúng ta sẽ lập trình cho nó. Tập tin này được lưu trữ trong thư
mục `Chatbot` mà ta đã tạo trước đó. đây là mã nguồn đầu tiên của tập tin
`chatbot.py`

```python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask("app", template_folder="./")

app.config["DEBUG"] = True

@app.route('/')
def homepage():
    return render_template('chatbot.html');

if __name__ == "__main__":
    app.run('0.0.0.0', port=9090)

```

Ở đoạn mã trên chúng ta sẽ lần lượt tìm hiểu các chức năng và hàm của nó

Dòng đầu tiên `# -*- coding: utf-8 -*-` thông báo cho trình biên dịch `python`
hiểu là chúng ta sẽ viết mã nguồn có ký tự `utf-8` ví dụ như tiếng việt của
chúng ta chẳng hạn, nếu sử dụng tiếng anh thì không cần thiết khai báo dòng
này nhưng nên khai báo vì biết đâu trong quá trình chúng ta viết chúng ta
sẽ sử dụng như ký tự của các biểu tượng.

Dòng `from flask import Flask` và `from flask import render_template` là
hai dòng dùng để gọi Framework `Flask` và hàm để xuất giao diện cho chúng
ta `Flask` là một đối tượng còn `render_template` là một hàm được xây dựng
sẵn của Framework `Flask`

Dòng `app = Flask("app", template_folder="./")` là dòng khởi tạo đối tượng
`app` từ đối tượng `Flask` trong đó có hai tham trị được truyền vào là `app`
và `template_folder` là `./` với `app` là cái tên mà khi chúng ta xem tiến trình
sẽ hiện trong `taskmanager` của hệ điều hành. còn `template_folder` là khai
báo rằng Flask sẽ lấy các mẫu giao diện từ thư mục hiện tại chưa tập tin 
`chatbot.py`

Đoạn mã `app.config["DEBUG"] = True` là khai báo chúng ta đang viết và kiểm
thử mã nguồn nếu có lỗi thì sẽ hiện ra cho chúng ta để chúng ta tiến hành
chỉnh sửa và loại bỏ lỗi.

Đoạn mã tiếp theo

```python
@app.route('/')
def homepage():
    return render_template('chatbot.html');

```

Đoạn này sẽ khai báo cho ứng dụng khi người dùng đi vào trang chủ thì sẽ
tải mẫu giao diện `chatbot.html` để hiển thị cho người dùng thấy. Trong `python`
có một chức năng gọi hàm lồng nhau cho nên `@app.route('/')` chính là một
hàm được định nghĩa sẵn và sẽ gọi hàm `homepage` để chạy những mã lệnh chúng
ta viết ở trong hàm này.

Đoạn cuối cùng

```python
if __name__ == "__main__":
    app.run('0.0.0.0', port=9090)

```

Đây là đoạn mà ứng dụng sẽ bắt đầu chạy và chúng ta gọi hàm `run` của từ đối
tượng `Flask` với hai tham trị đơn giản đầu tiên `'0.0.0.0'` là `hostname`
ứng dụng sẽ chạy và `port=9090` là ứng dụng chạy trên cổng `9090` trong trường
hợp `hostname` là `0.0.0.0` thì ứng dụng sẽ lấy địa chỉ IP của máy.

Đến đây thì mã nguồn cơ bản đã hoàn thành nhưng chúng ta cần phải tạo một
mẫu giao diện để ứng dụng bắt đầu chạy và hiện thị, chúng ta sẽ bắt đầu
xây dựng mẫu giao diện `chatbot.html` như sau

```HTML
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Simple Chatbot</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {
    margin:0;
    padding:0;
    box-sizing:border-box;
    outline:none;
}
</style>
</head>
<body>
    <h1>Simple Chatbot</h1>
</body>
</html>

```

Chúng ta lưu nó vào thư mục `Chatbot` đã tạo vừa rồi sau khi chúng ta lưu
xong chúng ta dùng cửa sổ lệnh trong Windows là `cmd` còn trong hệ điều hành
mã nguồn mở là `terminal` gõ lệnh `python3 chatbot.py`

Sau khi chạy chúng ta sẽ có kết quả như sau

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.0.144:9090/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 583-830-554
```

Trong kết quả trên chúng ta thấy `Running on http://192.168.0.144:9090/` thì
có nghĩa là mã nguồn của chúng ta đã được chạy thành công tại địa chỉ IP
`192.168.0.144` với cổng `9090` và `192.168.0.144` cũng là địa chỉ `127.0.0.1`
là địa chỉ `localhost` chúng ta mở trình duyệt lên gõ vào `http://192.168.0.144:9090/`
hoặc `http://127.0.0.1:9090/` và chúng ta sẽ thấy kết quả là 

```
Simple Chatbot
```

Như vậy chúng ta đã hoàn thành bước cơ bản đầu tiên của công việc tạo một
nền tảng Chatbot của chúng ta. Chúng ta sẽ đi tới bước xây dựng giao diện
đơn giản cho Chatbot của chúng ta.