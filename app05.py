import sqlite3
from bottle import route, run, template, request

# sqlを使って入力した文字列をデータベースに登録	

@route('/add', method=["GET", "POST"])
def add_item():
	if request.method == "POST":
		# POSTアクセスならDBに登録する
		# フォームから入力されたアイテム名の取得(Python2ならrequest.POST.getunicodeを使用)
		item_name = request.POST.getunicode("item_name")
		conn = sqlite3.connect('items.db')
		c = conn.cursor()
		# 現在の最大ID取得(fetchoneの戻り値はタプル)
		new_id = c.execute("select max(id) + 1 from items").fetchone()[0]
		c.execute("insert into items values(?, ?)", (new_id, item_name))
		conn.commit()
		conn.close()
		return "SUCCESS"
	else:
		# GETアクセスならフォーム表示
		return template("add_tmpl")

#run(reloader=True, port=9999)

