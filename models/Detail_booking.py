from app import db

class Detail_booking(db.Model):
    id_detail = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_booking = db.Column(db.BigInteger, nullable=False)
    id_meja = db.Column(db.BigInteger, nullable=False)
    id_pembayaran = db.Column(db.BigInteger, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    jam_mulai = db.Column(db.Time, nullable=False)
    jam_akhir = db.Column(db.Time, nullable=False)
    
    def __repr__(self):
        return "<Detail_booking {}>".format(self.name)