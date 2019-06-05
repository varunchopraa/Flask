from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Homepage here!"

@app.route('/about/')   #URL for website
def about():
 	return "About content goes here!"

if __name__ == "__main__":
	app.run(debug = True)

