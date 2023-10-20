from string import ascii_lowercase, ascii_uppercase,digits,punctuation
from os import path

latinitca = ascii_uppercase + ascii_lowercase + digits
password = latinitca + punctuation
def check_latinitca(*arg):
    ans = []
    for i in arg:
        if len(i) > 0 :
            aaa = list(map(lambda s : True if s in password else False, i))
            ans.append(all(aaa))
        else:
            return False
    return all(ans)

def check_fsettings():
    if not path.exists('../settings.conf'):
        with open('../settings.conf', "w") as file:
            file.write("[base]\n")
            file.write("username = \n")
            file.write("path_db = \n")

def check_db_table():
    pass
