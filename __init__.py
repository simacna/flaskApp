from flask import Flask, render_template
from content_management import Content #import Content() class 

TOPIC_DICT = Content() #create variable and set it as the Content() class with the returned list

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/slashboard/') #whatever function is provided  below the route will appear, hence both /slashboard and
#/dashboard will render the 'hi' page

@app.route('/dashboard/')
def dashboard():
	# return render_template("main.html")
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT) #the first TOPIC_DICT is what will be referenced in the HTML

@app.errorhandler(404) #app is the above app = Flask(__name__) and errorhandler is part of Flask
def page_not_found(e):
	return render_template("404.html")

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')

