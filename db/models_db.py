from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from typing import NoReturn

from db.database import Base
from datetime import datetime

class Servers(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True)
    dns_name = Column(String)
    ip = Column(String)
    username = Column(String)
    password = Column(String)
    ssh_port = Column(Integer)
    group = Column(String)
    system = Column(String)

    def __init__(self, name, ip, user, pasw, port, group,system) -> NoReturn:
        self.dns_name = name
        self.ip = ip
        self.username = user
        self.password = pasw
        self.ssh_port = port
        self.group = group
        self.system = system

class Syslog(Base):
    __tablename__ = "syslog"
    id = Column(Integer, primary_key=True)
    date = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    message = Column(String)

    def __init__(self, mes) -> NoReturn:
        self.message = mes