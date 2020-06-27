# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printdialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(700, 500)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.StackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.StackedWidget.setObjectName("StackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridlayout1 = QtWidgets.QGridLayout(self.page)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout1.addWidget(self.line, 1, 0, 1, 1)
        self.Files = FileTable(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Files.sizePolicy().hasHeightForWidth())
        self.Files.setSizePolicy(sizePolicy)
        self.Files.setObjectName("Files")
        self.gridlayout1.addWidget(self.Files, 2, 0, 1, 1)
        self.StackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridlayout2 = QtWidgets.QGridLayout(self.page_2)
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.page_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridlayout2.addWidget(self.line_2, 1, 0, 1, 1)
        self.PrinterName = PrinterNameComboBox(self.page_2)
        self.PrinterName.setObjectName("PrinterName")
        self.gridlayout2.addWidget(self.PrinterName, 2, 0, 1, 1)
        self.OptionsToolBox = PrintSettingsToolbox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsToolBox.sizePolicy().hasHeightForWidth())
        self.OptionsToolBox.setSizePolicy(sizePolicy)
        self.OptionsToolBox.setObjectName("OptionsToolBox")
        self.gridlayout2.addWidget(self.OptionsToolBox, 3, 0, 1, 1)
        self.StackedWidget.addWidget(self.page_2)
        self.gridlayout.addWidget(self.StackedWidget, 0, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridlayout.addWidget(self.line_3, 1, 0, 1, 5)
        self.StepText = QtWidgets.QLabel(Dialog)
        self.StepText.setObjectName("StepText")
        self.gridlayout.addWidget(self.StepText, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(251, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 2, 1, 1, 1)
        self.BackButton = QtWidgets.QPushButton(Dialog)
        self.BackButton.setObjectName("BackButton")
        self.gridlayout.addWidget(self.BackButton, 2, 2, 1, 1)
        self.NextButton = QtWidgets.QPushButton(Dialog)
        self.NextButton.setObjectName("NextButton")
        self.gridlayout.addWidget(self.NextButton, 2, 3, 1, 1)
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton, 2, 4, 1, 1)

        self.retranslateUi(Dialog)
        self.StackedWidget.setCurrentIndex(1)
        self.OptionsToolBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HP Device Manager - Print"))
        self.label_2.setText(_translate("Dialog", "Select Files to Print"))
        self.label_3.setText(_translate("Dialog", "Select Printer and Options"))
        self.StepText.setText(_translate("Dialog", "Step %1 of %2"))
        self.BackButton.setText(_translate("Dialog", "< Back"))
        self.NextButton.setText(_translate("Dialog", "Next >"))
        self.CancelButton.setText(_translate("Dialog", "Cancel"))
from .filetable import FileTable
from .printernamecombobox import PrinterNameComboBox
from .printsettingstoolbox import PrintSettingsToolbox
