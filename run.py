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


"""
Login 
"""


@app.route("/login", methods=['POST', 'GET'])
def login():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["user"]

    jsonreq = request.get_json()
    req = {"Username": jsonreq["Username"], "Password": jsonreq["Password"]}
    for x in mycol.find(req):
        session["Username"] = jsonreq["Username"]
        session["Password"] = jsonreq["Password"]
        print(session["Username"])
        return "Login succeed"

    return abort(404)


@app.route("/logout")
def logout():
    if "Username" in session:
        session.pop("Username")
        print(session("Username"))
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
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True,
    )


