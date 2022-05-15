import json
from operator import methodcaller
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import datetime

import db
app = Flask(__name__, template_folder='templates')
app.secret_key = "hellworld"

@app.route("/")
def index():
    if not session:
        return render_template("login-page/login.html")
    else:
        loggedUsrDetails = db.fetchdetails(session['username'])
        print(session['username'])
        loggedtime = datetime.datetime.now()
        # print(loggedUsrDetails)
        loggedUsrDetails = [(loggedUsrDetails[0][0].split())[0], loggedUsrDetails[0][-2], loggedUsrDetails[0][-1], request.remote_addr, loggedtime]
        print(loggedUsrDetails)
        return render_template("home-page/BMS.html", loggedUsrDetails = loggedUsrDetails)

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

@app.route("/login-emp", methods=['POST'])
def loginEmp():
    details = request.get_json()
    res = db.LogBankEmployee([details['empid'], details['pass']])
    return (jsonify(res))

@app.route("/transfer", methods=['GET'])
def transfer():
    trxDetails = db.fetchtrxDetails(session['username'])
    return render_template("tran-page/index.html", len = len(trxDetails), trxDetails = trxDetails)

@app.route("/trnx", methods = ['GET', 'POST'])
def trnx():
    accountno = request.form["accno"]
    amount = request.form["amount"]
    res = db.transfer([accountno, amount, session['username']])
    print(res)
    if (res==True):
        print("Transaction is done")
        return "Transaction is processing <script>window.location.href = '/'</script>"
    return "Transaction is failed"

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)