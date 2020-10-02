from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

# define db address, disable tracking (takes space) 
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app);

# add code here to add producer info & examples that help to 
# demostrate the app.
