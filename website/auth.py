from flask import Blueprint, render_template, flash, redirect
from .forms import LoginForm, SignUpForm
from .models import Customer
from . import db
from flask_login import login_user, login_required, logout_user
# tells flask that views.py containing a bunch of url or routes
auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        passward1 = form.password1.data
        passward2 = form.password2.data

        if passward1 == passward2:
            new_customer = Customer()
            new_customer.email = email
            new_customer.username = username
            new_customer.password = passward2

            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Account Created Successfully, You can now Login')
                return redirect('/login')
            except Exception as e:
                print(e)
                flash('Account Not Created!!, Email already exists')
            
            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''


    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        customer = Customer.query.filter_by(email=email).first()

        if customer:
            if customer.verify_password(password=password):
                login_user(customer)
                return redirect('/')
            else:
                flash('Incorrect email or password')

        else:
            flash('Account does not exist please Sign up')



    return render_template('login.html', form=form)



@auth.route('/logout',  methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user
    return redirect('/')