from PyQt5 import QtWidgets
from UI_Scripts.ConjuntosUI import Ui_Conjuntos
import Plot
import sys


class Conjuntos(QtWidgets.QMainWindow, Ui_Conjuntos):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.clicked.connect(self.check)
        self.radioButton_2.clicked.connect(self.check)
        self.btnUnion.clicked.connect(self.clicked_union)
        self.btnIntersection.clicked.connect(self.clicked_intersection)
        self.btnSymmetry.clicked.connect(self.clicked_symmetric)
        self.btnDifference.clicked.connect(self.clicked_difference)

    # Funcion que llama al modulo de plot y llama a las funciones setter que tomara para graficar los conjuntos
    def open_plot(self, conjunto1, conjunto2, conjunto3, operacion, opcion):
        self.object = Plot.Window()
        self.object.set_conjunto1(conjunto1)
        self.object.set_conjunto2(conjunto2)
        self.object.set_conjunto3(conjunto3)
        self.object.set_operacion(operacion)
        self.object.set_numero(opcion)
        self.object.show()

    # Funcion que retorna el conjunto dependiendo de la seleccion que se da en el combo box
    def cmb_option(self, option):
        print(option)
        if option == "A":
            return self.setA
        elif option == "B":
            return self.setB
        elif option == "C":
            return self.setC
        else:
            return set()

    # Funcion que revisa si se van a evaluar 2 o tres conjuntos. Si se evaluan 2 va a bloquear una combo box
    # para que no se pueda usar
    def check(self):

        if self.radioButton.isChecked():
            self.cmb1.setEnabled(False)
            self.cmb1.setCurrentText("-")
        else:
            self.cmb1.setEnabled(True)

    def input_parsing(self, _set):
        _set = _set.lower().replace(" ", "").replace(",", " ")
        _set = set(list(_set.split(" ")))
        return _set

    # Funcion que toma el texto de las cajas y llama a otra funcion para parsearlo
    def input_getter(self):
        self.setA = self.input_parsing(self.txtSetA.text())
        self.setB = self.input_parsing(self.txtSetB.text())
        self.setC = self.input_parsing(self.txtSetC.text())

    # Funcion para evaluar uniones (El codigo se repite en las operaciones pero se cambian los signos que se evaluan)
    def clicked_union(self):
        self.lbOperador2.setText("∪")
        self.lbOperador2_2.setText("∪")
        self.input_getter()
        if self.radioButton.isChecked():  # Si esta seleccionada la opcion de 2 conjuntos solo para la union de los 2 conjuntos
            self.conjunto1 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 | self.conjunto2)
            self.opcion = 1  # Este valor se manda al modulo plot para que solo cree un diagrama de venn con 2 conjuntos
            self.open_plot(self.conjunto1, self.conjunto2, set(), self.operacion, self.opcion)
        else:
            self.conjunto1 = self.cmb_option(self.cmb1.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto3 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 | (self.conjunto2 | self.conjunto3))
            self.opcion = 2  # Este valor se manda al modulo plot para que solo cree un diagrama de venn con 3 conjuntos
            self.open_plot(self.conjunto1, self.conjunto2, self.conjunto3, self.operacion, self.opcion)

    def clicked_intersection(self):
        self.lbOperador2.setText("∩")
        self.lbOperador2_2.setText("∩")
        self.input_getter()
        if self.radioButton.isChecked():
            self.conjunto1 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 & self.conjunto2)
            self.opcion = 1
            self.open_plot(self.conjunto1, self.conjunto2, set(), self.operacion, self.opcion)
        else:
            self.conjunto1 = self.cmb_option(self.cmb1.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto3 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 & (self.conjunto2 & self.conjunto3))
            self.opcion = 2
            self.open_plot(self.conjunto1, self.conjunto2, self.conjunto3, self.operacion, self.opcion)

    def clicked_difference(self):
        self.lbOperador2.setText("-")
        self.lbOperador2_2.setText("-")
        self.input_getter()
        if self.radioButton.isChecked():
            self.conjunto1 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 - self.conjunto2)
            self.opcion = 1
            self.open_plot(self.conjunto1, self.conjunto2, set(), self.operacion, self.opcion)
        else:
            self.conjunto1 = self.cmb_option(self.cmb1.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto3 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 - (self.conjunto2 - self.conjunto3))
            self.opcion = 2
            self.open_plot(self.conjunto1, self.conjunto2, self.conjunto3, self.operacion, self.opcion)

    def clicked_symmetric(self):
        self.lbOperador2.setText("△")
        self.lbOperador2_2.setText("△")
        self.input_getter()
        if self.radioButton.isChecked():
            self.conjunto1 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 ^ self.conjunto2)
            self.opcion = 1
            self.open_plot(self.conjunto1, self.conjunto2, set(), self.operacion, self.opcion)
        else:
            self.conjunto1 = self.cmb_option(self.cmb1.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto3 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 ^ (self.conjunto2 ^ self.conjunto3))
            self.opcion = 2
            self.open_plot(self.conjunto1, self.conjunto2, self.conjunto3, self.operacion, self.opcion)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    conjuntos = Conjuntos()
    conjuntos.show()
    sys.exit(app.exec_())
