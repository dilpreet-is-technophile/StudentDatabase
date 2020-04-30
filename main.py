# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from StudentLogin import Ui_StudentLogin
from TeacherLogin import Ui_TeacherLogin


class Ui_welcomePage(object):
    # open student login window when pressed login

    def OpenStudentWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StudentLogin()  # class name of new window you wanna open
        self.ui.setupUi(self.window)
        self.window.show()
        welcomePage.hide()

    # open teacher login window when pressed login

    def OpenTeacherWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TeacherLogin()  # class name of new window you wanna open
        self.ui.setupUi(self.window)
        self.window.show()
        welcomePage.hide()

    def setupUi(self, welcomePage):
        welcomePage.setObjectName("welcomePage")
        welcomePage.setWindowModality(QtCore.Qt.NonModal)
        welcomePage.resize(1009, 780)
        welcomePage.setMaximumSize(QtCore.QSize(1009, 780))
        welcomePage.setAutoFillBackground(False)
        welcomePage.setStyleSheet("background:url(:/prefix1/bg.jpg);\n"
                                  "font: 81 20pt \"Open Sans Extrabold\";")
        self.centralwidget = QtWidgets.QWidget(welcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(-10, 10, 1020, 141))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMaximumSize(QtCore.QSize(1020, 141))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("color:#CBC0D3; background:transparent;")
        self.Title.setObjectName("Title")
        self.welcomeInfo = QtWidgets.QLabel(self.centralwidget)
        self.welcomeInfo.setGeometry(QtCore.QRect(0, 160, 1011, 191))
        self.welcomeInfo.setStyleSheet("background: rgb(53,58,71,0.6);")
        self.welcomeInfo.setWordWrap(False)
        self.welcomeInfo.setObjectName("welcomeInfo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 430, 490, 351))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background:rgb(128,206,215,0.4); \n"
                                 "border: 2px solid white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.teacherProfile = QtWidgets.QLabel(self.frame)
        self.teacherProfile.setGeometry(QtCore.QRect(190, 10, 111, 111))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.teacherProfile.sizePolicy().hasHeightForWidth())
        self.teacherProfile.setSizePolicy(sizePolicy)
        self.teacherProfile.setStyleSheet("background:url(:/prefix1/teacher.png) no-repeat;\n"
                                          "border:none;")
        self.teacherProfile.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.teacherProfile.setText("")
        self.teacherProfile.setTextFormat(QtCore.Qt.PlainText)
        self.teacherProfile.setScaledContents(False)
        self.teacherProfile.setWordWrap(False)
        self.teacherProfile.setObjectName("teacherProfile")
        self.TeacherLabel = QtWidgets.QLabel(self.frame)
        self.TeacherLabel.setGeometry(QtCore.QRect(0, 120, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.TeacherLabel.setFont(font)
        self.TeacherLabel.setStyleSheet("color:rgb(255, 143, 121);\n"
                                        "background:transparent; font-size:20px;\n"
                                        "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                        "border: none;")
        self.TeacherLabel.setObjectName("TeacherLabel")
        self.TeacherButton = QtWidgets.QPushButton(self.frame)
        self.TeacherButton.setGeometry(QtCore.QRect(90, 240, 301, 71))
        self.TeacherButton.setStyleSheet("border: 2px solid white;")
        self.TeacherButton.setObjectName("TeacherButton")

        # linking button to our function
        self.TeacherButton.clicked.connect(self.OpenTeacherWindow)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(520, 430, 490, 351))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(
            "background:rgb(227,74,111,0.4);  opacity:0.2; border: 2px solid white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.studentLable = QtWidgets.QLabel(self.frame_2)
        self.studentLable.setGeometry(QtCore.QRect(0, 120, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.studentLable.setFont(font)
        self.studentLable.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                        "background:transparent; font-size:20px;\n"
                                        "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                        "border: none;")
        self.studentLable.setObjectName("studentLable")
        self.studentProfile = QtWidgets.QLabel(self.frame_2)
        self.studentProfile.setGeometry(QtCore.QRect(200, 10, 111, 111))
        self.studentProfile.setStyleSheet(
            "background:url(:/prefix1/student.png), no-repeat;border: none;")
        self.studentProfile.setText("")
        self.studentProfile.setObjectName("studentProfile")
        self.studentButton = QtWidgets.QPushButton(self.frame_2)
        self.studentButton.setGeometry(QtCore.QRect(100, 240, 301, 71))
        self.studentButton.setStyleSheet("border: 2px solid white;")
        self.studentButton.setObjectName("studentButton")

        # linking button to our function
        self.studentButton.clicked.connect(self.OpenStudentWindow)

        welcomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcomePage)
        QtCore.QMetaObject.connectSlotsByName(welcomePage)

    def retranslateUi(self, welcomePage):
        _translate = QtCore.QCoreApplication.translate
        welcomePage.setWindowTitle(_translate("welcomePage", "MainWindow"))
        self.Title.setText(_translate(
            "welcomePage", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">MMDU Student Database</span></p></body></html>"))
        self.welcomeInfo.setText(_translate("welcomePage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffaa7f;\">Welcome to </span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffaa7f;\">the student database management system of</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffaa7f;\">Maharishi Markandeshwar Deemed to be University, Mullana.</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#df1c74;\">Students can login to view their result of previous examinations.</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#5ee5ff;\">Teachers can login to update student database with recent data.</span></p></body></html>"))
        self.TeacherLabel.setText(_translate(
            "welcomePage", "<html><head/><body><p align=\"center\">Teacher</p></body></html>"))
        self.TeacherButton.setText(_translate("welcomePage", "Login"))
        self.studentLable.setText(_translate(
            "welcomePage", "<html><head/><body><p align=\"center\">Student</p></body></html>"))
        self.studentButton.setText(_translate("welcomePage", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcomePage = QtWidgets.QMainWindow()
    ui = Ui_welcomePage()
    ui.setupUi(welcomePage)
    welcomePage.show()
    sys.exit(app.exec_())
