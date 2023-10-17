from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE = "default.db"
engine = create_engine(f"sqlite:///{DATABASE}")
Session = sessionmaker(bind=engine)
Base = declarative_base()

def connect_db():
    Base.metadata.create_all(engine)

