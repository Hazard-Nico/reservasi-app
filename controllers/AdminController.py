from models.Admin import Admin
from models.Booking import Booking
from models.Detail_booking import Detail_booking
from models.Meja import Meja
from app import app, db
from datetime import datetime, timedelta, date, time
from flask import Flask, request, render_template, redirect, url_for, session

def login():
        # error = None
        username = request.form['username']
        password = request.form['password']
        
        if username == '' or password == '':
            return render_template('admin/login.html', error='Email atau Password harus diisi!')
            
        user = Admin.query.filter_by(username=username).first()
        
        if not user:
            return render_template('admin/login.html', error="Email tidak terdaftar")
        if not user.checkPassword(password):
            return render_template('admin/login.html', error="Kombinasi Password Salah")
        else:
            session['admin'] = user.email
            print(session['admin'])  
            return redirect('/admin/dashboard')
        
def register():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user = Admin.query.filter_by(email = email).first()
    
    if user:
        return render_template('login/register.html', error='Email sudah terdaftar')
    
    register = Admin(name = name, username = username, email = email)
    register.setPassword(password)
    db.session.add(register)
    db.session.commit()
    
    return redirect("/admin/login")
        
def index():
    return render_template('admin/index.html')

def meja():
    meja = Meja.query.all()
    return render_template('admin/meja.html', meja=meja)

def input_meja():
    no_meja = request.form['no_meja']
    slot_kursi = request.form['slot_kursi']
    tipe_meja = slot_kursi + "-" + request.form['tipe_meja'] + ".svg"
    
    meja = Meja(no_meja = no_meja, slot_kursi = slot_kursi, tipe_meja = tipe_meja)
    db.session.add(meja)
    db.session.commit()
    return redirect('/admin/meja')

def booking_data():
    booking = Booking.query.all()
    return render_template('admin/booking.html', booking=booking, datetime=datetime.now().time())

def detail_booking(id):
    book = Booking.query.filter_by(id_booking = id).first()
    meja = Detail_booking.query.filter_by(id_booking = book.id_booking)
    return render_template('admin/detail-booking.html', book=book, meja=meja)


def booking():
    email = request.form['email']
    tanggal = request.form['tanggal']
    jam_mulai = request.form['jam_mulai']
    jam_akhir = datetime.strptime(jam_mulai, "%H:%M") + timedelta(hours=2)
    isi_slot = request.form['isi_slot']
    
    # if tanggal == date.now() and jam_mulai == time.now():
    #     return render_template('admin/booking-post.html', error='')
    booking = Booking(email = email, tanggal = tanggal, jam_mulai = jam_mulai, jam_akhir = jam_akhir, isi_slot = isi_slot)
    db.session.add(booking)
    db.session.commit()
    return redirect('/admin/booking')