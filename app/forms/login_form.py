from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        # CSRF is enforced globally by CSRFProtect via the X-CSRFToken header
        csrf = False

    email = StringField('Email', validators=[DataRequired(message='Enter your email.')],
                        filters=[lambda v: v.strip().lower() if v else v])
    password = PasswordField('Password', validators=[DataRequired(message='Enter your password.')])
