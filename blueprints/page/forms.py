"""Forms out page blueprint."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form."""

    email = EmailField("email", [DataRequired(), Length(3, 254)])
    message = TextAreaField("message", [DataRequired(), Length(1, 8192)])
    recaptcha = RecaptchaField()
