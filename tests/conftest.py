from db.models_db import User_data, Servers
from db.database import Session
import pytest

@pytest.fixture
def clean_user_table():
    session = Session()
    session.query(User_data).delete()
    session.commit()

@pytest.fixture
def clean_servers_table():
    session = Session()
    session.query(Servers).delete()
    session.commit()
