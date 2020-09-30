from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
#should db be imported here to add some data to db before app does anything else?
import routes

