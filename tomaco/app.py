from bottle import app, route, run

application = app()


@route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    run(app=application)
