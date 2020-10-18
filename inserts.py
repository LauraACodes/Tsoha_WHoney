from db import db
from flask import session
import results

def addbox(hive_id, date):
    care_id = 2
    sql = "UPDATE hives SET boxes=boxes+1 WHERE hive_id=:hive_id"
    db.session.execute(sql, {"hive_id":hive_id})
    db.session.commit()
    newhivecare(hive_id, care_id, date)
    return True

def harvest(hive_id, date):
    care_id = 6
    hive = results.get_hive(hive_id)
    boxes = hive[6]-2
    sql = "UPDATE hives SET boxes='2' WHERE hive_id=:hive_id"
    db.session.execute(sql, {"hive_id":hive_id})
    db.session.commit()
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    harvest_sql = "INSERT INTO harvest (hivecare_id, hive_id, date, boxes) \
        VALUES (:hivecare_id, :hive_id, :date, :boxes)"
    db.session.execute(harvest_sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "boxes":boxes})
    db.session.commit()
    return True

def checkup(hive_id, date, allok, explain):
    care_id = 1
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO checkup (hivecare_id, hive_id, date, allok, explain) \
        VALUES (:hivecare_id, :hive_id, :date, :allok, :explain)"
    db.session.execute(sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "allok":allok, "explain":explain})
    db.session.commit()
    if allok == 3:
        sql_hive = "UPDATE hives SET alive='2' WHERE hive_id=:hive_id"
        db.session.execute(sql_hive, {"hive_id":hive_id})
        db.session.commit()
    return True

def changequeen(hive_id, date, queen_id):
    care_id = 5
    newhivecare(hive_id, care_id, date)
    oldq = results.get_queenidfromhive(hive_id)
    sql_oldq = "UPDATE queens SET alive ='2' WHERE queen_id=:queen_id"
    db.session.execute(sql_oldq, {"queen_id":oldq})
    db.session.commit()
    sql_hive = "UPDATE hives SET queen_id=:queen_id WHERE hive_id=:hive_id"
    db.session.execute(sql_hive, {"queen_id":queen_id, "hive_id":hive_id})
    db.session.commit()
    return True

def sugar(hive_id, date, kg):
    care_id = 3
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO sugar (hivecare_id, hive_id, date, kg) \
        VALUES (:hivecare_id, :hive_id, :date, :kg)"
    db.session.execute(sql, {"hivecare_id":hivecare_id, "hive_id":hive_id, "date":date, "kg":kg})
    db.session.commit()
    return True

def fix(hive_id, date, checkup_id, explain):
    sql = "UPDATE checkup SET allok=3 WHERE checkup_id=:checkup_id"
    db.session.execute(sql, {"checkup_id":checkup_id})
    db.session.commit()
    checkup(hive_id,date,1,explain)
    return True

def diseace(hive_id, date, diseace_id):
    care_id = 4
    newhivecare(hive_id, care_id, date)
    hivecare_id = getnewesthivecare()
    sql = "INSERT INTO diseacecont (hivecare_id, hive_id, date, diseace_id) \
        VALUES (:hivecare_id, :hive_id, :date, :diseace_id)"
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

