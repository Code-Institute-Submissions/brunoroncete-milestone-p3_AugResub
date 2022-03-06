import os
import pymongo
import env
from flask_pymongo import PyMongo
from flask import Flask, request, abort, session
from bson.objectid import ObjectId

url = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


@app.route("/register", methods=['POST'])
def register():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["user"]
    jsonreq = request.get_json()
    print(jsonreq)
       
    existing_user = mycol.find_one({"username": jsonreq["username"]})
    print(existing_user)

    if existing_user:
        return "username already exists"

    req = {"username": jsonreq["username"], "password": jsonreq["password"]}

    x = mycol.insert_one(req)

    print(x.inserted_id)


    return "Successful registration"




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
    if "username" in session:
        session.pop("username")
        print(session("username"))
    return "Logged out"

@app.route("/states", methods=['GET', 'POST'])
def get_states():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["states"]
    states = mycol.find("")

    return render_template("states.html")




"""
Opening server on port 5000
"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


