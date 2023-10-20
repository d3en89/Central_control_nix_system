from db.database import connect_db, DATABASE
from scripts.sc_database import add_user, add_server, get_user,get_servers
from os import path, remove
import pytest

@pytest.mark.parametrize("db", [DATABASE])
def test_create_database(db):
    if path.exists(db):
        remove(db)
    connect_db()
    assert path.exists(db) == True

def test_user_create(clean_user_table):
    clean_user_table
    add_user("haos", "patron")
    assert get_user() == (1,"haos", "patron")


def test_server_create(clean_servers_table):
    clean_servers_table
    list_servers = [("router", "332", "admin","pass", 22,"1","1","centos"),("mi", "34fd", "admina","passfff", 222,"","",""),
                    ("ro", "322232", "an","fffffpass", 212,"","",""),("cisco", "332333", "prptpt","pasfsdfvs", 2244,"","","")]
    for i in list_servers:
       add_server(*i)
    assert get_servers() == list_servers
