from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from UI_Scripts.RelacionesUI import Ui_Relaciones
import sys

class Relaciones(QtWidgets.QMainWindow, Ui_Relaciones):
    closing = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.relation = None
        self.codomain = None
        self.domain = None
        self.setupUi(self)
        self.btnGenerate.clicked.connect(self.calculate)


    def calculate(self):
        self.outputBox.clear()
        self.input_parse()
        self.calculate_domain()
        self.calculate_codomain()
        self.outputBox.insertPlainText(f'Dominio: {self.domain}\n')
        self.outputBox.insertPlainText(f'Codominio: {self.codomain}\n')
        self.outputBox.insertPlainText("Es función\n" if self.is_function() else "No es función\n")
        if self.is_function():
            self.outputBox.insertPlainText("Es inyectiva\n" if self.is_injective() else "No es inyectiva\n")
            self.outputBox.insertPlainText("Es subyectiva\n" if self.is_surjective() else "No es subjectiva\n")
            self.outputBox.insertPlainText("Es biyectiva\n" if self.is_surjective() and self.is_injective() else "No es biyectiva\n")
        self.outputBox.insertPlainText("Es reflexiva\n" if self.is_reflexive() else "No es reflexiva\n")
        self.outputBox.insertPlainText("Es simétrica\n" if self.is_symmetric() else "No es simétrica\n")
        self.outputBox.insertPlainText("Es transitiva\n" if self.is_transitive() else "No es transitiva\n")

    def input_parse(self):
        self.relation = list(eval(self.inputLine.text()))
        print(self.relation)

    def calculate_domain(self):
        self.domain = set(a for a, _ in self.relation)

    def calculate_codomain(self):
        self.codomain = set(a for _, a in self.relation)

    def is_function(self):
        for a, b in self.relation:
            for c, d, in self.relation:
                if a == c and b != d:
                    return False
        return True

    def is_injective(self):
        for a,b in self.relation:
            for c,d in self.relation:
                if a!=c and b == d:
                    return False
        return True

    def is_reflexive(self):
        result = set(ab for ab in self.relation if ab[0] == ab[1])
        return True if len(self.domain) == len(result) else False

    def is_symmetric(self):
        for a, b in self.relation:
            if (b, a) not in self.relation:
                return False
        return True

    def is_transitive(self):
        for a, b in self.relation:
            for c, d in self.relation:
                if b == c and ((a, d) not in self.relation):
                    return False
        return True

    def is_surjective(self):
        count = 0
        for _, b in self.relation:
            print(b)
            if b not in list(self.codomain):
                return False
        return True

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
    relaciones = Relaciones()
    relaciones.show()
    sys.exit(app.exec_())