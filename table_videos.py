import sqlite3

DATABASE = 'user.db'
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS videos (
                        video_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        filename TEXT NOT NULL,
                        upload_time TEXT NOT NULL,
                        username TEXT NOT NULL,
                        category TEXT NOT NULL,
                        likes INTEGER,
                        reg_id INTEGER,
                        FOREIGN KEY (reg_id) REFERENCES user(reg_id))''')
        

def db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

         
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS likes (
    reg_id INTEGER,
    video_id INTEGER,
    PRIMARY KEY (reg_id, video_id),
    FOREIGN KEY (reg_id) REFERENCES register_user(reg_id),
    FOREIGN KEY (video_id) REFERENCES videos(video_id)
    )''')
    conn.commit()
    conn.close()

init_db()
db()
