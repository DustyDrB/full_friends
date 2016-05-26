from flask import Flask, flash, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'email')
app.secret_key = "adorable_beagles"

@app.route('/')
def 
if __name__ =="__main__":
	app.run(debug=True)