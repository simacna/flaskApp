from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/dashboard')
def homepage():
	return render_template("main.html")

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')

