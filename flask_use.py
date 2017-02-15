#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_testappend():#这个名字不重要,随便写
    return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])
def signin_fo():#这个名字不重要,随便写
    return '''<form action='/signin'method='post'>
              <p><input name='username'></p>
              <p><input name='password' type='password'></p>
              <p><button type='submit'>Sign In</button></p>
              </form>'''

@app.route('/signin',methods=['POST'])
def signin():#这个名字不重要,随便写
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>hello,admin!</h3>'
    return '<h3>bad name or password</h3>'
if __name__=='__main__':
    app.run()


