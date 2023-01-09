from app import db
from datetime import datetime

class Pembayaran(db.Model):
    id_pembayaran = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_rek = db.Column(db.Text)
    jenis_pembayaran = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Pembayaran {}>".format(self.name)