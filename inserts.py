from db import db
from flask import session

def addbox(hive_id, date):
    care_id = 2
    sql = "UPDATE hives SET boxes=boxes+1 WHERE hive_id=hive_id"
    db.session.execute(sql, {"hive_id":hive_id})
    db.session.commit()
    newhivecare(hive_id, care_id, date)
    return True

def checkup(hive_id, date, allok, explain):
    care_id = 1
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO checkup (hivecare_id, hive_id, date, allok, explain) VALUES (:hivecare_id, :hive_id, :date, :allok, :explain)"
    db.session.execute(sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "allok":allok, "explain":explain})
    db.session.commit()
    return True

def sugar(hive_id, date, kg):
    care_id = 3
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO sugar (hivecare_id, hive_id, date, kg) VALUES (:hivecare_id, :hive_id, :date, :kg)"
    db.session.execute(sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "kg":kg})
    db.session.commit()
    return True

def diseace(hive_id, date, diseace):
    care_id = 4
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO diseacecont (hivecare_id, hive_id, date, diseace_id) VALUES (:hivecare_id, :hive_id, :date, :diseace_id)"
    db.session.execute(sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "diseace_id":diseace_id})
    db.session.commit()
    return True

def newhivecare(hive_id, care_id, date):
    sql = "INSERT INTO hivecare (hive_id, care_id, date) VALUES (:hive_id, :care_id, :date)"
    db.session.execute(sql, {"hive_id":hive_id,"care_id":care_id,"date":date})
    db.session.commit()
    return True    

def getnewesthivecare():
    sql = "SELECT MAX(hivecare_id) FROM hivecare"
    result = db.session.execute(sql)
    return result.fetchone()[0]