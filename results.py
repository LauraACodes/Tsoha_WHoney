from db import db

def get_notok():
    sql = "SELECT hives.name, checkup.explain FROM checkup JOIN hives ON hives.hive_id = checkup.hive_id WHERE checkup.allok='2'"
    result = db.session.execute(sql)
    return result.fetchall()