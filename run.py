import os
import pymongo
import env
import json
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

url = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["user"]
        username = request.form['username']
        password = request.form['password']
        
        existing_user = mycol.find_one({"username": username})
        print(existing_user)

        if existing_user:
            return "username already exists"

        req = {"username": username, "password": password}

        x = mycol.insert_one(req)

        print(x.inserted_id)


    return render_template("register.html")




@app.route("/login", methods=['POST', 'GET'])
def login():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["user"]

    jsonreq = request.get_json()
    req = {"username": jsonreq["username"], "password": jsonreq["password"]}
    for x in mycol.find(req):
        session["username"] = jsonreq["username"]
        session["password"] = jsonreq["password"]
        print(session["username"])
        return "Login succeed"

    return abort(404)


@app.route("/logout")
def logout():
    try:
         session.pop("username", None)
    finally:
        return "Logged out"

@app.route("/states", methods=['GET'])
def get_states():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["state"]
    states = mycol.find()

    return states




"""
Opening server 
"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


