# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\crateUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createUser(object):
    def setupUi(self, createUser):
        createUser.setObjectName("createUser")
        createUser.resize(400, 101)
        self.label_new_user = QtWidgets.QLabel(createUser)
        self.label_new_user.setGeometry(QtCore.QRect(80, 10, 25, 16))
        self.label_new_user.setObjectName("label_new_user")
        self.label__new_password = QtWidgets.QLabel(createUser)
        self.label__new_password.setGeometry(QtCore.QRect(70, 40, 46, 16))
        self.label__new_password.setObjectName("label__new_password")
        self.pushButton_post = QtWidgets.QPushButton(createUser)
        self.pushButton_post.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButton_post.setObjectName("pushButton_post")
        self.lineEdit_new_user = QtWidgets.QLineEdit(createUser)
        self.lineEdit_new_user.setGeometry(QtCore.QRect(130, 10, 133, 20))
        self.lineEdit_new_user.setObjectName("lineEdit_new_user")
        self.lineEdit_new_password = QtWidgets.QLineEdit(createUser)
        self.lineEdit_new_password.setGeometry(QtCore.QRect(130, 40, 133, 20))
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")

        self.retranslateUi(createUser)
        QtCore.QMetaObject.connectSlotsByName(createUser)

    def retranslateUi(self, createUser):
        _translate = QtCore.QCoreApplication.translate
        createUser.setWindowTitle(_translate("createUser", "Form"))
        self.label_new_user.setText(_translate("createUser", "Login"))
        self.label__new_password.setText(_translate("createUser", "Password"))
        self.pushButton_post.setText(_translate("createUser", "Создать"))
