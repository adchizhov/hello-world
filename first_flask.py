from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Good day, sir!'

@app.route('/hello')
def hello():
	return 'Hello, my name is Adolf'

if __name__ == '__main__':
	app.run()