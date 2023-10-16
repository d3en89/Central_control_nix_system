from db.database import create_db, Session, DATABASE
from db.models_db import User_data, Servers
from os import path

def create_database():
    if not path.exists(DATABASE):
        try:
            create_db()
            return "Создание базы прошло успешно"
        except Exception as err:
            return err
    else:
        return "Такое имя базы уже существует"


def add_user(name='admin', pasw='admin'):
    user = User_data(name, pasw)
    session = Session()
    session.add(user)
    session.commit()
    session.close()


def add_server(name, ip, username, password, ssh_port):
    srv = Servers(name, ip, username, password, ssh_port)
    session = Session()
    session.add(srv)
    session.commit()
    session.close()


print(create_database())
add_server('router', '192.168.1.1', 'admin', 'passwords', '22')

