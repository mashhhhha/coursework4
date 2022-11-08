from marshmallow import Schema, fields

from dao.model.genre import GenreSchema
from setup_db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    favorite_genre = db.relationship('Genre')


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Nested(GenreSchema, only=['name'])