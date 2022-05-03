from PyQt5 import QtWidgets
from RelacionesUI import Ui_Relaciones
import sys

class Relaciones(QtWidgets.QMainWindow, Ui_Relaciones):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    relaciones = Relaciones()
    relaciones.show()
    sys.exit(app.exec_())