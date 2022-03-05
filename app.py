import os
import pymongo
import env

url = os.environ.get("MONGO_URI")


DATABASE = "GranTurismo"
STATES = "State"
HOTELS = "Hotel"
USERS = "User"
COMMENTS = "Comment"


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
    {"State": "Espirito Santo"},
    {"State": "Sao Paulo"},
    {"State": "Rio de Janeiro"},
    {"State": "Bahia"},
    {"State": "Pernambuco"},
]

y = coll.insert_many(mystates)

print(y.inserted_ids)

coll = conn[DATABASE][HOTELS]

myhotel = [
    {"Hotel": "Ibis", "State": y.inserted_ids[0]},
]

z = coll.insert_many(myhotel)

print(z.inserted_ids)

coll = conn[DATABASE][USERS]

myuser = {"Username": "bruno123", "Password": "12345"}

user1 = coll.insert_one(myuser)

coll = conn[DATABASE][COMMENTS]

mycomment = {"comment": "hello", "user": user1.inserted_id, "hotel": z.inserted_ids[0]}

comment1 = coll.insert_one(mycomment)
