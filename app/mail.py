from app import mail, app
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread

#加速寄件(讓前端先顯示)
def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_reset_password_mail(user, token):
    msg = Message("[Flask App] Reset Your Password",
                    sender=current_app.config['MAIL_PASSWORD'],
                    recipients=[user.email],
                    html=render_template('reset_password_mail.html', user=user, token=token)
                  )
    #mail.send(msg)
    Thread(target=send_reset_password_mail, args=(app, msg, )).start()