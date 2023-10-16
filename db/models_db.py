from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from db.database import Base
from datetime import datetime


class User_data(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)

    def __init__(self, name, pasw):
        self.login = name
        self.password = pasw

class Servers(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    dns_name = Column(String)
    ip = Column(String)
    username = Column(String)
    password = Column(String)
    ssh_port = Column(Integer)

    def __init__(self, name, ip, user, pasw, port):
        self.dns_name = name
        self.ip = ip
        self.username = user
        self.password = pasw
        self.ssh_port = port

