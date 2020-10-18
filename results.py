from db import db
import datetime

def get_notok():
    sql = "SELECT hives.name, checkup.explain, checkup.checkup_id FROM checkup \
        JOIN hives ON hives.hive_id = checkup.hive_id WHERE checkup.allok='2'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_hives_notok(hive_id):
    sql = "SELECT hives.name, checkup.explain, checkup.checkup_id FROM checkup \
        JOIN hives ON hives.hive_id = checkup.hive_id WHERE checkup.allok='2' AND hives.hive_id=:hive_id"
    result = db.session.execute(sql, {"hive_id":hive_id})
    return result.fetchall()

def get_queens():
    sql = "SELECT queen_id, name FROM queens WHERE alive='1'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_freequeens():
    sql = "SELECT queen_id, name FROM queens WHERE queen_id NOT IN \
        (SELECT queen_id FROM hives) AND queens.alive='1'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_producers():
    sql = "SELECT producer_id, name FROM producers"
    result = db.session.execute(sql)
    return result.fetchall()

def get_hives():
    sql = "SELECT hive_id, name FROM hives"
    result = db.session.execute(sql)
    return result.fetchall()

def get_diseaces():
    sql = "SELECT diseace_id, name FROM diseacelist"
    result = db.session.execute(sql)
    return result.fetchall()

def get_hive(id):
    sql = "SELECT * FROM hives WHERE hive_id=:hive_id"
    result = db.session.execute(sql, {"hive_id":id})
    return result.fetchone()

def get_queenfromhive(hive_id):
    sql = "SELECT queens.name FROM hives LEFT JOIN queens ON hives.queen_id = queens.queen_id \
        WHERE hive_id=:hive_id AND queens.alive='1'"
    result = db.session.execute(sql, {"hive_id":hive_id})
    return result.fetchone()[0]

def get_queenidfromhive(id):
    sql = "SELECT queen_id FROM hives WHERE hive_id=:hive_id"
    result = db.session.execute(sql, {"hive_id":id})
    return result.fetchone()[0]

def count_alivehives():
    sql = "SELECT COUNT(*) FROM hives WHERE alive = 1"
    result = db.session.execute(sql)
    return result.fetchone()

def count_honey_boxes():
    sql = "SELECT SUM(boxes) FROM hives WHERE alive = 1"
    result = db.session.execute(sql)
    boxes = result.fetchone()
    hives = count_alivehives()
    honey_boxes = boxes[0] - (hives[0]*2)
    return honey_boxes

def get_harvest():
    sql = "SELECT SUM(boxes) FROM harvest WHERE date BETWEEN '2020-01-01' AND '2020-12-31'"
    result = db.session.execute(sql)
    return result.fetchone()

def get_careactions():
    sql = "SELECT COUNT(*) FROM hivecare WHERE date BETWEEN '2020-01-01' AND '2020-12-31'"
    result = db.session.execute(sql)
    return result.fetchone()

def get_sugar():
    sql = "SELECT SUM(kg) FROM sugar WHERE date BETWEEN '2020-01-01' AND '2020-12-31'"
    result = db.session.execute(sql)
    return result.fetchone()

def get_action_list():
    sql = "SELECT hivecare.date AS date, hives.name AS name, carelist.name AS care \
        FROM hivecare JOIN carelist ON hivecare.care_id=carelist.care_id JOIN hives \
        ON hivecare.hive_id=hives.hive_id ORDER BY date DESC LIMIT 5"
    result = db.session.execute(sql)
    return result.fetchall()