from flask import Flask, render_template, request, redirect, session
import mysql.connector
from db_config import db_params

app = Flask(__name__)
app.secret_key = 'supersecurekey'

@app.route('/hardware')
def hardware_redirect():
    hardware_id = request.args.get('id')
    return render_template('login.html', hardware_id=hardware_id)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hardware_id = request.form['hardware_id']

    conn = mysql.connector.connect(**db_params)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        cursor.execute("SELECT * FROM hardware WHERE id=%s", (hardware_id,))
        data = cursor.fetchone()
        conn.close()
        return render_template('hardware.html', data=data)
    else:
        return render_template('login.html', error="Invalid credentials", hardware_id=hardware_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
