from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UI_Scripts.SucesionesUI import Ui_MainWindow
import sys
import re


# This function replaces any letter other than k for a k
def replace_letters(expression):
    return re.sub(r'[a-zA-Z]', r'k', expression)


def parse(expression, n):
    return expression.replace('k', n)

#Función recursiva de serie para la multiplicacion.
def recursion_multiplication(expression, x, n):
    if x < n:
        return 1
    else:
        return float(eval(parse(expression, str(x)))) * recursion_multiplication(expression, x - 1, n)


class Sucesiones(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.solve_series)
        self.msg = QMessageBox()

    #Función recursiva de serie para la suma. Se llama dentro de la clase para poder acceder al elemento de caja de texto
    def recursion_addition(self, expression, x, n):
        if x < n:
            return 0
        else:
            self.textEdit.insertPlainText(f'{parse(expression, str(x))}: {float(eval(parse(expression, str(x))))}\n')
            return float(eval(parse(expression, str(x)))) + self.recursion_addition(expression, x - 1, n)

    def solve_series(self):
        expression = self.lineEdit.text()
        start = int(self.lineEdit_3.text())
        end = int(self.lineEdit_2.text())
        expression = replace_letters(expression)
        try:
            self.sum = self.recursion_addition(expression, end, start)
            self.mult = recursion_multiplication(expression, end, start)
        except ZeroDivisionError:
            self.msg.setText("Hay una indefincion, intenta cambiar tu rango de evaluacion")
            self.msg.exec_()
            self.close()

        self.textEdit.insertPlainText(f'\nSuma: {str(self.sum)}\n')
        self.textEdit.insertPlainText(f'Multiplicacion: {str(self.mult)}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sucesiones = Sucesiones()
    sucesiones.show()
    sys.exit(app.exec_())
