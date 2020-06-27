import os
from gui.main_window import font_size
from PyQt5 import QtCore, QtWidgets, QtGui

font_setting = font_size()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ray_fusion(object):
    def setupUi(self, ray_fusion):
        ray_fusion.setObjectName(_fromUtf8("ray_fusion"))
        ray_fusion.resize(821, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/fusion.png" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ray_fusion.setWindowIcon(icon)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(ray_fusion)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(ray_fusion)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Page-World.ico" % (os.getcwd()))))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.target_edit = QtWidgets.QLineEdit(ray_fusion)
        self.target_edit.setMinimumSize(QtCore.QSize(281, 0))
        self.target_edit.setObjectName(_fromUtf8("target_edit"))
        self.horizontalLayout.addWidget(self.target_edit)
        self.port_edit = QtWidgets.QLineEdit(ray_fusion)
        self.port_edit.setMaximumSize(QtCore.QSize(51, 20))
        self.port_edit.setObjectName(_fromUtf8("port_edit"))
        self.horizontalLayout.addWidget(self.port_edit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.help_button = QtWidgets.QPushButton(ray_fusion)
        self.help_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Help.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QtCore.QSize(30, 30))
        self.help_button.setFlat(True)
        self.help_button.setObjectName(_fromUtf8("help_button"))
        self.horizontalLayout_4.addWidget(self.help_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.groupBox = QtWidgets.QGroupBox(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.http_https_radio = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.http_https_radio.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Page-World.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.http_https_radio.setIcon(icon2)
        self.http_https_radio.setIconSize(QtCore.QSize(20, 20))
        self.http_https_radio.setChecked(True)
        self.http_https_radio.setObjectName(_fromUtf8("http_https_radio"))
        self.horizontalLayout_2.addWidget(self.http_https_radio)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.telnet_radio = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.telnet_radio.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Application-Osx-Terminal.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.telnet_radio.setIcon(icon3)
        self.telnet_radio.setObjectName(_fromUtf8("telnet_radio"))
        self.horizontalLayout_2.addWidget(self.telnet_radio)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.ftp_radio = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.ftp_radio.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Ftp.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ftp_radio.setIcon(icon4)
        self.ftp_radio.setIconSize(QtCore.QSize(20, 20))
        self.ftp_radio.setObjectName(_fromUtf8("ftp_radio"))
        self.horizontalLayout_2.addWidget(self.ftp_radio)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.settings_button = QtWidgets.QPushButton(ray_fusion)
        self.settings_button.setMaximumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.settings_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Setting-Tools.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon5)
        self.settings_button.setObjectName(_fromUtf8("settings_button"))
        self.horizontalLayout_11.addWidget(self.settings_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.settings_groupbox = QtWidgets.QGroupBox(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.settings_groupbox.setFont(font)
        self.settings_groupbox.setObjectName(_fromUtf8("settings_groupbox"))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings_groupbox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.default_wordlist_radio = QtWidgets.QRadioButton(self.settings_groupbox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.default_wordlist_radio.setFont(font)
        self.default_wordlist_radio.setChecked(True)
        self.default_wordlist_radio.setObjectName(_fromUtf8("default_wordlist_radio"))
        self.horizontalLayout_9.addWidget(self.default_wordlist_radio)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.custom_wordlist_radio = QtWidgets.QRadioButton(self.settings_groupbox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.custom_wordlist_radio.setFont(font)
        self.custom_wordlist_radio.setObjectName(_fromUtf8("custom_wordlist_radio"))
        self.horizontalLayout_9.addWidget(self.custom_wordlist_radio)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.blank_username_checkbox = QtWidgets.QCheckBox(self.settings_groupbox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.blank_username_checkbox.setFont(font)
        self.blank_username_checkbox.setChecked(True)
        self.blank_username_checkbox.setObjectName(_fromUtf8("blank_username_checkbox"))
        self.horizontalLayout_9.addWidget(self.blank_username_checkbox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.blank_password_checkbox = QtWidgets.QCheckBox(self.settings_groupbox)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.blank_password_checkbox.setFont(font)
        self.blank_password_checkbox.setChecked(True)
        self.blank_password_checkbox.setObjectName(_fromUtf8("blank_password_checkbox"))
        self.horizontalLayout_9.addWidget(self.blank_password_checkbox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtWidgets.QLabel(self.settings_groupbox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.time_interval_spinbox = QtWidgets.QSpinBox(self.settings_groupbox)
        self.time_interval_spinbox.setObjectName(_fromUtf8("time_interval_spinbox"))
        self.horizontalLayout_5.addWidget(self.time_interval_spinbox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addWidget(self.settings_groupbox)
        self.custom_wordlist_groupbox = QtWidgets.QGroupBox(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.custom_wordlist_groupbox.setFont(font)
        self.custom_wordlist_groupbox.setTitle(_fromUtf8(""))
        self.custom_wordlist_groupbox.setObjectName(_fromUtf8("custom_wordlist_groupbox"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.custom_wordlist_groupbox)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.user_wordlist_led = QtWidgets.QLabel(self.custom_wordlist_groupbox)
        self.user_wordlist_led.setText(_fromUtf8(""))
        self.user_wordlist_led.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/red_led.png" % (os.getcwd()))))
        self.user_wordlist_led.setObjectName(_fromUtf8("user_wordlist_led"))
        self.horizontalLayout_12.addWidget(self.user_wordlist_led)
        self.userlist_button = QtWidgets.QPushButton(self.custom_wordlist_groupbox)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Page-White-Database.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userlist_button.setIcon(icon6)
        self.userlist_button.setIconSize(QtCore.QSize(20, 20))
        self.userlist_button.setObjectName(_fromUtf8("userlist_button"))
        self.horizontalLayout_12.addWidget(self.userlist_button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.password_wordlist_led = QtWidgets.QLabel(self.custom_wordlist_groupbox)
        self.password_wordlist_led.setText(_fromUtf8(""))
        self.password_wordlist_led.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/red_led.png" % (os.getcwd()))))
        self.password_wordlist_led.setObjectName(_fromUtf8("password_wordlist_led"))
        self.horizontalLayout_12.addWidget(self.password_wordlist_led)
        self.passwordlist_button = QtWidgets.QPushButton(self.custom_wordlist_groupbox)
        self.passwordlist_button.setIcon(icon6)
        self.passwordlist_button.setIconSize(QtCore.QSize(20, 20))
        self.passwordlist_button.setObjectName(_fromUtf8("passwordlist_button"))
        self.horizontalLayout_12.addWidget(self.passwordlist_button)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.verticalLayout_9.addWidget(self.custom_wordlist_groupbox)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_8 = QtWidgets.QLabel(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.credential_table = QtWidgets.QTableWidget(ray_fusion)
        self.credential_table.setFrameShape(QtWidgets.QFrame.VLine)
        self.credential_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.credential_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.credential_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.credential_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.credential_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.credential_table.setObjectName(_fromUtf8("credential_table"))
        self.verticalLayout_7.addWidget(self.credential_table)
        spacerItem14 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem14)
        self.launch_bruteforce = QtWidgets.QPushButton(ray_fusion)
        self.launch_bruteforce.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.launch_bruteforce.setFont(font)
        self.launch_bruteforce.setObjectName(_fromUtf8("launch_bruteforce"))
        self.verticalLayout_7.addWidget(self.launch_bruteforce)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtWidgets.QLabel(ray_fusion)
        self.label_3.setMaximumSize(QtCore.QSize(52, 32))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Statistics.ico" % (os.getcwd()))))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line_2 = QtWidgets.QFrame(ray_fusion)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.statistics_username = QtWidgets.QLabel(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.statistics_username.setFont(font)
        self.statistics_username.setObjectName(_fromUtf8("statistics_username"))
        self.verticalLayout_2.addWidget(self.statistics_username)
        self.statistics_password = QtWidgets.QLabel(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.statistics_password.setFont(font)
        self.statistics_password.setObjectName(_fromUtf8("statistics_password"))
        self.verticalLayout_2.addWidget(self.statistics_password)
        self.statistics_percentage = QtWidgets.QLabel(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.statistics_percentage.setFont(font)
        self.statistics_percentage.setObjectName(_fromUtf8("statistics_percentage"))
        self.verticalLayout_2.addWidget(self.statistics_percentage)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(ray_fusion)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.save_credentials = QtWidgets.QPushButton(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.save_credentials.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Page-Save.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_credentials.setIcon(icon7)
        self.save_credentials.setIconSize(QtCore.QSize(20, 20))
        self.save_credentials.setObjectName(_fromUtf8("save_credentials"))
        self.verticalLayout_3.addWidget(self.save_credentials)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.clear_credentials = QtWidgets.QPushButton(ray_fusion)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.clear_credentials.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Shape-Square-Delete.ico" % (os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_credentials.setIcon(icon8)
        self.clear_credentials.setIconSize(QtCore.QSize(20, 20))
        self.clear_credentials.setObjectName(_fromUtf8("clear_credentials"))
        self.verticalLayout_3.addWidget(self.clear_credentials)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem17)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        spacerItem19 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem19)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.retranslateUi(ray_fusion)
        QtCore.QMetaObject.connectSlotsByName(ray_fusion)
        ray_fusion.setTabOrder(self.target_edit, self.port_edit)
        ray_fusion.setTabOrder(self.port_edit, self.default_wordlist_radio)
        ray_fusion.setTabOrder(self.default_wordlist_radio, self.custom_wordlist_radio)
        ray_fusion.setTabOrder(self.custom_wordlist_radio, self.blank_username_checkbox)
        ray_fusion.setTabOrder(self.blank_username_checkbox, self.blank_password_checkbox)
        ray_fusion.setTabOrder(self.blank_password_checkbox, self.time_interval_spinbox)
        ray_fusion.setTabOrder(self.time_interval_spinbox, self.save_credentials)
        ray_fusion.setTabOrder(self.save_credentials, self.http_https_radio)
        ray_fusion.setTabOrder(self.http_https_radio, self.telnet_radio)
        ray_fusion.setTabOrder(self.telnet_radio, self.ftp_radio)
        ray_fusion.setTabOrder(self.ftp_radio, self.clear_credentials)
        ray_fusion.setTabOrder(self.clear_credentials, self.settings_button)
        ray_fusion.setTabOrder(self.settings_button, self.credential_table)
        ray_fusion.setTabOrder(self.credential_table, self.help_button)
        ray_fusion.setTabOrder(self.help_button, self.userlist_button)
        ray_fusion.setTabOrder(self.userlist_button, self.passwordlist_button)

    def retranslateUi(self, ray_fusion):
        ray_fusion.setWindowTitle(QtWidgets.QApplication.translate("ray_fusion", "Fern - Ray Fusion", None, 0))
        self.target_edit.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Insert target address here</p></body></html>", None, 0))
        self.port_edit.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Insert service port number</p></body></html>", None, 0))
        self.port_edit.setText(QtWidgets.QApplication.translate("ray_fusion", "80", None, 0))
        self.help_button.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Help</p></body></html>", None, 0))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("ray_fusion", "Service ", None, 0))
        self.http_https_radio.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>HTTP or HTTPS Service (Supports only Basic Authentication)</p></body></html>", None, 0))
        self.http_https_radio.setText(QtWidgets.QApplication.translate("ray_fusion", "HTTP / HTTPS (Basic)", None, 0))
        self.telnet_radio.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Telnet service</p></body></html>", None, 0))
        self.telnet_radio.setText(QtWidgets.QApplication.translate("ray_fusion", "TELNET", None, 0))
        self.ftp_radio.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>FTP Service</p></body></html>", None, 0))
        self.ftp_radio.setText(QtWidgets.QApplication.translate("ray_fusion", "FTP", None, 0))
        self.settings_button.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>click to hide or show settings</p></body></html>", None, 0))
        self.settings_button.setText(QtWidgets.QApplication.translate("ray_fusion", "Hide Settings", None, 0))
        self.settings_groupbox.setTitle(QtWidgets.QApplication.translate("ray_fusion", "Settings", None, 0))
        self.default_wordlist_radio.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Select to use internal wordlists</p></body></html>", None, 0))
        self.default_wordlist_radio.setText(QtWidgets.QApplication.translate("ray_fusion", "Default Wordlists", None, 0))
        self.custom_wordlist_radio.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Select to use your custom wordlists</p></body></html>", None, 0))
        self.custom_wordlist_radio.setText(QtWidgets.QApplication.translate("ray_fusion", "Custom Wordlists", None, 0))
        self.blank_username_checkbox.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Attempt blank password when bruteforcing</p></body></html>", None, 0))
        self.blank_username_checkbox.setText(QtWidgets.QApplication.translate("ray_fusion", "Attempt Blank Username", None, 0))
        self.blank_password_checkbox.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Attempt blank password when bruteforcing</p></body></html>", None, 0))
        self.blank_password_checkbox.setText(QtWidgets.QApplication.translate("ray_fusion", "Attempt Blank Password", None, 0))
        self.label_2.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Time interval between each try</p></body></html>", None, 0))
        self.label_2.setText(QtWidgets.QApplication.translate("ray_fusion", "Time Interval:", None, 0))
        self.time_interval_spinbox.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Time interval between each try</p></body></html>", None, 0))
        self.userlist_button.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Select wordlist with usernames</p></body></html>", None, 0))
        self.userlist_button.setText(QtWidgets.QApplication.translate("ray_fusion", "Import User Wordlist", None, 0))
        self.passwordlist_button.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Select wordlist with passwords</p></body></html>", None, 0))
        self.passwordlist_button.setText(QtWidgets.QApplication.translate("ray_fusion", "Import Password Wordlist", None, 0))
        self.label_8.setText(QtWidgets.QApplication.translate("ray_fusion", "Successful Login Credentials", None, 0))
        self.launch_bruteforce.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Start or Stop Bruteforce Attack</p></body></html>", None, 0))
        self.launch_bruteforce.setText(QtWidgets.QApplication.translate("ray_fusion", "Start", None, 0))
        self.label_4.setText(QtWidgets.QApplication.translate("ray_fusion", "Statistics", None, 0))
        self.statistics_username.setText(QtWidgets.QApplication.translate("ray_fusion", "Username:", None, 0))
        self.statistics_password.setText(QtWidgets.QApplication.translate("ray_fusion", "Password:", None, 0))
        self.statistics_percentage.setText(QtWidgets.QApplication.translate("ray_fusion", "0% Complete", None, 0))
        self.save_credentials.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Save credentials to disk</p></body></html>", None, 0))
        self.save_credentials.setText(QtWidgets.QApplication.translate("ray_fusion", "Save Credentials", None, 0))
        self.clear_credentials.setToolTip(QtWidgets.QApplication.translate("ray_fusion", "<html><head/><body><p>Clear all bruteforced credentials</p></body></html>", None, 0))
        self.clear_credentials.setText(QtWidgets.QApplication.translate("ray_fusion", "Clear Credentials", None, 0))

