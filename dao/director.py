from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_page(self, page_num):
        books = self.session.query(Director).paginate(page=page_num, per_page=12).items
        return books