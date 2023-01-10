from models.User import User
from app import app, db
from flask import Flask, request, render_template, redirect, url_for, session

def login():
        # error = None
        username = request.form['username']
        password = request.form['password']
        
        if username == '' or password == '':
            return render_template('login/login2.html', error='Email atau Password harus diisi!')
            
        user = User.query.filter_by(username=username).first()
        
        if not user:
            return render_template('login/login2.html', error="Email tidak terdaftar")
        if not user.checkPassword(password):
            return render_template('login/login2.html', error="Kombinasi Password Salah")
        else:
            session['user'] = user.email
            print(session['user'])  
            return redirect('/')
        
def register():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user = User.query.filter_by(email = email).first()
    
    if user:
        return render_template('login/register2.html', error='Email sudah terdaftar')
    
    register = User(name = name, username = username, email = email)
    register.setPassword(password)
    db.session.add(register)
    db.session.commit()
    
    # return render_template('login/login2.html', error='Register berhasil')
    return redirect("/login")
