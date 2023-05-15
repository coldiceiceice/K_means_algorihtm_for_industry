
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addWidget(object):
    def setupUi(self, addWidget):
        addWidget.setObjectName("addWidget")
        addWidget.resize(240, 289)
        addWidget.setMinimumSize(QtCore.QSize(240, 289))
        addWidget.setMaximumSize(QtCore.QSize(240, 289))
        self.BackgroundLabel = QtWidgets.QLabel(addWidget)
        self.BackgroundLabel.setGeometry(QtCore.QRect(0, 0, 241, 321))
        self.BackgroundLabel.setMinimumSize(QtCore.QSize(241, 321))
        self.BackgroundLabel.setMaximumSize(QtCore.QSize(241, 321))
        self.BackgroundLabel.setStyleSheet("background-color: rgb(48, 49, 60);\n"
                                           "border-top: 20px solid rgb(157, 200, 234);")
        self.BackgroundLabel.setText("")
        self.BackgroundLabel.setObjectName("BackgroundLabel")
        self.delbtn = QtWidgets.QPushButton(addWidget)
        self.delbtn.setGeometry(QtCore.QRect(10, 240, 221, 41))
        self.delbtn.setStyleSheet("QPushButton {\n"
                                  "    \n"
                                  "    background-color: rgb(99, 100, 130);\n"
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
        self.delbtn.setObjectName("delbtn")
        self.delInput = QtWidgets.QLineEdit(addWidget)
        self.delInput.setGeometry(QtCore.QRect(10, 60, 221, 31))
        self.delInput.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid rgb(154, 196, 229);\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 2px solid rgb(251, 145, 91);\n"
                                    "}")
        self.delInput.setObjectName("delInput")
        self.delInput_2 = QtWidgets.QLineEdit(addWidget)
        self.delInput_2.setGeometry(QtCore.QRect(10, 130, 221, 31))
        self.delInput_2.setStyleSheet("QLineEdit {\n"
                                      "    border: 2px solid rgb(154, 196, 229);\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(251, 145, 91);\n"
                                      "}")
        self.delInput_2.setObjectName("delInput_2")
        self.delInput_3 = QtWidgets.QLineEdit(addWidget)
        self.delInput_3.setGeometry(QtCore.QRect(10, 200, 221, 31))
        self.delInput_3.setStyleSheet("QLineEdit {\n"
                                      "    border: 2px solid rgb(154, 196, 229);\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(251, 145, 91);\n"
                                      "}")
        self.delInput_3.setObjectName("delInput_3")
        self.TextLabel = QtWidgets.QLabel(addWidget)
        self.TextLabel.setGeometry(QtCore.QRect(10, 20, 231, 41))
        self.TextLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(154, 196, 229);")
        self.TextLabel.setObjectName("TextLabel")
        self.TextLabel_2 = QtWidgets.QLabel(addWidget)
        self.TextLabel_2.setGeometry(QtCore.QRect(10, 90, 231, 41))
        self.TextLabel_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(154, 196, 229);")
        self.TextLabel_2.setObjectName("TextLabel_2")
        self.TextLabel_3 = QtWidgets.QLabel(addWidget)
        self.TextLabel_3.setGeometry(QtCore.QRect(10, 160, 131, 41))
        self.TextLabel_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(154, 196, 229);")
        self.TextLabel_3.setObjectName("TextLabel_3")

        self.retranslateUi(addWidget)
        QtCore.QMetaObject.connectSlotsByName(addWidget)

    def retranslateUi(self, addWidget):
        _translate = QtCore.QCoreApplication.translate
        addWidget.setWindowTitle(_translate("addWidget", "Добавление элемента"))
        self.delbtn.setText(_translate("addWidget", "Добавить"))
        self.TextLabel.setText(_translate("addWidget", "Выручка"))
        self.TextLabel_2.setText(_translate("addWidget", "Рентабельность"))
        self.TextLabel_3.setText(_translate("addWidget", "Оборачиваемость"))
