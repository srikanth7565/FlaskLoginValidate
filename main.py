from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import numpy as np


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    password=request.form['password']
    username=request.form['username']
    if not len(password)>=6:
        status= "201"
        msg="Failure: password should be of length 6 "
        return render_template('second.html', data=status, data1=msg)
    if not username.isalpha():
        status="203"
        msg="Failure, only characters allowed"
        return render_template('second.html', data=status, data1=msg)
    if password.isalpha() or password.isnumeric():
        status= "202"
        msg="Failure: password to have 1 character and 1 number"
        return render_template('second.html', data=status, data1=msg)
    else:
        status= "200"
        msg="Success"        
        return render_template('success.html', data=status, data1=msg)

    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
