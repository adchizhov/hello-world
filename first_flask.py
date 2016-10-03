from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return 'Good day, sir!'

@app.route('/hello')
def hello():
	return 'Welcome to my ultimate first amazing godlike server!!! Let the moneyrain begins!'

@app.route('/hello/<username>')
def user(username):
	return render_template('color_user.html', name=username)

@app.route('/hello/day/<int:day>')
def today(day):
	return 'Maybe today is {} day'.format(day)

if __name__ == '__main__':
	app.run(debug=True)