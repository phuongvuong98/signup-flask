from flask_wtf import Form
from wtforms import TextField, StringField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField(
        'Description', validators=[DataRequired(), Length(max=140)])
