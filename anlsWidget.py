from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnlsWidget(object):
    def setupUi(self, AnlsWidget):
        AnlsWidget.setObjectName("AnlsWidget")
        AnlsWidget.resize(648, 547)
        AnlsWidget.setMinimumSize(QtCore.QSize(648, 547))
        AnlsWidget.setMaximumSize(QtCore.QSize(648, 547))
        self.BackgroundLabel = QtWidgets.QLabel(AnlsWidget)
        self.BackgroundLabel.setGeometry(QtCore.QRect(0, 0, 661, 551))
        self.BackgroundLabel.setStyleSheet("background-color: rgb(48, 49, 60);\n"
                                           "border-top: 20px solid rgb(185, 209, 122)")
        self.BackgroundLabel.setText("")
        self.BackgroundLabel.setObjectName("BackgroundLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(AnlsWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 631, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.TablesLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.TablesLayout.setContentsMargins(0, 0, 0, 0)
        self.TablesLayout.setObjectName("TablesLayout")
        self.ClassATable = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.ClassATable.setObjectName("ClassATable")
        self.ClassATable.setColumnCount(0)
        self.ClassATable.setRowCount(0)
        self.TablesLayout.addWidget(self.ClassATable)
        self.ClaccBTable = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.ClaccBTable.setMinimumSize(QtCore.QSize(205, 239))
        self.ClaccBTable.setObjectName("ClaccBTable")
        self.ClaccBTable.setColumnCount(0)
        self.ClaccBTable.setRowCount(0)
        self.TablesLayout.addWidget(self.ClaccBTable)
        self.ClaccCTable = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.ClaccCTable.setObjectName("ClaccCTable")
        self.ClaccCTable.setColumnCount(0)
        self.ClaccCTable.setRowCount(0)
        self.TablesLayout.addWidget(self.ClaccCTable)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(AnlsWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 20, 650, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ClassLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ClassLayout.setContentsMargins(0, 0, 0, 0)
        self.ClassLayout.setObjectName("ClassLayout")
        self.loadLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.loadLabel.setStyleSheet("font: 16pt \"Mongolian Baiti\";\n"
                                     "color: rgb(185, 209, 122);")
        self.loadLabel.setObjectName("loadLabel")
        self.ClassLayout.addWidget(self.loadLabel)
        self.loadLabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.loadLabel_2.setStyleSheet("font: 16pt \"Mongolian Baiti\";\n"
                                       "color:  rgb(185, 209, 122);")
        self.loadLabel_2.setObjectName("loadLabel_2")
        self.ClassLayout.addWidget(self.loadLabel_2)
        self.loadLabel_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.loadLabel_3.setStyleSheet("font: 16pt \"Mongolian Baiti\";\n"
                                       "color:  rgb(185, 209, 122);")
        self.loadLabel_3.setObjectName("loadLabel_3")
        self.ClassLayout.addWidget(self.loadLabel_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(AnlsWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 320, 631, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.FormulsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.FormulsLayout.setContentsMargins(0, 0, 0, 0)
        self.FormulsLayout.setObjectName("FormulsLayout")
        self.formul1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.formul1.setStyleSheet("font: 14pt \"Mongolian Baiti\";\n"
                                   "color:  rgb(185, 209, 122);")
        self.formul1.setObjectName("formul1")
        self.FormulsLayout.addWidget(self.formul1)
        self.formul2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.formul2.setStyleSheet("font: 14pt \"Mongolian Baiti\";\n"
                                   "color:  rgb(185, 209, 122);")
        self.formul2.setObjectName("formul2")
        self.FormulsLayout.addWidget(self.formul2)
        self.formul3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.formul3.setStyleSheet("font: 14pt \"Mongolian Baiti\";\n"
                                   "color:  rgb(185, 209, 122);")
        self.formul3.setObjectName("formul3")
        self.FormulsLayout.addWidget(self.formul3)
        self.showGraphBtn = QtWidgets.QPushButton(AnlsWidget)
        self.showGraphBtn.setGeometry(QtCore.QRect(14, 482, 621, 51))
        self.showGraphBtn.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(99, 100, 130);\n"
                                        "    border-top: 5px solid rgb(185, 209, 122);\n"
                                        "    color:  rgb(185, 209, 122);\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-top: 10px solid  rgb(185, 209, 122);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-top: 17px solid rgb(185, 209, 122);\n"
                                        "}")
        self.showGraphBtn.setObjectName("showGraphBtn")

        self.retranslateUi(AnlsWidget)
        QtCore.QMetaObject.connectSlotsByName(AnlsWidget)

    def retranslateUi(self, AnlsWidget):
        _translate = QtCore.QCoreApplication.translate
        AnlsWidget.setWindowTitle(_translate("AnlsWidget", "Результаты анализа"))
        self.loadLabel.setText(_translate("AnlsWidget", "Самое Рискованое  "))
        self.loadLabel_2.setText(_translate("AnlsWidget", "Рискованое"))
        self.loadLabel_3.setText(_translate("AnlsWidget", "Устойчивое"))
        self.formul1.setText(_translate("AnlsWidget", "f1 ="))
        self.formul2.setText(_translate("AnlsWidget", "f2 ="))
        self.formul3.setText(_translate("AnlsWidget", "f3 ="))
        self.showGraphBtn.setText(_translate("AnlsWidget", "Показать график распределения"))
