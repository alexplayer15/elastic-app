import re

def validate_firstname(firstname):

    if firstname == '':
        print('Cannot leave your firstname blank')
        return False

    elif len(firstname) < 2 or len(firstname) > 50:
            print('Name length must be between 2 and 50 characters.')
            return False
    else:
        if firstname.isascii() and firstname.isalpha():
            print(f'Your firstname is {firstname}')
            print(f'Length of your firstname is {len(firstname)} characters')
            return True
        else:
            print('You cannot use that character, please try again')
            return False

def validate_lastname(lastname):

    if lastname == '':
        print('Cannot leave your lastname blank')
        return False

    elif len(lastname) < 2 or len(lastname) > 75:
            print('Name length must be between 2 and 75 characters.')
            return False

    else:
        if lastname.isascii() and lastname.isalpha():
            print(f'Your lastname is {lastname}')
            print(f'Length of your lastname is {len(lastname)} characters')
            return True
        else:
            print('You cannot use that character, please try again')
            return False


def validate_username(username):

    if username == '':
        print('Cannot leave your username blank')
        return False

    elif len(username) < 2 or len(username) > 50:
            print('Name length must be between 2 and 50 characters.')
            return False

    else:
        if username.isascii() and username.isalnum():
            print(f'Your username is {username}')
            print(f'Length of your username is {len(username)} characters')
            return True
        else:
            print('You cannot use that character, please try again')
            return False
        
def validate_email(email):
    
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if email == '':
        print('Cannot leave your email blank')
        return False

    else:
        if re.match(email_pattern, email):
            print('Valid email')
            return True 
        
        else:
            print('Please enter a valid email')
            return False
       

def validate_password(password):

    space_count = 0 

    for character in password:      
        if character == ' ':
                space_count += 1
    if password == '':
            print('Please enter a password')
            return False
    elif len(password) < 10:
            print(f'Password must be at least 10 characters long. You entered {len(password)}.')
            return False
    elif space_count > 0:
            print(f'You cannot use spaces in your password. You used {space_count}.')
            return False
    else:        
            num_count = 0
            upper_count = 0
            for character in password:
                if character.isnumeric():
                    num_count += 1
                elif character.isupper():
                    upper_count += 1 
                
            if num_count >= 2 and upper_count >= 2:
                return True
            else:
                print(f'Your password must contain atleast two numbers and two upper case characters. You currently have {num_count} numbers and {upper_count} upper case characters.')
                return False

def validate_re_password(rePassword, password_not_hash):
     
     if password_not_hash != rePassword:
          print('Please enter matching passwords')
          return False
     else:
          return True 

