import sqlite3

conn = sqlite3.connect('vtube.db')  


cursor = conn.cursor()

#admin table
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin(
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_email TEXT NOT NULL,
    admin_password TEXT NOT NULL
)
''')

#comment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS comment(
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_id INTEGER FORIGN KEY,
    video_id INTEGER FORIGN KEY,
    comment_text TEXT NOT NULL,
    comment_datetime TEXT  -- Storing datetime as text (ISO 8601 format)
)
''')

#like table
cursor.execute('''
CREATE TABLE IF NOT EXISTS like(
    like_id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_id INTEGER FORIGN KEY,
    video_id INTEGER FORIGN KEY,
    like_datetime TEXT  -- Storing datetime as text (ISO 8601 format)
)
''')

#register table
cursor.execute('''
CREATE TABLE IF NOT EXISTS register(
    register_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL,
    phoneno TEXT NOT NULL,
    password TEXT NOT NULL,
    profile_image TEXT,
    age TEXT NOT NULL,
    gender TEXT NOT NULL,
    security_question TEXT NOT NULL,
    ans TEXT NOT NULL,
    register_datetime TEXT  -- Storing datetime as text (ISO 8601 format)
)
''')

#saved table
cursor.execute('''
CREATE TABLE IF NOT EXISTS saved(
    saved_id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_id INTEGER FORIGN KEY,
    video_id INTEGER FORIGN KEY,
    saved_datetime TEXT  -- Storing datetime as text (ISO 8601 format)
)
''')

#video table
cursor.execute('''
CREATE TABLE IF NOT EXISTS video(
    video_id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_id INTEGER FORIGN KEY,
    video_liked INTEGER NOT NULL,
    video_duration TEXT NOT NULL,
    video_title TEXT NOT NULL,
    video_category TEXT NOT NULL,
    video_formet TEXT NOT NULL,
    video TEXT NOT NULL,
    video_comment TEXT NOT NULL,
    video_upload_datetime TEXT  -- Storing datetime as text (ISO 8601 format),
    video_upload_location TEXT NOT NULL
)
''')




conn.commit()


cursor.close()
conn.close()


