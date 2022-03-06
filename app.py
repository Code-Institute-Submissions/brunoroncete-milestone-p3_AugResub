import os
import pymongo
import env
from flask_pymongo import PyMongo

url = os.environ.get("MONGO_URI")


DATABASE = "GranTurismo"
STATES = "state"
HOTELS = "hotel"
USERS = "user"
COMMENTS = "comment"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(url)

coll = conn[DATABASE][STATES]

mystates = [
    {"state": "Espirito Santo"},
    {"state": "Sao Paulo"},
    {"state": "Rio de Janeiro"},
    {"state": "Bahia"},
    {"state": "Pernambuco"},
    {"state": "Ceara"},
    {"state": "Rio Grande do Sul"},
    {"state": "Santa Catarina"}
    ]

y = coll.insert_many(mystates)

print(y.inserted_ids)

coll = conn[DATABASE][HOTELS]

myhotel = [{"hotel": "Ibis", "state": y.inserted_ids[0]}]

z = coll.insert_many(myhotel)

print(z.inserted_ids)

coll = conn[DATABASE][USERS]

myuser = {"Username": "bruno123", "Password": "12345"}

user1 = coll.insert_one(myuser)

coll = conn[DATABASE][COMMENTS]

mycomment = {"comment": "hello", "user": user1.inserted_id, "hotel": z.inserted_ids[0]}

comment1 = coll.insert_one(mycomment)
