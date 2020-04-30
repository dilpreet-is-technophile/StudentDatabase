# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeacherLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from TeacherMarks import Ui_TeacherMarks


class Ui_TeacherLogin(object):
    def OpenTeacherMarks(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TeacherMarks()  # class name of new window you wanna open
        self.ui.setupUi(self.window)
        self.window.show()
        TeacherLogin.hide()
    # message box

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

        # login function

    def login(self):
        Teacher_id = self.TeacherIDInput.text()
        Teacher_pass = self.TeacherPasswordInput.text()
        conn = sqlite3.connect('result.db')
        c = conn.cursor()
        query = "SELECT * FROM Teacher_login WHERE Teacher_id=(?) and Teacher_pass=(?)"
        data = c.execute(query, (Teacher_id, Teacher_pass))
        if(len(c.fetchall()) > 0):
            self.messagebox("congrats", "you are loged in")
            self.OpenTeacherMarks()
        else:
            self.warning("Alert", "enter correct details")

    def setupUi(self, TeacherLogin):
        TeacherLogin.setObjectName("TeacherLogin")
        TeacherLogin.resize(1009, 780)
        TeacherLogin.setMaximumSize(QtCore.QSize(1009, 780))
        TeacherLogin.setStyleSheet("background:rgba(227,74,111,0.4); ")
        self.centralwidget = QtWidgets.QWidget(TeacherLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 611, 811))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("TeacherLogin.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.TeacherLoginTitle = QtWidgets.QLabel(self.centralwidget)
        self.TeacherLoginTitle.setGeometry(QtCore.QRect(610, -10, 401, 121))
        self.TeacherLoginTitle.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                             "background:#48BF84;\n"
                                             "font-size:20px;\n"
                                             "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                             "border: none;")
        self.TeacherLoginTitle.setObjectName("TeacherLoginTitle")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 230, 321, 461))
        self.groupBox.setStyleSheet(
            "background:rgb( 255, 143, 121,0.4); border: 2px solid white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.TeacherID = QtWidgets.QLabel(self.groupBox)
        self.TeacherID.setGeometry(QtCore.QRect(30, 70, 261, 51))
        self.TeacherID.setStyleSheet("border:none; background:#48BF84; ")
        self.TeacherID.setObjectName("TeacherID")
        self.TeacherIDInput = QtWidgets.QLineEdit(self.groupBox)
        self.TeacherIDInput.setGeometry(QtCore.QRect(30, 140, 261, 41))
        self.TeacherIDInput.setStyleSheet("background:Transparent; font:16px;")
        self.TeacherIDInput.setObjectName("TeacherIDInput")
        self.TeacherLoginButton = QtWidgets.QPushButton(self.groupBox)
        self.TeacherLoginButton.setGeometry(QtCore.QRect(60, 350, 191, 51))
        self.TeacherLoginButton.setStyleSheet(
            " background:#48BF84; font:25px bold;")
        self.TeacherLoginButton.setObjectName("TeacherLoginButton")

        # connecting login button
        self.TeacherLoginButton.clicked.connect(self.login)

        self.TeacherPassword = QtWidgets.QLabel(self.groupBox)
        self.TeacherPassword.setGeometry(QtCore.QRect(30, 200, 261, 51))
        self.TeacherPassword.setStyleSheet("border:none; background:#48BF84; ")
        self.TeacherPassword.setObjectName("TeacherPassword")
        self.TeacherPasswordInput = QtWidgets.QLineEdit(self.groupBox)
        self.TeacherPasswordInput.setGeometry(QtCore.QRect(30, 270, 261, 41))
        self.TeacherPasswordInput.setStyleSheet(
            "background:Transparent; font:16px;")
        self.TeacherPasswordInput.setObjectName("TeacherPasswordInput")
        TeacherLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeacherLogin)
        QtCore.QMetaObject.connectSlotsByName(TeacherLogin)

    def retranslateUi(self, TeacherLogin):
        _translate = QtCore.QCoreApplication.translate
        TeacherLogin.setWindowTitle(_translate(
            "TeacherLogin", "Teacher Login Page"))
        self.TeacherLoginTitle.setText(_translate(
            "TeacherLogin", "<html><head/><body><p align=\"center\">Teacher Login</p></body></html>"))
        self.TeacherID.setText(_translate(
            "TeacherLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Teacher ID</span></p></body></html>"))
        self.TeacherIDInput.setText(_translate("TeacherLogin", "1"))
        self.TeacherLoginButton.setText(_translate("TeacherLogin", "LOGIN"))
        self.TeacherPassword.setText(_translate(
            "TeacherLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Password</span></p></body></html>"))
        self.TeacherPasswordInput.setText(_translate("TeacherLogin", "Adam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeacherLogin = QtWidgets.QMainWindow()
    ui = Ui_TeacherLogin()
    ui.setupUi(TeacherLogin)
    TeacherLogin.show()
    sys.exit(app.exec_())
