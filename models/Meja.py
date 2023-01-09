from app import db
from datetime import datetime

class Meja(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_meja = db.Column(db.BigInteger, nullable=False)
    slot_kursi = db.Column(db.Integer, nullable=False)
    tipe_meja = db.Column(db.Text)
    
    def __repr__(self):
        return "<Meja {}>".format(self.name)

