import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Ruthkimani12"
    )

    if connection.is_connected():
        # Create a cursor object
        cursor = connection.cursor()
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database 'alxbookstore' created successfully!")

except mysql.connector.Error as err:
    # Handle MySQL-specific errors
    print(f"Error: {err}")

finally:
    # Close cursor and connection if they exist
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()