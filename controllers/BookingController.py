from models.Booking import Booking
from models.Detail_booking import Detail_booking
from models.Meja import Meja

from app import app, db
from flask import Flask, request, render_template, redirect, url_for, session, flash
from datetime import datetime, timedelta

def search():
    tanggal = request.form['tanggal']
    jam_mulai = request.form['jam_mulai']
    isi_slot = int(request.form['isi_slot'])
    detail_booking = Detail_booking.query.filter_by(tanggal = tanggal, jam_mulai = jam_mulai).first()
    # detail_booking = Detail_booking.query.all()
    meja = Meja.query.all()
    
    return render_template('home/index.html', meja=meja, detail=detail_booking, isi_slot = isi_slot, tanggal = tanggal, jam_mulai = jam_mulai)


def book():
    a = search()
    email = request.form['email']
    tanggal = request.form['tanggal']
    jam_mulai = request.form['jam_mulai']
    isi_slot = int(request.form['isi_slot'])
    jam_akhir = datetime.strptime(jam_mulai, "%H:%M") + timedelta(hours=2)
    id_meja = request.form.getlist('id_meja')
    id_pembayaran = request.form['id_pembayaran']
    
    book = Booking(email = email, tanggal = tanggal, jam_mulai = jam_mulai, jam_akhir = jam_akhir, isi_slot = isi_slot)
    db.session.add(book)
    db.session.commit()
    for i in range(len(id_meja)):
        detail = Detail_booking(tanggal = tanggal, id_booking = book.id_booking, jam_mulai = jam_mulai, jam_akhir = jam_akhir, id_meja = id_meja[i], id_pembayaran = id_pembayaran)
        db.session.add(detail)
        db.session.commit()
    print('You were successfully submit')
    return redirect('/')