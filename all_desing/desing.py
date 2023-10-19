# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\desing.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(847, 432)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainMenu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu_base = QtWidgets.QMenu(self.menuBar)
        self.menu_base.setObjectName("menu_base")
        self.obj_settings = QtWidgets.QMenu(self.menuBar)
        self.obj_settings.setObjectName("obj_settings")
        MainMenu.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainMenu)
        self.statusBar.setObjectName("statusBar")
        MainMenu.setStatusBar(self.statusBar)
        self.action_create_db = QtWidgets.QAction(MainMenu)
        self.action_create_db.setObjectName("action_create_db")
        self.action_connect_db = QtWidgets.QAction(MainMenu)
        self.action_connect_db.setObjectName("action_connect_db")
        self.action_settings = QtWidgets.QAction(MainMenu)
        self.action_settings.setObjectName("action_settings")
        self.action_exit = QtWidgets.QAction(MainMenu)
        self.action_exit.setObjectName("action_exit")
        self.action_syslog = QtWidgets.QAction(MainMenu)
        self.action_syslog.setObjectName("action_syslog")
        self.menu_base.addAction(self.action_create_db)
        self.menu_base.addAction(self.action_connect_db)
        self.menu_base.addSeparator()
        self.menu_base.addAction(self.action_syslog)
        self.obj_settings.addAction(self.action_settings)
        self.obj_settings.addSeparator()
        self.obj_settings.addAction(self.action_exit)
        self.menuBar.addAction(self.obj_settings.menuAction())
        self.menuBar.addAction(self.menu_base.menuAction())

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Controlcenter"))
        self.menu_base.setTitle(_translate("MainMenu", "База"))
        self.obj_settings.setTitle(_translate("MainMenu", "Настройки"))
        self.action_create_db.setText(_translate("MainMenu", "Создать базу данных"))
        self.action_connect_db.setText(_translate("MainMenu", "Подключить базу данных"))
        self.action_settings.setText(_translate("MainMenu", "Настройки пользователя"))
        self.action_exit.setText(_translate("MainMenu", "Выход"))
        self.action_syslog.setText(_translate("MainMenu", "Просмотр логов"))