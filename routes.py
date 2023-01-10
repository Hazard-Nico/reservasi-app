from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from controllers import UserController, AdminController, BookingController


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.form)
    # print(request.form.get("account"))
    if request.method == 'POST':
        return BookingController.search()
    return render_template("home/index.html")

@app.route("/profile", methods=["GET"])
def profile():
    if session.get('user'):
        return UserController.profile()
    else:
        return redirect('/login')
    
@app.route("/profile/booking/<id>", methods=["GET"])
def detail_profile(id):
    if session.get('user'):
        return UserController.detail_booking(id)
    else:
        return redirect("/login")

@app.route("/checkout", methods=["GET", "POST"])
def reserve():
    if request.method =="POST":
        return BookingController.book()
    # return render_template("transaction/transaction.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # error = None
    if request.method == 'POST':
        return UserController.login()
    return render_template('login/login2.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return UserController.register()
    return render_template('login/register2.html')

@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user', None)
        return redirect('login')
    elif session.get('admin'):
        session.pop('admin', None)
        return redirect('/admin/login')

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        return AdminController.login()
    return render_template('admin/login.html')

@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":
        return AdminController.register()
    return render_template('admin/register.html')


@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    if session.get('admin'):
        return AdminController.index()
    else:
        return redirect('/admin/login')
    
@app.route("/admin/meja", methods=["GET"])
def data_meja():
    if session.get('admin'):
        return AdminController.meja()
    else:
        return redirect('/admin/login')
    
@app.route("/admin/input_meja", methods=["GET", "POST"])
def input_meja():
    if request.method == "POST":
        return AdminController.input_meja()
    return render_template('admin/meja_post.html')
    
@app.route("/admin/booking", methods=["GET"])
def data_booking():
    if session.get('admin'):
        if request.method == "GET":
            return AdminController.booking_data()
    else:
        return redirect('/admin/login')
    
@app.route("/admin/booking/<id>", methods=["GET"])
def detail_booking(id):
    if session.get('admin'):
        if request.method == "GET":
            return AdminController.detail_booking(id)
    else:
        return redirect('/admin/login')
    
@app.route('/admin/input_booking', methods=["GET", "POST"])
def booking():
    if session.get('admin'):
        if request.method == 'POST':
            return AdminController.booking()
        return render_template('admin/booking_post.html')
    else:
        return redirect('/admin/login')

@app.route("/transaction", methods=["GET"])
def transaction():
    return render_template("transaction/transaction.html")