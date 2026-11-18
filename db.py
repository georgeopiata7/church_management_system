import mysql.connector
import os
from dotenv import load_dotenv

#Load information from .env

load_dotenv()

def connect_db():
    connection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_CHURCH_MANAGEMENT_DB")

    )


    return connection