"""Page endpoints."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from blueprints.page import ContactForm
from utils import detect_spam, send_mail


page = Blueprint("page", __name__, template_folder="templates")


@page.route("/", methods=["GET", "POST"])
def index():
    """Render index."""
    form = ContactForm()
    if form.validate_on_submit():
        sender = request.form.get("email")
        message = request.form.get("message")
        try:
            detect_spam(sender, message)
        except Exception as e:
            flash(str(e), "warning")
        else:
            send_mail(sender, message)
            flash("Thanks, expect a response shortly.", "success")
            return redirect(url_for("page.index"))
    elif request.method == "POST":
        flash("Looks like you tried to submit an empty form.", "warning")
    return render_template("page/index.html", form=form)
