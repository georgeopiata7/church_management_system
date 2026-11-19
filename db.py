import mysql.connector
import os
from dotenv import load_dotenv

#Load information from .env

load_dotenv()

def connect_db():
    connection = mysql.connector.connect(
        host = os.getenv("MYSQLHOST"),
        port = int(os.getenv("MSQLPORT")),
        user = os.getenv("MSQLUSER"),
        password = os.getenv("MSQLPASSWORD"),
        database = os.getenv("MYSQLDATABASE")

    )


    return connection