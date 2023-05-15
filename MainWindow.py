from PyQt5 import QtCore, QtWidgets
import sys
from mathApp import main
from delWidget import Ui_delWidget
from addWindow import Ui_addWidget
from anlsWidget import Ui_AnlsWidget
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 432)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 432))
        MainWindow.setMaximumSize(QtCore.QSize(800, 432))
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "    background-color: rgb(99, 100, 130);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(99, 95, 115);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 771, 291))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.TableLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.TableLayout.setContentsMargins(0, 0, 0, 0)
        self.TableLayout.setObjectName("TableLayout")
        self.startTableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTableWidget.sizePolicy().hasHeightForWidth())
        self.startTableWidget.setSizePolicy(sizePolicy)
        self.startTableWidget.setStyleSheet("border: 3px solid   rgb(99, 100, 130)\n"
                                            "")
        self.startTableWidget.setColumnCount(0)
        self.startTableWidget.setObjectName("startTableWidget")


####################### НАЧАЛЬНОЕ ЗАПОЛНЕНИЕ ТАБЛИЦЫ ####################################
        df = pd.read_excel('proizvodsvo.xlsx')
        df = df.dropna()  # Удаляем nan значения
        df = df.reset_index(drop=True)  # Сопоставляем индексы
        self.startTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.startTableWidget.setRowCount(df.shape[0])
        self.startTableWidget.setColumnCount(df.shape[1])

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(df.iloc[row, col]))
                self.startTableWidget.setItem(row, col, item)
        self.startTableWidget.setHorizontalHeaderLabels(['Название', 'Выручка', 'Рентабельность', 'Оборачиваемость'])

