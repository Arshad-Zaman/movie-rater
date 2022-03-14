# pylint: disable= import-error, no-member, missing-module-docstring, invalid-name, too-few-public-methods, cyclic-import
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from . import db

ma = Marshmallow()


class User(UserMixin, db.Model):
    """User table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)


class Rating(db.Model):
    """Rating table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    movie_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String())


class RatingSchema(ma.Schema):
    """Create schema for rating"""

    class Meta:
        """Set model to rating"""

        fields = ("id", "username", "movie_id", "rating", "comment")
