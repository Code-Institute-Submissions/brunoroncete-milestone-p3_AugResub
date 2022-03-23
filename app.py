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
    {"state": "Acre"},
    {"state": "Alagoas"},
    {"state": "Amapa"},
    {"state": "Amazonas"},
    {"state": "Bahia"},
    {"state": "Ceara"},
    {"state": "Distrito Federal"},
    {"state": "Espirito Santo"},
    {"state": "Goias"},
    {"state": "Maranhao"},
    {"state": "Mato Grosso"},
    {"state": "Mato Grosso do Sul"},
    {"state": "Minas Gerais"},
    {"state": "Para"},
    {"state": "Paraiba"},
    {"state": "Parana"},
    {"state": "Pernambuco"},
    {"state": "Piaui"},
    {"state": "Rio de Janeiro"},
    {"state": "Rio Grande do Norte"},
    {"state": "Rio Grande do Sul"},
    {"state": "Rondonia"},
    {"state": "Roraima"},
    {"state": "Santa Catarina"},
    {"state": "Sao Paulo"},
    {"state": "Sergipe"},
    {"state": "Tocantins"}
    ]

y = coll.insert_many(mystates)

print(y.inserted_ids)

coll = conn[DATABASE][USERS]

myuser = {"username": "bruno123", "password": "12345", "email":"blabla@bla.com" }

user1 = coll.insert_one(myuser)