#######################################################
        self.TableLayout.addWidget(self.startTableWidget)
        self.loadLabel = QtWidgets.QLabel(self.centralwidget)
        self.loadLabel.setGeometry(QtCore.QRect(200, 310, 411, 31))
        self.loadLabel.setStyleSheet("font: 16pt \"Mongolian Baiti\";\n"
                                     "color: rgb(255, 255, 255);")
        self.loadLabel.setObjectName("loadLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 350, 781, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ButtonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.anlsBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.anlsBtn.setMinimumSize(QtCore.QSize(0, 75))
        self.anlsBtn.setStyleSheet("QPushButton{\n"
                                   "    border-top: 5px solid rgb(185, 209, 122) ;\n"
                                   "    color:  rgb(185, 209, 122);\n"
                                   "    \n"
                                   "    font: 14pt \"MS Shell Dlg 2\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    border-top: 10px solid rgb(185, 209, 122) ;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    border-top: 17px solid rgb(185, 209, 122) ;\n"
                                   "}")
        self.anlsBtn.setObjectName("anlsBtn")
        self.ButtonsLayout.addWidget(self.anlsBtn)
        self.resetBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.resetBtn.setMinimumSize(QtCore.QSize(0, 75))
        self.resetBtn.setStyleSheet("QPushButton {\n"
                                    "    border-top:5px solid rgb(255, 129, 83);\n"
                                    "    color:rgb(255, 129, 83);\n"
                                    "    font: 14pt \"MS Shell Dlg 2\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    border-top:10px solid rgb(255, 129, 83);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    border-top: 17px solid rgb(255, 129, 83) ;\n"
                                    "}")
        self.resetBtn.setObjectName("resetBtn")
        self.ButtonsLayout.addWidget(self.resetBtn)
        self.addBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addBtn.setMinimumSize(QtCore.QSize(0, 75))
        self.addBtn.setStyleSheet("QPushButton {\n"
                                  "    border-top: 5px solid rgb(162, 206, 241);\n"
                                  "    color:  rgb(162, 206, 241);\n"
                                  "    font: 14pt \"MS Shell Dlg 2\";\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    border-top: 10px solid rgb(162, 206, 241);    \n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "    border-top: 17px solid rgb(162, 206, 241) ;\n"
                                  "}")
        self.addBtn.setObjectName("addBtn")
        self.ButtonsLayout.addWidget(self.addBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteBtn.setMinimumSize(QtCore.QSize(0, 75))
        self.deleteBtn.setStyleSheet("QPushButton {\n"
                                     "    border-top: 5px solid rgb(251, 93, 85);\n"
                                     "    color: rgb(251, 93, 85);\n"
                                     "    font: 14pt \"MS Shell Dlg 2\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    border-top: 10px solid rgb(251, 93, 85);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-top: 17px solid rgb(251, 93, 85) ;\n"
                                     "}")
        self.deleteBtn.setObjectName("deleteBtn")
        self.ButtonsLayout.addWidget(self.deleteBtn)
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(-4, -8, 811, 451))
        self.backgroundLabel.setStyleSheet("background-color: rgb(48, 49, 60);")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.backgroundLabel.raise_()
        self.horizontalLayoutWidget.raise_()
        self.loadLabel.raise_()
        self.horizontalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnClicked()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ предприятий"))
        self.loadLabel.setText(_translate("MainWindow", "Данные получены"))
        self.anlsBtn.setText(_translate("MainWindow", "Провести анализ"))
        self.resetBtn.setText(_translate("MainWindow", "Обновить данные"))
        self.addBtn.setText(_translate("MainWindow", "Добавить элемент"))
        self.deleteBtn.setText(_translate("MainWindow", "Удалить элемент"))

    def showDelWidget(self):
        self.delWindow = QtWidgets.QDialog()
        self.ui = Ui_delWidget()
        self.ui.setupUi(self.delWindow)
        self.delWindow.show()

    def showAddWidget(self):
        self.addWindow = QtWidgets.QWidget()
        self.ui = Ui_addWidget()
        self.ui.setupUi(self.addWindow)
        self.addWindow.show()

    def showAnlsWidget(self):
        self.anlsWindow = QtWidgets.QWidget()
        self.ui = Ui_AnlsWidget()
        self.ui.setupUi(self.anlsWindow)

        classA, classB, classC, lda = main()

        self.ui.ClassATable.setColumnCount(classA.shape[1])
        self.ui.ClassATable.setRowCount(classA.shape[0])
        for row in range(classA.shape[0]):
            for col in range(classA.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(classA.iloc[row, col]))
                self.ui.ClassATable.setItem(row, col, item)

        self.ui.ClaccBTable.setColumnCount(classB.shape[1])
        self.ui.ClaccBTable.setRowCount(classB.shape[0])
        for row in range(classB.shape[0]):
            for col in range(classB.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(classB.iloc[row, col]))
                self.ui.ClaccBTable.setItem(row, col, item)

        self.ui.ClaccCTable.setColumnCount(classC.shape[1])
        self.ui.ClaccCTable.setRowCount(classC.shape[0])
        for row in range(classC.shape[0]):
            for col in range(classC.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(classC.iloc[row, col]))
                self.ui.ClaccCTable.setItem(row, col, item)
        self.ui.formul1.setText(
            f"f1= {round(lda.coef_[0][0], 4)} * В.+ {round(lda.coef_[0][1], 4)} * Р. + {round(lda.coef_[0][2], 4)} *"
            f" Об. + {round(lda.intercept_[0], 4)}"
        )
        self.ui.formul2.setText(
            f"f2= {round(lda.coef_[1][0], 4)} * В. + {round(lda.coef_[1][1], 4)} * Р. + {round(lda.coef_[1][2], 4)} *"
            f" Об. + {round(lda.intercept_[1], 4)}"
        )
        self.ui.formul3.setText(
            f"f3= {round(lda.coef_[2][0], 4)} * В. + {round(lda.coef_[2][1], 4)} * Р. + {round(lda.coef_[2][2], 4)} *"
            f" Об. + {round(lda.intercept_[2], 4)}"
        )

        self.anlsWindow.show()

    def btnClicked(self):
        self.addBtn.clicked.connect(lambda: self.showAddWidget())
        self.deleteBtn.clicked.connect(lambda: self.showDelWidget())
        self.anlsBtn.clicked.connect(lambda: self.showAnlsWidget())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
