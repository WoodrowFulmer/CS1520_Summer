from flask import Flask, request, abort, url_for, redirect, session, render_template, Blueprint
from data import users

"""
***Blueprint for registration view
"""
#***
registration_blueprint = Blueprint('registration', __name__, template_folder = 'templates')

#***
@registration_blueprint.route("/register/", methods=["GET", "POST"])
def register():
	# first check if the user is already logged in
	if "username" in session:
		return redirect(url_for("profile.profile", username=session["username"]))
		
	# if not, and the incoming request is via POST try to log them in
	elif request.method == "POST":
		if (not request.form["user"] in users) and (request.form["pass"] == request.form["verify"]):
			session["username"] = request.form["user"]
			users.update({request.form["user"]:request.form["pass"]})
			#*** need to specify the blueprint name and view
			return redirect(url_for("profile.profile", username=session["username"]))
			
	return render_template("createProf.html")