from fileinput import close
from tkinter import image_names
from PyQt5 import QtCore, QtGui, QtWidgets
from cv2 import waitKey
import image
from widget_1 import*
from widget_2 import*
from widget_3 import*
from widget_4 import*
from widget_5 import*
import face_recognition
from video import*
import cv2
import sys
import os
import glob
from firebase import firebase
import time 
from simple_facerec import SimpleFacerec
firebase = firebase.FirebaseApplication('https://doan2-f1530-default-rtdb.firebaseio.com/', None)
Tu1 = 'Wardrobe/Tu1'
Name1 = '/Name'
PassWord1 = "/PassWord"
Status1 = '/Status'
Tu2 = 'Wardrobe/Tu2'
Name2 = '/Name'
Status2 = '/Status'
PassWord2 = "/PassWord"
Tu3 = 'Wardrobe/Tu3'
Name3 = '/Name'
Status3 = '/Status'
PassWord3 = "/PassWord"
Tu4 = 'Wardrobe/Tu4'
Name4 = '/Name'
Status4 = '/Status'
PassWord4 = "/PassWord"
# Giao dien cai dat mo khoa bang khuon mat
class Widget_1(QDialog):
    def __init__(self, parent=None):
        super(Widget_1, self).__init__(parent)
        self.ui_1 = Ui_Dialog_1()
        self.ui_1.setupUi_1(self)
        self.ui_3 = Widget_3()
        self.name =""
        self.selection = 0
        self.ui_1.loadbtn.clicked.connect(self.create)
    def set(self, selection):
        if selection ==1:
                self.name = firebase.get(Tu1, "Name")
                self.ui_1.line.clear()
                self.ui_1.line.setEnabled(True)
                if self.name!="":
                        self.ui_1.line.setText(self.name)
                        self.ui_1.line.setEnabled(False)
        if selection ==2:
                self.name = firebase.get(Tu2, "Name")
                self.ui_1.line.clear()
                self.ui_1.line.setEnabled(True)
                if self.name!="":
                        self.ui_1.line.setText(self.name)
                        self.ui_1.line.setEnabled(False)
        if selection ==3:
                self.name = firebase.get(Tu3, "Name")
                self.ui_1.line.clear()
                self.ui_1.line.setEnabled(True)
                if self.name!="":
                        self.ui_1.line.setText(self.name)
                        self.ui_1.line.setEnabled(False)
        if selection ==4:
                self.name = firebase.get(Tu4, "Name")
                self.ui_1.line.clear()
                self.ui_1.line.setEnabled(True)
                if self.name!="":
                        self.ui_1.line.setText(self.name)
                        self.ui_1.line.setEnabled(False)
    def create(self):
        name =  self.ui_1.line.text()
        if name =="": return
        self.ui_3.selection = self.selection
        self.ui_3.name = name
        self.ui_3.Run.Capture = cv2.VideoCapture(0)
        self.ui_3.Run.ThreadActive = True
        self.ui_3.Run.start()
        self.ui_3.show()
        self.close()
