#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)
print(__name__)

@app.route('/',methods=['GET','POST'])
def home_test():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_from():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
  username=request.form['username']
  password=request.form['password']
  if username=='admin' and password=='password':
      return render_template('signok.html',username=username)
  return render_template('form.html',message='bad username or password',username=username)

if __name__=='__main__':
    app.run(debug=True)


