from flask_wtf import Form
from wtforms import TextField, PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    email = EmailField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=0, max=25)]
    )
    # confirm = PasswordField(
    #     'Repeat password',
    #     validators=[
    #         DataRequired(), EqualTo('password', message='Passwords must match.')
    #     ]
    # )
