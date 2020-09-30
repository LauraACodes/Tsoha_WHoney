from db import db

def insertq():
    # sql = "INSERT INTO (producer_id, date, name) VALUES (:producer, :date, :qname)"
    sql = "INSERT INTO queens (producer_id, date, name) VALUES (1, '2020-02-20', 'mirkku')"
    db.session.execute(sql)
    db.session.commit()
    return 