#Giao dien tao mat khau
class Widget_4(QDialog):
    def __init__(self, parent=None):
        super(Widget_4, self).__init__(parent)
        self.ui_4 = Set_PassWord()
        self.ui_4.setupUi(self)
        self.name = ""
        self.password = ""
        self.selection = 0
        self.ui_4.loadbtn.clicked.connect(self.create)
    def set(self, selection):
        if selection ==1:
                self.name = firebase.get(Tu1, "Name")
                self.ui_4.line_name.clear()
                self.ui_4.line_1.clear()
                self.ui_4.line.clear()
                self.ui_4.line_name.setEnabled(True)
                if self.name!="":
                        self.ui_4.line_name.setText(self.name)
                        self.ui_4.line_name.setEnabled(False)
        if selection ==2:
                self.name = firebase.get(Tu2, "Name")
                self.ui_4.line_name.clear()
                self.ui_4.line_1.clear()
                self.ui_4.line.clear()
                self.ui_4.line_name.setEnabled(True)
                if self.name!="":
                        self.ui_4.line_name.setText(self.name)
                        self.ui_4.line_name.setEnabled(False)
        if selection ==3:
                self.name = firebase.get(Tu3, "Name")
                self.ui_4.line_name.clear()
                self.ui_4.line_1.clear()
                self.ui_4.line.clear()
                self.ui_4.line_name.setEnabled(True)
                if self.name!="":
                        self.ui_4.line_name.setText(self.name)
                        self.ui_4.line_name.setEnabled(False)
        if selection ==4:
                self.name = firebase.get(Tu4, "Name")
                self.ui_4.line_name.clear()
                self.ui_4.line_1.clear()
                self.ui_4.line.clear()
                self.ui_4.line_name.setEnabled(True)
                if self.name!="":
                        self.ui_4.line_name.setText(self.name)
                        self.ui_4.line_name.setEnabled(False)
    def create(self):
        name = self.ui_4.line_name.text()
        password =  self.ui_4.line.text()
        if name == "": return
        if password =="": return
        confirm = self.ui_4.line_1.text()
        if confirm == "": return
        if confirm !=password:
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("The confirm password is not same!   ")
                self.dlg.setWindowTitle("Infomation")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                return
        if self.selection == 1:
                firebase.put(Tu1,Name1, name)
                firebase.put(Tu1,PassWord1, password)
        if self.selection == 2:
                firebase.put(Tu2,Name2, name)
                firebase.put(Tu2,PassWord2, password)  
        if self.selection == 3:
                firebase.put(Tu3,Name3, name)
                firebase.put(Tu3,PassWord3, password)  
        if self.selection == 4:
                firebase.put(Tu4,Name4, name)
                firebase.put(Tu4,PassWord4, password)
        self.dlg_2 = QMessageBox()
        self.dlg_2.setIcon(QMessageBox.Information)
        self.dlg_2.setText("Successfully!               ")
        self.dlg_2.setWindowTitle("Infomation")
        self.dlg_2.setStandardButtons(QMessageBox.Ok)
        self.dlg_2.exec()
        self.close()
#Giao dien kiem tra mat khau
class Widget_5(QDialog):
    def __init__(self, parent=None):
        super(Widget_5, self).__init__(parent)
        self.ui_5 = Enter_PassWord()
        self.ui_5.setupUi_1(self)
        self.ui_2 = Widget_2()
        self.ui_6 = Widget_6()
        self.ui_5.loadbtn.clicked.connect(self.create)
        self.selection = 0
    def PasswordBox(self, text):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msg.button(QMessageBox.Yes)
        buttonY.setText("Open Closet UI")
        buttonN = msg.button(QMessageBox.No)
        buttonN.setText("Change PassWord")
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setWindowTitle('Set up closet')
        msg.exec_()
        button = msg.clickedButton()
        sb = msg.standardButton(button)
        if sb == QMessageBox.Yes:
                return 1
        else: 
                return 2
    def create(self):
        password =  self.ui_5.line.text()
        self.ui_5.line.clear()
        if password =="": return
        if self.selection == 1:
                result = firebase.get(Tu1,"PassWord")
                if str(password) == str(result):
                        self.close()
                        password_mode = self.PasswordBox("Which method do you want?          ")
                        if password_mode == 1:
                                self.ui_2.selection = 1
                                self.ui_2.name = firebase.get(Tu1,"Name")
                                self.ui_2.show()
                                self.close()
                        elif password_mode == 2:
                                self.ui_6.selection =1
                                self.ui_6.show()
                                self.close()
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
        if self.selection == 2:
                result = firebase.get(Tu2,"PassWord")
                if str(password) == str(result):
                        self.close()
                        password_mode = self.PasswordBox("Which method do you want?          ")
                        if password_mode == 1:
                                self.ui_2.selection = 2
                                self.ui_2.name = firebase.get(Tu2,"Name")
                                self.ui_2.show()
                                self.close()
                        elif password_mode == 2:
                                self.ui_6.selection =2
                                self.ui_6.show()
                                self.close()
        if self.selection == 3:
                result = firebase.get(Tu3,"PassWord")
                if str(password) == str(result):
                        self.close()
                        password_mode = self.PasswordBox("Which method do you want?          ")
                        if password_mode == 1:
                                self.ui_2.selection = 3
                                self.ui_2.name = firebase.get(Tu3,"Name")
                                self.ui_2.show()
                                self.close()
                        elif password_mode == 2:
                                self.ui_6.selection =3
                                self.ui_6.show()
                                self.close()
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
        if self.selection == 4:
                result = firebase.get(Tu4,"PassWord")
                if str(password) == str(result):
                        self.close()
                        password_mode = self.PasswordBox("Which method do you want?          ")
                        if password_mode == 1:
                                self.ui_2.selection = 4
                                self.ui_2.name = firebase.get(Tu4,"Name")
                                self.ui_2.show()
                                self.close()
                        elif password_mode == 2:
                                self.ui_6.selection =4
                                self.ui_6.show()
                                self.close()
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()              
        
