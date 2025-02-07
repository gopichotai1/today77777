from flask import Flask, redirect , request , render_template, session, url_for
import sqlite3
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import flash
import os
from datetime import timedelta


app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)

# Database setup
DATABASE = 'user.db'

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi'}

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Initialize SQLite DB (if it doesn't exist)


        
@app.route('/like/<int:video_id>', methods=['POST'])
def like_video(video_id):
    user_email = session.get('email')

    if not user_email:
        return redirect(url_for('login'))  # Redirect to login if the user is not logged in

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

   
    # Update the likes count in the videos table
    cursor.execute('UPDATE videos SET likes = likes + 1 WHERE video_id = ?', (video_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))


@app.route('/')
def hello():
    if 'email' in session:
        return render_template('head.html', email=session['email'])
    return redirect(url_for('login'))

@app.route('/admin_head')
def admin_head():
    if 'email' in session:
        return render_template('admin_head.html', email=session['email'])
    return redirect(url_for('login'))

    
@app.route('/home')
def home():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM videos ORDER BY upload_time DESC')
    videos = cursor.fetchall()
        
    # Fetch videos and their like count
    cursor.execute('SELECT * FROM videos')
    videos = cursor.fetchall()

    # Check if the current user has already liked a video (session based)
    reg_id = session.get('reg_id')
    liked_videos = set()

    if reg_id:
        # Get list of video IDs the current user has liked
        cursor.execute('SELECT video_id FROM likes WHERE reg_id = ?', (reg_id,))
        liked_videos_set = cursor.fetchall()
        liked_videos = {video[0] for video in liked_videos_set}  # Set of video ids user has liked

    conn.close()
    
    # Render the template and pass the necessary data
    return render_template('head.html', content='home.html', videos=videos, liked_videos=liked_videos,email=session['email'])

@app.route('/history')
def history():
    if 'email' in session:
        return render_template('head.html', content='history.html',email=session['email'])

@app.route('/search')
def search():
    return render_template('head.html', content='search.html',email=session['email'])

@app.route('/youraccount')
def youraccount():
    return render_template('head.html', content='youraccount.html',email=session['email'])

'''@app.route('/contact')
def contact():
    return render_template('head.html', content='contact.html')'''

@app.route('/edit_profile')
def edit_profile():
    return render_template('head.html', content='edit_profile.html',email=session['email'])

@app.route('/your_video')
def your_video():
    return render_template('head.html', content='your_video.html')

@app.route('/liked_video')
def liked_video():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM videos ORDER BY upload_time DSC')
        videos = cursor.fetchall()
    return render_template('head.html', content='home.html', videos=videos)

   
    return render_template('head.html', content='liked_video.html', videos=videos)

@app.route('/video_upload', methods=['GET', 'POST'])
def video_upload():
    if request.method == 'POST':
        # Get file and user data
        file = request.files['file']
        username = request.form['username']
        category = request.form['category']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Save data to SQLite DB
            upload_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with sqlite3.connect(DATABASE) as conn:
                conn.execute('''INSERT INTO videos (filename, upload_time, username,category,likes)
                                VALUES (?, ?, ? ,?,0 )''', (filename, upload_time, username ,category ))
                conn.commit()
            
            return redirect(url_for('home'))
    
    return render_template('head.html', content='video_upload.html')
    
    

@app.route('/saved_video')
def saved_video():
    return render_template('head.html', content='saved_video.html')


@app.route('/register')
def register():    
    # Data to populate the dropdown list
    dropdown_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    return render_template('register.html', options=dropdown_options)

@app.route('/change_password')
def change_password():
    return render_template('change_password.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgotpass_1.html')

@app.route('/forgotpass_2')
def forgotpass_2():
    return render_template('forgotpass_2.html')

@app.route('/forgotpass_3')
def forgotpass_3():
    return render_template('forgotpass_3.html')


    
'''@app.before_first_request
def populate_categories():
    if security_question.query.count() == 0:
        db.session.add_all([
            security_question(name="Category 1"),
            security_question(name="Category 2"),
            security_question(name="Category 3")
        ])
        db.session.commit()'''

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phoneno = request.form['phoneno']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        hashed_password = generate_password_hash(password)
        hashed_password_confirm = generate_password_hash(confirm_password)
        age = request.form['age']
        gender = request.form['gender']
        security_question = request.form['security_question']
        ans = request.form['ans']
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check if username already exists
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('SELECT * FROM register_user WHERE email=?', (email,))
        existing_user = c.fetchone()

        if existing_user:
            
            return render_template('register.html', errors='Username already exists!')
            
        
        # Insert data into SQLite database
        conn = sqlite3.connect('user.db', timeout=50.0)
        c = conn.cursor()
        if password == confirm_password:
            c.execute('''
            INSERT INTO register_user (firstname, lastname, email, phoneno, password, age, gender, security_question, ans, date_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (firstname, lastname, email, phoneno, password, age, gender, security_question, ans, date_time))
            conn.commit()
            conn.close()
        else:
            return render_template('register.html', error='password not matched')

        flash("User registered successfully!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if user exists and password is correct
        conn = sqlite3.connect('user.db', timeout=50.0)
        c = conn.cursor()
        c.execute('SELECT * FROM register_user WHERE email=? AND password=?', (email,password))
        user = c.fetchone()
        conn.close()

        if email=='Saloni026@gmail.com' and password=='Saloni026':
            return redirect(url_for('admin_head'))

        elif user:  # Compare hashed password
            session['email'] = user[1]
            session.permanent = True # Store username in session
            return redirect(url_for('hello'))
        else:
            return render_template('login.html', error='Invalid username or password')
            

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Route to handle video upload
'''@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file and allowed_file(file.video_filename):
        filename = secure_filename(file.video_filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Save the video metadata in the database
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('INSERT INTO videos (video_name, video_filename) VALUES (?, ?)', 
                  (file.filename, filename))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return "Invalid file type", 400'''

  
if __name__ == '__main__':
    
    app.run(debug=True)
    
