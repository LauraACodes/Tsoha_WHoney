from app import app
import results
from db import db
from flask import render_template, request

@app.route("/")
def index():
    notoks= results.get_notok()
    return render_template("index.html", notoks=notoks)

@app.route("/careactions")
def careactions():
    return render_template("actions.html")

@app.route("/investments")
def investments():
    return render_template("investments.html")

@app.route("/newq", methods=["POST"])
def newq():
    return render_template("newqadded.html")

@app.route("/newh", methods=["POST"])
def newh():
    return render_template("newhadded.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")