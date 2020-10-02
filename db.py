from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

# define db address, disable tracking (takes space) 
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app);

# add code here to add producer info & examples that help to 
# demostrate the app.
sql = "INSERT INTO producers (producer_id, name) VALUES (1, 'Oma tuotanto'), (2, 'Mesimestarit'), (3, 'Korpiahon Hunaja')"
db.session.execute(sql)
db.session.commit()

sql1 = "INSERT INTO queens (queen_id, producer_id, date, name) VALUES (1, 1, '2019-05-10', 'Pirjo'), (2, 2, '2019-07-15', 'Sirkka'), (3, 2, '2020-07-20', 'Tyyne'), (4, 1, '2020-07-25', 'Pirjo2')"
db.session.execute(sql1)
db.session.commit()

sql2 = "INSERT INTO hives (hive_id, queen_id, producer_id, date, name) VALUES (1, 1, 3, '2019-05-10', 'Wilmala1'), (2, 2, 1, '2019-07-15', 'Wilmala2'), (3, 3, 1, '2020-07-20', 'Wilmala3')"
db.session.execute(sql2)
db.session.commit()

sql3 = "INSERT INTO carelist (care_id, name) VALUES (1, 'Tarkistus'), (2, 'Lisätila'), (3, 'Ruokinta'), (4, 'Tautitorjunta')"
db.session.execute(sql3)
db.session.commit()

sql4 = "INSERT INTO diseacelist (diseace_id, name) VALUES (1, 'Tymol-tyyny'), (2,'Muurahaishapotus'), (3, 'EKM-näyte'), (4, 'EKM-saneeraus')"
db.session.execute(sql4)
db.session.commit()

sql5 = "INSERT INTO hivecare (hivecare_id, hive_id, care_id, date) VALUES (1, 1, 1, '2020-06-06')"
db.session.execute(sql5)
db.session.commit()

slq6 = "INSERT INTO checkup (checkup_id, hivecare_id, hive_id, date, allok, explain) VALUES (1, 1, 1, '2020-06-06', 2, 'Munia ei näy, eikä Pirjoa! Onko Pirjo livistänyt?')"
db.session.execute(slq6)
db.session.commit()