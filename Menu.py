from PyQt5 import QtCore, QtGui, QtWidgets
from TruthCalculator import Ui_MainWindow
from Conjuntos import Ui_Conjuntos
from Sucesiones import Sucesiones


class Ui_Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 425)
        MainWindow.setMinimumSize(QtCore.QSize(572, 425))
        MainWindow.setMaximumSize(QtCore.QSize(572, 425))
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 544, 363))
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: black;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setEnabled(False)
        self.textEdit.setStyleSheet("background-color:black;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    background-color: #404040;\n"
                                        "    color: #FFFFFF;\n"
                                        "    border-style: outset;\n"
                                        "    padding: 2px;\n"
                                        "    font: bold 20px;\n"
                                        "    border-width: 6px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: #404040;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color:#39FF14;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_conjuntos)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: #404040;\n"
                                      "    color: #FFFFFF;\n"
                                      "    border-style: outset;\n"
                                      "    padding: 2px;\n"
                                      "    font: bold 20px;\n"
                                      "    border-width: 6px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: #404040;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color:#39FF14;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_truth)
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    background-color: #404040;\n"
                                        "    color: #FFFFFF;\n"
                                        "    border-style: outset;\n"
                                        "    padding: 2px;\n"
                                        "    font: bold 20px;\n"
                                        "    border-width: 6px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: #404040;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color:#39FF14;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_sucesiones)
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_truth(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_conjuntos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Conjuntos()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_sucesiones(self):
        self.sucesiones = Sucesiones()
        MainWindow.hide()
        self.sucesiones.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; color:#00f900;\">Bienvenidx a tu calculadora lógica y de conjuntos.   </span></p>\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; color:#00f900;\">Para comenzar, selecciona cualquiera de las opciones inferiores:</span></p>\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Conjuntos"))
        self.pushButton.setText(_translate("MainWindow", "Tablas de Verdad"))
        self.pushButton_3.setText(_translate("MainWindow", "Sucesiones"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
