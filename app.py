from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from bson.objectid import ObjectId
from RegDetails import UserDetails
from curd import UserRepo

app = Flask(__name__)
app.secret_key = "This is my super secret never guessed secret key."
repository = UserRepo()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add_contact",methods=["GET","POST"])
def Register():
	if request.method == "GET":
		return render_template("Reg.html")
	elif request.method == "POST":
		 '''for item,val in request.form.items():
		 	print("{0}={1}",format(item, val)'''
		 try:
			User = UserDetails(User_Name=request.form['UserName'],
				FullName=request.form['FullName'],
				Email=request.form['Email'],
				Password=request.form['PassWord'])

			User_id = repository.create(User)
			'''print("Contact succesfully created with id={0}".format(User_id))'''
			if User_id is None:
				print User_id
				flash("User already Exist")
				return redirect(url_for("Register"))
		 except KeyError as e:
			print e

		 return redirect(url_for("index"))
	else:
		 return redirect(url_for("index"))


@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	elif request.method == "POST":
		user_name = request.form['username']
		password = request.form['password']
		if repository.is_user_valid(user_name, password):
			session['user_logged_in'] = True
			error_message = "User {} successfuly logged in.".format(user_name)
			flash(error_message)
			return redirect(url_for("location"))
		else:
			flash("Invalid user/password!")
			return redirect(url_for("login"))
	else:
		error_message = "Invalid request method:{}".format(request.method)
		flash(error_message)
		return redirect(url_for("login"))

@app.route("/logout", methods=["GET"])
def logout():
    session['user_logged_in'] = False
    flash("Logout successful") 
    return redirect(url_for("index"))

@app.route("/location", methods=["GET"])
def location():
 	return render_template("location.html")

  




if __name__ == "__main__":
    app.run(debug=True)
