# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sucesiones.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 325)
        MainWindow.setMinimumSize(QtCore.QSize(490, 207))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))
        MainWindow.setStyleSheet("background-color: black;\n"
                                 "color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 191, 21))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #404040;\n"
"    color: #00f900;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 13px;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: #404040;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#39FF14;\n"
"}")
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 120, 51, 20))
        self.lineEdit_2.setStyleSheet("    background-color: black;\n"
"    color: #FFFFFF;\n"
"    border-style: groove;\n"
"    padding: 2px;\n"
"    font: bold 10px;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 120, 51, 20))
        self.lineEdit_3.setStyleSheet("    background-color: black;\n"
"    color: #FFFFFF;\n"
"    border-style: groove;\n"
"    padding: 2px;\n"
"    font: bold 10px;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.lineEdit.setStyleSheet("    background-color: black;\n"
"    color: #FFFFFF;\n"
"    border-style: groove;\n"
"    padding: 2px;\n"
"    font: bold 10px;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(136, 60, 71, 20))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: #404040;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 13px;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: #404040;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#39FF14;\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 120, 91, 21))
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: #404040;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 11px;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: #404040;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#39FF14;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 101, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-color: #404040;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 11px;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: #404040;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#39FF14;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(470, 40, 251, 221))
        self.textEdit.setStyleSheet("    color: #FFFFFF;")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Generar"))
        self.label.setText(_translate("MainWindow", "Fórmula:"))
        self.label_3.setText(_translate("MainWindow", "Límite inferior:"))
        self.label_2.setText(_translate("MainWindow", "Límite superior:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
