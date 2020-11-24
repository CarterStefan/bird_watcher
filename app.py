import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


# ENVIRONMENT VARIABLES
app = Flask(__name__)
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# PAGE FOR USER REGISTRATION
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


# PAGE FOR USER LOGIN
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


# PAGE FOR USER LOGOUT
@app.route("/logout")
def logout():

    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# HOMEPAGE
@app.route("/")
@app.route("/home")
def home():
    if session.get('user'):
        # Gets the list of birds seen for user from the DB
        birds_seen = mongo.db.bird_sightings.find(
            {"username": session["user"]}).sort(
            "bird_name", 1)

        all_birds = mongo.db.bird_species.find()

        # Gets the number of birds seen for a user
        number = birds_seen.count()

        # Gets the total number of birds on DB
        bird_count = all_birds.count()

        return render_template(
            "home.html",
            number=number,
            bird_count=bird_count)

    return redirect(url_for("login"))


# VIEW ALL BIRDS ON DB
@app.route("/uk_birds")
def uk_birds():
    # Get all bird species from DB and sort alpabetically
    bird_species = mongo.db.bird_species.find().sort("bird_name", 1)
    bird_family = mongo.db.bird_family.find().sort("family_name", 1)
    return render_template(
        "bird_species.html", bird_species=bird_species,
        bird_family=bird_family)


# SEARCH FUNCTION TO FILTER BY BIRD SPECIES
@app.route("/search", methods=["GET", "POST"])
def search():
    # Get bird families from DB
    bird_family = mongo.db.bird_family.find().sort("family_name", 1)
    # Select to search by bird family
    bird_family_search = request.form.get("bird_family_search")
    bird_species = mongo.db.bird_species.find({
        "$text": {"$search": '"'+bird_family_search+'"'}}).sort(
            "bird_name", 1)

    # Flash message if no results found
    if bird_species.count() < 1:
        flash("No bird matched this search, please try another family")
        return redirect(url_for("uk_birds"))

    # Return search results
    return render_template(
        "bird_species.html", bird_species=bird_species,
        bird_family=bird_family)


# PAGE TO VIEW SPECIFIC BIRD INFORMATION
# BIRD_ID PASSED IN FROM CLICK ON UK BIRDS PAGE
@app.route("/view_bird/<bird_id>")
def view_bird(bird_id):

    if session.get('user'):
        # Get information about specific bird clicked on from DB
        bird = mongo.db.bird_species.find_one({"_id": ObjectId(bird_id)})

        # Check for existing sighting
        existing_sighting = mongo.db.bird_sightings.find({
            "username": session["user"]})

        for sighting in existing_sighting:
            if bird_id == str(sighting["bird_id"]):
                flash("You have seen this bird")

        return render_template("view_bird.html", bird=bird)

    return redirect(url_for("login"))


# PAGE FOR USERS REPORTED SIGHTINGS
@app.route("/my_sightings", methods=["GET", "POST"])
def my_sightings():

    # Show my sightings page if user is logged in
    if session.get('user'):
        # Gets the session users username from the DB
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Gets the list of birds seen for user from the DB
        birds_seen = mongo.db.bird_sightings.find(
            {"username": session["user"]}).sort(
            "bird_name", 1)

        all_birds = mongo.db.bird_species.find()

        # Gets the number of birds seen for a user
        number = birds_seen.count()

        # Get total number of birds from DB
        bird_count = all_birds.count()

        if number == bird_count:
            flash("Challenge Completed")

        return render_template(
            "my_sightings.html",
            username=username,
            number=number,
            birds_seen=birds_seen,
            bird_count=bird_count)

    # Show login page if user is logged out
    return redirect(url_for("login"))


# PAGE TO REPORT NEW SIGHTING
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
                "location": request.form.get("location"),
                "bird_image": mongo.db.bird_species.find_one(
                    {"bird_name": request.form.get(
                        "bird_seen")})["image"]
            }

            # Check for existing sighting
            existing_sighting = mongo.db.bird_sightings.find({
                "username": session["user"]})

            new_sighting = request.form.get("bird_seen")

            for bird in existing_sighting:
                if new_sighting == bird["bird_name"]:
                    flash(
                        "You have seen this bird already, please try another")
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


