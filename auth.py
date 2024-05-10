"""
This module ...
"""
import secrets
from flask import request, redirect, render_template, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
from validation import \
    validate_firstname, \
    validate_lastname, \
    validate_username, \
    validate_password, \
    validate_email, \
    validate_re_password

from extensions import db, mail
from models import User

auth_bp = Blueprint('auth', __name__)

def send_email(subject, recipients, body):
    """
    This function creates an email object. 
    """
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)

@auth_bp.route("/signin", methods = ['GET', 'POST'])

def signin():
    """
    This function handles the user signing in by taking in the username and password inputs. 
    """
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        user=User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username']=username
            return redirect('/success')

    return render_template('sign_in.html')

@auth_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    This function handles the user signing up by taking in basic user inputs, validating them. 
    """
    print('This bit happened')
    if request.method=='POST':
        firstname = request.form['firstname']
        print('firstname =', firstname)
        lastname = request.form['lastname']
        print('lastname =', lastname)
        username = request.form['username']
        print('username =', username)
        email = request.form['email']
        print('email =', email)
        password = generate_password_hash(request.form['password'])
        password_not_hash = request.form['password']
        print('password_not_hash =', password_not_hash)
        print('password =', password)
        re_password = request.form['re-password']
        print('re-password =', re_password)

        existing_user=User.query.filter_by(username=username).first()
        existing_email=User.query.filter_by(email=email).first()

        all_verified = (validate_firstname(firstname)
        and validate_lastname(lastname)
        and validate_password(password)
        and validate_username(username)
        and validate_email(email)
        and validate_re_password(re_password,password_not_hash))

        if existing_user or existing_email:
            print('User or email already exists')
            return render_template('sign_up.html')
        if all_verified:
            print('This bit happened 3')

            verification_token=secrets.token_urlsafe(16)

            new_user = User(firstname=firstname,
                            lastname=lastname,
                            username=username,
                            password=password,
                            email=email,
                            token=verification_token)

            db.session.add(new_user)
            db.session.commit()

            send_email('Welcome to Our App', [email],
            f'Thank you for signing up!/n' 
            f'Here is your verification link: http://127.0.0.1:5000/verify/{verification_token}')

            session['username']=username
            session['firstname']=firstname
            session['lastname']=lastname
            session['password']=password
            session['email']=email

            return redirect('/email')
    else:
        print('This is happening')

    return render_template('sign_up.html')

@auth_bp.route('/email')
def email_func():
    """
    This function displays the email page users are directed to after a successful sign-up. 
    """
    return render_template('email_page.html')

@auth_bp.route('/verify/<token>', methods=['GET'])
def verify(token):
    """
    This function verifies the email token. 
    """
    user = User.query.filter_by(token=token).first()

    if user:
        user.verified = True
        db.session.commit()
        return redirect('/signin')

    return 'Invalid verification token'

@auth_bp.route('/success')
def success():
    """
    This function displays the home page users are directed to after a successful sign-in. 
    """

    return render_template('home.html')
