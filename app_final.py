import sqlite3
from bottle import route, run, template, request, redirect

# list(default page)
@route("/list")
def view_list():
	# items.db$B$H$D$J$0(B
	conn = sqlite3.connect('items.db')
	c = conn.cursor()
	c.execute("select id, name from items order by id")
	item_list = []
	for row in c.fetchall():
		item_list.append({
			"id": row[0],
			"name": row[1]
		})
	conn.close()
	return template("list_tmpl", item_list=item_list)

# add page
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
		return redirect("/list")
	else:
		# GET$B%"%/%;%9$J$i%U%)!<%`I=<((B
		return template("add_tmpl")

# delete page
# /del/100 -> item_id = 100
# /del/one -> HTTPError 404

@route("/del/<item_id:int>")
def del_item(item_id):
	conn = sqlite3.connect('items.db')
	c = conn.cursor()
	# $B;XDj$5$l$?(Bitem_id$B$r85$K(BDB$B%G!<%?$r:o=|(B
	c.execute("delete from items where id=?", (item_id, ))
	conn.commit()
	conn.close()
	# $B=hM}8e$K0lMw2hLL$KLa$9(B
	return redirect("/list")

run(reloader=True, port=9999)

