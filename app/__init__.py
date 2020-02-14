from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__) #目前執行的模組

#導入config
app.config.from_object('config')

bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to account this page'
login.login_message_category = 'info'
mail = Mail(app)

#一般金鑰不寫在app.py程式中，寫在config.py
#app.config['SECRET_KEY'] = '123456789'
#app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
#RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

from app.routes import *

