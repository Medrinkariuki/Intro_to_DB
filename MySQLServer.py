import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Ruthkimani12"  # Your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Failed to connect or create database: {e}")

finally:
    # Close connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")