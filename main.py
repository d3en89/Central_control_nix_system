import sys
from PyQt5 import QtWidgets, QtCore

import desing
import os


class ExampleApp(QtWidgets.QMainWindow, desing.Ui_MainMenu):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        ### Settings
        self.action_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        ### DataBase


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


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()