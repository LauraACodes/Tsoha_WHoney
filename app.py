from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)

#should db be imported here to add some data to db before app does anything else?
import routes

