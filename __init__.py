from flask import Flask, render_template, flash
from content_management import Content #import Content() class

TOPIC_DICT = Content() #create variable and set it as the Content() class with the returned list

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template("main.html")

# @app.route('/slashboard/') #whatever function is provided  below the route will appear, hence both /slashboard and
#/dashboard will render the 'hi' page

@app.route('/dashboard/')
def dashboard():
	# return render_template("main.html")
	flash("flash test!!!")
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT) #the first TOPIC_DICT is what will be referenced in the HTML

@app.errorhandler(404) #app is the above app = Flask(__name__) and errorhandler is part of Flask
def page_not_found(e):
	return render_template("404.html")

# @app.route('/slashboard/') this was just a 500 error handling sample
# def slashboard():
# 	try:
# 	# return render_template("main.html")
# 		return render_template("dashboard.html", TOPIC_DICT = boner)
# 	except Exception as e:
# 		return render_template("500.html", error=e)

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	
	app.run(debug=True, port=8000, host='0.0.0.0')

