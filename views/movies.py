from decorators import auth_required
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        status = request.args.get('status')
        page_number = request.args.get('page')

        filters = {
            "status": status,
            "page": page_number
        }

        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@movie_ns.route('/<int:bid>/')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200