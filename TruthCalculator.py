from PyQt5 import QtCore, QtGui, QtWidgets
from tablasVerdad import table_Window


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 534)
        MainWindow.setMaximumSize(QtCore.QSize(360, 534))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(360, 483))
        self.centralwidget.setMaximumSize(QtCore.QSize(360, 483))
        self.centralwidget.setStyleSheet("background-color: rgb(5, 5, 5);")
        self.centralwidget.setObjectName("centralwidget")
        self.inputLine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLine.setGeometry(QtCore.QRect(20, 20, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.inputLine.setFont(font)
        self.inputLine.setStyleSheet("color:white;")
        self.inputLine.setText("")
        self.inputLine.setFrame(True)
        self.inputLine.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.inputLine.setObjectName("inputLine")
        self.btnClean = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.btnClean.setGeometry(QtCore.QRect(20, 110, 115, 75))
        self.btnClean.setStyleSheet("QPushButton {\n"
                                    "    background-color: black;\n"
                                    "    color: #FFFFFF;\n"
                                    "    border-style: outset;\n"
                                    "    padding: 2px;\n"
                                    "    font: bold 20px;\n"
                                    "    border-width: 6px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color:  green;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color:#39FF14;\n"
                                    "}")
        self.btnClean.setObjectName("btnClean")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_item())
        self.btnDelete.setGeometry(QtCore.QRect(140, 110, 115, 75))
        self.btnDelete.setStyleSheet("QPushButton {\n"
                                     "    background-color: black;\n"
                                     "    color: #FFFFFF;\n"
                                     "    border-style: outset;\n"
                                     "    padding: 2px;\n"
                                     "    font: bold 20px;\n"
                                     "    border-width: 6px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color:  green;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color:#39FF14;\n"
                                     "}")
        self.btnDelete.setObjectName("btnDelete")
        self.btnResult = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.solves_it(MainWindow))
        self.btnResult.setGeometry(QtCore.QRect(260, 110, 70, 75))
        self.btnResult.setStyleSheet("QPushButton {\n"
                                     "    background-color: black;\n"
                                     "    color: #FFFFFF;\n"
                                     "    border-style: outset;\n"
                                     "    padding: 2px;\n"
                                     "    font: bold 20px;\n"
                                     "    border-width: 6px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color:  green;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color:#39FF14;\n"
                                     "}")
        self.btnResult.setObjectName("btnResult")
        self.btnP = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("p"))
        self.btnP.setGeometry(QtCore.QRect(20, 200, 70, 75))
        self.btnP.setStyleSheet("QPushButton {\n"
                                "    background-color: black;\n"
                                "    color: #FFFFFF;\n"
                                "    border-style: outset;\n"
                                "    padding: 2px;\n"
                                "    font: bold 20px;\n"
                                "    border-width: 6px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color:  green;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color:#39FF14;\n"
                                "}")
        self.btnP.setObjectName("btnP")
        self.btnQ = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("q"))
        self.btnQ.setGeometry(QtCore.QRect(100, 200, 70, 75))
        self.btnQ.setStyleSheet("QPushButton {\n"
                                "    background-color: black;\n"
                                "    color: #FFFFFF;\n"
                                "    border-style: outset;\n"
                                "    padding: 2px;\n"
                                "    font: bold 20px;\n"
                                "    border-width: 6px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color:  green;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color:#39FF14;\n"
                                "}")
        self.btnQ.setObjectName("btnQ")
        self.btnR = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("r"))
        self.btnR.setGeometry(QtCore.QRect(180, 200, 70, 75))
        self.btnR.setStyleSheet("QPushButton {\n"
                                "    background-color: black;\n"
                                "    color: #FFFFFF;\n"
                                "    border-style: outset;\n"
                                "    padding: 2px;\n"
                                "    font: bold 20px;\n"
                                "    border-width: 6px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color:  green;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color:#39FF14;\n"
                                "}")
        self.btnR.setObjectName("btnR")
        self.btnS = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("s"))
        self.btnS.setGeometry(QtCore.QRect(260, 200, 70, 75))
        self.btnS.setStyleSheet("QPushButton {\n"
                                "    background-color: black;\n"
                                "    color: #FFFFFF;\n"
                                "    border-style: outset;\n"
                                "    padding: 2px;\n"
                                "    font: bold 20px;\n"
                                "    border-width: 6px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color:  green;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color:#39FF14;\n"
                                "}")
        self.btnS.setObjectName("btnS")
        self.btnNot = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("~"))
        self.btnNot.setGeometry(QtCore.QRect(20, 290, 70, 75))
        self.btnNot.setStyleSheet("QPushButton {\n"
                                  "    background-color: black;\n"
                                  "    color: #FFFFFF;\n"
                                  "    border-style: outset;\n"
                                  "    padding: 2px;\n"
                                  "    font: bold 20px;\n"
                                  "    border-width: 6px;\n"
                                  "    border-radius: 10px;\n"
                                  "    border-color:  green;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "    background-color:#39FF14;\n"
                                  "}")
        self.btnNot.setObjectName("btnNot")
        self.btnConjunction = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("^"))
        self.btnConjunction.setGeometry(QtCore.QRect(100, 290, 70, 75))
        self.btnConjunction.setStyleSheet("QPushButton {\n"
                                          "    background-color: black;\n"
                                          "    color: #FFFFFF;\n"
                                          "    border-style: outset;\n"
                                          "    padding: 2px;\n"
                                          "    font: bold 20px;\n"
                                          "    border-width: 6px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color:  green;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color:#39FF14;\n"
                                          "}")
        self.btnConjunction.setObjectName("btnConjunction")
        self.btnDisjunction = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("|"))
        self.btnDisjunction.setGeometry(QtCore.QRect(180, 290, 70, 75))
        self.btnDisjunction.setStyleSheet("QPushButton {\n"
                                          "    background-color: black;\n"
                                          "    color: #FFFFFF;\n"
                                          "    border-style: outset;\n"
                                          "    padding: 2px;\n"
                                          "    font: bold 20px;\n"
                                          "    border-width: 6px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color:  green;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color:#39FF14;\n"
                                          "}")
        self.btnDisjunction.setObjectName("btnDisjunction")
        self.btnConditional = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("->"))
        self.btnConditional.setGeometry(QtCore.QRect(260, 290, 70, 75))
        self.btnConditional.setStyleSheet("QPushButton {\n"
                                          "    background-color: black;\n"
                                          "    color: #FFFFFF;\n"
                                          "    border-style: outset;\n"
                                          "    padding: 2px;\n"
                                          "    font: bold 20px;\n"
                                          "    border-width: 6px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color:  green;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color:#39FF14;\n"
                                          "}")
        self.btnConditional.setObjectName("btnConditional")
        self.btnBiconditional = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("<->"))
        self.btnBiconditional.setGeometry(QtCore.QRect(20, 380, 70, 75))
        self.btnBiconditional.setStyleSheet("QPushButton {\n"
                                            "    background-color: black;\n"
                                            "    color: #FFFFFF;\n"
                                            "    border-style: outset;\n"
                                            "    padding: 2px;\n"
                                            "    font: bold 20px;\n"
                                            "    border-width: 6px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color:  green;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color:#39FF14;\n"
                                            "}")
        self.btnBiconditional.setObjectName("btnBiconditional")
        self.btnOpenBracket = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("("))
        self.btnOpenBracket.setGeometry(QtCore.QRect(100, 380, 70, 75))
        self.btnOpenBracket.setStyleSheet("QPushButton {\n"
                                          "    background-color: black;\n"
                                          "    color: #FFFFFF;\n"
                                          "    border-style: outset;\n"
                                          "    padding: 2px;\n"
                                          "    font: bold 20px;\n"
                                          "    border-width: 6px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color:  green;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color:#39FF14;\n"
                                          "}")
        self.btnOpenBracket.setObjectName("btnOpenBracket")
        self.btnCloseBracket = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it(")"))
        self.btnCloseBracket.setGeometry(QtCore.QRect(180, 380, 70, 75))
        self.btnCloseBracket.setStyleSheet("QPushButton {\n"
                                           "    background-color: black;\n"
                                           "    color: #FFFFFF;\n"
                                           "    border-style: outset;\n"
                                           "    padding: 2px;\n"
                                           "    font: bold 20px;\n"
                                           "    border-width: 6px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color:  green;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color:#39FF14;\n"
                                           "}")
        self.btnCloseBracket.setObjectName("btnCloseBracket")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionArchivo = QtWidgets.QAction(MainWindow)
        self.actionArchivo.setObjectName("actionArchivo")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.action_Ayuda = QtWidgets.QAction(MainWindow)
        self.action_Ayuda.setObjectName("action_Ayuda")
        self.menuAyuda.addAction(self.action_Ayuda)
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Remover caracter
    def remove_item(self):
        screen = self.inputLine.text()
        # Quitar el ultimo elemento
        screen = screen[:-1]
        self.inputLine.setText(screen)

    # Concatenar cada uno de los input
    def press_it(self, pressed):
        if pressed == "C":
            self.inputLine.setText("")
        else:
            self.inputLine.setText(f'{self.inputLine.text()}{pressed}')

    # Tomar la cadena o enunciado completo
    def solves_it(self, MainWindow):

        statement = self.inputLine.text()
        statement = statement.replace("<->", "=")
        statement = statement.replace("->", ">")
        statement = statement.replace("^", "&")

        self.open_window(statement, MainWindow)

    def open_window(self, statement, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = table_Window()
        self.ui.set_statement(statement)
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tablas de Verdad"))
        self.btnClean.setText(_translate("MainWindow", "AC"))
        self.btnDelete.setText(_translate("MainWindow", "DEL"))
        self.btnResult.setText(_translate("MainWindow", "="))
        self.btnP.setText(_translate("MainWindow", "p"))
        self.btnQ.setText(_translate("MainWindow", "q"))
        self.btnR.setText(_translate("MainWindow", "r"))
        self.btnS.setText(_translate("MainWindow", "s"))
        self.btnNot.setText(_translate("MainWindow", "~"))
        self.btnConjunction.setText(_translate("MainWindow", "^"))
        self.btnDisjunction.setText(_translate("MainWindow", "|"))
        self.btnConditional.setText(_translate("MainWindow", "->"))
        self.btnBiconditional.setText(_translate("MainWindow", "<->"))
        self.btnOpenBracket.setText(_translate("MainWindow", "("))
        self.btnCloseBracket.setText(_translate("MainWindow", ")"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionArchivo.setText(_translate("MainWindow", "Archivo"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.action_Ayuda.setText(_translate("MainWindow", "? Ayuda"))
