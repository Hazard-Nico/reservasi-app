from flask import Flask, render_template, request, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'xxxxxxxxxx'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import User, Booking, Detail_booking, Meja, Admin, Pembayaran
import routes






if __name__ == '__main__':
    app.run(debug=True)
