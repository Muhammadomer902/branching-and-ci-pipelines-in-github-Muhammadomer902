from flask import Flask, render_template
from nonexistent_module import something 

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from main page"


@app.route("/about")
def about():
    return render_template("about.html")
