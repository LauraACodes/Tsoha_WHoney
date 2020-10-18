from app import app
import results
import inserts
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
        return render_template("error.html",errordet="Sinua ei löytynyt! Luo tili tai tarkasta oikeinkirjoitus.")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("error.html",errordet="Salasana väärin, voi ei! Oletko unohtanut...?")

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
        return render_template("error.html",errordet="Kyseinen käyttäjänimi on jo käytössä. Keksi uusi.")

@app.route("/")
def index():
    hives = results.get_hives()
    notoks = results.get_notok()
    return render_template("index.html", hives=hives, notoks=notoks)

@app.route("/apu", methods=["POST"])
def apu():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    return redirect("careactions/"+str(hive_id)+"/"+str(date)+"/")

@app.route("/careactions/<int:hive_id>/<string:date>/", methods=["GET", "POST"])
def careactions(hive_id, date):
    hive = results.get_hive(hive_id)
    hivename = hive[4]
    box = hive[6]
    queen = results.get_queenfromhive(hive_id)
    freequeens = results.get_freequeens()
    diseaces = results.get_diseaces()
    notoks = results.get_hives_notok(hive_id)
    return render_template("actions.html", hivename=hivename, queen=queen, freequeens=freequeens, \
        box=box, hive_id=hive_id, date=date, diseaces=diseaces, notoks=notoks)

@app.route("/addbox/", methods=["POST"])
def addbox():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    inserts.addbox(hive_id, date)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/harvest/", methods=["POST"])
def harvest():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    inserts.harvest(hive_id, date)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/checkup", methods=["POST"])
def checkup():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    allok = request.form["allok"]
    explain = request.form["explain"]
    inserts.checkup(hive_id, date, allok, explain)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/fixproblem", methods=["POST"])
def fixproblem():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    checkup_id = request.form["checkup_id"]
    explain = request.form["explain"]
    inserts.fix(hive_id, date, checkup_id, explain)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/changequeen", methods=["POST"])
def changequeen():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    queen_id = request.form["queen_id"]
    inserts.changequeen(hive_id, date, queen_id)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/feeding", methods=["POST"])
def feeding():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    kg = request.form["kg"]
    inserts.sugar(hive_id, date, kg)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/disease", methods=["POST"])
def disease():
    hive_id = request.form["hive_id"]
    date = request.form["date"]
    diseace_id = request.form["diseace_id"]
    inserts.diseace(hive_id, date, diseace_id)
    return redirect("/careactions/"+str(hive_id)+"/"+str(date))

@app.route("/buyqueen")
def buyqueen():
    producers = results.get_producers()    
    return render_template("buyqueen.html", producers=producers)

@app.route("/buyhive")
def buyhive():
    producers = results.get_producers()   
    queens = results.get_queens()    
    return render_template("buyhive.html", producers=producers, queens=queens)

@app.route("/newq", methods=["POST"])
def newq():
    producer_id = request.form["producer_id"]
    name = request.form["name"]
    date = request.form["date"]
    sql1 = "SELECT * FROM queens WHERE name=:name"
    result = db.session.execute(sql1, {"name":name})
    queen = result.fetchone()
    if queen == None:
        sql = "INSERT INTO queens (producer_id, date, name) VALUES (:producer_id, :date, :name)"
        db.session.execute(sql, {"producer_id":producer_id,"date":date,"name":name})
        db.session.commit()
        return render_template("newqadded.html")
    else:
        return render_template("error.html", errordet="Ehdottamasi niminen kuningatar pörrää pesässä jo - keksi uusi nimi!")

@app.route("/newh", methods=["POST"])
def newh():
    producer_id = request.form["producer_id"]
    queen_id = request.form["queen_id"]
    name = request.form["name"]
    date = request.form["date"]
    sql = "INSERT INTO hives (queen_id, producer_id, date, name) \
        VALUES (:queen_id, :producer_id, :date, :name)"
    db.session.execute(sql, {"queen_id":queen_id,"producer_id":producer_id,"date":date,"name":name})
    db.session.commit()
    return render_template("newhadded.html")


@app.route("/statistics")
def statistics():
    hives_a = results.count_alivehives()
    hives_alive = hives_a[0]
    honey_boxes = results.count_honey_boxes()
    harvested_b = results.get_harvest()
    harvested_boxes = harvested_b[0]
    caretaking = results.get_careactions()[0]
    sugarkg = results.get_sugar()[0]
    actions = results.get_action_list()
    return render_template("statistics.html", hives_alive=hives_alive, honey_boxes=honey_boxes, \
        harvested_boxes=harvested_boxes, caretaking=caretaking, sugarkg=sugarkg, actions=actions)
