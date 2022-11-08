from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, page_number):
        if page_number is None:
            return self.dao.get_all()

        return self.dao.get_by_page(int(page_number))