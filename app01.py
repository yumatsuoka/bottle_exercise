from bottle import route, run, template

# Hello world

@route('/')
def index():
    return '<h1>Welcome !</h1>'

run(reloader=True, port=8080)

