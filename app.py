import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Page for all birds on DB
@app.route("/uk_birds")
def uk_birds():
    bird_species = mongo.db.bird_species.find()
    return render_template("bird_species.html", bird_species=bird_species)


# Page for user registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # This will check if the username exists in the DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username taken, please choose another or login")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("my_sightings", username=session["user"]))

    return render_template("register.html")


# Page for user login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # This will check if the username exists in the DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check hashed password matched user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "my_sightings", username=session["user"]))
            else:
                # Password does not match
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            #Username does not exist
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Page for users bird sightings
@app.route("/my_sightings/<username>", methods=["GET", "POST"])
def my_sightings(username):
    # Gets the session users username from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_sightings.html", username=username)

    return redirect(url_for("login"))


# Page for logging user out
@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/report_sighting/<username>", methods=["GET", "POST"])
def report_sighting(username):
    # Gets list of bird species from the DB
    bird_species = mongo.db.bird_species.find()
    # Gets the session users username from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("report_sighting.html", username=username, bird_species=bird_species)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
