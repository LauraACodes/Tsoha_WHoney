from app import app
import results
from flask import render_template

@app.route("/")
def index():
    notoks= results.get_notok()
    return render_template("index.html", notoks=notoks)
