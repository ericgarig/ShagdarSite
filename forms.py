from flask_wtf import FlaskForm
from wtforms import StringField as string, TextAreaField as text
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    email = string('email',
                   validators=[DataRequired(message='Email is required'),
                               Email(message='Enter a valid email')],
                   render_kw={'placeholder': 'email'})
    subject = string('subject',
                     validators=[DataRequired(message='Enter a subject')],
                     render_kw={'placeholder': 'subject'})
    message = text('message',
                   validators=[DataRequired(message='Send me a message')],
                   render_kw={'placeholder': 'message'})
