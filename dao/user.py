from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        users = self.session.query(User).all()

        return users

    def get_one(self, uid):
        user = self.session.query(User).get(uid)

        return user

    def get_by_name(self, username):
        user = self.session.query(User).filter(User.username == username).first()

        return user

    def get_by_email(self, email: str):
        user = self.session.query(User).filter(User.email == email.lower()).first()

        return user

    def create(self, user_data):
        new_user = User(**user_data)

        self.session.add(new_user)
        self.session.commit()

        return new_user

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_by_email(user_data.get('email'))

        user.name = user_data.get('name')
        user.surname = user_data.get('surname')
        user.favorite_genre_id = user_data.get('favorite_genre_id')

        self.session.add(user)
        self.session.commit()