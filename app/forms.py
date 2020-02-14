from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.user_model import User
from flask_wtf.file import FileField, FileRequired

#註冊
class RegisterForm(FlaskForm):

    #User註冊表單
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    #自定義驗證(辨識註冊資料是否已被使用)
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use, please choose anther one.')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use, please choose anther one.')

#登入
class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    remember = BooleanField('Remember')
    submit = SubmitField('Sigh in')

#寄出密碼重置信件
class PasswordResetRequestForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email not exists.')

#更換新密碼
class ResetPasswordForm(FlaskForm):

    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

#PO貼文
class PostTweetForm(FlaskForm):

    text = TextAreaField('Write something ...', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Post Text')

class UploadPhotoForm(FlaskForm):

    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')

