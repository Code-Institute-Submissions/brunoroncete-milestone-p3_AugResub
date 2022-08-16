import os
import pymongo

from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

if os.path.exists("env.py"):
    import env

DEBUG = True

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
    {"state": "Acre", "img_url" : ""},
    {"state": "Alagoas", "img_url" : "https://images.unsplash.com/photo-1565310104425-8cb0ae3228d2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80"},
    {"state": "Amapa", "img_url" : ""},
    {"state": "Amazonas", "img_url" : "https://images.unsplash.com/photo-1574238959725-c727a8f8b4a0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"},
    {"state": "Bahia", "img_url" : "https://images.unsplash.com/photo-1603237568326-e7c5adde84ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=667&q=80"},
    {"state": "Ceara", "img_url" : "https://images.unsplash.com/photo-1623524160429-e7895627f024?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1632&q=80"},
    {"state": "Distrito Federal", "img_url" : "https://images.unsplash.com/photo-1591297545337-212cc106ee6f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80"},
    {"state": "Espirito Santo", "img_url" : "https://images.unsplash.com/photo-1627663412342-d77cd974e9ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80"},
    {"state": "Goias", "img_url" : ""},
    {"state": "Maranhao", "img_url" : "https://images.unsplash.com/photo-1566296942542-b15c4da81c06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8bWFyYW5oYW98ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"},
    {"state": "Mato Grosso", "img_url" : "#"},
    {"state": "Mato Grosso do Sul", "img_url" : "#"},
    {"state": "Minas Gerais", "img_url" : "https://images.unsplash.com/photo-1605045629496-fa725dec5d93?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032&q=80"},
    {"state": "Para", "img_url" : "#"},
    {"state": "Paraiba", "img_url" : "#"},
    {"state": "Parana", "img_url" : "#"},
    {"state": "Pernambuco", "img_url" : "https://images.unsplash.com/photo-1583214552082-dff0bb815203?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"},
    {"state": "Piaui", "img_url" : "#"},
    {"state": "Rio de Janeiro", "img_url" : "https://images.unsplash.com/photo-1516306580123-e6e52b1b7b5f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1526&q=80"},
    {"state": "Rio Grande do Norte", "img_url" : "#"},
    {"state": "Rio Grande do Sul", "img_url" : "#"},
    {"state": "Rondonia", "img_url" : "#"},
    {"state": "Roraima", "img_url" : "#"},
    {"state": "Santa Catarina", "img_url" : "#"},
    {"state": "Sao Paulo", "img_url" : "https://images.unsplash.com/photo-1578002573559-689b0abc4148?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"},
    {"state": "Sergipe", "img_url" : "https://images.unsplash.com/photo-1574179556294-d2d21a8e9707?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c2VyZ2lwZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"},
    {"state": "Tocantins", "img_url" : "#"}
    ]

y = coll.insert_many(mystates)

print(y.inserted_ids)

coll = conn[DATABASE][USERS]

myuser = {"username": "bruno123", "password": "12345", "email":"blabla@bla.com" }

user1 = coll.insert_one(myuser)
