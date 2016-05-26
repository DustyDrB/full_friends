from flask import Flask, flash, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():


app.run(debug=True)