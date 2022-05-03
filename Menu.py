from PyQt5 import QtWidgets
from UI_Scripts.MenuUI import Ui_Menu
from UI_Scripts.ConjuntosUI import Ui_Conjuntos
from TruthCalculator import Ui_MainWindow
from Sucesiones import Sucesiones
from Relaciones import Relaciones
import sys

class Menu(QtWidgets.QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_truth)
        self.pushButton_2.clicked.connect(self.open_conjuntos)
        self.pushButton_3.clicked.connect(self.open_sucesiones)
        self.pushButton_4.clicked.connect(self.open_relaciones)

    def open_conjuntos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Conjuntos()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_truth(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_sucesiones(self):
        self.sucesiones = Sucesiones()
        self.hide()
        self.sucesiones.show()

    def open_relaciones(self):
        self.relaciones = Relaciones()
        self.hide()
        self.relaciones.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
