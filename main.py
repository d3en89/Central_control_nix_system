import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QMessageBox
import configparser

from sc_database import create_database, add_user, DATABASE, Config
from all_desing import desing, createUser



class CreateNewDBUser(QtWidgets.QWidget, createUser.Ui_createUser):
    """ Иницилизируем класс дизайна который будет вызывться при нажатии кнопки Создать базу данных """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = ""
        self.pushButton_post.clicked.connect(self.create_datebase)
    def create_datebase(self):
        error = QMessageBox()
        if  self.lineEdit_new_user.text() == "" or self.lineEdit_new_password.text()  == "":
            error.setWindowTitle("Ошибка")
            error.setText( "Обязательно надо ввести новые имя пользователя и пароль ")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
            return CreateNewDBUser().show()
        else:
            status_db = create_database()
            if status_db == f"Создание базы {DATABASE} прошло успешно":
                setting = Config()
                setting.get_settings()
                print(setting.db, setting.username)
                setting.set_settings(self.lineEdit_new_user.text())
                add_user(self.lineEdit_new_user.text(), self.lineEdit_new_password.text())
                error.setWindowTitle("Информация")
                error.setText("База данных и новый пользователь успешно созданны")
                error.setIcon(QMessageBox.Information)
                error.exec_()
            else:
                error.setWindowTitle("Внимание")
                error.setText(f"{status_db}")
                error.setIcon(QMessageBox.Warning)
                error.exec_()

        self.close()


class ExampleApp(QtWidgets.QMainWindow, desing.Ui_MainMenu):
    """ Иницилизируем класс основного дизайна """
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.action_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.action_create_db.triggered.connect(self.active_proc_create)


    def active_proc_create(self):
        self.user = CreateNewDBUser()
        self.user.show()



    # def browse_folder(self):
    #     self.listWidget.clear()  # На случай, если в списке уже есть элементы
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    #     # открыть диалог выбора директории и установить значение переменной
    #     # равной пути к выбранной директории
    #
    #     if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
    #         for file_name in os.listdir(directory):  # для каждого файла в директории
    #             self.listWidget.addItem(file_name)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()