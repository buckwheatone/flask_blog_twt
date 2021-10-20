from flask import Blueprint, render_template, redirect, url_for, request, flash
from website.forms import RegistrationForm

from website.forms import LoginForm
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/", methods=['GET', 'POST'])
def landing():
    form = LoginForm()
    # if request.method == 'post':
    #     return redirect('login') 
    return render_template("landing.html", user=current_user, form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('views.home'))
    form = LoginForm()
    print("form created")
    print(f"em: {form.email.data}, pw: {form.password.data}")
    user = User.query.filter_by(email=form.email.data, active=1).first()
    if user: 
        print(user.email, user.password) 
    if form.submit():
        print("submitted")
    if form.validate():
        print("validated") 
    if form.validate_on_submit():
        print("submitted and validated") 
        user = User.query.filter_by(email=form.email.data, active=1).first()
        if user:
            print("user exists")
        if user and check_password_hash(user.password, form.password.data) :
            login_user(user, remember=True)
            flash("Logged in!", category='success')
            next_page = request.args.get('next') 
            return redirect(next_page) if next_page else redirect(url_for('views.home')) 
        else:
            flash('Username and/or Password incorrect.', category='error') 
    return render_template("login.html", user=current_user, form=form) 


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated: 
        return redirect(url_for('views.home'))
    form = RegistrationForm()
    if form.validate_on_submit():

        new_user = User(
                email=form.email.data.lower(), 
                username=form.username.data, 
                password=generate_password_hash(form.password.data, 
                method='sha256')
            )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash(f"Account created for {form.username.data}!", category="success")
        return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user, form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.landing"))

