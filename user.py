from flask import Flask, request, jsonify, redirect, render_template, session, Blueprint
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/edit', methods=['GET','POST'])
def edit():

        username = session.get('username')

        user = User.query.filter_by(username=username).first()

        if request.method == 'POST' and user:
             
            bio = request.form['bio']
            print('bio =', bio)
            location = request.form['location']
            print('location =', location)
            role = request.form['role']
            print('role =', role)
            genre = request.form['genre']
            print('genre =', genre)
            equipment = request.form['equipment']
            print('equipment =', equipment)

            #validate these inputs later

            #also add condition where if user input is null then keep original value 

            user.bio = bio
            user.location = location
            user.role = role
            user.genre = genre
            user.equipment = equipment

            db.session.commit()

        return render_template('edit.html')

@user_bp.route('/delete', methods=['GET','POST'])
def delete_account():

    username = session.get('username')

    user = User.query.filter_by(username=username).first()

    if request.method == 'POST' and user:

                db.session.delete(user)
                db.session.commit()
                session.pop('username')
                session.pop('firstname')
                session.pop('lastname')
                session.pop('password')
                session.pop('email')
                return redirect('/signup')
    
    #add page to confirm user has deleted their account and email. Send them back to sign up. 

    else:
        print('error')
    
    return render_template('delete.html')

@user_bp.route('/view',methods=['GET'])
def view():
     
    username = session.get('username')

    user = User.query.filter_by(username=username).first()

    return render_template('view.html', user=user)
     

@user_bp.route('/error')
def error():
     
     return render_template('test.html')

