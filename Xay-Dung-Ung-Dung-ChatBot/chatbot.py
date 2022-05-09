# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request, jsonify

app = Flask("app", template_folder="./")

app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

@app.route('/')
def homepage():
    return render_template('chatbot.html');

@app.route('/api',methods=['POST'])
def chatreply():
    # Nếu gửi lên bằng JSON thì chúng ta sẽ lấy JSON
    if request.content_type and "application/json" in request.content_type:
        data = request.get_json()
    else:
        # Chúng ta sẽ lây thông qua form data
        data = request.form
    # Lấy nội dung người dùng gửi lên
    text = data.get('text','').strip()
    # Nếu như không có gì thì thông báo lỗi và thoát
    if not text:
        return jsonify({
            "error":"Tôi không nghe bạn nói gì cả."
        })
    # Đơn giản ở phần này chúng ta gửi trả lại những gì người ta gửi lên
    return jsonify({
        "message":text,
        "reply":text
    })

if __name__ == "__main__":
    app.run('0.0.0.0', port=9090)
