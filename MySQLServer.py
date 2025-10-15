import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'spic3s',
        password = 'StrongPassword123!'
    )

    cursor = mydb.cursor()

    cursor.execute("""  
        CREATE DATABASE IF NOT EXISTS alx_book_store;
    """)

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"{err}")

finally:
    cursor.close()
    mydb.close()
