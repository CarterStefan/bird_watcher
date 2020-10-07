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


app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


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
            "password": generate_password_hash(request.form.get("password")),
            "birds_seen": []
        }
        mongo.db.users.insert_one(register)

        # put the user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("my_sightings"))

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
                    "my_sightings"))
            else:
                # Password does not match
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # Username does not exist
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Page for logging user out
@app.route("/logout")
def logout():

    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Page for all birds on DB
@app.route("/uk_birds")
def uk_birds():
    # Get all bird species from DB and sort alpabetically
    bird_species = mongo.db.bird_species.find().sort("bird_name", 1)
    bird_family = mongo.db.bird_family.find().sort("name", 1)
    return render_template(
        "bird_species.html", bird_species=bird_species,
        bird_family=bird_family)


# Search function on view all birds
@app.route("/search", methods=["GET", "POST"])
def search():
    # Get bird families from DB
    bird_family = mongo.db.bird_family.find().sort("name", 1)
    # Select to search by bird family
    bird_family_search = request.form.get("bird_family_search")
    bird_species = mongo.db.bird_species.find({
        "$text": {"$search": bird_family_search}}).sort(
            "bird_name", 1)
    # Return search results
    return render_template(
        "bird_species.html", bird_species=bird_species,
        bird_family=bird_family)


# Page for users bird sightings
@app.route("/my_sightings", methods=["GET", "POST"])
def my_sightings():
    # Show my sightings page if user is logged in
    if session.get('user'):
        # Gets the session users username from the DB
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Gets the list of birds seen for user from the DB
        birds_seen = mongo.db.bird_sightings.find(
            {"username": session["user"]})

        # Gets the number of birds seen for a user
        number = birds_seen.count()

        return render_template(
            "my_sightings.html",
            username=username,
            number=number,
            birds_seen=birds_seen)

    # Show login page if user is logged out
    return redirect(url_for("login"))


# Page to report new sighting
@app.route("/report_sighting", methods=["GET", "POST"])
def report_sighting():
    if session.get('user'):
        counties = mongo.db.counties.find().sort("county_name", 1)
        bird_species = mongo.db.bird_species.find().sort("bird_name", 1)
        if request.method == "POST":
            new_bird_sighting = {
                "username": session["user"],
                "bird_name": request.form.get("bird_seen"),
                "bird_id": mongo.db.bird_species.find_one({
                    "bird_name": request.form.get(
                        "bird_seen")})["_id"],
                "date_seen": request.form.get("date_seen"),
                "location": request.form.get("location")
            }

            # Check for existing sighting
            existing_sighting = mongo.db.bird_sightings.find({
                "username": session["user"]})

            new_sighting = request.form.get("bird_seen")

            for bird in existing_sighting:
                if new_sighting == bird["bird_name"]:
                    flash("You have seen this bird already, please try another")
                    return redirect(url_for("report_sighting"))

            # Adds new sighting to DB
            mongo.db.bird_sightings.insert_one(new_bird_sighting)
            flash("Thankyou, your sighting has been added")
            return redirect(url_for("my_sightings"))

        return render_template(
            "report_sighting.html",
            bird_species=bird_species,
            counties=counties)

    return redirect(url_for("login"))


# Page to add new bird
@app.route("/add_new_bird/", methods=["GET", "POST"])
def add_new_bird():
    # Get bird families from the database
    bird_family = mongo.db.bird_family.find().sort("name", 1)

    # Add bird to database using form when user clicks submit
    if request.method == "POST":
        bird = {
            "bird_name": request.form.get("bird_name"),
            "scientific_name": request.form.get("scientific_name"),
            "length": request.form.get("length"),
            "wingspan": request.form.get("wingspan"),
            "weight": request.form.get("weight"),
            "description": request.form.get("description"),
            "feeding": request.form.get("feeding"),
            "where": request.form.get("where"),
            "image": request.form.get("image"),
            "bird_family": request.form.get("bird_family"),
            "added_by": session["user"]
        }
        # This will check if the bird name exists in the DB
        existing_bird = mongo.db.bird_species.find_one(
            {"bird_name": request.form.get("bird_name").lower()})
        # If it does, flash message to user and reload form
        if existing_bird:
            flash("Bird already added")
            return redirect(url_for("add_new_bird"))
        # Else add bird to DB
        mongo.db.bird_species.insert_one(bird)
        flash("Thankyou, your bird has been added")
        if request.form.get("add_to_sightings"):
            return redirect(url_for("report_sighting"))

        return redirect(url_for("uk_birds"))

    # Display form to add new bird and pass in bird families from db
    # if user is logged in
    if session.get('user'):
        return render_template("add_new_bird.html", bird_family=bird_family)

    return redirect(url_for("login"))


# View a specific bird
@app.route("/view_bird/<bird_id>")
def view_bird(bird_id):
    # Get information about specific bird clicked on from DB
    bird = mongo.db.bird_species.find_one({"_id": ObjectId(bird_id)})

    return render_template("view_bird.html", bird=bird)


# Page to edit information about a bird
@app.route("/edit_bird/<bird_id>", methods=["GET", "POST"])
def edit_bird(bird_id):
    # Edit bird on database when user clicks submit
    if request.method == "POST":
        bird_submit = {
            "bird_name": request.form.get("bird_name"),
            "scientific_name": request.form.get("scientific_name"),
            "length": request.form.get("length"),
            "wingspan": request.form.get("wingspan"),
            "weight": request.form.get("weight"),
            "description": request.form.get("description"),
            "feeding": request.form.get("feeding"),
            "where": request.form.get("where"),
            "image": request.form.get("image"),
            "bird_family": request.form.get("bird_family"),
            "added_by": session["user"]
        }
        mongo.db.bird_species.update({"_id": ObjectId(bird_id)}, bird_submit)
        flash("Thankyou, your edit was successful")

    # Get existing information about bird from DB
    bird = mongo.db.bird_species.find_one({"_id": ObjectId(bird_id)})
    # Get bird family options for dropdown from DB
    bird_family = mongo.db.bird_family.find().sort("name", 1)
    # Show form to edit a birds information if logged in
    if session.get('user'):
        return render_template(
            "edit_bird.html", bird=bird, bird_family=bird_family)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
