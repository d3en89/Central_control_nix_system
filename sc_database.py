from os import path
import configparser

from db.database import connect_db, Session, DATABASE
from db.models_db import User_data, Servers, Syslog


class Config(configparser.ConfigParser):
    __config_path = 'settings.conf'

    def get_settings(self):
        self.read(self.__config_path)
        self.db = self.get('base', 'path_db')
        self.username = self.get('base', 'username')

    def set_settings(self, username, database='default.db'):
        self.set('base', 'path_db', database)
        self.set('base', 'username', username)
        with open(self.__config_path, 'r+') as conf_file:
            self.write(conf_file)


def check_settings():
    if not path.exists('settings.conf'):
        with open('settings.conf', "w") as file:
            file.write("[base]\n")
            file.write("username = \n")
            file.write("path_db = \n")

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

def add_user(name="admin", pasw="admin"):
    try:
        user = User_data(name, pasw)
        session = Session()
        session.add(user)
        session.commit()
        session.close()
        log_write(f"User create {name} and password")
    except Exception as err:
        log_write(err)
        return err


def add_server(name, ip, username, password, ssh_port,group="",domain="",system=""):
    try:
        srv = Servers(name, ip, username, password, ssh_port,group,domain,system)
        session = Session()
        session.add(srv)
        session.commit()
        session.close()
        log_write(f"Server added {name}, {ip}, {username}, {ssh_port} and password")
    except Exception as err:
        log_write(err)
        return err

def get_user(name=""):
    session = Session()
    return  session.query(User_data.id, User_data.login,User_data.password).first()

def get_servers(name=""):
    session = Session()
    return session.query(Servers.dns_name,Servers.ip,Servers.username,Servers.password,Servers.ssh_port,Servers.group,
                         Servers.domain,Servers.system).all()

