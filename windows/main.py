# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Main:

    def generate(self, Form):
        Form.setObjectName("dell-charge-manager-gui")
        Form.resize(291, 84)
        Form.setMaximumSize(QtCore.QSize(291, 84))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/windowicon.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.description = QtWidgets.QLabel(Form)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 0, 0, 1, 1)
        self.quitButton = QtWidgets.QPushButton(Form)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.gridLayout.addWidget(self.quitButton, 2, 0, 1, 1)
        self.applyButton = QtWidgets.QPushButton(Form)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 2, 1, 1, 1)
        self.maxCharge = QtWidgets.QSpinBox(Form)
        self.maxCharge.setMinimum(55)
        self.maxCharge.setMaximum(100)
        self.maxCharge.setSingleStep(5)
        self.maxCharge.setDisplayIntegerBase(10)
        self.maxCharge.setSuffix("%")
        self.maxCharge.setObjectName("maxCharge")
        self.gridLayout.addWidget(self.maxCharge, 0, 1, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dell Charge Manager"))
        self.description.setText(_translate("Form", "Limit Charge To:"))
        self.quitButton.setText(_translate("Form", "Quit"))
        self.applyButton.setText(_translate("Form", "Apply"))