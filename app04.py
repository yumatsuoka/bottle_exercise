import sqlite3
from bottle import route, run, template

# 入力ボックスを表示するテンプレートの使用

@route('/add', method=["GET", "POST"])
def add_item():
	return template("add_tmpl")

#run(reloader=True, port=9999)

