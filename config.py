import os
#-----------------------------------------------
#隨機生成金鑰
#os.urandom(24)
#-----------------------------------------------

#加密金鑰SECRET_KEY可隨意設置
SECRET_KEY = '123456789'
#此RECAPTCHA_PUBLIC_KEY為測試KEY，須至Google reCAPTCHA申請
RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

#flask gmail config(參考https://hackmd.io/@shaoeChen/BytvGKs4M?type=view)
#不同mail的sever、port個不同需再查詢相關配置

#hotmail
'''
MAIL_SERVER = 'smtp.live.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'hotmail帳號'
MAIL_PASSWORD = 'hotmail密碼'
'''

#gmail(要把信箱設為低安全性)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'gmail帳號'
MAIL_PASSWORD = 'gmail密碼'

#MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'MAIL_USERNAME'
#MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'MAIL_PASSWORD'


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:465x225x490mm@localhost:3306/flask_user'
#'資料庫類型+資料庫驅動://資料庫用戶名:資料庫密碼@IP:資料庫名稱'
SQLALCHEMY_TRACK_MODIFICATIONS = True

'''
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Database configuration(從環境變數中獲得databaseURL,若沒有就創建一個)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''