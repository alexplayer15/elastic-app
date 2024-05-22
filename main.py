"""
This module ...
"""
import os
from dotenv import load_dotenv
from flask import Flask
from auth import auth_bp
from user import user_bp
from extensions import db, mail

load_dotenv()

app=Flask(__name__, static_folder='static')

app.config['SECRET_KEY']=os.getenv('APP_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['MAIL_SERVER']="smtp.fastmail.com"
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=os.getenv('EMAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USERNAME')

db.init_app(app)
mail.init_app(app)

app.register_blueprint(auth_bp,\
                        secret_key=app.config['SECRET_KEY'],\
                        database_url=app.config['SQLALCHEMY_DATABASE_URI'],\
                        mail_server=app.config['MAIL_SERVER'],\
                        mail_port=app.config['MAIL_PORT'],\
                        mail_username=app.config['MAIL_USERNAME'],\
                        mail_password=app.config['MAIL_PASSWORD'],\
                        use_tls=app.config['MAIL_USE_TLS'],\
                        use_ssl=app.config['MAIL_USE_SSL'],\
                        default_sender=app.config['MAIL_DEFAULT_SENDER'])
app.register_blueprint(user_bp,\
                       secret_key=app.config['SECRET_KEY'],\
                       database_url=app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
