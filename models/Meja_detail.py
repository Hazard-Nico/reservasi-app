from app import db
from datetime import datetime

class Meja_detail(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    slot_kursi = db.Column(db.Integer, nullable=False)
    bentuk = db.Column(db.Text)
    
    def __repr__(self):
        return "<Meja {}>".format(self.name)

