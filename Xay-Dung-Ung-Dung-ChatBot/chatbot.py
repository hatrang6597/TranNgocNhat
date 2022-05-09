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
