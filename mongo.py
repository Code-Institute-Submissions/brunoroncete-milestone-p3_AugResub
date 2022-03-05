import os
import pymongo
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "MyFirstDB"
COLLECTION = "State"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


documents = coll.find()

for doc in documents:
    print(doc)

myregion = [
    {"Region":"South-east"},
    {"Region":"North-east"},
    {"Region":"South"},
    {"Region":"North"},
    {"Region":"North-east"},
    {"Region":"Central-east"},
    {"Region":"Central-west"}]

x = coll.insert_many(myregion)

print(x.inserted_ids)

mystate = {"State":"Espirito Santo", "Region": myregion[0]}


y = coll.insert_one(mystate)

print(y.inserted_id)

