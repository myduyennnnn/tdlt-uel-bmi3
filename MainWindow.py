# Form implementation generated from reading ui file 'D:\Tuduylaptrinh\tdlt-uel-bmi\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 321, 51))
        self.label.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(203, 255, 174);\n"
"color: rgb(0, 85, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 81, 41))
        self.label_2.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 81, 41))
        self.label_3.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 81, 41))
        self.label_4.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 91, 41))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 100, 51, 41))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 140, 51, 41))
        self.label_7.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 180, 61, 41))
        self.label_8.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButtonCaculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCaculate.setGeometry(QtCore.QRect(90, 260, 121, 31))
        self.pushButtonCaculate.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 10pt \"Arial Black\"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Tuduylaptrinh\\tdlt-uel-bmi\\../baitaptuluyen/chuong7/baitapvenha/LearnPushButton/images/calculate.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCaculate.setIcon(icon)
        self.pushButtonCaculate.setObjectName("pushButtonCaculate")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(240, 260, 121, 31))
        self.pushButtonClose.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 10pt \"Arial Black\"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Tuduylaptrinh\\tdlt-uel-bmi\\../baitaptuluyen/chuong7/baitapvenha/LearnPushButton/images/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon1)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.lineEditWeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditWeight.setGeometry(QtCore.QRect(140, 109, 151, 21))
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.lineEditHeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditHeight.setGeometry(QtCore.QRect(140, 150, 151, 20))
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.labelBMI = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelBMI.setGeometry(QtCore.QRect(190, 180, 81, 41))
        self.labelBMI.setStyleSheet("font: 12pt \"MV Boli\";\n"
"")
        self.labelBMI.setObjectName("labelBMI")
        self.labelComment = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelComment.setGeometry(QtCore.QRect(190, 220, 91, 41))
        self.labelComment.setStyleSheet("font: 12pt \"MV Boli\";\n"
"")
        self.labelComment.setObjectName("labelComment")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonClose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hồng Gấm _ Quỳnh Hương _ Mỹ Duyên"))
        self.label.setText(_translate("MainWindow", "BMI Application"))
        self.label_2.setText(_translate("MainWindow", "Weight: "))
        self.label_3.setText(_translate("MainWindow", "Height: "))
        self.label_4.setText(_translate("MainWindow", "BMI: "))
        self.label_5.setText(_translate("MainWindow", "Comment: "))
        self.label_6.setText(_translate("MainWindow", "(Kg)"))
        self.label_7.setText(_translate("MainWindow", "(Cm)"))
        self.label_8.setText(_translate("MainWindow", "kg/m2"))
        self.pushButtonCaculate.setText(_translate("MainWindow", "Caculate"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
        self.labelBMI.setText(_translate("MainWindow", "27.68"))
        self.labelComment.setText(_translate("MainWindow", "Overweight"))
