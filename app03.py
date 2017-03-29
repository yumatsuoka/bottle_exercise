from bottle import route, run, template

# template$B$r;H$C$F(Bhtml$BItJ,$rCj>]2=(B

@route('/list')
def view_list():
	# $B%@!<%_!<%G!<%?(B($B$"$H$G(BDB$B$+$i<hF@(B)
	item_list = [
		{"id": 1, "name":"$B$j$s$4(B"},
		{"id": 2, "name":"$B$Q$J$^(B"},
		{"id": 3, "name":"$B$9$$$+(B"},
	]
	return template("list_tmpl", item_list=item_list)

run(reloader=True, port=9999)

