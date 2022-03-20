import os
import pymongo
import env
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

url = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=False)


@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["user"]
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))
        
        existing_user = mycol.find_one({"username": username})
        print(existing_user)

        if existing_user:
            flash ("username already exists")
            return redirect(url_for("register"))

        req = {"username": username, "password": password}

        x = mycol.insert_one(req)

        print(x.inserted_id)
        flash("Registration Successful!")


    return render_template("register.html")




@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["user"]
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = mycol.find_one({"username": username})

        if existing_user:
            if check_password_hash(
                existing_user["password"], password):
                    session["user"] = username
                    flash("Welcome, {}".format(username))
                    return redirect(url_for("get_states"))
                   
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
                
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user", None)
    
    return redirect(url_for("get_states"))


@app.route("/states", methods=['GET'])
def get_states():
    if "user" in session:

        return render_template("states.html")

    return redirect(url_for('login'))

@app.route("/hotels", methods=['POST','GET'])
def hotels():
    if request.method == "GET":
        return render_template("hotels.html", states = request.args.get('states'))

    return render_template("hotels.html")




"""
Opening server 
"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


