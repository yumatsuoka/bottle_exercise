from bottle import route, run, template

# templateを使ってhtml部分を抽象化

@route('/list')
def view_list():
	# ダーミーデータ(あとでDBから取得)
	item_list = [
		{"id": 1, "name":"りんご"},
		{"id": 2, "name":"ぱなま"},
		{"id": 3, "name":"すいか"},
	]
	return template("list_tmpl", item_list=item_list)

run(reloader=True, port=9999)

