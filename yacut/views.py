from random import choice
from string import ascii_letters, digits

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .include.constans import SHORT_ID_LEN
from .models import URLMap


def short_id_exist(short):
    return (URLMap.query.filter_by(short=short).first() is not None)


def get_unique_short_id(length):
    letters = ascii_letters + digits
    rand_string = ''.join(choice(letters) for i in range(length))
    if short_id_exist(rand_string):
        rand_string = get_unique_short_id(length)
    return rand_string


@app.route('/', methods=['GET', 'POST'])
def yacut_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            short = get_unique_short_id(SHORT_ID_LEN)
        elif short_id_exist(form.custom_id.data):
            flash(
                f'Имя {form.custom_id.data} уже занято!',
                'Bad url'
            )
            return render_template('yacut.html', form=form)
        else:
            short = form.custom_id.data

        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('yacut.html', form=form, link=short)
    return render_template('yacut.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
