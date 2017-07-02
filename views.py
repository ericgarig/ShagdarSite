from app import app, mail
from flask import render_template, request
from flask_mail import Message
from forms import ContactForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    alert = None
    if form.validate_on_submit():
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        send_email('ShagdarSite: {}'.format(subject),
                   app.config['MAIL_USERNAME'],
                   app.config['ADMIN_EMAIL'],
                   email,
                   'A message from {}:\n\n{}'.format(email, message))
        alert = 'sent'
    elif request.method == 'POST':
        alert = 'fail'
    return render_template('index.html', form=form, alert=alert)


def send_email(subject, sender, recipients, reply_to, body):
    msg = Message(subject, recipients, body, sender=sender, reply_to=reply_to)
    mail.send(msg)
