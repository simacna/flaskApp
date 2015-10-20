from flask import Flask, render_template, flash, request, url_for, redirect #url_for allows us to get the url for a function
from content_management import Content #import Content() class
from dbconnect import connection

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
	# flash("flash test!!!")
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT) #the first TOPIC_DICT is what will be referenced in the HTML

@app.errorhandler(404) #app is the above app = Flask(__name__) and errorhandler is part of Flask
def page_not_found(e):
	return render_template("404.html")

# @app.errorhandler(405) -- assuming the login route did  not pass the methods=['GET', 'POST']
#then method_not_found function would run
# def method_not_found(e):
# 	return render_template("404.html")

# @app.route('/slashboard/') this was just a 500 error handling sample
# def slashboard():
# 	try:
# 	# return render_template("main.html")
# 		return render_template("dashboard.html", TOPIC_DICT = boner)
# 	except Exception as e:
# 		return render_template("500.html", error=e)

@app.route('/login/', methods=['GET', 'POST'])
def login_page():
	error = ''
	try:
		if request.method == "POST": #this is for a POST request
			attempted_username = request.form['username'] #username is in reference to value="{{request.form.username}}" in the login.html page
			attempted_password = request.form['password']

			# flash(attempted_username)
			# flash(attempted_password) #just doing this for debugging

			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for('dashboard')) #if they login then we send to the dashboard. 'dashboard' looks for a function named
				#dashboard and this will look above, find the dashboard function and send user to /dashboard

			else:
				error = "Invalid credentials. Try Again." #if login doesn't work 

		return render_template("login.html", error=error) #this will only run if the if statement above doesn't return/redirect
		#to /dashboard



	except Exception as e:
		flash(e) #we'll remove this, generally it's a bad idea to let errors be displayed - just here for debugging purposes
		return render_template("login.html", error=error)
	# return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register_page(): 
	try:
		c, conn = connection() #Python connecting to the database
		return("OK")
	except Exception as e:
		return(str(e))

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	
	app.run(debug=True, port=8000, host='0.0.0.0')

