from flask import Flask, flash, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/', methods=['GET'])
def index():
	query = "SELECT id, concat(first_name, ' ', last_name) as name, occupation FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	 query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	 data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'occupation': request.form['occupation']
	 }
	 mysql.query_db(query, data)
	 return redirect('/')
@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
	query = "SELECT id, concat(first_name, ' ', last_name) as name, occupation FROM friends WHERE id = :id"
	data = {
			'id': id
	}
	friend = mysql.query_db(query, data)[0]
	return render_template('friend.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'occupation': request.form['occupation'],
			'id': id
	}
	mysql.query_db(query, data)
	return redirect('/')
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	 query = "DELETE FROM friends WHERE id = :id"
	 data= {
			'id': id
	 }
	 mysql.query_db(query, data)
	 return redirect('/')

app.run(debug=True)