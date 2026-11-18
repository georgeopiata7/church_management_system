from db import connect_db

try: 
    connection = connect_db()

    if connection.is_connected():
        print("connected successfully")
except Exception as e:
    print("Database connection failed", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

