from PyQt5 import QtCore, QtGui, QtWidgets
import Plot


class Ui_Conjuntos(object):
    def setupUi(self, Conjuntos):
        Conjuntos.setObjectName("Conjuntos")
        Conjuntos.resize(876, 554)
        Conjuntos.setMinimumSize(QtCore.QSize(0, 554))
        Conjuntos.setMaximumSize(QtCore.QSize(876, 554))
        Conjuntos.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(Conjuntos)
        self.centralwidget.setMinimumSize(QtCore.QSize(876, 512))
        self.centralwidget.setMaximumSize(QtCore.QSize(876, 512))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 831, 482))
        self.verticalLayoutWidget_4.setMaximumSize(QtCore.QSize(831, 482))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 90))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    background-color: #404040;\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-style: outset;\n"
                                   "    padding: 2px;\n"
                                   "    font: bold 20px;\n"
                                   "    border-width: 6px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: green;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setMinimumSize(QtCore.QSize(0, 90))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet(" QLabel{\n"
                                 "    background-color: #404040;\n"
                                 "    color: #FFFFFF;\n"
                                 "    border-style: outset;\n"
                                 "    padding: 2px;\n"
                                 "    font: bold 20px;\n"
                                 "    border-width: 6px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: green;\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setMinimumSize(QtCore.QSize(0, 90))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_3.setStyleSheet(" QLabel{\n"
                                   "    background-color: #404040;\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-style: outset;\n"
                                   "    padding: 2px;\n"
                                   "    font: bold 20px;\n"
                                   "    border-width: 6px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: green;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtSetA = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.txtSetA.setMinimumSize(QtCore.QSize(680, 90))
        self.txtSetA.setMaximumSize(QtCore.QSize(680, 100))
        self.txtSetA.setStyleSheet("\n"
                                   "    background-color: #404040;\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-style: double;\n"
                                   "    padding: 2px;\n"
                                   "    font: bold 20px;\n"
                                   "    border-width: 6px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: green;")
        self.txtSetA.setObjectName("txtSetA")
        self.verticalLayout_2.addWidget(self.txtSetA)
        self.txtSetB = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.txtSetB.setMinimumSize(QtCore.QSize(680, 90))
        self.txtSetB.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txtSetB.setStyleSheet("\n"
                                   "    background-color: #404040;\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-style: double;\n"
                                   "    padding: 2px;\n"
                                   "    font: bold 20px;\n"
                                   "    border-width: 6px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: green;")
        self.txtSetB.setObjectName("txtSetB")
        self.verticalLayout_2.addWidget(self.txtSetB)
        self.txtSetC = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.txtSetC.setMinimumSize(QtCore.QSize(680, 90))
        self.txtSetC.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txtSetC.setStyleSheet("\n"
                                   "    background-color: #404040;\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-style: double;\n"
                                   "    padding: 2px;\n"
                                   "    font: bold 20px;\n"
                                   "    border-width: 6px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: green;")
        self.txtSetC.setObjectName("txtSetC")
        self.verticalLayout_2.addWidget(self.txtSetC)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(829, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_35.setMinimumSize(QtCore.QSize(10, 0))
        self.label_35.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_5.addWidget(self.label_35)
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_34.setMinimumSize(QtCore.QSize(290, 29))
        self.label_34.setMaximumSize(QtCore.QSize(60, 29))
        self.label_34.setStyleSheet("color:white;")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_5.addWidget(self.label_34)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton.setStyleSheet("color: white;")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_2.setStyleSheet("color:white;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.label_40 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_40.setMinimumSize(QtCore.QSize(60, 29))
        self.label_40.setMaximumSize(QtCore.QSize(60, 29))
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_5.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_41.setMinimumSize(QtCore.QSize(60, 29))
        self.label_41.setMaximumSize(QtCore.QSize(60, 29))
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_5.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_42.setMinimumSize(QtCore.QSize(60, 29))
        self.label_42.setMaximumSize(QtCore.QSize(60, 29))
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_5.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_43.setMinimumSize(QtCore.QSize(60, 29))
        self.label_43.setMaximumSize(QtCore.QSize(60, 29))
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_5.addWidget(self.label_43)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setMinimumSize(QtCore.QSize(60, 29))
        self.label_4.setMaximumSize(QtCore.QSize(60, 29))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setMinimumSize(QtCore.QSize(60, 29))
        self.label_6.setMaximumSize(QtCore.QSize(60, 29))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setMinimumSize(QtCore.QSize(60, 29))
        self.label_8.setMaximumSize(QtCore.QSize(60, 29))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_9.setMinimumSize(QtCore.QSize(110, 29))
        self.label_9.setMaximumSize(QtCore.QSize(110, 29))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.cmb1 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.cmb1.setEnabled(False)
        self.cmb1.setMinimumSize(QtCore.QSize(71, 29))
        self.cmb1.setMaximumSize(QtCore.QSize(71, 29))
        self.cmb1.setStyleSheet("QComboBox{\n"
                                "  background-color: #404040;\n"
                                "  border: thin solid blue;\n"
                                "  border-radius: 4px;\n"
                                "  font: inherit;\n"
                                "  color: #FFFFFF;\n"
                                "  line-height: 1.5em;\n"
                                "  padding: 0.5em 0.2em 0.2em 0.2em;\n"
                                "}\n"
                                "\n"
                                " QComboBox::down-arrow {\n"
                                "     image: url(/Users/benjamin/PycharmProjects/FCC_Toolkit/Designs/arrow.png);\n"
                                " }")
        self.cmb1.setDuplicatesEnabled(False)
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.horizontalLayout.addWidget(self.cmb1)
        self.lbOperador2_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lbOperador2_2.setMaximumSize(QtCore.QSize(48, 29))
        self.lbOperador2_2.setStyleSheet("color: #FFFFFF;")
        self.lbOperador2_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbOperador2_2.setObjectName("lbOperador2_2")
        self.horizontalLayout.addWidget(self.lbOperador2_2)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_18.setMaximumSize(QtCore.QSize(48, 29))
        self.label_18.setStyleSheet("color: #FFFFFF;")
        self.label_18.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.cmb1_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.cmb1_3.setMinimumSize(QtCore.QSize(71, 29))
        self.cmb1_3.setMaximumSize(QtCore.QSize(71, 29))
        self.cmb1_3.setStyleSheet("QComboBox{\n"
                                  "  background-color: #404040;\n"
                                  "  border: thin solid blue;\n"
                                  "  border-radius: 4px;\n"
                                  "  font: inherit;\n"
                                  "  color: #FFFFFF;\n"
                                  "  line-height: 1.5em;\n"
                                  "  padding: 0.5em 0.2em 0.2em 0.2em;\n"
                                  "}\n"
                                  "\n"
                                  " QComboBox::down-arrow {\n"
                                  "     image: url(/Users/benjamin/PycharmProjects/FCC_Toolkit/Designs/arrow.png);\n"
                                  " }")
        self.cmb1_3.setObjectName("cmb1_3")
        self.cmb1_3.addItem("")
        self.cmb1_3.addItem("")
        self.cmb1_3.addItem("")
        self.cmb1_3.addItem("")
        self.horizontalLayout.addWidget(self.cmb1_3)
        self.lbOperador2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.lbOperador2.setMaximumSize(QtCore.QSize(48, 29))
        self.lbOperador2.setStyleSheet("color: #FFFFFF;")
        self.lbOperador2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbOperador2.setObjectName("lbOperador2")
        self.horizontalLayout.addWidget(self.lbOperador2)
        self.cmb1_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.cmb1_2.setMinimumSize(QtCore.QSize(71, 29))
        self.cmb1_2.setMaximumSize(QtCore.QSize(71, 29))
        self.cmb1_2.setStyleSheet("QComboBox{\n"
                                  "  background-color: #404040;\n"
                                  "  border: thin solid blue;\n"
                                  "  border-radius: 4px;\n"
                                  "  font: inherit;\n"
                                  "  color: #FFFFFF;\n"
                                  "  line-height: 1.5em;\n"
                                  "  padding: 0.5em 0.2em 0.2em 0.2em;\n"
                                  "}\n"
                                  "\n"
                                  " QComboBox::down-arrow {\n"
                                  "     image: url(/Users/benjamin/PycharmProjects/FCC_Toolkit/Designs/arrow.png);\n"
                                  " }")
        self.cmb1_2.setObjectName("cmb1_2")
        self.cmb1_2.addItem("")
        self.cmb1_2.addItem("")
        self.cmb1_2.addItem("")
        self.cmb1_2.addItem("")
        self.horizontalLayout.addWidget(self.cmb1_2)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_21.setMaximumSize(QtCore.QSize(49, 29))
        self.label_21.setStyleSheet("color: #FFFFFF;")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_11.setMinimumSize(QtCore.QSize(60, 29))
        self.label_11.setMaximumSize(QtCore.QSize(60, 29))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_10.setMinimumSize(QtCore.QSize(60, 29))
        self.label_10.setMaximumSize(QtCore.QSize(60, 29))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(60, 29))
        self.label_7.setMaximumSize(QtCore.QSize(60, 29))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setMinimumSize(QtCore.QSize(60, 29))
        self.label_5.setMaximumSize(QtCore.QSize(60, 29))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(829, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btnUnion = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btnUnion.setStyleSheet("QPushButton{\n"
                                    "    font: bold 18px;\n"
                                    "    border-style: inset;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: green;\n"
                                    "    color: #FFFFFF;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed\n"
                                    "{\n"
                                    "    background-color : green;\n"
                                    "}")
        self.btnUnion.setObjectName("btnUnion")
        self.btnUnion.clicked.connect(self.clicked_union)
        self.horizontalLayout_11.addWidget(self.btnUnion)
        self.btnIntersection = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btnIntersection.setMaximumSize(QtCore.QSize(203, 26))
        self.btnIntersection.setStyleSheet("QPushButton{\n"
                                           "    font: bold 18px;\n"
                                           "    border-style: inset;\n"
                                           "    border-width: 2px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color: green;\n"
                                           "    color: #FFFFFF;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton::pressed\n"
                                           "{\n"
                                           "    background-color : green;\n"
                                           "}")
        self.btnIntersection.setObjectName("btnIntersection")
        self.btnIntersection.clicked.connect(self.clicked_intersection)
        self.horizontalLayout_11.addWidget(self.btnIntersection)
        self.btnDifference = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btnDifference.setMaximumSize(QtCore.QSize(202, 26))
        self.btnDifference.setStyleSheet("QPushButton{\n"
                                         "    font: bold 18px;\n"
                                         "    border-style: inset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: green;\n"
                                         "    color: #FFFFFF;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{\n"
                                         "    background-color : green;\n"
                                         "}")
        self.btnDifference.setObjectName("btnDifference")
        self.btnDifference.clicked.connect(self.clicked_difference)
        self.horizontalLayout_11.addWidget(self.btnDifference)
        self.btnSymmetry = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btnSymmetry.setMaximumSize(QtCore.QSize(202, 26))
        self.btnSymmetry.setStyleSheet("QPushButton{\n"
                                       "    font: bold 18px;\n"
                                       "    border-style: inset;\n"
                                       "    border-width: 2px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: green;\n"
                                       "    color: #FFFFFF;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::pressed\n"
                                       "{\n"
                                       "    background-color : green;\n"
                                       "}")
        self.btnSymmetry.setObjectName("btnSymmetry")
        self.btnSymmetry.clicked.connect(self.clicked_symmetric)
        self.horizontalLayout_11.addWidget(self.btnSymmetry)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        Conjuntos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Conjuntos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 21))
        self.menubar.setObjectName("menubar")
        Conjuntos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Conjuntos)
        self.statusbar.setObjectName("statusbar")
        Conjuntos.setStatusBar(self.statusbar)

        self.retranslateUi(Conjuntos)
        QtCore.QMetaObject.connectSlotsByName(Conjuntos)

    def retranslateUi(self, Conjuntos):
        _translate = QtCore.QCoreApplication.translate
        Conjuntos.setWindowTitle(_translate("Conjuntos", "MainWindow"))
        self.label_2.setText(_translate("Conjuntos", "Conjunto A:"))
        self.label.setText(_translate("Conjuntos", "Conjunto B:"))
        self.label_3.setText(_translate("Conjuntos", "Conjunto C:"))
        self.label_34.setText(_translate("Conjuntos", "Selecciona el número de conjuntos a evaluar:"))
        self.radioButton.setText(_translate("Conjuntos", "Dos Conjuntos"))
        self.radioButton.clicked.connect(self.check)
        self.radioButton_2.setText(_translate("Conjuntos", "Tres Conjuntos"))
        self.radioButton_2.clicked.connect(self.check)
        self.cmb1.setItemText(0, _translate("Conjuntos", "-"))
        self.cmb1.setItemText(1, _translate("Conjuntos", "A"))
        self.cmb1.setItemText(2, _translate("Conjuntos", "B"))
        self.cmb1.setItemText(3, _translate("Conjuntos", "C"))
        self.lbOperador2_2.setText(_translate("Conjuntos", "*"))
        self.label_18.setText(_translate("Conjuntos", "("))
        self.cmb1_3.setItemText(0, _translate("Conjuntos", "-"))
        self.cmb1_3.setItemText(1, _translate("Conjuntos", "A"))
        self.cmb1_3.setItemText(2, _translate("Conjuntos", "B"))
        self.cmb1_3.setItemText(3, _translate("Conjuntos", "C"))
        self.lbOperador2.setText(_translate("Conjuntos", "*"))
        self.cmb1_2.setItemText(0, _translate("Conjuntos", "-"))
        self.cmb1_2.setItemText(1, _translate("Conjuntos", "A"))
        self.cmb1_2.setItemText(2, _translate("Conjuntos", "B"))
        self.cmb1_2.setItemText(3, _translate("Conjuntos", "C"))
        self.label_21.setText(_translate("Conjuntos", ")"))
        self.btnUnion.setText(_translate("Conjuntos", "Unión"))
        self.btnIntersection.setText(_translate("Conjuntos", "Intersección"))
        self.btnDifference.setText(_translate("Conjuntos", "Diferencia"))
        self.btnSymmetry.setText(_translate("Conjuntos", "Diferencia Simétrica"))

    # Funcion que llama al modulo de plot y llama a las funciones setter que tomara para graficar los conjuntos
    def open_plot(self, conjunto1, conjunto2, conjunto3, operacion, opcion):
        self.object = Plot.Window()
        self.object.set_conjunto1(conjunto1)
        self.object.set_conjunto2(conjunto2)
        self.object.set_conjunto3(conjunto3)
        self.object.set_operacion(operacion)
        self.object.set_numero(opcion)
        self.object.show()

    #Funcion que retorna el conjunto dependiendo de la seleccion que se da en el combo box
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

    #Funcion que revisa si se van a evaluar 2 o tres conjuntos. Si se evaluan 2 va a bloquear una combo box
    # para que no se pueda usar
    def check(self):

        if self.radioButton.isChecked():
            self.cmb1.setEnabled(False)
            self.cmb1.setCurrentText("-")
        else:
            self.cmb1.setEnabled(True)

    #Funcion que elimina cualquier de los espacios del input y ademas los convierte en un set
    def input_parsing(self, _set):
        _set = _set.lower().replace(" ", "").replace(",", " ")
        _set = set(list(_set.split(" ")))
        return _set

    #Funcion que toma el texto de las cajas y llama a otra funcion para parsearlo
    def input_getter(self):
        self.setA = self.input_parsing(self.txtSetA.text())
        self.setB = self.input_parsing(self.txtSetB.text())
        self.setC = self.input_parsing(self.txtSetC.text())

    #Funcion para evaluar uniones (El codigo se repite en las operaciones pero se cambian los signos que se evaluan)
    def clicked_union(self):
        self.lbOperador2.setText("∪")
        self.lbOperador2_2.setText("∪")
        self.input_getter()
        if self.radioButton.isChecked(): #Si esta seleccionada la opcion de 2 conjuntos solo para la union de los 2 conjuntos
            self.conjunto1 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 | self.conjunto2)
            self.opcion = 1 #Este valor se manda al modulo plot para que solo cree un diagrama de venn con 2 conjuntos
            self.open_plot(self.conjunto1, self.conjunto2, set(), self.operacion, self.opcion)
        else:
            self.conjunto1 = self.cmb_option(self.cmb1.currentText())
            self.conjunto2 = self.cmb_option(self.cmb1_3.currentText())
            self.conjunto3 = self.cmb_option(self.cmb1_2.currentText())
            self.operacion = (self.conjunto1 | (self.conjunto2 | self.conjunto3))
            self.opcion = 2 #Este valor se manda al modulo plot para que solo cree un diagrama de venn con 3 conjuntos
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

'''

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Conjuntos = QtWidgets.QMainWindow()
    ui = Ui_Conjuntos()
    ui.setupUi(Conjuntos)
    Conjuntos.show()
    sys.exit(app.exec_())

'''