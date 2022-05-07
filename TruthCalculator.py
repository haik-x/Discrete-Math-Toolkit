from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from UI_Scripts.TruthCalculatorUI import Ui_MainWindow
from TruthTables import Tables
import sys


class Truth(QtWidgets.QMainWindow, Ui_MainWindow):
    closing = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnClean.clicked.connect(lambda: self.press_it("C"))
        self.btnDelete.clicked.connect(self.remove_item)
        self.btnResult.clicked.connect(self.solves_it)
        self.btnP.clicked.connect(lambda: self.press_it("p"))
        self.btnQ.clicked.connect(lambda: self.press_it("q"))
        self.btnR.clicked.connect(lambda: self.press_it("r"))
        self.btnS.clicked.connect(lambda: self.press_it("s"))
        self.btnNot.clicked.connect(lambda: self.press_it("~"))
        self.btnConjunction.clicked.connect(lambda: self.press_it("^"))
        self.btnDisjunction.clicked.connect(lambda: self.press_it("|"))
        self.btnConditional.clicked.connect(lambda: self.press_it("->"))
        self.btnBiconditional.clicked.connect(lambda: self.press_it("<->"))
        self.btnOpenBracket.clicked.connect(lambda: self.press_it("("))
        self.btnCloseBracket.clicked.connect(lambda: self.press_it(")"))

    # Concatenar cada uno de los input
    def press_it(self, pressed):
        if pressed == "C":
            self.inputLine.setText("")
        else:
            self.inputLine.setText(f'{self.inputLine.text()}{pressed}')

    # Remover character
    def remove_item(self):
        screen = self.inputLine.text()
        # Quitar el ultimo elemento
        screen = screen[:-1]
        self.inputLine.setText(screen)

# Tomar la cadena o enunciado completo
    def solves_it(self):

        statement = self.inputLine.text()
        statement = statement.replace("<->", "=")
        statement = statement.replace("->", ">")
        statement = statement.replace("^", "&")

        self.open_window(statement)

    def open_window(self, statement):
        self.table = Tables(statement)
        self.table.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "¿Seguro que deseas salir?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.closing.emit()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    truth = Truth()
    truth.show()
    sys.exit(app.exec_())
