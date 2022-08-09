from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Set_PassWord(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 200,30))
        self.label.setObjectName("label")

        self.line_name = QtWidgets.QLineEdit(Dialog)
        self.line_name .setGeometry(QtCore.QRect(50, 30, 200,30))
        self.line_name .setObjectName("line")

        self.line = QtWidgets.QLineEdit(Dialog)
        self.line .setGeometry(QtCore.QRect(50, 70, 200,30))
        self.line .setObjectName("line")
        self.line.setEchoMode(QLineEdit.Password)

        self.line_1 = QtWidgets.QLineEdit(Dialog)
        self.line_1.setGeometry(QtCore.QRect(50, 110, 200,30))
        self.line_1.setObjectName("line_2")
        self.line_1.setEchoMode(QLineEdit.Password)

        self.loadbtn = QtWidgets.QPushButton(Dialog)
        self.loadbtn .setGeometry(QtCore.QRect(80, 150, 100,30))
        self.loadbtn .setObjectName("newlabel")

        self.retranslateUi_1(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi_1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set New Password"))
        self.label.setText("Set Password")
        self.loadbtn.setText("Finish")
        self.line_name.setPlaceholderText("Enter Name")
        self.line.setPlaceholderText("Enter Password")
        self.line_1.setPlaceholderText("Confirm password")


