# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request, jsonify
import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask("app", template_folder="./")

app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

sentences = []
try:
    with open('brain.txt','r',encoding='utf-8') as fin:
        text = []
        for line in fin:
            line = line.strip()
            if not line:
                sentences.append(" ".join(text))
                text = []
                continue
            text.append(line)
except:
    pass

# Tách các câu trả lời ra thành các câu nhỏ hơn.
sent_tokens = set()
for sent in sentences:
    sents = [s.strip() for s in re.compile(r'[.?!]\s+').split(sent.strip()) if s.strip() ]
    for s in sents:
        s = s.lower()
        # Loại bỏ ký tự đặc biệt trong câu
        s = " ".join([w for w in s.split() if w.strip() and w not in string.punctuation ])
        if not s.strip():
            continue
        if s not in sent_tokens:
            sent_tokens.add(s)

# Khai báo hàm tách từ
def tokenize(text):
    return re.compile(r'\s+').split(text.strip())

# Khai báo hàm lấy câu trả lời
def chatbot_reply(text):
    tokens = list(sent_tokens)
    if len(tokens) == 0:
        return 'Xin lỗi tôi chưa hiểu ý bạn muốn nói, tôi sẽ học lại sau'
    tokens.append(text.lower())
    TfidfVec = TfidfVectorizer(tokenizer=tokenize,stop_words=None)
    tfidf = TfidfVec.fit_transform(tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        return 'Xin lỗi tôi chưa hiểu ý bạn muốn nói, tôi sẽ học lại sau'
    return tokens[idx]

# Kiểm tra người dùng có chào hỏi hay không
def chaohoi(text):
    if not text.strip():
        return None
    chao_hoi = ["chào","hi","halo","bonjour","hello"]
    dap_lai = ["Vâng xin chào","Rất vui khi được gặp bạn","Tôi có thể giúp được gì không"]
    for word in text.split(' '):
        if word.lower() in chao_hoi:
            return random.choice(dap_lai)
    return None

# Kiểm tra người dùng có cám ơn hay không
def camon(text):
    if not text.strip():
        return None
    cam_on = ["cảm ơn","thank","thanks"]
    dap_lai = ["Vâng không có gì","Rất vui khi được giúp bạn","Tôi rất hân hạnh khi có thể giúp được bạn"]
    for word in text.split(' '):
        if word.lower() in cam_on:
            return random.choice(dap_lai)
    return None

# Kiểm tra xem người dùng có tạm biệt
def tambiet(text):
    if not text.strip():
        return None
    tam_biet = ["chào nhé","bye","tạm biệt"]
    dap_lai = ["Vâng xin chào ạ","Vâng tạm biết hi vọng cuộc nói chuyện vui vẻ"]
    for word in text.split(' '):
        if word.lower() in tam_biet:
            return random.choice(dap_lai)
    return None

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
    # Chúng ta sẽ xử lý câu trả lời lại cho chatbot
    reply = chaohoi(text) # Xem có chào không
    if reply is None:
        reply = tambiet(text) # Không chào xem có tạm biẹt không 

    if reply is None:
        reply = camon(text) # Xem thử có cám ơn không

    if reply is None:
        reply = chatbot_reply(text) # Cuối cùng là tìm câu trả lời

    return jsonify({
        "message":text,
        "reply":reply
    })

if __name__ == "__main__":
    app.run('0.0.0.0', port=9090)
