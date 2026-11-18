from flask import Flask, render_template, request , flash, redirect, url_for, session
from werkzeug.security import generate_password_hash
from db import connect_db
import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector

#Create flask Application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
@app.route('/')
def home():
    return render_template("user.html")

#User registration router
@app.route("/register_user", methods = ["POST"])
def register_user():
    full_name = request.form.get("full_name").strip()
    email = request.form.get("email").strip()
    password = request.form.get("password").strip()
    contact = request.form.get("contact").strip()
    role = request.form.get("role").strip()


    #Hashing the password
    hashed_password = generate_password_hash(password)
    connection = None
    cursor = None

    try:
        #Connect to Msql database
        connection = connect_db()

        #create cursor
        cursor = connection.cursor()

        #Sql query

        sql = """
        INSERT INTO users(full_name, email, password, contact, role)
        VALUES(%s, %s, %s, %s, %s)
        """

        #Execute query

        cursor.execute(sql, (
            full_name, email, hashed_password, contact, role
        ))

        #Save changes
        connection.commit()

        session['user_email'] = email

        return redirect(url_for("dashboard"))

    except Exception as e:
        #Cancel changes if error occur

        if connection:
            connection.rollback()

        return f"An error occured: {e}"

    finally:
        #Close connection and cursor
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


@app.route('/dashboard')
def dashboard():

    #if 'username' not in session:
       # return redirect("/")

    return render_template("dashboard.html")

   

@app.route("/announcement")
def announcement():
    #Check whethter user is logged in
    if 'user_email' not in session:
        return redirect('/')
    connection = None
    cursor = None

    try:
        #Connect to msql
        connection = connect_db()

        #Create cursor
        cursor = connection.cursor(dictionary=True)

        #Retrieve announcement from the msql

        sql ="""
        SELECT id, title, message, date_posted
        FROM announcement
        ORDER BY date_posted DESC

        """

        cursor.execute(sql)

        #Get all announcements
        announcement = cursor.fetchall()

        #Send announcement to html page

        return render_template("announcement.html", announcement = announcement)

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()




    


    

    


 





#Run Application
if __name__ =="__main__":
    app.run(debug=True)



