from PyQt5 import QtCore, QtGui, QtWidgets
from TruthCalculator import Ui_MainWindow
from Conjuntos import Ui_Conjuntos


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 381)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color: black;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
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
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def open_truth(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def open_conjuntos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Conjuntos()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">Bienvenidx a tu calculadora lógica y de conjuntos.   </span></p>\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">Para comenzar, selecciona cualquiera de las opciones inferiores:</span></p>\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Conjuntos"))
        self.pushButton.setText(_translate("Dialog", "Tablas de Verdad"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
