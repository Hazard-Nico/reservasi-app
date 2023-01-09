from models.Booking import Booking
from models.Detail_booking import Detail_booking
from models.Meja import Meja

from app import app, db
from flask import Flask, request, render_template, redirect, url_for, session
from datetime import datetime


def book():
    tanggal = request.form['tanggal']
    jam_mulai = request.form['jam_mulai']
    isi_slot = request.form['isi_slot']
    
    detail_booking = Detail_booking.query.filter_by(tanggal = tanggal, jam_mulai = jam_mulai).first()
    meja = Meja.query.all()
    
    return render_template('home/index.html', meja=meja, detail=detail_booking, isi_slot = isi_slot)