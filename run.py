import os
import pymongo
import env
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

url = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return redirect("hotels")

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["user"]
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))
        
        existing_user = mycol.find_one({"username": username})
        print(existing_user)

        if existing_user:
            flash ("username already exists")
            return redirect(url_for("register"))

        req = {"username": username, "password": password}

        x = mycol.insert_one(req)

        print(x.inserted_id)
        flash("Registration Successful!")


    return render_template("register.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["user"]
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = mycol.find_one({"username": username})

        if existing_user:
            if check_password_hash(
                existing_user["password"], password):
                    session["user"] = username
                    flash("Welcome, {}".format(username))
                    return redirect(url_for("get_states"))
                
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
                
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user", None)
    
    return redirect(url_for("get_states"))


@app.route("/states", methods=['GET'])
def get_states():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["state"]
    print(list(mycol.find()))
    return render_template("states.html", states = list(mycol.find()))


@app.route("/add_hotel", methods=['POST','GET'])
def add_hotel():
    if request.method == "POST":
        myclient = pymongo.MongoClient(url)
        mydb = myclient["GranTurismo"]
        mycol = mydb["hotel"]
        name = request.form.get('hotel_name')
        description = request.form.get('hotel_description')
        img_url = request.form.get('img_url')
        hotel_link = request.form.get('hotel_link')
        
        
        existing_hotel = mycol.find_one({"name": name})
        
        if existing_hotel:
            flash ("Hotel already exists")
            return redirect(url_for("add_hotel"))

        req = {"name": name, "description": description, "img_url" : img_url, "hotel_link" : hotel_link}

        x = mycol.insert_one(req)
        
        return redirect(url_for("hotel_mngt"))

    if "user" in session :
        return render_template("add_hotel.html")
 
    return redirect(url_for("login"))

@app.route("/hotels", methods=['POST','GET'])
def hotels():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["hotel"]
        
    return render_template("hotels.html", hotels = list(mycol.find()))

@app.route("/hotel_mngt", methods=['POST','GET'])
def hotel_mngt():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["hotel"]
        
    return render_template("hotel_mngt.html", hotels = list(mycol.find()))

@app.route("/edit", methods=['POST','GET'])
def edit():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["hotel"]
    hotel_id = request.args.get('id')
  
    if request.method == "POST":
        name = request.form.get('hotel_name')
        description = request.form.get('hotel_description')
        img_url = request.form.get('img_url')
        hotel_link = request.form.get('hotel_link')
        req = {"name": name, "description": description, "img_url" : img_url, "hotel_link" : hotel_link }
        mycol.update_one({"_id": ObjectId(hotel_id)}, {"$set": req}, upsert=False)
        return redirect(url_for("hotel_mngt"))
  
    if not hotel_id:
        return redirect(url_for("hotel_mngt"))

    hotel = mycol.find_one({"_id": ObjectId(hotel_id)})
    
    if "user" in session :
        return render_template("edit.html", hotel = hotel)
 
    return redirect(url_for("login"))

@app.route("/delete", methods=['POST','GET'])
def delete():
    myclient = pymongo.MongoClient(url)
    mydb = myclient["GranTurismo"]
    mycol = mydb["hotel"]
    hotel_id = request.args.get('id')

    if not hotel_id:
        return redirect(url_for("hotel_mngt"))
    
    mycol.delete_one({"_id": ObjectId(hotel_id)})
    
    return redirect(url_for("hotel_mngt"))



"""
Opening server 
"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


