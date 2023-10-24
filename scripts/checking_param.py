from string import ascii_lowercase, ascii_uppercase,digits,punctuation
from os import path
import sqlalchemy
from typing import NoReturn

from db.models_db import Syslog, Servers

latinitca = ascii_uppercase + ascii_lowercase + digits
password = latinitca + punctuation
def check_latinitca(*arg) -> bool:
    ans = []
    for i in arg:
        if len(i) > 0 :
            aaa = list(map(lambda s : True if s in password else False, i))
            ans.append(all(aaa))
        else:
            return False
    return all(ans)

def check_fsettings() -> NoReturn:
    if not path.exists('./settings.conf'):
        with open('./settings.conf', "w") as file:
            file.write("[base]\n")
            file.write("username = \n")
            file.write("path_db = \n")

def check_db_table(path_to_db):
    list_class = [Servers, Syslog]
    engine = sqlalchemy.engine.create_engine(f"sqlite:///{path_to_db}")
    def check_table() -> bool:
        list_check = []
        for orig_table in list_class:
            if orig_table.__tablename__ in sqlalchemy.inspect(engine).get_table_names():
                list_check.append(True)
            else:
                list_check.append(False)
        return all(list_check)

    def check_column() -> bool:
        list_check = []
        try:
            for table in list_class:
                for column in sqlalchemy.inspect(table).column_attrs:
                    list_column_ans = list(map(lambda row: row['name'] ,sqlalchemy.inspect(engine).get_columns(table.__tablename__)))
                    if column.key in list_column_ans:
                        list_check.append(True)
                    else:
                        list_check.append(False)
        except Exception as err:
            list_check.append(False)
        return all(list_check)

    return all([check_table(),check_column()])