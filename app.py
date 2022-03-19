import os
import pymongo
import env
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

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

myhotel = [
    {"hotel": "A", "state": y.inserted_ids[0]},
    {"hotel": "B", "state": y.inserted_ids[0]},
    {"hotel": "C", "state": y.inserted_ids[1]},
    {"hotel": "D", "state": y.inserted_ids[1]},
    {"hotel": "E", "state": y.inserted_ids[2]},
    {"hotel": "F", "state": y.inserted_ids[2]},
    {"hotel": "G", "state": y.inserted_ids[3]},
    {"hotel": "H", "state": y.inserted_ids[3]},
    {"hotel": "I", "state": y.inserted_ids[4]},
    {"hotel": "J", "state": y.inserted_ids[4]},
    {"hotel": "K", "state": y.inserted_ids[5]},
    {"hotel": "L", "state": y.inserted_ids[5]},
    {"hotel": "M", "state": y.inserted_ids[6]},
    {"hotel": "N", "state": y.inserted_ids[6]},
    {"hotel": "O", "state": y.inserted_ids[7]},
    {"hotel": "P", "state": y.inserted_ids[7]},
    ]

z = coll.insert_many(myhotel)

print(z.inserted_ids)

coll = conn[DATABASE][USERS]

myuser = {"username": "bruno123", "password": "12345", "email":"blabla@bla.com" }

user1 = coll.insert_one(myuser)

coll = conn[DATABASE][COMMENTS]

mycomment = {"comment": "hello", "user": user1.inserted_id, "hotel": z.inserted_ids[0]}

comment1 = coll.insert_one(mycomment)
