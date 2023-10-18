import sys
from PyQt5 import QtWidgets, QtCore
from  PyQt5.QtWidgets import QInputDialog, QMessageBox
from sc_database import create_database
from all_desing import desing, createUser

class CreateNewUser(QtWidgets.QWidget, createUser.Ui_createUser):
    """ Иницилизируем класс дизайна который будет вызывться при нажатии кнопки Создать базу данных """
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExampleApp(QtWidgets.QMainWindow, desing.Ui_MainMenu):
    """ Иницилизируем класс основного дизайна """
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.action_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.action_create_db.triggered.connect(self.database_create)


    def database_create(self):
        self.user = CreateNewUser()
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