from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World"

#@app.route("/david")
#def david():
#    return "Hello, david"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}"
