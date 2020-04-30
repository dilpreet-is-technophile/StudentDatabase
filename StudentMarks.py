# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentMarks.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_StudentMarks(object):
    # storing Student ID
    global student_ID
    file = open("studentID.txt", "r")
    student_ID = file.read()

    def setupUi(self, StudentMarks):
        StudentMarks.setObjectName("StudentMarks")
        StudentMarks.resize(1009, 780)
        StudentMarks.setMaximumSize(QtCore.QSize(1009, 780))
        StudentMarks.setStyleSheet("\n"
                                   "background:#1C5253;")
        self.centralwidget = QtWidgets.QWidget(StudentMarks)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(303, -24, 711, 811))
        self.label.setStyleSheet(
            "background:rgb(227,74,111); border: 2px solid white;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.studentPhoto = QtWidgets.QLabel(self.centralwidget)
        self.studentPhoto.setGeometry(QtCore.QRect(90, 60, 111, 111))
        self.studentPhoto.setStyleSheet("background:transparent;")
        self.studentPhoto.setText("")
        self.studentPhoto.setPixmap(QtGui.QPixmap("student.png"))
        self.studentPhoto.setObjectName("studentPhoto")
        self.StudentNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.StudentNameLabel.setGeometry(QtCore.QRect(33, 210, 241, 51))
        self.StudentNameLabel.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.StudentNameLabel.setObjectName("StudentNameLabel")
        self.StudentSemesterlabel = QtWidgets.QLabel(self.centralwidget)
        self.StudentSemesterlabel.setGeometry(QtCore.QRect(33, 426, 241, 71))
        self.StudentSemesterlabel.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.StudentSemesterlabel.setText("")
        self.StudentSemesterlabel.setObjectName("StudentSemesterlabel")
        self.StudentBranchLabel = QtWidgets.QLabel(self.centralwidget)
        self.StudentBranchLabel.setGeometry(QtCore.QRect(30, 570, 241, 91))
        self.StudentBranchLabel.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.StudentBranchLabel.setText("")
        self.StudentBranchLabel.setObjectName("StudentBranchLabel")
        self.StudentTitle = QtWidgets.QLabel(self.centralwidget)
        self.StudentTitle.setGeometry(QtCore.QRect(310, 40, 701, 91))
        self.StudentTitle.setStyleSheet(
            "background:transparent;font: 81 36pt \"Montserrat ExtraBold\";")
        self.StudentTitle.setObjectName("StudentTitle")
        self.StudentTitle_3 = QtWidgets.QLabel(self.centralwidget)
        self.StudentTitle_3.setGeometry(QtCore.QRect(450, 250, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.StudentTitle_3.setFont(font)
        self.StudentTitle_3.setStyleSheet("\n"
                                          "background:#1C5253;\n"
                                          "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                          "border: none;")
        self.StudentTitle_3.setObjectName("StudentTitle_3")
        self.StudentTitle_4 = QtWidgets.QLabel(self.centralwidget)
        self.StudentTitle_4.setGeometry(QtCore.QRect(740, 250, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.StudentTitle_4.setFont(font)
        self.StudentTitle_4.setStyleSheet("\n"
                                          "background:#1C5253;\n"
                                          "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                          "border: none;")
        self.StudentTitle_4.setObjectName("StudentTitle_4")
        self.ComputerLabel = QtWidgets.QLabel(self.centralwidget)
        self.ComputerLabel.setGeometry(QtCore.QRect(450, 360, 151, 91))
        self.ComputerLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                         "background:transparent; font-size:20px;\n"
                                         "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                         "border: none;")
        self.ComputerLabel.setObjectName("ComputerLabel")
        self.MathsLabel = QtWidgets.QLabel(self.centralwidget)
        self.MathsLabel.setGeometry(QtCore.QRect(450, 470, 151, 91))
        self.MathsLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                      "background:transparent; font-size:20px;\n"
                                      "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                      "border: none;")
        self.MathsLabel.setObjectName("MathsLabel")
        self.ScienceLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScienceLabel.setGeometry(QtCore.QRect(450, 590, 151, 91))
        self.ScienceLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                        "background:transparent; font-size:20px;\n"
                                        "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                        "border: none;")
        self.ScienceLabel.setObjectName("ScienceLabel")
        self.ComputerProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.ComputerProgress.setGeometry(QtCore.QRect(750, 380, 131, 61))
        self.ComputerProgress.setStyleSheet("")
        self.ComputerProgress.setProperty("value", 24)
        self.ComputerProgress.setObjectName("ComputerProgress")
        self.ScienceProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.ScienceProgress.setGeometry(QtCore.QRect(750, 610, 131, 61))
        self.ScienceProgress.setStyleSheet("")
        self.ScienceProgress.setProperty("value", 24)
        self.ScienceProgress.setObjectName("ScienceProgress")
        self.MathsProgress = QtWidgets.QProgressBar(self.centralwidget)
        self.MathsProgress.setGeometry(QtCore.QRect(750, 490, 131, 61))
        self.MathsProgress.setStyleSheet("")
        self.MathsProgress.setProperty("value", 24)
        self.MathsProgress.setObjectName("MathsProgress")
        self.TotalMarksLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalMarksLabel.setGeometry(QtCore.QRect(710, 700, 281, 61))
        self.TotalMarksLabel.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.TotalMarksLabel.setText("")
        self.TotalMarksLabel.setObjectName("TotalMarksLabel")
        StudentMarks.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentMarks)
        QtCore.QMetaObject.connectSlotsByName(StudentMarks)

    def retranslateUi(self, StudentMarks):
        _translate = QtCore.QCoreApplication.translate
        StudentMarks.setWindowTitle(_translate("StudentMarks", "StudentMarks"))
        self.StudentNameLabel.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\"/></p></body></html>"))
        self.StudentTitle.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Student Performance</span></p></body></html>"))
        self.StudentTitle_3.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Subject</span></p></body></html>"))
        self.StudentTitle_4.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Marks</span></p></body></html>"))
        self.ComputerLabel.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Computer</span></p></body></html>"))
        self.MathsLabel.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Maths</span></p></body></html>"))
        self.ScienceLabel.setText(_translate(
            "StudentMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Science</span></p></body></html>"))

        # Database Coding
        conn = sqlite3.connect("result.db")
        c = conn.cursor()

        # calling student details table
        query = "SELECT * FROM Student_Details WHERE Student_id=(?)"
        d = c.execute(query, (student_ID))
        rows = c.fetchall()

        # displaying name
        name = rows[0][1]
        self.StudentNameLabel.setText(name)

        # displaying semester
        semester = rows[0][5]
        self.StudentSemesterlabel.setText(str(semester)+"th Semester")

        # # displaying branch
        branch = rows[0][6]
        self.StudentBranchLabel.setText(branch)

        # displaying marks
        query1 = "SELECT * FROM Student_Marks WHERE Student_id=(?)"
        d1 = c.execute(query1, (student_ID))
        rows1 = c.fetchall()

        global computer, maths, science, total

        computer = int(rows1[0][1])
        maths = int(rows1[0][2])
        science = int(rows1[0][3])

        total = (computer + maths + science)

        self.ComputerProgress.setProperty("value", computer)
        self.ComputerProgress.setFormat("%v")
        self.ScienceProgress.setProperty("value", maths)
        self.ScienceProgress.setFormat("%v")
        self.MathsProgress.setProperty("value", science)
        self.MathsProgress.setFormat("%v")

        self.TotalMarksLabel.setText("Total Marks "+str(total))
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentMarks = QtWidgets.QMainWindow()
    ui = Ui_StudentMarks()
    ui.setupUi(StudentMarks)
    StudentMarks.show()
    sys.exit(app.exec_())
