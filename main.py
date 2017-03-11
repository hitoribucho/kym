# coding: utf-8
from flask import Flask,render_template,url_for
from flask_wtf import FlaskForm
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField
from wtforms.validators import Length, Required, URL
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import os
import pickle

app = Flask(__name__)
app.secret_key = 'AskfjghjdsaDFkrdnaladfae'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

#データベース
import sqlite3
class Database():
    def __init__(self):
        conn = psycopg2.connect("dbname=test host=localhost user=postgres")

    def close(self):
        pass

    def reset(self):
        pass

    def insert(self,url_info):
        pass

class UrlForm(FlaskForm):
    url = StringField(
        label='URL：',
        validators=[
            Required('URLを入力してください'),
            Length(min=1, max=1024, message='URLは1024文字以内で入力してください'),
            URL(message='URLが正しくありません'),
        ])

@app.route('/', methods=['GET', 'POST'])
def send_url():
    form = UrlForm()
    if form.validate_on_submit():
        url = form.url.data
        # print('送られたURLは {} だよ'.format(url))

        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        #データの読み書き
        Data=Database()
        #データベースを保存して閉じる
        Data.close()

        return render_template('index.html', form=form)

    else:
        Data=Database()
        Data.close()
        return render_template('index.html', form=form)

@app.route('/reset')
def reset_db():
    form = UrlForm()
    Data=Database()
    Data.reset()
    Data.close()
    return render_template('index.html',form=form)
'''
@app.route('/download_db')
def download_db():
    form = UrlForm()
    filename = os.path.join(app.root_path, "database.db")}
    urllib.request.urlretrieve(filename,'buckup.db')
    return render_template('index.html',form=form)
'''

# アプリケーションの実行
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
