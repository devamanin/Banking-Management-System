from flask import Flask, request, jsonify, render_template, redirect, url_for, session

import db
app = Flask(__name__, template_folder='templates')
app.secret_key = "hellworld"

@app.route("/")
def index():
    if not session:
        return render_template("login-page/login.html")
    else:
        return render_template("home-page/BMS.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    accCheck = db.userAuthenticate([username, password])
    if accCheck[0] == "usrFound":
        session['loggedin'] = True
        session['username'] = accCheck[1][0][1]
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)