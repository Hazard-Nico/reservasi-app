from app import db
from datetime import datetime, timedelta

class Booking(db.Model):
    id_booking = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), nullable=False, index=True, unique=True)
    tanggal = db.Column(db.Date, nullable=False)
    jam_mulai = db.Column(db.Time, nullable=False)
    jam_akhir = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    isi_slot = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Booking {}>'.format(self.name)