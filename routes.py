from app import app
import results
from db import db
from flask import render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/start")
def start():
    return render_template("newuser.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        return render_template("loginerror.html",errordet="Sinua ei löytynyt! Luo tili tai tarkasta oikeinkirjoitus.")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("loginerror.html",errordet="Salasana väärin, voi ei! Oletko unohtanut...?")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/newuser", methods=["POST"])
def newuser():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql1 = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql1, {"username":username})
    user = result.fetchone()
    if user == None:
        sql2 = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql2, {"username":username,"password":hash_value})
        db.session.commit() 
        return redirect("/")
    else:
        return render_template("loginerror.html",errordet="Kyseinen käyttäjänimi on jo käytössä. Keksi uusi.")
    
@app.route("/")
def index():
    notoks = results.get_notok()
    return render_template("index.html", notoks=notoks)

@app.route("/careactions")
def careactions():
    return render_template("actions.html")

@app.route("/investments")
def investments():
    producers = results.get_producers()    
    return render_template("investments.html", producers=producers)

@app.route("/newq", methods=["POST"])
def newq():
    prod = request.form["prod"]
    qname = request.form["qname"]
    date = request.form["ostopvm"]
    sql = "INSERT INTO queens (producer_id, date, name) VALUES (:prod, :date, :qname)"
    db.session.execute(sql, {"producer_id":prod,"date":date,"name":qname})
    db.session.commit()
    return render_template("newqadded.html")

@app.route("/newh", methods=["POST"])
def newh():
    return render_template("newhadded.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")
