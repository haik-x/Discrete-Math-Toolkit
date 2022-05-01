from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

class Window(QDialog):

    # constructor
    def __init__(self, parent=None):

        super(Window, self).__init__(parent)

        # Crea una instancia de figura para plasmarla en el el vans
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        #Crea el widget de navegacion para poder guardar la imagen que se crea con los conjuntos
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Agrega un boton que al presionar nos grafica el diagrama
        self.button = QPushButton('Presiona para graficar el diagrama')



        self.button.clicked.connect(self.plot)


        #Anade los elementos al widget
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

        self.setLayout(layout)


    def plot(self): #Aqui evalua si se hara un diagrama de 2 o 3 conjuntos
        if self.get_numero() == 1:
            self.conjunto1 = self.get_conjunto1()
            self.conjunto2 = self.get_conjunto2()
            venn2([self.conjunto1, self.conjunto2])
        else:
            self.conjunto1 = self.get_conjunto1()
            self.conjunto2 = self.get_conjunto2()
            self.conjunto3 = self.get_conjunto3()
            venn3([self.conjunto1, self.conjunto2, self.conjunto3])

        plt.title('{'+",".join(self.operacion)+'}')
        plt.plot()
        self.canvas.draw()

    #Funciones de getter y setter
    def get_conjunto1(self):
        return self.conjunto1

    def set_conjunto1(self, x):
        self.conjunto1 = x

    def get_conjunto2(self):
        return self.conjunto2

        # setter method
    def set_conjunto2(self, x):
        self.conjunto2 = x

    def get_conjunto3(self):
        return self.conjunto3

        # setter method
    def set_conjunto3(self, x):
        self.conjunto3 = x

    def get_operacion(self):
        return self.operacion

    def set_operacion(self, x):
        self.operacion = x

    def get_numero(self):
        return self.numero

    def set_numero(self, x):
        self.numero = x
        print(self.numero)

# driver code
'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())'''
