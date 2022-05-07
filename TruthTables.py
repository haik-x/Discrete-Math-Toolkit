from PyQt5 import QtCore, QtWidgets
from UI_Scripts.TruthTablesUI import table_Window
import sys


class Tables(QtWidgets.QMainWindow, table_Window):
    def __init__(self, statement):
        super().__init__()
        self.setupUi(self)
        self.statement = statement
        self.loadData()

    def loadData(self):
        self.operar()

    def operar(self):
        # Funcion con los operadores que se pueden implementar en nuestra calaculadora
        def is_operator(c):
            if c in ["&", "|", "^", ">", "=", "~"]: return True
            return False

        # Funcion que se utiliza para identificar la precedencia de los operadores. En este caso particular
        # se tienen precedencias del 1 al 3. Siendo el operador de mayor importancia la negacion
        def get_precedence(o):
            if o in [">", "="]: return 1
            if o in ["&", "|", "^"]: return 2
            if o in ["~"]: return 3
            return 0

        # Funcion que se utiliza para identificar el tipo de asociacion de los operadores. Si son por la izquierda
        # O por la derecha
        def left_assoc(o):
            if o in ["&", "|", "^", ">", "="]: return True
            if o in ["~"]: return False

        # Funcion que hace las evaluaciones en notacion postfijo utilizando un acercamiento
        # similar al algoritmo de shunting yard
        def convert_infix(infix):
            infix = infix.replace(" ", "")
            stack, queue = [], []
            postfix = ""

            for i in infix:
                if is_operator(i):
                    # Evaluamos asociaciones y precedencias para poder encontrar la ubicacione correcta de los operadores
                    while (len(stack) != 0 and ((left_assoc(i) and (get_precedence(i) <= get_precedence(stack[-1])) or (
                            not left_assoc(i) and (get_precedence(i) < get_precedence(stack[-1])))))):
                        queue.append(stack.pop());
                    stack.append(i)
                elif i == "(":
                    stack.append(i)
                elif i == ")":
                    while stack[-1] != "(":
                        queue.append(stack.pop())
                    stack.pop()
                else:
                    queue.append(i)

            while len(stack) != 0:
                queue.append(stack.pop())
            return (queue)

        # Encontrar las literales que van a ser evaluadas
        def get_operands(postfix):
            operands = []
            for i in postfix:
                if not is_operator(i): operands.append(i)

            seen = set()
            seen_add = seen.add
            operands = [x for x in operands if not (x in seen or seen_add(x))]
            return operands

        # Utilizamos el inverso del algoritmo de notacion polaca inversa para regresar a nuestra funcion en
        # su expresion normal para poder ser evaluada
        def parse_postfix(postfix, values, k, l):
            stack = []
            val = []
            expr2 = []
            for i in postfix:
                if not is_operator(i):
                    stack.append(int(values[i]))
                    val.append(i)
                else:
                    if i == "&":
                        a1 = val.pop()
                        b2 = val.pop()
                        stack.append(stack.pop() & stack.pop())
                        val.append(b2 + "^" + a1)
                        # Las siguientes funciones rellenan nuestra tabla con los datos segun se van obteniendo
                        # Notese la repeticion en todas las evaluaciones condicionales
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    elif i == "|":
                        a1 = val.pop()
                        b2 = val.pop()
                        stack.append(stack.pop() | stack.pop())
                        val.append(b2 + "|" + a1)
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    elif i == "^":
                        a1 = val.pop()
                        b2 = val.pop()
                        stack.append(stack.pop() ^ stack.pop())
                        val.append(b2 + "x" + a1)
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    elif i == "~":
                        stack.append(~stack.pop() + 2)
                        val.append("~" + val.pop())
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    elif i == ">":
                        b = stack.pop()
                        a = stack.pop()
                        a1 = val.pop()
                        b2 = val.pop()
                        stack.append((~a + 2) | b)
                        val.append(b2 + "->" + a1)
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    elif i == "=":
                        b = stack.pop()
                        a = stack.pop()
                        a1 = val.pop()
                        b2 = val.pop()
                        stack.append(int(a == b))
                        val.append(b2 + "<->" + a1)
                        self.item = QtWidgets.QTableWidgetItem(str(stack[len(stack) - 1]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(l, k, self.item)
                        k += 1
                    expr2 = expr2 + val.copy()
            if len(stack) > 1:
                sys.stdout.write("Invalid Expression\n")
                exit()

            expr2 = list(dict.fromkeys(expr2))
            # print("\n")
            return expr2

        # funcion quese utilza para obtener los caso a evaluar. Rellena con valores de verdad y retorna
        # un vector que sera analizado despues
        def get_tests(operands):
            num = len(operands)
            vectors = []
            for x in range(pow(2, num)):
                v = list(('{0:0' + str(num) + 'b}').format(x))
                vectors.append(dict(zip(operands, v)))
            return vectors

        # Funcion utilizada para imprimir la tabla y que hace una llamada anidada
        # a las funciones previas
        def print_table(exp, sep=" ", endl="\n"):
            if isinstance(exp, str): exp = [exp]

            postfix = []
            operands = []
            for e in exp:
                postfix.append(convert_infix(e))

                ops = get_operands(postfix[-1])
                for op in ops:
                    if op not in operands:
                        operands.append(op)

            # Valores de verdad para las variables usadas
            tests = get_tests(operands)
            # Imprime los headers de la tabla

            header = postfix[0].copy()
            remove_operands = str.maketrans('', '', str(operands))
            header = [s.translate(remove_operands) for s in header]
            header = [string for string in header if string != ""]

            if (len(operands) == 1):
                self.tableWidget.setRowCount(2)
            else:
                self.tableWidget.setRowCount(len(operands) ** 2)

            self.tableWidget.setColumnCount(len(header) + len(operands))
            expr2 = []
            i = 0
            j = 0
            l = 0
            k = (len(operands))
            for t in tests:
                for x in operands:
                    self.item = QtWidgets.QTableWidgetItem(t[x])
                    self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tableWidget.setItem(i, j, self.item)
                    j = j + 1
                j = 0
                i = i + 1
                for e in postfix:
                    expr2 = parse_postfix(e, t, k, l)
                l = l + 1

            operands.extend(expr2)
            self.tableWidget.setHorizontalHeaderLabels(operands)
            sys.stdout.write(endl)

        i = self.statement.split(",")
        print_table(i)


'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tables = Tables()
    tables.show()
    sys.exit(app.exec_())'''
