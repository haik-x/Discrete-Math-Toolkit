from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class table_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 507)
        MainWindow.setMinimumSize(QtCore.QSize(571, 507))
        MainWindow.setMaximumSize(QtCore.QSize(571, 507))
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: black;")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 571, 471))
        self.tableWidget.setMinimumSize(QtCore.QSize(571, 471))
        self.tableWidget.setMaximumSize(QtCore.QSize(571, 471))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                       "color:#20C20E;\n"
                                       "background:#444444;\n"
                                       "border:1px solid #242424;\n"
                                       "alternate-background-color:#525252;\n"
                                       "gridline-color:#242424;\n"
                                       "}\n"
                                       " \n"
                                       "QTableWidget::item:selected{\n"
                                       "color:#20C20E;\n"
                                       "background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
                                       "}\n"
                                       " \n"
                                       "QTableWidget::item:hover{\n"
                                       "background:#5B5B5B;\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "text-align:center;\n"
                                       "background:#5E5E5E;\n"
                                       "padding:3px;\n"
                                       "margin:0px;\n"
                                       "color:#20C20E;\n"
                                       "border:1px solid #242424;\n"
                                       "border-left-width:0;\n"
                                       "}\n"
                                       " \n"
                                       "QListView::section{\n"
                                       "text-align:center;\n"
                                       "}\n"
                                       "QScrollBar:vertical{\n"
                                       "background:#484848;\n"
                                       "padding:0px;\n"
                                       "border-radius:6px;\n"
                                       "max-width:12px;\n"
                                       "}\n"
                                       " \n"
                                       " \n"
                                       "QScrollBar::handle:vertical{\n"
                                       "background:#CCCCCC;\n"
                                       "}\n"
                                       " \n"
                                       "QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
                                       "background:#A7A7A7;\n"
                                       "}\n"
                                       "QScrollBar::sub-page:vertical{\n"
                                       "background:444444;\n"
                                       "}\n"
                                       " \n"
                                       " \n"
                                       "QScrollBar::add-page:vertical{\n"
                                       "background:5B5B5B;\n"
                                       "}\n"
                                       " \n"
                                       "QScrollBar::add-line:vertical{\n"
                                       "background:none;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical{\n"
                                       "background:none;\n"
                                       "}")
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tabla de Vedad"))


