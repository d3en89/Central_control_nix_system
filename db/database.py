from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import NoReturn

DATABASE = "default.db"
engine = create_engine(f"sqlite:///{DATABASE}")
Session = sessionmaker(bind=engine)
Base = declarative_base()

def connect_db() -> NoReturn:
    Base.metadata.create_all(engine)

