from os import path
import configparser
import hashlib

from db.database import connect_db, Session, DATABASE
from db.models_db import Servers, Syslog


class Config(configparser.ConfigParser):
    __config_path = './settings.conf'

    def get_settings(self):
        self.read(self.__config_path)
        self.db = self.get('base', 'path_db')
        self.username = self.get('base', 'username')

    def set_settings(self, username, database='default.db'):
        self.set('base', 'path_db', database)
        self.set('base', 'username', username)
        with open(self.__config_path, 'r+') as conf_file:
            self.write(conf_file)


def log_write(mes :str):
    session = Session()
    str_log = Syslog(mes)
    session.add(str_log)
    session.commit()
    session.close()


def create_database(name=DATABASE):
    if not path.exists(name):
        try:
            connect_db()
            log_write(f"Создание базы {name} прошло успешно")
            return f"Создание базы {name} прошло успешно"
        except Exception as err:
            return err
    else:
        return f"Имя default.db уже существует"

def get_hash(login, password, serv_p=''):
    u = hashlib.md5(login.encode()).hexdigest()
    p = hashlib.md5((login+password).encode()).hexdigest()
    if len(serv_p) != 0:
        return hashlib.md5((login+serv_p+password).encode()).hexdigest()
    else:
        return (u,p)



def add_server(name, ip, username, password, ssh_port,group="",system="" ):
    try:
        srv = Servers(name, ip, username, password, ssh_port,group,system)
        session = Session()
        session.add(srv)
        session.commit()
        session.close()
        log_write(f"Server added {name}, {ip}, {username}, {ssh_port} and password")
    except Exception as err:
        log_write(err)
        return err

def get_servers(name=""):
    session = Session()
    return session.query(Servers.dns_name,Servers.ip,Servers.username,Servers.password,Servers.ssh_port,Servers.group,
                         Servers.system).all()