#Giao dien doi mat khau
class Widget_6(QDialog):
    def __init__(self, parent=None):
        super(Widget_6, self).__init__(parent)
        self.ui_6 = Change_PassWord()
        self.ui_6.setupUi(self)
        self.ui_2 = Widget_2()
        self.ui_6.loadbtn.clicked.connect(self.create)
        self.selection = 0
    def create(self):
        old_password =  self.ui_6.line.text()
        new_password = self.ui_6.line_1.text()
        confirm_password = self.ui_6.line_2.text()
        if old_password =="" or new_password =="" or confirm_password=="": return
        if self.selection == 1:
                result = firebase.get(Tu1,"PassWord")
                if old_password !=result:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                if confirm_password !=new_password:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is not same!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                else:
                        firebase.put(Tu1,PassWord1, new_password)
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("Successfully!        ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.ui_2.selection = 1
                        self.ui_2.name = firebase.get(Tu1,"Name")
                        self.ui_2.show()
                        self.close()
        if self.selection == 2:
                result = firebase.get(Tu2,"PassWord")
                if old_password !=result:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                if confirm_password !=new_password:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is not same!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                else:
                        firebase.put(Tu2,PassWord2, new_password)
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("Successfully!        ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.ui_2.selection = 2
                        self.ui_2.name = firebase.get(Tu2,"Name")
                        self.ui_2.show()
                        self.close()
        if self.selection == 3:
                result = firebase.get(Tu3,"PassWord")
                if old_password !=result:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                if confirm_password !=new_password:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is not same!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                else:
                        firebase.put(Tu3,PassWord3, new_password)
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("Successfully!        ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.ui_2.selection = 3
                        self.ui_2.name = firebase.get(Tu3,"Name")
                        self.ui_2.show()
                        self.close()
        if self.selection == 4:
                result = firebase.get(Tu4,"PassWord")
                if old_password !=result:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                if confirm_password !=new_password:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is not same!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
                        return
                else:
                        firebase.put(Tu1,PassWord4, new_password)
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("Successfully!        ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.ui_2.selection = 4
                        self.ui_2.name = firebase.get(Tu4,"Name")
                        self.ui_2.show()
                        self.close()
                

#Giao dien tuong tac nguoi dung
class Widget_2(QDialog):
    def __init__(self, parent=None):
        super(Widget_2, self).__init__(parent)
        self.ui_2 = Ui_Dialog_2()
        self.ui_2.setupUi_2(self)
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.start(1000)
        self.timer.timeout.connect(self.settime)
        self.ui_2.exit.clicked.connect(self.close)
        self.ui_2.open_btn.clicked.connect(self.open_closet)
        self.ui_2.close_btn.clicked.connect(self.close_closet)
        self.ui_2.unregister.clicked.connect(self.delete)
        self.name = ""
        self.selection = 0
        self.settime()
    def settime(self):
        time_module = time.localtime()
        time_time = time.strftime("%H:%M:%S %p", time_module)
        self.ui_2.Time.setText(time_time)
        self.ui_2.user_name.setText(self.name)
    def open_closet(self):
        self.ui_2.closet_status.setStyleSheet("image: url(:/Closet/closet_open.png);")
        if self.selection == 1:
                firebase.put(Tu1,Status1,"1")
        if self.selection == 2:
                firebase.put(Tu2,Status2,"1") 
        if self.selection == 3:
                firebase.put(Tu3,Status3,"1") 
        if self.selection == 4:
                firebase.put(Tu4,Status4,"1")
    def close_closet(self):
        self.ui_2.closet_status.setStyleSheet("image: url(:/Closet/closet_close.png);")
        if self.selection == 1:
                firebase.put(Tu1,Status1,"0")
        if self.selection == 2:
                firebase.put(Tu2,Status2,"0") 
        if self.selection == 3:
                firebase.put(Tu3,Status3,"0") 
        if self.selection == 4:
                firebase.put(Tu4,Status4,"0")
    def delete(self):
        if self.selection == 1:
                images_path = glob.glob(r"closet_1\*.jpg")
                if len(images_path) != 0:
                        os.remove("closet_" + str(self.selection)+"/"+self.name+".jpg")
                firebase.put(Tu1,Name1,"")
                firebase.put(Tu1,PassWord1,"")
                firebase.put(Tu1,Status1,"0")
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Successfully!                 ")
                self.dlg.setWindowTitle("Infomation")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.close()
        if self.selection == 2:
                images_path = glob.glob(r"closet_2\*.jpg")
                if len(images_path) != 0:
                        os.remove("closet_" + str(self.selection)+"/"+self.name+".jpg")
                firebase.put(Tu2,Name2,"")
                firebase.put(Tu2,PassWord2,"")
                firebase.put(Tu2,Status2,"0")
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Successfully!                 ")
                self.dlg.setWindowTitle("Infomation")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.close()
        if self.selection == 3:
                images_path = glob.glob(r"closet_3\*.jpg")
                if len(images_path) != 0:
                        os.remove("closet_" + str(self.selection)+"/"+self.name+".jpg")
                firebase.put(Tu3,Name3,"")
                firebase.put(Tu3,PassWord3,"")
                firebase.put(Tu3,Status3,"0")
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Successfully!                 ")
                self.dlg.setWindowTitle("Infomation")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.close()
        if self.selection == 4:
                images_path = glob.glob(r"closet_4\*.jpg")
                if len(images_path) != 0:
                        os.remove("closet_" + str(self.selection)+"/"+self.name+".jpg")
                firebase.put(Tu4,Name4,"")
                firebase.put(Tu4,PassWord4,"")
                firebase.put(Tu4,Status4,"0")
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Successfully!                 ")
                self.dlg.setWindowTitle("Infomation")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.close()
#Giao dien kiem tra mat khau khi dang ki khoa khuon mat
class Widget_7(QDialog):
    def __init__(self, parent=None):
        super(Widget_7, self).__init__(parent)
        self.ui_5 = Enter_PassWord()
        self.ui_5.setupUi_1(self)
        self.ui_1 = Widget_1()
        self.ui_5.loadbtn.clicked.connect(self.create)
        self.selection = 0
        self.check  = 0 
    def create(self):
        password =  self.ui_5.line.text()
        self.ui_5.line.clear()
        if password =="": return
        if self.selection == 1:
                result = firebase.get(Tu1,"PassWord")
                if str(password) == str(result):
                        self.close()
                        self.ui_1.selection = 1
                        self.ui_1.set(1)               
                        self.ui_1.show()
  
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
        if self.selection == 2:
                result = firebase.get(Tu2,"PassWord")
                if str(password) == str(result):
                        self.close()
                        self.ui_1.selection = 2
                        self.ui_1.set(2)               
                        self.ui_1.show()
  
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
        if self.selection == 3:
                result = firebase.get(Tu3,"PassWord")
                if str(password) == str(result):
                        self.close()
                        self.ui_1.selection = 3
                        self.ui_1.set(3)               
                        self.ui_1.show()
  
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()
        if self.selection == 4:
                result = firebase.get(Tu4,"PassWord")
                if str(password) == str(result):
                        self.close()
                        self.ui_1.selection = 4
                        self.ui_1.set(4)               
                        self.ui_1.show()
  
                else:
                        self.dlg = QMessageBox()
                        self.dlg.setIcon(QMessageBox.Information)
                        self.dlg.setText("The password is incorrect!   ")
                        self.dlg.setWindowTitle("Infomation")
                        self.dlg.setStandardButtons(QMessageBox.Ok)
                        self.dlg.exec()
                        self.close()              
        
#Thread khoi dong camera tren pyqt5
class Run(QThread):
    ImageUpdate = pyqtSignal(QImage)
    ThreadActive = False
    def run(self):    
        while self.ThreadActive:
            ret, self.frame = self.Capture.read()
            if ret:
                Image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                ConvertToQTFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQTFormat.scaled(600, 600, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def Stop(self):
        self.ThreadActive = False
        self.quit()
# Giao dien dang ki khoa khuon mat
class Widget_3(QDialog):
    def __init__(self, parent=None):
        super(Widget_3, self).__init__(parent)
        self.ui_3 = Video()
        self.ui_3.setupUi(self)
        self.ui_3.btn1.clicked.connect(self.capture)
        self.ui_3.btn2.clicked.connect(self.close_cam)
        self.Run = Run()
        self.Run.ImageUpdate.connect(self.ImageUpdateShot)
        self.Run.start()
        self.selection = 0
        self.name = ""
    def ImageUpdateShot(self, Image):
        self.ui_3.video_label.setPixmap(QPixmap.fromImage(Image))
    def capture(self):
        self.Run.ThreadActive = False
        cv2.imwrite("closet_" + str(self.selection)+"/"+self.name+".jpg",self.Run.frame)
        image = face_recognition.load_image_file("closet_" + str(self.selection)+"/"+self.name+".jpg")
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0: 
                os.remove("closet_" + str(self.selection)+"/"+self.name+".jpg")
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Cannot detect your face, Try again!")
                self.dlg.setWindowTitle("Warning")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.Run.Capture = cv2.VideoCapture(0)
                self.Run.ThreadActive = True
                self.Run.start()
        else:
                if self.selection == 1:
                        firebase.put(Tu1,Name1, self.name)
                if self.selection == 2:
                        firebase.put(Tu2,Name2, self.name)  
                if self.selection == 3:
                        firebase.put(Tu3,Name3, self.name)  
                if self.selection == 4:
                        firebase.put(Tu4,Name4, self.name)
                self.dlg = QMessageBox()
                self.dlg.setIcon(QMessageBox.Information)
                self.dlg.setText("Sucessful!                ")
                self.dlg.setWindowTitle("Information")
                self.dlg.setStandardButtons(QMessageBox.Ok)
                self.dlg.exec()
                self.Run.Capture.release()
                self.close()
    def close_cam(self):
        self.Run.ThreadActive = False
        self.Run.Capture.release()
        self.close()

#Giao dien chinh
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #9bdee7;")
        MainWindow.resize(711, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closet_1 = QtWidgets.QLabel(self.centralwidget)
        self.closet_1.setGeometry(QtCore.QRect(80, 100, 131, 131))
        self.closet_1.setStyleSheet("image: url(:/Closet/closet_close.png);\n"
"")
        self.closet_1.setText("")
        self.closet_1.setObjectName("closet_1")
        self.closet_4 = QtWidgets.QLabel(self.centralwidget)
        self.closet_4.setGeometry(QtCore.QRect(120, 70, 61, 20))
        self.closet_4.setObjectName("closet_4")
        font = QtGui.QFont() 
        font.setBold(True)
        self.closet_4.setFont(font)
        self.closet_2 = QtWidgets.QLabel(self.centralwidget)
        self.closet_2.setGeometry(QtCore.QRect(220, 100, 131, 131))
        self.closet_2.setStyleSheet("image: url(:/Closet/closet_close.png);\n"
"")
        self.closet_2.setText("")
        self.closet_2.setObjectName("closet_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 70, 61, 20))
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont() 
        font.setBold(True)
        self.label_5.setFont(font)
        self.closet_3 = QtWidgets.QLabel(self.centralwidget)
        self.closet_3.setGeometry(QtCore.QRect(360, 100, 131, 131))
        self.closet_3.setStyleSheet("image: url(:/Closet/closet_close.png);\n"
"")
        self.closet_3.setText("")
        self.closet_3.setObjectName("closet_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 70, 61, 20))
        self.label_6.setObjectName("label_6")
        font = QtGui.QFont() 
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 100, 131, 131))
        self.label_7.setStyleSheet("image: url(:/Closet/closet_close.png);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(540, 70, 61, 20))
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont() 
        font.setBold(True)
        self.label_8.setFont(font)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(250, 240, 75, 23))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(390, 240, 75, 23))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(530, 240, 75, 23))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(580, 10, 80, 20))
        self.btn_5.setObjectName("btn_5")
        self.btn_5.setText("EXIT")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_5.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: White;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 330, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ui_1 = Widget_1()
        self.ui_2 = Widget_2()
        self.ui_3 = Widget_3()
        self.ui_4 = Widget_4()
        self.ui_5 = Widget_5()
        self.ui_6 = Widget_6()
        self.ui_7 = Widget_7()
        #Processing
        self.btn_1.setText("ENTER")
        self.btn_2.setText("ENTER")
        self.btn_3.setText("ENTER")
        self.btn_4.setText("ENTER")
        self.btn_1.setStyleSheet("border: 2px solid black; background-color: #ccc")
        self.btn_2.setStyleSheet("border: 2px solid black; background-color: #ccc")
        self.btn_3.setStyleSheet("border: 2px solid black; background-color: #ccc")
        self.btn_4.setStyleSheet("border: 2px solid black; background-color: #ccc")
        self.btn_1.clicked.connect(self.open_folder_1)
        self.btn_2.clicked.connect(self.open_folder_2)
        self.btn_3.clicked.connect(self.open_folder_3)
        self.btn_4.clicked.connect(self.open_folder_4)
        self.btn_5.clicked.connect(self.closeEvent)
    def closeEvent(self):
        sb = self.question("Do you want to exit?")
        if sb == 1:
                os._exit(0)
        else:
                return
        # Function
    def question(self, text):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setWindowTitle('Register Question')
        msg.exec_()
        button = msg.clickedButton()
        sb = msg.standardButton(button)
        if sb == QMessageBox.Yes:
                return 1
        else: 
                return 2
    def MessBox(self, text):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msg.button(QMessageBox.Yes)
        buttonY.setText("PassWord")
        buttonN = msg.button(QMessageBox.No)
        buttonN.setText("Face Unlock")
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setWindowTitle('Set up closet')
        msg.exec_()
        button = msg.clickedButton()
        sb = msg.standardButton(button)
        if sb == QMessageBox.Yes:
                return 1
        elif sb == QMessageBox.No: 
                return 2
    def face_recognition(self,folder,Tu,Status,mode,selection):
        cap = cv2.VideoCapture(0)
        sfr = SimpleFacerec()
        sfr.load_encoding_images(folder)
        while True:
                realname = "Unknown"
                ret, frame = cap.read()
                face_locations, face_names = sfr.detect_known_faces(frame)
                for face_loc, name in zip(face_locations, face_names):
                        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                        if name != "Unknown":
                                firebase.put(Tu,Status, "1")
                                realname = name
                cv2.imshow("Frame", frame)
                k = cv2.waitKey(1)
                if k%256 == 27:
                        cv2.destroyAllWindows()
                        break
                if realname != "Unknown":
                        #time.sleep(2)
                        if mode == 1:
                                self.ui_2.name = realname
                                self.ui_2.selection = selection
                                self.ui_2.show()
                        else:
                                self.ui_4.selection = selection
                                self.ui_4.set(1)              
                                self.ui_4.show()
                        cap.release()
                        cv2.destroyAllWindows()
                        break
    def open_folder_1(self):
        person = firebase.get(Tu1,"Name")
        if person == "":
                result = self.question(" Do you want to register? ")
                if result==1:
                        request = self.MessBox("Which method do you want?          ")
                        if request==2:
                                self.ui_1.set(1)
                                self.ui_1.selection = 1             
                                self.ui_1.show()
                        elif request==1:
                                self.ui_4.set(1)
                                self.ui_4.selection = 1
                                self.ui_4.name = firebase.get(Tu1, "Name")                  
                                self.ui_4.show()
                                 
        else:   
                        result = self.question(" This closet is belong to "+ person + "\n" + "Do you want to continue?")
                        if result == 1:
                                request = self.MessBox("Which method do you want?          ")
                                if request == 2:
                                        images_path = glob.glob(r"closet_1\*.jpg")
                                        if len(images_path)!=0:
                                                person = firebase.get(Tu1, "Name")
                                                self.face_recognition("closet_1/",Tu1,Status1,1,1)
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.ui_7.selection =1
                                                        self.ui_7.show()

                                elif request==1:
                                        result = firebase.get(Tu1,"PassWord")
                                        if result!="":
                                                self.ui_5.selection = 1
                                                self.ui_5.show()
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.face_recognition("closet_1/",Tu1,Status1,0,1)

    def open_folder_2(self):
        person = firebase.get(Tu2,"Name")
        if person == "":
                result = self.question(" Do you want to register? ")
                if result==1:
                        request = self.MessBox("Which method do you want?          ")
                        if request==2:
                                self.ui_1.set(2)
                                self.ui_1.selection = 2             
                                self.ui_1.show()
                        elif request==1:
                                self.ui_4.set(2)
                                self.ui_4.selection = 2
                                self.ui_4.name = firebase.get(Tu2, "Name")                  
                                self.ui_4.show()
                                 
        else:   
                        result = self.question(" This closet is belong to "+ person + "\n" + "Do you want to continue?")
                        if result == 1:
                                request = self.MessBox("Which method do you want?          ")
                                if request == 2:
                                        images_path = glob.glob(r"closet_2\*.jpg")
                                        if len(images_path)!=0:
                                                person = firebase.get(Tu2, "Name")
                                                self.face_recognition("closet_2/",Tu2,Status2,1,2)
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.ui_7.selection =2
                                                        self.ui_7.show()
                                elif request==1:
                                        result = firebase.get(Tu2,"PassWord")
                                        if result!="":
                                                self.ui_5.selection = 2
                                                self.ui_5.show()
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.face_recognition("closet_2/",Tu2,Status2,0,2)

    def open_folder_3(self):
        person = firebase.get(Tu3,"Name")
        if person == "":
                result = self.question(" Do you want to register? ")
                if result==1:
                        request = self.MessBox("Which method do you want?          ")
                        if request==2:
                                self.ui_1.set(3)
                                self.ui_1.selection = 3             
                                self.ui_1.show()
                        elif request==1:
                                self.ui_4.set(3)
                                self.ui_4.selection = 3
                                self.ui_4.name = firebase.get(Tu3, "Name")                  
                                self.ui_4.show()
                                 
        else:   
                        result = self.question(" This closet is belong to "+ person + "\n" + "Do you want to continue?")
                        if result == 1:
                                request = self.MessBox("Which method do you want?          ")
                                if request == 2:
                                        images_path = glob.glob(r"closet_3\*.jpg")
                                        if len(images_path)!=0:
                                                person = firebase.get(Tu3, "Name")
                                                self.face_recognition("closet_3/",Tu3,Status3,1,3)
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.ui_7.selection =3
                                                        self.ui_7.show()
                                elif request==1:
                                        result = firebase.get(Tu3,"PassWord")
                                        if result!="":
                                                self.ui_5.selection = 3
                                                self.ui_5.show()
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.face_recognition("closet_3/",Tu3,Status3,0,3)

    def open_folder_4(self):
        person = firebase.get(Tu4,"Name")
        if person == "":
                result = self.question(" Do you want to register? ")
                if result==1:
                        request = self.MessBox("Which method do you want?          ")
                        if request==2:
                                self.ui_1.set(4)
                                self.ui_1.selection = 4             
                                self.ui_1.show()
                        elif request==1:
                                self.ui_4.set(4)
                                self.ui_4.selection = 4
                                self.ui_4.name = firebase.get(Tu4, "Name")                  
                                self.ui_4.show()
                                 
        else:   
                        result = self.question(" This closet is belong to "+ person + "\n" + "Do you want to continue?")
                        if result == 1:
                                request = self.MessBox("Which method do you want?          ")
                                if request == 2:
                                        images_path = glob.glob(r"closet_4\*.jpg")
                                        if len(images_path)!=0:
                                                person = firebase.get(Tu4, "Name")
                                                self.face_recognition("closet_4/",Tu4,Status4,1,4)
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.ui_7.selection =4
                                                        self.ui_7.show()
                                elif request==1:
                                        result = firebase.get(Tu4,"PassWord")
                                        if result!="":
                                                self.ui_5.selection = 4
                                                self.ui_5.show()
                                        else:
                                                mode = self.question("The method is not register. Do you want to register?")
                                                if mode == 1:
                                                        self.face_recognition("closet_4/",Tu4,Status4,0,4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APP UI"))
        self.closet_4.setText(_translate("MainWindow", "LOCKER 1"))
        self.label_5.setText(_translate("MainWindow", "LOCKER 2"))
        self.label_6.setText(_translate("MainWindow", "LOCKER 3"))
        self.label_8.setText(_translate("MainWindow", "LOCKER 4"))
        self.label.setText(_translate("MainWindow", "SMART LOCKER UI"))
        self.label_2.setText(_translate("MainWindow", "Make by:  Ngô Trung Nguyên - Nguyễn Trung Hiếu"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
