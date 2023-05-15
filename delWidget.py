from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delWidget(object):
    def setupUi(self, delWidget):
        delWidget.setObjectName("delWidget")
        delWidget.resize(240, 119)
        self.TextLabel = QtWidgets.QLabel(delWidget)
        self.TextLabel.setGeometry(QtCore.QRect(10, 25, 91, 41))
        self.TextLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(251, 93, 85);")
        self.TextLabel.setObjectName("TextLabel")
        self.BackgroundLabel = QtWidgets.QLabel(delWidget)
        self.BackgroundLabel.setGeometry(QtCore.QRect(0, -8, 241, 181))
        self.BackgroundLabel.setStyleSheet("background-color: rgb(48, 49, 60);\n"
                                           "border-top: 20px solid rgb(251, 93, 85);")
        self.BackgroundLabel.setText("")
        self.BackgroundLabel.setObjectName("BackgroundLabel")
        self.delInput = QtWidgets.QLineEdit(delWidget)
        self.delInput.setGeometry(QtCore.QRect(110, 30, 111, 31))
        self.delInput.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid rgb(246, 91, 83);\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 2px solid rgb(251, 145, 91);\n"
                                    "}")
        self.delInput.setObjectName("delInput")
        self.delbtn = QtWidgets.QPushButton(delWidget)
        self.delbtn.setGeometry(QtCore.QRect(10, 70, 221, 41))
        self.delbtn.setStyleSheet("QPushButton {\n"
                                  "    background-color: rgb(99, 100, 130);\n"
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
        self.delbtn.setObjectName("delbtn")
        self.BackgroundLabel.raise_()
        self.TextLabel.raise_()
        self.delInput.raise_()
        self.delbtn.raise_()

        self.retranslateUi(delWidget)
        QtCore.QMetaObject.connectSlotsByName(delWidget)

    def retranslateUi(self, delWidget):
        _translate = QtCore.QCoreApplication.translate
        delWidget.setWindowTitle(_translate("delWidget", "Удаление элемента"))
        self.TextLabel.setText(_translate("delWidget", "Введите ID:"))
        self.delbtn.setText(_translate("delWidget", "Удалить"))
