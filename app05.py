import sqlite3
from bottle import route, run, template, request

# sql$B$r;H$C$FF~NO$7$?J8;zNs$r%G!<%?%Y!<%9$KEPO?(B	

@route('/add', method=["GET", "POST"])
def add_item():
	if request.method == "POST":
		# POST$B%"%/%;%9$J$i(BDB$B$KEPO?$9$k(B
		# $B%U%)!<%`$+$iF~NO$5$l$?%"%$%F%`L>$N<hF@(B(Python2$B$J$i(Brequest.POST.getunicode$B$r;HMQ(B)
		item_name = request.POST.getunicode("item_name")
		conn = sqlite3.connect('items.db')
		c = conn.cursor()
		# $B8=:_$N:GBg(BID$B<hF@(B(fetchone$B$NLa$jCM$O%?%W%k(B)
		new_id = c.execute("select max(id) + 1 from items").fetchone()[0]
		c.execute("insert into items values(?, ?)", (new_id, item_name))
		conn.commit()
		conn.close()
		return "SUCCESS"
	else:
		# GET$B%"%/%;%9$J$i%U%)!<%`I=<((B
		return template("add_tmpl")

#run(reloader=True, port=9999)

