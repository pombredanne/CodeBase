import os
from gui.main_window import font_size
from PyQt5 import QtCore, QtWidgets, QtGui

font_setting = font_size()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class toolbox_win(object):
    def setupUi(self, toolbox_win):
        toolbox_win.setObjectName(_fromUtf8("toolbox_win"))
        toolbox_win.resize(736, 304)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295905972_tool_kit.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolbox_win.setWindowIcon(icon)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(toolbox_win)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtWidgets.QGroupBox(toolbox_win)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtWidgets.QSpacerItem(11, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtWidgets.QSpacerItem(190, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.geotrack_button = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geotrack_button.sizePolicy().hasHeightForWidth())
        self.geotrack_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.geotrack_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/map.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.geotrack_button.setIcon(icon1)
        self.geotrack_button.setIconSize(QtCore.QSize(49, 49))
        self.geotrack_button.setObjectName(_fromUtf8("geotrack_button"))
        self.verticalLayout.addWidget(self.geotrack_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtWidgets.QSpacerItem(11, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem4 = QtWidgets.QSpacerItem(190, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem4)
        self.cookie_hijack_button = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookie_hijack_button.sizePolicy().hasHeightForWidth())
        self.cookie_hijack_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.cookie_hijack_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/cookies-icon.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cookie_hijack_button.setIcon(icon2)
        self.cookie_hijack_button.setIconSize(QtCore.QSize(60, 60))
        self.cookie_hijack_button.setObjectName(_fromUtf8("cookie_hijack_button"))
        self.verticalLayout_6.addWidget(self.cookie_hijack_button)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem6 = QtWidgets.QSpacerItem(11, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem7 = QtWidgets.QSpacerItem(190, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem7)
        self.ray_fusion_button = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ray_fusion_button.sizePolicy().hasHeightForWidth())
        self.ray_fusion_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.ray_fusion_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/fusion.png" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ray_fusion_button.setIcon(icon3)
        self.ray_fusion_button.setIconSize(QtCore.QSize(60, 60))
        self.ray_fusion_button.setObjectName(_fromUtf8("ray_fusion_button"))
        self.verticalLayout_8.addWidget(self.ray_fusion_button)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(toolbox_win)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem9 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem10 = QtWidgets.QSpacerItem(158, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem10)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.pushButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295906241_preferences-desktop-font.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(48, 49))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem12 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem13 = QtWidgets.QSpacerItem(158, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem13)
        self.attack_options_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attack_options_button.sizePolicy().hasHeightForWidth())
        self.attack_options_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.attack_options_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/wifi_4.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attack_options_button.setIcon(icon5)
        self.attack_options_button.setIconSize(QtCore.QSize(48, 49))
        self.attack_options_button.setObjectName(_fromUtf8("attack_options_button"))
        self.verticalLayout_4.addWidget(self.attack_options_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_5.addWidget(self.groupBox)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)

        self.retranslateUi(toolbox_win)
        QtCore.QMetaObject.connectSlotsByName(toolbox_win)

    def retranslateUi(self, toolbox_win):
        toolbox_win.setWindowTitle(QtWidgets.QApplication.translate("toolbox_win", "Fern - ToolBox", None, 0))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("toolbox_win", "Features", None, 0))
        self.geotrack_button.setText(QtWidgets.QApplication.translate("toolbox_win", "Geolocatory Tracker", None, 0))
        self.cookie_hijack_button.setText(QtWidgets.QApplication.translate("toolbox_win", "Cookie Hijacker", None, 0))
        self.ray_fusion_button.setText(QtWidgets.QApplication.translate("toolbox_win", "Ray Fusion", None, 0))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("toolbox_win", "General Settings", None, 0))
        self.pushButton.setText(QtWidgets.QApplication.translate("toolbox_win", "Font Settings", None, 0))
        self.attack_options_button.setText(QtWidgets.QApplication.translate("toolbox_win", "WIFI Attack Options", None, 0))

