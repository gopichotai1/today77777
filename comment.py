import sql.py 

# Insert a new event with the current datetime
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # ISO 8601 format

cursor.execute("INSERT INTO events (event_name, event_datetime) VALUES (?, ?)", 
               ('Sample Event', current_datetime))

# Commit changes and close the connection
conn.commit()
conn.close()
