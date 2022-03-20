#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Đầu tiên chúng ta tải thư viện Flask để tiến hành cài đặt
# ứng dụng chạy.
#
# Trong ví dụ đơn giản này chúng ta sử dụng cách trả về JSON
# để đơn giản không phải thiết kế giao diện hiển thị.
# Để trả về JSON thì chúng ta cần thêm vào hàm `jsonify`
# ngoài ra để lấy dữ liệu từ người dùng chúng ta cần thêm vào
# hàm `request` để lấy dữ liệu từ `POST` hoặc là `GET`

from flask import Flask
from flask import jsonify, request

# Khởi động đối tượng Flask

app = Flask("app")

# Vài cấu hình cơ bản

app.config["JSON_AS_ASCII"] = False # Cái này cấu hình không bị mã hõa chữ tiếng việt
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False # Cái này cấu hình để
# không in ra JSON kiểu có format đẹp khi chúng ta đưa ứng dụng vào thực tiễn để chạy cho khách hàng
app.config["DEBUG"] = True # cái này báo với ứng dụng rằng đang trong quá trình chạy thử

# Nào bây giờ chúng ta sẽ bắt đầu viết các điều hướng cơ bản
# để xem thử

# Đầu tiên là khi vô địa chỉ không có điều hướng nào `/`

# Khi chúng ta gõ lên thanh địa chỉ trình duyệt là
# `http://127.0.0.1:9090/` tạm trả về là ['chào bạn']

@app.route('/')
def homepage():
    return jsonify(["chào bạn"])

# Nào bắt đầu chạy ứng dụng nhé

if __name__ == "__main__":
    app.run('0.0.0.0', port=9090)
