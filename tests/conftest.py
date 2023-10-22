from db.models_db import Servers
from db.database import Session
import pytest

@pytest.fixture
def clean_servers_table():
    session = Session()
    session.query(Servers).delete()
    session.commit()
