from bottle import route, run, template

# 表を作ってみる

@route('/list')
def view_list():
	# ダーミーデータ(あとでDBから取得)
	item_list = [
		{"id": 1, "name":"りんご"},
		{"id": 2, "name":"ぱなま"},
		{"id": 3, "name":"すいか"},
	]
	# 表示用のHTMLを組み立てる
	display_html = "<table border='1'>"
	for item in item_list:
		display_html += "<tr>"
		display_html += "<td>{}</td>".format(item["id"])
		display_html += "<td>{}</td>".format(item["name"])
		display_html += "</tr>"
	display_html += "</table>"
	return display_html

run(reloader=True, port=9999)

