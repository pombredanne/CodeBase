# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fabwindow_base.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridlayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")
        self.Splitter = QtWidgets.QSplitter(self.centralwidget)
        self.Splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Splitter.setObjectName("Splitter")
        self.GroupTableWidget = FABGroupTable(self.Splitter)
        self.GroupTableWidget.setAlternatingRowColors(True)
        self.GroupTableWidget.setObjectName("GroupTableWidget")
        self.GroupTableWidget.setColumnCount(1)
        self.GroupTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.GroupTableWidget.setHorizontalHeaderItem(0, item)
        self.NameTableWidget = FABNameTable(self.Splitter)
        self.NameTableWidget.setAlternatingRowColors(True)
        self.NameTableWidget.setObjectName("NameTableWidget")
        self.NameTableWidget.setColumnCount(1)
        self.NameTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.NameTableWidget.setHorizontalHeaderItem(0, item)
        self.NameFrame = QtWidgets.QFrame(self.Splitter)
        self.NameFrame.setEnabled(False)
        self.NameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NameFrame.setObjectName("NameFrame")
        self.gridlayout1 = QtWidgets.QGridLayout(self.NameFrame)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label = QtWidgets.QLabel(self.NameFrame)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(self.NameFrame)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridlayout1.addWidget(self.NameLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.NameFrame)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 1, 0, 1, 1)
        self.FaxNumberLineEdit = QtWidgets.QLineEdit(self.NameFrame)
        self.FaxNumberLineEdit.setObjectName("FaxNumberLineEdit")
        self.gridlayout1.addWidget(self.FaxNumberLineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.NameFrame)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3, 2, 0, 1, 1)
        self.NotesTextEdit = QtWidgets.QTextEdit(self.NameFrame)
        self.NotesTextEdit.setObjectName("NotesTextEdit")
        self.gridlayout1.addWidget(self.NotesTextEdit, 3, 0, 1, 2)
        self.gridlayout.addWidget(self.Splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 27))
        self.menubar.setObjectName("menubar")
        self.menuGroup = QtWidgets.QMenu(self.menubar)
        self.menuGroup.setObjectName("menuGroup")
        self.menuName = QtWidgets.QMenu(self.menubar)
        self.menuName.setObjectName("menuName")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.NewGroupAction = QtWidgets.QAction(MainWindow)
        self.NewGroupAction.setObjectName("NewGroupAction")
        self.NewNameAction = QtWidgets.QAction(MainWindow)
        self.NewNameAction.setObjectName("NewNameAction")
        self.RemoveGroupAction = QtWidgets.QAction(MainWindow)
        self.RemoveGroupAction.setEnabled(False)
        self.RemoveGroupAction.setObjectName("RemoveGroupAction")
        self.QuitAction = QtWidgets.QAction(MainWindow)
        self.QuitAction.setObjectName("QuitAction")
        self.RemoveNameAction = QtWidgets.QAction(MainWindow)
        self.RemoveNameAction.setEnabled(False)
        self.RemoveNameAction.setObjectName("RemoveNameAction")
        self.NewGroupFromSelectionAction = QtWidgets.QAction(MainWindow)
        self.NewGroupFromSelectionAction.setEnabled(False)
        self.NewGroupFromSelectionAction.setObjectName("NewGroupFromSelectionAction")
        self.ImportAction = QtWidgets.QAction(MainWindow)
        self.ImportAction.setObjectName("ImportAction")
        self.RenameGroupAction = QtWidgets.QAction(MainWindow)
        self.RenameGroupAction.setEnabled(False)
        self.RenameGroupAction.setObjectName("RenameGroupAction")
        self.RemoveFromGroupAction = QtWidgets.QAction(MainWindow)
        self.RemoveFromGroupAction.setEnabled(False)
        self.RemoveFromGroupAction.setObjectName("RemoveFromGroupAction")
        self.AddToGroupAction = QtWidgets.QAction(MainWindow)
        self.AddToGroupAction.setEnabled(False)
        self.AddToGroupAction.setObjectName("AddToGroupAction")
        self.menuGroup.addAction(self.NewGroupAction)
        self.menuGroup.addAction(self.NewGroupFromSelectionAction)
        self.menuGroup.addAction(self.RenameGroupAction)
        self.menuGroup.addSeparator()
        self.menuGroup.addAction(self.RemoveGroupAction)
        self.menuName.addAction(self.NewNameAction)
        self.menuName.addSeparator()
        self.menuName.addAction(self.AddToGroupAction)
        self.menuName.addAction(self.RemoveFromGroupAction)
        self.menuName.addSeparator()
        self.menuName.addAction(self.RemoveNameAction)
        self.menuFile.addAction(self.ImportAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.QuitAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGroup.menuAction())
        self.menubar.addAction(self.menuName.menuAction())
        self.toolBar.addAction(self.NewGroupAction)
        self.toolBar.addAction(self.NewGroupFromSelectionAction)
        self.toolBar.addAction(self.RenameGroupAction)
        self.toolBar.addAction(self.RemoveGroupAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.NewNameAction)
        self.toolBar.addAction(self.AddToGroupAction)
        self.toolBar.addAction(self.RemoveFromGroupAction)
        self.toolBar.addAction(self.RemoveNameAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HP Device Manager - Fax Address Book"))
        item = self.GroupTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Group"))
        item = self.NameTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Fax Number:"))
        self.label_3.setText(_translate("MainWindow", "Notes:"))
        self.menuGroup.setTitle(_translate("MainWindow", "Group"))
        self.menuName.setTitle(_translate("MainWindow", "Name"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.NewGroupAction.setText(_translate("MainWindow", "New Group..."))
        self.NewNameAction.setText(_translate("MainWindow", "New Name..."))
        self.RemoveGroupAction.setText(_translate("MainWindow", "Delete Group..."))
        self.QuitAction.setText(_translate("MainWindow", "Quit"))
        self.RemoveNameAction.setText(_translate("MainWindow", "Delete Name..."))
        self.NewGroupFromSelectionAction.setText(_translate("MainWindow", "New Group From Selection..."))
        self.ImportAction.setText(_translate("MainWindow", "Import..."))
        self.RenameGroupAction.setText(_translate("MainWindow", "Rename Group..."))
        self.RemoveFromGroupAction.setText(_translate("MainWindow", "Leave Group"))
        self.AddToGroupAction.setText(_translate("MainWindow", "Join Group..."))
from .fabgrouptable import FABGroupTable
from .fabnametable import FABNameTable
