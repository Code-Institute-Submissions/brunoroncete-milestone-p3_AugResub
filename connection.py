import os
import pymongo
import env

url = os.environ.get("MONGO_URI")

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(url)

dblist = conn.list_database_names()
if not "granturismo" in dblist:
  mydb = conn["granturismo"]
