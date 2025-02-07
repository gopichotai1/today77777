import sqlite3

# Connect to the SQLite database (replace 'example.db' with your database file)
conn = sqlite3.connect('vtube.db')
cursor = conn.cursor()

try:
    # Execute a SELECT query to get all records from a table (e.g., 'users')
    cursor.execute("SELECT * FROM admin")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Loop through the rows and print each record
    for row in rows:
        print(row)  # You can format this to show specific columns if needed

except sqlite3.DatabaseError as e:
    print(f"Error fetching records: {e}")

finally:
    # Close the connection to the database
    conn.close()


'''insert_query = 'INSERT INTO admin (admin_email,admin_password) VALUES (?, ?)'


data = ('saloni@gmail.com','saloni')'''
