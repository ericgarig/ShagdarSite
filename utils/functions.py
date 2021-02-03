import re

from flask_mail import Message

from flask import current_app
from extensions import mail


def as_bool(v):
    """Convert string to boolean."""
    return str(v).lower() in ("yes", "true", "t", "1")


def detect_spam(sender: str, body: str):
    """Determine if the sender or body of the email is considered spam."""
    if sender[-3:] == ".ru":
        raise Exception("Spam email address detected.")
    if bool(re.search("[а-яА-Я]", body)):
        raise Exception("Spam body detected.")
    if bool(
        re.search(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            body,
        )
    ):
        raise Exception("Links are not allowed.")


def send_mail(sender: str, body: str):
    msg = Message(
        f"[{current_app.config['APP_NAME']}] Contact",
        sender=f"{current_app.config['MAIL_USERNAME']}",
        recipients=[f"{current_app.config['SEND_MAIL_TO']}"],
    )
    msg.body = f"{sender} wrote:\n\n{body}"
    mail.send(msg)
