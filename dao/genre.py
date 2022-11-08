from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_page(self, page_number):
        genres = self.session.query(Genre).paginate(page=page_number, per_page=12).items

        return genres