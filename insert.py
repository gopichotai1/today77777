import sqlite3
from flask import Flask, app , render_template,url_for,request,redirect
@app.route('/')
def ac():
    return render_template()


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phoneno = request.form['phoneno']
        password = request.form['password']
        age = request.form['age']
        gender = request.form['gender']
        security_question = request.form['security_question']
        ans = request.form['ans']

        cursor.execute('INSERT INTO register (name, email) VALUES (?, ?)', (name, email))
        
        return redirect(url_for('index'))  # Redirect back to the home page after submission'''
