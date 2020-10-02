from db import db

def get_notok():
    sql = "SELECT hives.name, checkup.explain FROM checkup JOIN hives ON hives.hive_id = checkup.hive_id WHERE checkup.allok='2'"
    result = db.session.execute(sql)
    return result.fetchall()

def get_queens():
    sql = "SELECT queen_id, name FROM queens WHERE alive='1'"
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

def get_queenfromhive(id):
    sql = "SELECT queens.name FROM hives LEFT JOIN queens ON hives.queen_id = queens.queen_id WHERE hive_id=:hive_id AND queens.alive='1'"
    result = db.session.execute(sql, {"hive_id":id})
    return result.fetchone()[0]

