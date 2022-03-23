# Git và github cho người mới bắt đầu.

## Git là gì ?

**Git** là một mã nguồn mở dùng cho việc quản lý phiên bản của mã ngồn được
được phát triển vào năm 2005 cho tất cả các nhà phát triển nhân Linux.

So với một vài ứng dụng khác thì **Git** có ưu điểm nhiều hơn vì vậy **Git**
được chọn và phát triển ngày càng tối ưu hơn trong việc quản lý phiên bản
của mã nguồn.

## Git làm những gì ?

**Git** đơn giản chỉ quản lý những thay đổi của mã nguồn giúp cho lập trình
viên có thể kiểm soát mã nguồn, kiểm soát được quá trình viết mã nguồn của 
chính lập trình viên hoặc với các lập trình viên khác khi lập nhóm

Tất nhiên khi làm với nhóm thì **Git** phải có một mạng lưới có thể thông
qua mạng internet hoặc là dùng _USB_ chép qua chép lại cũng được.

**Git** dùng danh sách những nhật ký _commits_ để lưu giữ thông tin của thay
đổi bao gồm các tập tin được thay đổi, nội dung nhật ký thay đổi, thời gian
và thông tin của người chỉnh sửa mã nguồn.

Tại mỗi nhật ký _commit_ đã được lưu giữ nếu như quá trình kiểm thử có lỗi
thì chúng ta có thể tạo được một yêu cầu để chỉnh sửa và **Git** cũng dễ dàng
cho ta quay lại từ nhật ký đó để tiến hành chỉnh sửa mã nguồn cập nhật vá
lỗi cho ứng dụng.

## Github là gì ?

**Github** là một hệ thống dành cho người dùng sử dụng trực quan cũng như
tập trung các bản **Git** và dùng **Git** làm nền tảng bên dưới, cơ bản
**Github** hoạt động ở nền tảng bên dưới là những dòng lệnh cơ bản của **Git**
và phủ lên trên là một giao diện để người dùng có thể dễ dàng sử dụng **Git**
một các đơn giản và tập trung. **Github** được thành lập năm 2008 bởi một
công ty.

Như đã đề cập **Git** ở trên **Git** có thể dùng thông qua mạng cho nên 
**Github** chính là phát huy tính năng dùng thông qua mạng của **Git** một
cách hiệu quả.

Nếu chúng ta không sử dụng **Github** thì vẫn sử dụng **Git** bình thường
nhưng **Git** sẽ bị giới hạn khoảng cách, còn khi sử dụng **Github** chúng
ta có thể toàn cầu hóa được **Git** bất cứ lúc nào và ở đâu miễn sao chúng
ta có kết nối tới mạng internet toàn cầu. Để biết thêm chi tiết về **Github**
đã và đang làm vui lòng tham khảo tại các bài viết trên trang **Github.Com**

## Cài đặt Git

Với hệ điều hành mã nguồn mở thì quá trình cài đặt git quá dễ dàng chỉ cần
một dòng lệnh có thể cài đặt được **Git** và quá trình này chỉ vài giây là
xong sau cú nhấn phím enter cụ thể như sau

**Với hệ điều hành Ubuntu**

```bash
sudo apt-get install git
```

**Với hệ điều hành CentOS**

```bash
sudo yum install git
```

**Với hệ điều hành Mac OS**

```bash
brew install git
```

