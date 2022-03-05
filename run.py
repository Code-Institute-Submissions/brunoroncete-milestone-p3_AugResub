import os
import pymongo
import env
from flask import Flask, request, abort

url = os.environ.get("MONGO_URI")

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["User"]

    x = mycol.find_one()

    for x in mycol.find({"Username": "bruno123", "Password": "12345"}):
        return "Login succeed"

    abort(404)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
