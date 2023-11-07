from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from .include.constans import (MAX_LINK_LEN, MAX_CUSTOM_ID_LEN,
                               MIN_CUSTOM_ID_LEN, MIN_LINK_LEN)


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_LINK_LEN, MAX_LINK_LEN)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(MIN_CUSTOM_ID_LEN, MAX_CUSTOM_ID_LEN),
                    Optional()]
    )
    submit = SubmitField('Создать')
