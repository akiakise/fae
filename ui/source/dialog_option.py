# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_option.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(300, 345)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(500, 700))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_aliases = QtWidgets.QLabel(Dialog)
        self.label_aliases.setMinimumSize(QtCore.QSize(70, 20))
        self.label_aliases.setMaximumSize(QtCore.QSize(70, 20))
        self.label_aliases.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aliases.setObjectName("label_aliases")
        self.gridLayout.addWidget(self.label_aliases, 1, 0, 1, 1)
        self.button_confirm = QtWidgets.QPushButton(Dialog)
        self.button_confirm.setMinimumSize(QtCore.QSize(70, 0))
        self.button_confirm.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_confirm.setObjectName("button_confirm")
        self.gridLayout.addWidget(self.button_confirm, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_fallback_value = ClickableLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fallback_value.sizePolicy().hasHeightForWidth())
        self.label_fallback_value.setSizePolicy(sizePolicy)
        self.label_fallback_value.setMinimumSize(QtCore.QSize(150, 20))
        self.label_fallback_value.setMaximumSize(QtCore.QSize(150, 20))
        self.label_fallback_value.setObjectName("label_fallback_value")
        self.gridLayout.addWidget(self.label_fallback_value, 0, 1, 1, 1)
        self.label_fallback = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fallback.sizePolicy().hasHeightForWidth())
        self.label_fallback.setSizePolicy(sizePolicy)
        self.label_fallback.setMinimumSize(QtCore.QSize(70, 20))
        self.label_fallback.setMaximumSize(QtCore.QSize(70, 20))
        self.label_fallback.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fallback.setObjectName("label_fallback")
        self.gridLayout.addWidget(self.label_fallback, 0, 0, 1, 1)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setMinimumSize(QtCore.QSize(70, 0))
        self.button_cancel.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Options"))
        self.label_aliases.setText(_translate("Dialog", "Aliases:"))
        self.button_confirm.setText(_translate("Dialog", "Confirm"))
        self.label_fallback_value.setText(_translate("Dialog", "Please choose a application!"))
        self.label_fallback.setText(_translate("Dialog", "Falback:"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))
from ui.util.ClickableLabel import ClickableLabel
