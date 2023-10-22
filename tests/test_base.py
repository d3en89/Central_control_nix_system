from db.database import connect_db, DATABASE
from scripts.sc_database import  add_server, get_servers
from os import path, remove
import pytest

@pytest.mark.parametrize("db", [DATABASE])
def test_create_database(db):
    if path.exists(db):
        remove(db)
    connect_db()
    assert path.exists(db) == True

def test_server_create(clean_servers_table):
    clean_servers_table
    list_servers = [("router", "332", "admin","pass", 22,"general","centos"),
                    ("mi", "34fd", "admina","passfff", 222,"general","ubuntu"),
                    ("ro", "322232", "an","fffffpass", 212,"general","ubuntu"),
                    ("cisco", "332333", "prptpt","pasfsdfvs", 2244,"general","feebsd")]
    for i in list_servers:
       add_server(*i)
    assert get_servers() == list_servers
