from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_with_filters(self, filters):
        if filters.get('status') == 'new' and filters.get('page') is not None:
            page = int(filters.get('page'))
            return self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page, per_page=12).items

        if filters.get('status') == 'new':
            return self.session.query(Movie).order_by(desc(Movie.year))

        if filters.get('page') is not None:
            page = int(filters.get('page'))
            return self.session.query(Movie).paginate(page=page, per_page=12).items