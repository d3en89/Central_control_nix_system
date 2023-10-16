from db.database import create_db, Session, DATABASE
from db.models_db import User_data, Servers, Syslog
from os import path

def log_write(mes):
    session = Session()
    str_log = Syslog(mes)
    session.add(str_log)
    session.commit()
    session.close()

def create_database(name=DATABASE):
    if not path.exists(name):
        try:
            create_db()
            log_write(f"Создание базы {name} прошло успешно")
        except Exception as err:
            log_write(err)
    else:
        log_write(f"Такое имя базы уже существует")

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

