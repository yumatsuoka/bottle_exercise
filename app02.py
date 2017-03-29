from bottle import route, run, template

# $BI=$r:n$C$F$_$k(B

@route('/list')
def view_list():
	# $B%@!<%_!<%G!<%?(B($B$"$H$G(BDB$B$+$i<hF@(B)
	item_list = [
		{"id": 1, "name":"$B$j$s$4(B"},
		{"id": 2, "name":"$B$Q$J$^(B"},
		{"id": 3, "name":"$B$9$$$+(B"},
	]
	# $BI=<(MQ$N(BHTML$B$rAH$_N)$F$k(B
	display_html = "<table border='1'>"
	for item in item_list:
		display_html += "<tr>"
		display_html += "<td>{}</td>".format(item["id"])
		display_html += "<td>{}</td>".format(item["name"])
		display_html += "</tr>"
	display_html += "</table>"
	return display_html

run(reloader=True, port=9999)

