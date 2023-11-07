from flask import url_for
from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view', short=self.short, _external=True
            ),
        )

    def from_dict(self, data):

        for field, value in {
            'original': 'url',
            'short': 'custom_id'
        }.items():
            if value in data:
                setattr(self, field, data[value])
