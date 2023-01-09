from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    username = db.Column(db.String(250))
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False, index=True, unique=True)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Admin {}>".format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)