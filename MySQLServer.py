import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Ruthkimani12"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database 'alxbookstore' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()