# FUNCTION TO REMOVE USER SIGHTING
# BIRD_NAME PASSED IN FROM CLICK ON MY_SIGHTINGS PAGE
@app.route("/remove_sighting/<bird_name>", methods=["GET", "POST"])
def remove_sighting(bird_name):
    mongo.db.bird_sightings.remove({
        "username": session["user"], "bird_name": bird_name})
    flash("Sighting Deleted")
    return redirect(url_for("my_sightings"))


# PAGE TO ADD NEW BIRD IF USER IS ADMIN
@app.route("/add_new_bird/", methods=["GET", "POST"])
def add_new_bird():
    # Get bird families from the database
    bird_family = mongo.db.bird_family.find().sort("family_name", 1)

    # Add bird to database using form when user clicks submit
    if request.method == "POST":
        bird = {
            "bird_name": request.form.get("bird_name"),
            "scientific_name": request.form.get("scientific_name"),
            "length": request.form.get("length"),
            "wingspan": request.form.get("wingspan"),
            "weight": request.form.get("weight"),
            "description": request.form.get("description"),
            "where": request.form.get("where"),
            "image": request.form.get("image"),
            "feeding": request.form.get("feeding"),
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
    if session.get('user') == 'admin':
        return render_template("add_new_bird.html", bird_family=bird_family)

    return redirect(url_for("uk_birds"))


# PAGE TO EDIT INFORMATION ABOUT SPECIFIC BIRD
# BIRD_ID PASSED IN FROM CLICK ON VIEW BIRD
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
            "where": request.form.get("where"),
            "feeding": request.form.get("feeding"),
            "image": request.form.get("image"),
            "bird_family": request.form.get("bird_family"),
            "added_by": session["user"]
        }
        mongo.db.bird_species.update({"_id": ObjectId(bird_id)}, bird_submit)
        flash("Thankyou, your edit was successful")

    # Get existing information about bird from DB
    bird = mongo.db.bird_species.find_one({"_id": ObjectId(bird_id)})

    # Get bird family options for dropdown from DB
    bird_family = mongo.db.bird_family.find().sort("family_name", 1)

    # Show form to edit a birds information if logged in
    if session.get('user') == 'admin':
        return render_template(
            "edit_bird.html", bird=bird, bird_family=bird_family)

    return redirect(url_for("home"))


# PAGE TO DELETE USERS ACCOUNT FROM DB
@app.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    if session.get('user'):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        return render_template("delete_account.html", username=username)

    return redirect(url_for("login"))


# PAGE TO CONFIRM ACCOUNT DELETION FROM DB
@app.route("/delete_account_confirmation", methods=["GET", "POST"])
def delete_account_confirmation():
    mongo.db.users.remove({"username": session["user"]})
    flash("User Deleted")
    session.pop("user")
    return redirect(url_for("register"))


# PAGE TO REPORT ERROR ON THE SITE
@app.route("/report_error", methods=["GET", "POST"])
def report_error():
    if session.get('user'):
        bird_species = mongo.db.bird_species.find().sort("bird_name", 1)
        if request.method == "POST":
            error = {
                "username": session["user"],
                "bird_name": request.form.get("bird_seen"),
                "description": request.form.get("description")
            }
            mongo.db.errors.insert_one(error)
            flash("Thankyou, your error has been reported")
            return redirect(url_for("uk_birds"))

        return render_template("report_error.html", bird_species=bird_species)

    return redirect(url_for("login"))


# PAGE TO VIEW ERRORS IF USER IS ADMIN
@app.route("/admin_errors", methods=["GET", "POST"])
def admin_errors():
    if session.get('user') == 'admin':
        errors = mongo.db.errors.find()
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "admin_errors.html", errors=errors, username=username)

    return redirect(url_for("uk_birds"))


# FUNCTION TO MARK ERROR AS RESOLVED - ERROR_ID PASSED IN FROM ERRORS PAGE
@app.route("/delete_error/<error_id>", methods=["GET", "POST"])
def delete_error(error_id):
    mongo.db.errors.remove({"_id": ObjectId(error_id)})
    flash("Error Resolved")
    return redirect(url_for("admin_errors"))


# PAGE FOR ERROR HANDLER 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
