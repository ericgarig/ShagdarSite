"""Page endpoints."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from blueprints.page.forms import ContactForm


page = Blueprint('page', __name__, template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def index():
    """Render index."""
    form = ContactForm()
    if form.validate_on_submit():
        # This prevents circular imports
        from blueprints.page.tasks import deliver_contact_email

        deliver_contact_email(request.form.get('email'),
                              request.form.get('message'))
        flash('Thanks, expect a response shortly.', 'success')
        return redirect(url_for('page.index'))
    elif request.method == 'POST':
        flash('Looks like you tried to submit an empty form.', 'warning')
    return render_template('page/index.html', form=form)