Đối với hệ điều hành window thì cần vào trang chủ của **Git** là [git-scm.com](https://git-scm.com/download/win)
để tải về phiên bản tương thích với máy tính của mình. Sau khi tải xong
chúng ta tiến hành cài đặt theo hướng dẫn từ cửa sổ cài đặt.

## Sử dụng Git

Ở mục tóm tắt cơ bản trên thì chúng ta sẽ bỏ qua việc tìm hiểu **Github**
và tiến hành nghiên cứu và sử dụng **Git** chi tiết như sau để đảm bảo
cho chúng ta có thể thao tác cơ bản với **Git** để phù hợp với công việc
của bản thân chúng ta hơn.

**Git** dùng tên là `git` nên khi chúng ta sử dụng sẽ bắt đầu bằng cái tên
này sau đó là dải những tùy chọn cho `git` để `git` làm việc. để hiểu nhiều
hơn về các lệnh của `git` vui lòng gõ lệnh `git help` để biết các lệnh của
`git` và cách sử dụng các lệnh đó.

Vì mục đích của bài viết này chỉ muốn người sử dụng biết và nắm rõ một
vài lệnh cơ bản để có thể sử dụng và gỡ được rối trong quá trình dùng **Git**
cho những mục đích cụ thể không nhất thiết phải hiểu sâu về **Git** quá nhiều
vì cơ bản **Git** đã có một mục tiêu cơ bản nhất là lưu trữ và quản lý phiên
bản mã nguồn, nên chúng ta chỉ cần quan tâm tới điều này trước, còn những
thứ xa xôi hơn như ghép nối các mảnh lại, thao tác khác chúng ta sẽ tự tìm
hiểu thêm sau khi chúng ta đã nhuần nhuyễn những lệnh cơ bản của **Git**
thì chúng ta sẽ tự hiểu được những lệnh khác.

### Tạo dự án Git

Khi ở trên máy tính cá nhân của chúng ta đã được cài đặt **Git** thì chúng
ta sẽ sử dụng lệnh sau _(mọi lệnh `git` đều giống nhau chỉ khác cách dùng lệnh
ở đâu trên hệ điều hành hiện tại)_

Giả sử chúng ta tạo một dự án có tên là `du-an` thì chúng ta sẽ bắt đầu như sau

```bash
mkdir du-an
cd du-an
git init
```

Khi gõ xong lệnh `git init` thì sẽ có thông báo tương tự như sau

```bash
Initialized empty Git repository in /du-an/.git/
```

Điều này có nghĩa là `git` đã tạo một dự án được lưu trữ những thông tin
vào trong thư mục `.git` của thư mục hiện tại và như vậy là chúng ta đã 
thành công trong việc tạo dự án **Git**

Chú thích các câu lệnh ở trên.

1. `mkdir du-an` lệnh này có nghĩa là tạo thư mục _(make directory)_ có tên là 
`du-an` tại thư mục hiện hành chúng ta đang đứng.
2. `cd du-an` lệnh này có nghĩa là đi vào thư mục _(change directory)_ `du-an`
3. `git init` đây là lệnh chính của `git` để `git` tạo dự án cho chúng ta.

### Thêm tập tin vào Git

Sau khi chúng ta đã tạo được dự án thì chúng ta sẽ bắt đầu những công việc
như viết mã, thực thi hay gì đó vân vân và mây mây ... thì chúng ta sẽ có lúc
nghỉ ngơi hoặc là ghi chú nó lại để một mai này xem lại nó thế nào trước
đó chúng ta đã làm gì thì đây chính là công việc chính của **Git**

Giả sử chúng ta tạo một tập tin cơ bản như sau

```bash
echo "1" > a.txt
```

Đoạn mã này có nghĩa là tạo một tập tin có tên `a.txt` với nội dung là `1`
để kiểm tra xem tập tin thì chúng ta dùng lệnh `git status` status tiếng anh
là (trạng thái/tình trạng) thì chúng ta sẽ thấy có ghi thông tin là `new file a.txt`

Để thêm tập tin này vào `git` chúng ta dùng lệnh `git add a.txt` chi tiết 
về lệnh `add` này chúng ta dùng lệnh `git help add` thì `git` sẽ có hướng
dẫn đầy đủ cách sử dụng nó.

Sau khi chúng ta thêm vào xong thì chúng ta sẽ bắt đầu lưu nó vào lịch sử
dùng lệnh `git commit` để biết chi tiết lệnh `commit` thì dùng lệnh `git help commit`
git sẽ hướng dẫn chi tiết chúng ta sẽ làm và truyền những đối số nào vào

Để đơn giản và nhanh với những ghi chú nhỏ chúng ta có thể dùng nhanh lệnh sau

```bash
git commit -m "nội dung ghi chú cho nhật ký"
```

Sau khi làm xong lệnh này thì `git` đã tạo cho chúng ta một nhật ký lưu lại
để kiểm tra các nhật ký chúng ta dùng lệnh `git log` ngoài ra để xem thêm vài
đối số cho việc xem `log` nhật ký ta dùng lệnh `git help log` để tùy biến
cho chúng ta có thể sử dụng và xem nhật ký sao cho thuận tiện với mục đích
của mình.

> `git add <ten_tap_tin|thu_muc>` đây là cách để thêm vào `git` các tập tin
với cấu trúc trong hệ điều hành thì `.` đại diện cho thư mục hiện tại chúng
ta đang ở đó, `../` có nghĩa là thư mục cha của thư mục hiện tại. `../../` có nghĩa
là thư mục cha của cha thư mục hiện tại...

Như vậy ở phần này chúng ta hiểu được việc thêm vào `git` tập tin. và trong quá trình
này chúng ta có thêm một lệnh nữa là `git reset` lệnh này có nghĩa là xóa 
danh sách cách tập tin trong hàng đợi mới dùng lệnh `git add` xong lưu ý là 
nó chưa gọi lệnh `git commit`, để biết chi tiết thì dùng lệnh `git help reset`
để biết thêm nhiều thông tin hơn. ở đây chúng ta sẽ tạm hiểu là đưa một hoặc
nhiều tập tin ra khỏi danh sách đã được thêm nếu không có đối số tiếp theo
thì tất cả trong `git` mới thêm sẽ được đưa ra khỏi danh sách, còn tên các
tập tin thì các tập tin sẽ được đưa ra khỏi `git`.

Giả sử trong `git` được thêm vào hai tập tin `a.txt` và `b.txt` nếu như
chúng ta dùng `git reset` thì cả hai tập tin `a.txt` và `b.txt` sẽ được đưa ra
còn nếu chúng ta thêm vào `git reset a.txt` thì khi đó chi mỗi tập tin `a.txt`
sẽ được đưa ra và tập tin `b.txt` sẽ được giữ lại. tương tự chúng ta truyền
vào nhiều tập tin phía sau thì các tập tin sẽ được đưa ra ví dụ `git reset a.txt b.txt`

### Đi tới một nhật ký

Trong quá trình viết mã và lưu giữ dùng `git` thì sẽ có danh sách các nhật
ký được lưu trong `git` để xem các nhật ký dùng lệnh `git log`

Sau khi dùng `git log` chúng ta có các nhật ký bây giờ chúng ta muốn sửa tại
một nhật ký nào đó hoặc lấy lại nội dung của một nhật ký nào đó thì ta dùng
lệnh `git checkout <commit_id>` chi tiết lệnh này chúng ta dùng `git help checkout`
sau khi dùng lệnh này xong thì chúng ta sẽ về tới nhật ký đã thay đổi trước
đó và tập tin nội dung cũng sẽ thay đổi theo như nhật ký đã được đi tới.

> Với mới tập tành về `git` thì dùng để xem lại nội dung tập tin đừng chỉnh sửa
vì khi chỉnh sửa sẽ cần phải biết thêm vài lệnh nữa mới đi về lại được phân
nhánh hiện tại

## Tóm lại

Như vậy **Git** chúng ta chỉ cần sử dụng nhiều với lệnh `git add` và `git commit`
chúng ta chỉ cần hiểu rõ hai lệnh cơ bản này thì chúng ta sử dụng được `git`
một cách cơ bản và rất hữu ích cho công việc và mục đích của chúng ta.

Sau khi hiểu được những lệnh cơ bản này thì chúng ta sẽ tìm hiểu tới các vấn
đề như **phân nhánh**, **hợp nhất các nhánh**, **đẩy nhật ký đi tới một dự án** ...

Tuần tự các lệnh `git` được sử dụng tần suất nhiều của lệnh `git` cơ bản
này là như sau

```bash
git add # (Thêm vào)
git reset # (Đưa ra tập tin không muốn đưa vào git)
git commit # (Lưu tập tin vào trong git)
```

Các lệnh như `git init` nó chỉ được làm một lần khi tạo mới dự án, `git pull`
sẽ được làm khi chúng ta muốn lấy thông tin từ dự án về máy mình, `git clone`
dùng để nhân bản dự án về máy mình. và lệnh `git push` dùng để đẩy nhật ký lên
dự án.

Tất cả mọi lệnh cũng như cách sử dụng thì `git` đã tạo ra lệnh `git help`
để chúng ta có thể tham khảo và sử dụng nó một cách rất chi tiết và cụ thể nhất

