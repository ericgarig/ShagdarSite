from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'email'})
    subject = StringField('subject',
                          validators=[DataRequired()],
                          render_kw={'placeholder': 'message'})
    message = TextAreaField('message',
                            validators=[DataRequired()],
                            render_kw={'placeholder': 'message'})
