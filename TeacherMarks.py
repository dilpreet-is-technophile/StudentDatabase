# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeacherMarks.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_TeacherMarks(object):

    # message displaying
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

    # database coding
    dbname = 'result.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Student_Marks(
      "Student_id" INTEGER,
      "Computer" INTEGER,
      "Maths" INTEGER,
      "Science"  INTEGER

        )''')
    conn.close()

    # function to add marks

    def add_marks(self, MainWindow):
        dbname = 'result.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        sid = self.StudentIdInputbox.text()
        computerMarks = self.ComputerMarksInput.text()
        mathsMarks = self.MathsMarksInput.text()
        scienceMarks = self.ScienceMarksInput.text()

        if(sid != "" and computerMarks != "" and mathsMarks != "" and scienceMarks != ""):
            query = "SELECT * FROM Student_Marks WHERE Student_id=(?)"
            data = cur.execute(query, (sid))
            if(len(cur.fetchall()) > 0):
                cur.execute('''
                    Update Student_Marks set Computer =(?), Maths=(?),Science = (?) where student_id = (?)
                    ''', (computerMarks, mathsMarks, scienceMarks, sid))
                conn.commit()
            else:
                cur.execute('''
                        INSERT INTO  Student_Marks(Student_id , Computer , Maths , Science) VALUES( ?,?,?,?)

                        ''', (sid, computerMarks, mathsMarks, scienceMarks))

                conn.commit()

            conn.close()
            self.messagebox("hurray", "Marks Added")
            self.StudentIdInputbox.setText("")
            self.ComputerMarksInput.setText("")
            self.ScienceMarksInput.setText("")
            self.MathsMarksInput.setText("")
        else:
            self.warning("lookout", "Fields Empty")

    def setupUi(self, TeacherMarks):
        TeacherMarks.setObjectName("TeacherMarks")
        TeacherMarks.resize(1009, 780)
        TeacherMarks.setMaximumSize(QtCore.QSize(1009, 780))
        TeacherMarks.setStyleSheet("background:#272121;")
        self.centralwidget = QtWidgets.QWidget(TeacherMarks)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(283, -24, 731, 811))
        self.label.setStyleSheet("background:rgb(128,206,215,0.4); \n"
                                 "border: 2px solid white;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.studentPhoto = QtWidgets.QLabel(self.centralwidget)
        self.studentPhoto.setGeometry(QtCore.QRect(90, 60, 111, 111))
        self.studentPhoto.setStyleSheet("background:transparent;")
        self.studentPhoto.setText("")
        self.studentPhoto.setPixmap(QtGui.QPixmap("teacher.png"))
        self.studentPhoto.setObjectName("studentPhoto")
        self.TeacherNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.TeacherNameLabel.setGeometry(QtCore.QRect(33, 210, 241, 51))
        self.TeacherNameLabel.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.TeacherNameLabel.setObjectName("TeacherNameLabel")
        self.StudentTitle = QtWidgets.QLabel(self.centralwidget)
        self.StudentTitle.setGeometry(QtCore.QRect(310, 40, 701, 91))
        self.StudentTitle.setStyleSheet(
            "background:transparent;font: 81 36pt \"Montserrat ExtraBold\";")
        self.StudentTitle.setObjectName("StudentTitle")
        self.ComputerLabel = QtWidgets.QLabel(self.centralwidget)
        self.ComputerLabel.setGeometry(QtCore.QRect(410, 320, 151, 91))
        self.ComputerLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                         "background:transparent; font-size:20px;\n"
                                         "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                         "border: none;")
        self.ComputerLabel.setObjectName("ComputerLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 190, 171, 51))
        self.label_2.setStyleSheet("font: 81 16pt \"Montserrat ExtraBold\";")
        self.label_2.setObjectName("label_2")
        self.StudentIdInputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.StudentIdInputbox.setGeometry(QtCore.QRect(700, 190, 61, 51))
        self.StudentIdInputbox.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.StudentIdInputbox.setObjectName("StudentIdInputbox")
        self.ScienceLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScienceLabel.setGeometry(QtCore.QRect(410, 570, 151, 91))
        self.ScienceLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                        "background:transparent; font-size:20px;\n"
                                        "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                        "border: none;")
        self.ScienceLabel.setObjectName("ScienceLabel")
        self.MathsLabel = QtWidgets.QLabel(self.centralwidget)
        self.MathsLabel.setGeometry(QtCore.QRect(410, 440, 151, 91))
        self.MathsLabel.setStyleSheet("color:rgb( 255, 143, 121);\n"
                                      "background:transparent; font-size:20px;\n"
                                      "font: 81 36pt \"Montserrat ExtraBold\";\n"
                                      "border: none;")
        self.MathsLabel.setObjectName("MathsLabel")
        self.ComputerMarksInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ComputerMarksInput.setGeometry(QtCore.QRect(640, 340, 111, 61))
        self.ComputerMarksInput.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.ComputerMarksInput.setObjectName("ComputerMarksInput")
        self.ScienceMarksInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ScienceMarksInput.setGeometry(QtCore.QRect(640, 580, 111, 61))
        self.ScienceMarksInput.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.ScienceMarksInput.setObjectName("ScienceMarksInput")
        self.MathsMarksInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MathsMarksInput.setGeometry(QtCore.QRect(640, 450, 111, 61))
        self.MathsMarksInput.setStyleSheet(
            "font: 81 24pt \"Montserrat ExtraBold\";")
        self.MathsMarksInput.setObjectName("MathsMarksInput")
        self.UpdateMarksButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateMarksButton.setGeometry(QtCore.QRect(850, 700, 141, 71))
        self.UpdateMarksButton.setStyleSheet(
            "background:rgb( 255, 143, 121);border: 2px solid white;font: 81 24pt \"Montserrat ExtraBold\";")
        self.UpdateMarksButton.setObjectName("UpdateMarksButton")

        # connecting button
        self.UpdateMarksButton.clicked.connect(self.add_marks)

        TeacherMarks.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeacherMarks)
        QtCore.QMetaObject.connectSlotsByName(TeacherMarks)

    def retranslateUi(self, TeacherMarks):
        _translate = QtCore.QCoreApplication.translate
        TeacherMarks.setWindowTitle(_translate("TeacherMarks", "TeacherMarks"))
        self.TeacherNameLabel.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\"/></p></body></html>"))
        self.StudentTitle.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Enter Student Marks</span></p></body></html>"))
        self.ComputerLabel.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Computer</span></p></body></html>"))
        self.label_2.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\">Student_ID</p></body></html>"))
        self.StudentIdInputbox.setText(_translate("TeacherMarks", "1"))
        self.ScienceLabel.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Science</span></p></body></html>"))
        self.MathsLabel.setText(_translate(
            "TeacherMarks", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Maths</span></p></body></html>"))
        self.ComputerMarksInput.setText(_translate("TeacherMarks", "Null"))
        self.ScienceMarksInput.setText(_translate("TeacherMarks", "Null"))
        self.MathsMarksInput.setText(_translate("TeacherMarks", "Null"))
        self.UpdateMarksButton.setText(_translate("TeacherMarks", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeacherMarks = QtWidgets.QMainWindow()
    ui = Ui_TeacherMarks()
    ui.setupUi(TeacherMarks)
    TeacherMarks.show()
    sys.exit(app.exec_())
