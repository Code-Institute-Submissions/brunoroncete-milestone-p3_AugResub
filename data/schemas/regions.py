import os
import pymongo
import env
import connection

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = os.environ.get("DATABASE")


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