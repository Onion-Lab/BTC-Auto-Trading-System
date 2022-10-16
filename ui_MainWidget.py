# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(599, 325)
        MainWidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(MainWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_6 = QGroupBox(MainWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startButton = QPushButton(self.groupBox_6)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        self.startButton.setMinimumSize(QSize(0, 30))
        self.startButton.setStyleSheet(u"QPushButton:enabled\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.startButton)

        self.stopButton = QPushButton(self.groupBox_6)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(0, 30))
        self.stopButton.setStyleSheet(u"QPushButton:enabled\n"
"{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.stopButton)


        self.gridLayout_2.addWidget(self.groupBox_6, 5, 2, 1, 1)

        self.groupBox = QGroupBox(MainWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.seed10Button = QPushButton(self.groupBox)
        self.buttonGroup_2 = QButtonGroup(MainWidget)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.seed10Button)
        self.seed10Button.setObjectName(u"seed10Button")
        self.seed10Button.setCheckable(True)
        self.seed10Button.setChecked(True)

        self.horizontalLayout_2.addWidget(self.seed10Button)

        self.seed25Button = QPushButton(self.groupBox)
        self.buttonGroup_2.addButton(self.seed25Button)
        self.seed25Button.setObjectName(u"seed25Button")
        self.seed25Button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.seed25Button)

        self.seed50Button = QPushButton(self.groupBox)
        self.buttonGroup_2.addButton(self.seed50Button)
        self.seed50Button.setObjectName(u"seed50Button")
        self.seed50Button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.seed50Button)

        self.seed75Button = QPushButton(self.groupBox)
        self.buttonGroup_2.addButton(self.seed75Button)
        self.seed75Button.setObjectName(u"seed75Button")
        self.seed75Button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.seed75Button)

        self.seed100Button = QPushButton(self.groupBox)
        self.buttonGroup_2.addButton(self.seed100Button)
        self.seed100Button.setObjectName(u"seed100Button")
        self.seed100Button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.seed100Button)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_5 = QGroupBox(MainWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statusLabel = QLabel(self.groupBox_5)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.statusLabel)


        self.gridLayout_2.addWidget(self.groupBox_5, 4, 2, 1, 1)

        self.groupBox_3 = QGroupBox(MainWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inposButton = QPushButton(self.groupBox_3)
        self.buttonGroup = QButtonGroup(MainWidget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.inposButton)
        self.inposButton.setObjectName(u"inposButton")
        self.inposButton.setEnabled(False)
        self.inposButton.setMinimumSize(QSize(0, 30))
        self.inposButton.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.inposButton.setCheckable(True)
        self.inposButton.setChecked(False)

        self.verticalLayout.addWidget(self.inposButton)

        self.noposButton = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.noposButton)
        self.noposButton.setObjectName(u"noposButton")
        self.noposButton.setEnabled(False)
        self.noposButton.setMinimumSize(QSize(0, 30))
        self.noposButton.setStyleSheet(u"QPushButton:checked\n"
"{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.noposButton.setCheckable(True)
        self.noposButton.setChecked(True)

        self.verticalLayout.addWidget(self.noposButton)


        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 2, 1)

        self.groupBox_2 = QGroupBox(MainWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lev1Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3 = QButtonGroup(MainWidget)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.lev1Button)
        self.lev1Button.setObjectName(u"lev1Button")
        self.lev1Button.setCheckable(True)
        self.lev1Button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.lev1Button)

        self.lev25Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev25Button)
        self.lev25Button.setObjectName(u"lev25Button")
        self.lev25Button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.lev25Button)

        self.lev35Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev35Button)
        self.lev35Button.setObjectName(u"lev35Button")
        self.lev35Button.setCheckable(True)
        self.lev35Button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.lev35Button)

        self.lev50Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev50Button)
        self.lev50Button.setObjectName(u"lev50Button")
        self.lev50Button.setCheckable(True)
        self.lev50Button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.lev50Button)

        self.lev75Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev75Button)
        self.lev75Button.setObjectName(u"lev75Button")
        self.lev75Button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.lev75Button)

        self.lev100Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev100Button)
        self.lev100Button.setObjectName(u"lev100Button")
        self.lev100Button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.lev100Button)

        self.lev125Button = QPushButton(self.groupBox_2)
        self.buttonGroup_3.addButton(self.lev125Button)
        self.lev125Button.setObjectName(u"lev125Button")
        self.lev125Button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.lev125Button)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox_4 = QGroupBox(MainWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pwEdit = QLineEdit(self.groupBox_4)
        self.pwEdit.setObjectName(u"pwEdit")
        self.pwEdit.setMinimumSize(QSize(0, 30))
        self.pwEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pwEdit, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.idEdit = QLineEdit(self.groupBox_4)
        self.idEdit.setObjectName(u"idEdit")
        self.idEdit.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.idEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 4, 1, 2, 1)

        self.groupBox_7 = QGroupBox(MainWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.amountSpin = QDoubleSpinBox(self.groupBox_7)
        self.amountSpin.setObjectName(u"amountSpin")
        self.amountSpin.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.amountSpin.setFont(font)
        self.amountSpin.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.amountSpin.setDecimals(5)
        self.amountSpin.setMinimum(0.000010000000000)
        self.amountSpin.setMaximum(999999.000000000000000)
        self.amountSpin.setSingleStep(0.000010000000000)
        self.amountSpin.setValue(0.000010000000000)

        self.horizontalLayout_4.addWidget(self.amountSpin)


        self.gridLayout_2.addWidget(self.groupBox_7, 3, 0, 1, 2)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"MainWidget", None))
        self.groupBox_6.setTitle("")
        self.startButton.setText(QCoreApplication.translate("MainWidget", u"Run", None))
        self.stopButton.setText(QCoreApplication.translate("MainWidget", u"Stop", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWidget", u"Seed Position", None))
        self.seed10Button.setText(QCoreApplication.translate("MainWidget", u"10%", None))
        self.seed25Button.setText(QCoreApplication.translate("MainWidget", u"25%", None))
        self.seed50Button.setText(QCoreApplication.translate("MainWidget", u"50%", None))
        self.seed75Button.setText(QCoreApplication.translate("MainWidget", u"75%", None))
        self.seed100Button.setText(QCoreApplication.translate("MainWidget", u"100%", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWidget", u"Status", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWidget", u"\uc815\uc9c0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWidget", u"Position", None))
        self.inposButton.setText(QCoreApplication.translate("MainWidget", u"IN", None))
        self.noposButton.setText(QCoreApplication.translate("MainWidget", u"NO", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWidget", u"Leverage", None))
        self.lev1Button.setText(QCoreApplication.translate("MainWidget", u"x1", None))
        self.lev25Button.setText(QCoreApplication.translate("MainWidget", u"x25", None))
        self.lev35Button.setText(QCoreApplication.translate("MainWidget", u"x35", None))
        self.lev50Button.setText(QCoreApplication.translate("MainWidget", u"x50", None))
        self.lev75Button.setText(QCoreApplication.translate("MainWidget", u"x75", None))
        self.lev100Button.setText(QCoreApplication.translate("MainWidget", u"x100", None))
        self.lev125Button.setText(QCoreApplication.translate("MainWidget", u"x125", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWidget", u"Login Info", None))
        self.pwEdit.setText(QCoreApplication.translate("MainWidget", u"test1234", None))
        self.label.setText(QCoreApplication.translate("MainWidget", u"ID", None))
        self.idEdit.setText(QCoreApplication.translate("MainWidget", u"sun107ksj.g@gmail.com", None))
        self.label_2.setText(QCoreApplication.translate("MainWidget", u"PW", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWidget", u"Amount", None))
        self.amountSpin.setPrefix("")
        self.amountSpin.setSuffix(QCoreApplication.translate("MainWidget", u" BTC", None))
    # retranslateUi

