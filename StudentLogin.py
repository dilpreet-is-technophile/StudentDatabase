# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from StudentMarks import Ui_StudentMarks


class Ui_StudentLogin(object):

    def OpenStudentMarks(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StudentMarks()  # class name of new window you wanna open
        self.ui.setupUi(self.window)
        self.window.show()
        StudentLogin.hide()

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
        Student_id = self.StudentIDInput.text()
        Student_pass = self.StudentPasswordInput.text()
        f = open("studentID.txt", "w")
        f.write(Student_id)
        f.close()
        conn = sqlite3.connect('result.db')
        c = conn.cursor()
        query = "SELECT * FROM Student_login WHERE Student_id=(?) and Student_pass=(?)"
        data = c.execute(query, (Student_id, Student_pass))
        if(len(c.fetchall()) > 0):
            self.messagebox("congrats", "you are loged in")
            self.OpenStudentMarks()
        else:
            self.warning("Alert", "enter correct details")

    def setupUi(self, StudentLogin):
        StudentLogin.setObjectName("StudentLogin")
        StudentLogin.resize(1009, 780)
        StudentLogin.setMaximumSize(QtCore.QSize(1009, 780))
        StudentLogin.setStyleSheet("background:rgba(227,74,111,0.4); ")
        self.centralwidget = QtWidgets.QWidget(StudentLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 611, 811))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("StudentLogin.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.StudentLoginTitle = QtWidgets.QLabel(self.centralwidget)
        self.StudentLoginTitle.setGeometry(QtCore.QRect(610, -10, 401, 121))
        self.StudentLoginTitle.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                             "background:#5398BE; \n"
                                             "font-size:20px;\n"
                                             "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                             "border: none;")
        self.StudentLoginTitle.setObjectName("StudentLoginTitle")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 230, 321, 461))
        self.groupBox.setStyleSheet(
            "background:rgb( 255, 143, 121,0.4); border: 2px solid white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.StudentID = QtWidgets.QLabel(self.groupBox)
        self.StudentID.setGeometry(QtCore.QRect(30, 70, 261, 51))
        self.StudentID.setStyleSheet("border:none; background:#5398BE; ")
        self.StudentID.setObjectName("StudentID")
        self.StudentIDInput = QtWidgets.QLineEdit(self.groupBox)
        self.StudentIDInput.setGeometry(QtCore.QRect(30, 140, 261, 41))
        self.StudentIDInput.setStyleSheet("background:Transparent; font:16px;")
        self.StudentIDInput.setObjectName("StudentIDInput")
        self.StudentLoginButton = QtWidgets.QPushButton(self.groupBox)
        self.StudentLoginButton.setGeometry(QtCore.QRect(60, 350, 191, 51))
        self.StudentLoginButton.setStyleSheet(
            " background:#5398BE; font:25px bold;")
        self.StudentLoginButton.setObjectName("StudentLoginButton")

    # connecting our button
        self.StudentLoginButton.clicked.connect(self.login)

        self.StudentPassword = QtWidgets.QLabel(self.groupBox)
        self.StudentPassword.setGeometry(QtCore.QRect(30, 200, 261, 51))
        self.StudentPassword.setStyleSheet("border:none; background:#5398BE; ")
        self.StudentPassword.setObjectName("StudentPassword")
        self.StudentPasswordInput = QtWidgets.QLineEdit(self.groupBox)
        self.StudentPasswordInput.setGeometry(QtCore.QRect(30, 270, 261, 41))
        self.StudentPasswordInput.setStyleSheet(
            "background:Transparent; font:16px;")
        self.StudentPasswordInput.setObjectName("StudentPasswordInput")
        StudentLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentLogin)
        QtCore.QMetaObject.connectSlotsByName(StudentLogin)

    def retranslateUi(self, StudentLogin):
        _translate = QtCore.QCoreApplication.translate
        StudentLogin.setWindowTitle(_translate(
            "StudentLogin", "Student Login Page"))
        self.StudentLoginTitle.setText(_translate(
            "StudentLogin", "<html><head/><body><p align=\"center\">Student Login</p></body></html>"))
        self.StudentID.setText(_translate(
            "StudentLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Student ID</span></p></body></html>"))
        self.StudentIDInput.setText(_translate("StudentLogin", "1"))
        self.StudentLoginButton.setText(_translate("StudentLogin", "LOGIN"))
        self.StudentPassword.setText(_translate(
            "StudentLogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Password</span></p></body></html>"))
        self.StudentPasswordInput.setText(
            _translate("StudentLogin", "Dilpreet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentLogin = QtWidgets.QMainWindow()
    ui = Ui_StudentLogin()
    ui.setupUi(StudentLogin)
    StudentLogin.show()
    sys.exit(app.exec_())
