import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialog

from scripts.sc_database import create_database, DATABASE, Config
from scripts.checking_param import  check_fsettings,check_db_table
from all_desing import desing, createUser


class EnterUser(QDialog, createUser.Ui_createUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_post.clicked.connect(self.enter_user)

    def enter_user(self):
        self.close()

class ExampleApp(QtWidgets.QMainWindow, desing.Ui_MainMenu):
    """ Иницилизируем класс основного дизайна """
    def __init__(self):
        super().__init__()
        self.ub = ''
        self.up = ''
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.action_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.action_create_db.triggered.connect(self.new_base)
        self.action_connect_db.triggered.connect(self.enter_base)

    def new_base(self):
        """ Используется для создания новой базы с названием default.db,
            база создаётся там же, от куда запускается данное приложение.
        """
        error = QMessageBox()
        try:
            status_db = create_database()
            if status_db == f"Создание базы {DATABASE} прошло успешно":
                setting = Config()
                setting.get_settings()
                setting.set_settings(self.ub)
                error.setWindowTitle("Информация")
                error.setText("База данных и новый пользователь успешно созданны")
                error.setIcon(QMessageBox.Information)
                error.exec_()
            else:
                error.setWindowTitle("Внимание")
                error.setText(f"{status_db}")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
        except Exception as err:
            error.setWindowTitle('Оибка')
            error.setIcon(QMessageBox.Warning)
            error.setText(f"{err}")
            error.exec_()

    def enter_base(self):
        """ Используется для подключения уже существущей базы которую вы укажитt
            изменяет параметры в файле settings.conf,  так же при подключении
            проверяет указанную базу на корректную структуру.
        """
        self.cwd = os.getcwd()
        db_file, filetype = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл базы данных", self.cwd, "All Files (*);;DB files (*.db);;SQL Lite (*.sqlite)")
        error = QMessageBox()
        try:
            if check_db_table(db_file):
                seti = Config()
                seti.get_settings()
                seti.set_settings(f"{self.ub}",f"{db_file}")
            else:
                error.setWindowTitle('Ошибка')
                error.setText('Выбранная вами база не подходит для работы программы')
                error.Warning
                error.exec_()
        except Exception as err:
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Critical)
            error.setText(f"{err}")
            error.exec_()




def main():
    check_fsettings()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    enter_us = EnterUser()
    enter_us.exec_()
    window.ub, window.up = enter_us.lineEdit_user.text(), enter_us.lineEdit_password.text()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == "__main__":  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()