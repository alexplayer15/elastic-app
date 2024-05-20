"""
This method...
"""
import re
from models import User

def validate_firstname(firstname):
    """
    This function...
    """
    if firstname == '':
        print('Cannot leave your firstname blank')
        return False

    if len(firstname) < 2 or len(firstname) > 50:
        print('Name length must be between 2 and 50 characters.')
        return False

    if firstname.isascii() and firstname.isalpha():
        print(f'Your firstname is {firstname}')
        print(f'Length of your firstname is {len(firstname)} characters')
        return True

    print('You cannot use that character, please try again')
    return False

def validate_lastname(lastname):
    """
    This function...
    """
    if lastname == '':
        print('Cannot leave your lastname blank')
        return False

    if len(lastname) < 2 or len(lastname) > 75:
        print('Name length must be between 2 and 75 characters.')
        return False


    if lastname.isascii() and lastname.isalpha():
        print(f'Your lastname is {lastname}')
        print(f'Length of your lastname is {len(lastname)} characters')
        return True

    print('You cannot use that character, please try again')
    return False


def validate_username(username):
    """
    This function...
    """
    user = User.query.filter_by(username=username).first()

    if user:
        print('That username already exists')
        return False

    if username == '':
        print('Cannot leave your username blank')
        return False

    if len(username) < 2 or len(username) > 50:
        print('Name length must be between 2 and 50 characters.')
        return False

    if username.isascii() and username.isalnum():
        print(f'Your username is {username}')
        print(f'Length of your username is {len(username)} characters')
        return True

    print('You cannot use that character, please try again')
    return False

def validate_email(email):
    """
    This function...
    """
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        print('Email already exists')
        return False

    if email == '':
        print('Cannot leave your email blank')
        return False


    if re.match(email_pattern, email):
        print('Valid email')
        return True

    print('Please enter a valid email')
    return False

def validate_password(password):
    """
    This function...
    """
    space_count = 0

    for character in password:
        if character == ' ':
            space_count += 1
    if password == '':
        print('Please enter a password')
        return False
    if len(password) < 10:
        print(f'Password must be at least 10 characters long. You entered {len(password)}.')
        return False
    if space_count > 0:
        print(f'You cannot use spaces in your password. You used {space_count}.')
        return False

    num_count = 0
    upper_count = 0
    for character in password:
        if character.isnumeric():
            num_count += 1
        elif character.isupper():
            upper_count += 1

    if num_count >= 2 and upper_count >= 2:
        return True

    print(f'Your password must contain atleast two numbers and two upper case characters.\n'
        f'You currently have {num_count} numbers and {upper_count} upper case characters.')
    return False

def validate_re_password(re_password, password_not_hash):
    """
    This function...
    """
    if password_not_hash != re_password:
        print('Please enter matching passwords')
        return False

    return True
