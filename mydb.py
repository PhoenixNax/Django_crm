# Install MySQL
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

try:
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NixNax1@"
    )
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT USER(), VERSION()")
    print(cursorObject.fetchone())
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS mydb")
    print("All Done!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'cursorObject' in locals():
        cursorObject.close()
    if 'dataBase' in locals() and dataBase.is_connected():
        dataBase.close()