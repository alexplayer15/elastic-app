"""
This module ...
"""
from extensions import db

class User(db.Model):
    """
    This class...
    """
    __tablename__='user_data'
    id = db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(75))
    username=db.Column(db.String(50))
    password=db.Column(db.String(200))
    email=db.Column(db.String(100))
    token=db.Column(db.String(150))
    bio=db.Column(db.String(2000))
    location=db.Column(db.String(100))
    role=db.Column(db.String(100))
    genre=db.Column(db.String(500))
    equipment=db.Column(db.String(500))
    verified=db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def print_user(self):
        """
        This function...
        """
        print(self.user)
