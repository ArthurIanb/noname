# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/leader_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(676, 614)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 80, 521, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.leader_vl = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.leader_vl.setContentsMargins(0, 0, 0, 0)
        self.leader_vl.setObjectName("leader_vl")
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(280, 530, 90, 34))
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Список лидеров"))
        self.close_btn.setText(_translate("Form", "закрыть"))
