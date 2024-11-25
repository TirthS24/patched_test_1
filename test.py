import sqlite3

def login_user(username, password):
    # Vulnerable query: directly embedding user input into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    print("Executing query:", query)
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")
