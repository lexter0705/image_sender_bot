from sqlalchemy import create_engine

from config import read_config
from database import Base


def create_database():
    config = read_config()
    engine = create_engine(config["database_path"])
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_database()
