import sqlite3
from bottle import route, run, template

# $BF~NO%\%C%/%9$rI=<($9$k%F%s%W%l!<%H$N;HMQ(B

@route('/add', method=["GET", "POST"])
def add_item():
	return template("add_tmpl")

#run(reloader=True, port=9999)

