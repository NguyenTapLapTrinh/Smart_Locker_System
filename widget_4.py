from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Enter_PassWord(object):
    def setupUi_1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 150)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 200,30))
        self.label.setObjectName("label")

        self.line = QtWidgets.QLineEdit(Dialog)
        self.line .setGeometry(QtCore.QRect(50, 30, 200,30))
        self.line .setObjectName("line")
        self.line.setEchoMode(QLineEdit.Password)

        self.loadbtn = QtWidgets.QPushButton(Dialog)
        self.loadbtn .setGeometry(QtCore.QRect(70, 100, 100,30))
        self.loadbtn .setObjectName("newlabel")

        self.retranslateUi_1(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi_1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Check PassWord"))
        self.label.setText("")
        self.loadbtn.setText("Finish")
        self.line.setPlaceholderText("Enter PassWord")