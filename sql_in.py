import sqlite3

def init_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS register_user (
            reg_id INTEGER PRIMARY KEY,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phoneno TEXT NOT NULL,
            password TEXT NOT NULL,
            
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            security_question TEXT NOT NULL,
            ans TEXT NOT NULL,
            date_time TEXT NOT NULL,
            profile_image TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call init_db() once to create the database and table
init_db()
