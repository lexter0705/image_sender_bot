from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import User


class UserWorker:
    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db')
        self.__session = sessionmaker(bind=self.__engine)

    def add_user(self, user: User):
        session = self.__session()
        session.add(user)
        session.commit()

    def is_user(self, user: User):
        session = self.__session()
        return session.get(User, user) is not None
