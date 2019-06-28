import os

import bottle
from bottle import default_app, static_file, template

PROJECT_PATH = os.path.dirname(__file__)
bottle.TEMPLATE_PATH.insert(0, os.path.join(PROJECT_PATH, "views"))

app = default_app()


@app.route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root=os.path.join(PROJECT_PATH, "static"))


@app.route("/")
def index():
    return template("index")


if __name__ == "__main__":
    app.run(app=app, debug=True, reload=True)
