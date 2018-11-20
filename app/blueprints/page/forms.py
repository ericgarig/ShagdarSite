"""Forms out page blueprint."""
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form."""

    email = EmailField('email', [DataRequired(), Length(3, 254)])
    message = TextAreaField('message', [DataRequired(), Length(1, 8192)])
