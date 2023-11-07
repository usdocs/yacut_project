import re

from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .error_handlers import InvalidAPIUsage
from .include.constans import REGEX, SHORT_ID_LEN, STRING_LEN
from .models import URLMap
from .views import get_unique_short_id, short_id_exist


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса', HTTPStatus.BAD_REQUEST
        )
    if 'url' not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST
        )
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id(SHORT_ID_LEN)
    elif short_id_exist(data['custom_id']):
        short_id = data['custom_id']
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.',
                              HTTPStatus.BAD_REQUEST)
    elif (
        len(data['custom_id']) > STRING_LEN or
        not re.match(REGEX, data['custom_id'])
    ):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            400
        )

    url_map = URLMap()
    url_map.from_dict(data)

    db.session.add(url_map)
    db.session.commit()

    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()

    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)

    return jsonify({'url': url_map.original}), HTTPStatus.OK
