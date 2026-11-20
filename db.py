import mysql.connector
import os
from dotenv import load_dotenv

#Load information from .env

load_dotenv()

print("MYSQLHOST:", repr(os.getenv("MYSQLHOST")))
print("MYSQLPORT:", repr(os.getenv("MYSQLPORT")))
print("MYSQLUSER:", repr(os.getenv("MYSQLUSER")))
print("MYSQLDATABASE:", repr(os.getenv("MYSQLDATABASE")))


def connect_db():
    connection = mysql.connector.connect(
        host = os.getenv("MYSQLHOST"),
        port = int(os.getenv("MYSQLPORT")),
        user = os.getenv("MYSQLUSER"),
        password = os.getenv("MSQLPASSWORD"),
        database = os.getenv("MYSQLDATABASE")

    )


    return connection