from db.database import create_db, Session, DATABASE
from db.models_db import User_data, Servers
from sc_database import create_database, add_user, add_server, get_user,get_servers
from os import path
import pytest

def test_user_create(clean_user_table):
    clean_user_table
    add_user('haos', 'patron')
    assert get_user() == (1,'haos', 'patron')


def test_server_create(clean_servers_table):
    clean_servers_table
    list_servers = [('router', '332', 'admin','pass', 22),('mi', '34fd', 'admina','passfff', 222),
                    ('ro', '322232', 'an','fffffpass', 212),('cisco', '332333', 'prptpt','pasfsdfvs', 2244)]
    for i in list_servers:
       add_server(*i)
    assert get_servers() == list_servers
