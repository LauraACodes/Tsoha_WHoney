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