from flask import Flask, render_template, jsonify
app = Flask(__name__)

# returns an html webpage
@app.route('/')
def index():
	return 'Good day, sir!'

# returns an html webpage
@app.route('/hello')
def hello():
	return 'Welcome to my ultimate first amazing godlike server!!! Let the moneyrain begins!'

# returns an html webpage
@app.route('/hello/<username>')
def user(username):
	return render_template('color_user.html', name=username)

# returns an html webpage
@app.route('/hello/day/<int:day>')
def today(day):
	return 'Maybe today is {} day'.format(day)

# returns a piece of data in JSON format
@app.route('/lotsofdata')
def people():
	my_people = {'Alice' : 25, 
	             'Bob' : 45,
	             'Sasha' : 26,
	             'Julia' : 26}
	return jsonify(my_people)
if __name__ == '__main__':
	app.run(debug=True)