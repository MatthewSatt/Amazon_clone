from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import User


def email_available(form, field):
    if User.query.filter(User.email == field.data).first():
        raise ValidationError('An account with this email already exists.')


def username_available(form, field):
    if User.query.filter(User.username == field.data).first():
        raise ValidationError('This username is taken.')


class SignUpForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('Username', filters=[lambda v: v.strip() if v else v], validators=[
        DataRequired(message='Choose a username.'),
        Length(min=3, max=40, message='Username must be 3-40 characters.'),
        username_available])
    email = StringField('Email', filters=[lambda v: v.strip().lower() if v else v], validators=[
        DataRequired(message='Enter your email.'),
        Email(message='Enter a valid email address.'),
        Length(max=255),
        email_available])
    password = PasswordField('Password', validators=[
        DataRequired(message='Enter a password.'),
        Length(min=6, max=128, message='Password must be at least 6 characters.')])
