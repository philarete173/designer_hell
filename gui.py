# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(310, 205)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.bootomwidget = QWidget(self.centralwidget)
        self.bootomwidget.setObjectName(u"bootomwidget")
        self.bottomLayout = QVBoxLayout(self.bootomwidget)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.pushButton = QPushButton(self.bootomwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))
        self.pushButton.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        self.pushButton.setFont(font)

        self.bottomLayout.addWidget(self.pushButton)

        self.saveButton = QPushButton(self.bootomwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 25))
        self.saveButton.setMaximumSize(QSize(16777215, 25))
        self.saveButton.setFont(font)

        self.bottomLayout.addWidget(self.saveButton)


        self.gridLayout.addWidget(self.bootomwidget, 2, 0, 1, 1, Qt.AlignBottom)

        self.topwidget = QWidget(self.centralwidget)
        self.topwidget.setObjectName(u"topwidget")
        self.topLayout = QHBoxLayout(self.topwidget)
        self.topLayout.setObjectName(u"topLayout")
        self.recolorLayout = QVBoxLayout()
        self.recolorLayout.setObjectName(u"recolorLayout")
        self.lineEdit = QLineEdit(self.topwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)

        self.recolorLayout.addWidget(self.lineEdit)

        self.lineEdit2 = QLineEdit(self.topwidget)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setMinimumSize(QSize(0, 25))
        self.lineEdit2.setMaximumSize(QSize(16777215, 25))
        self.lineEdit2.setFont(font)
        self.lineEdit2.setAlignment(Qt.AlignCenter)
        self.lineEdit2.setReadOnly(True)

        self.recolorLayout.addWidget(self.lineEdit2)

        self.lineEdit3 = QLineEdit(self.topwidget)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setMinimumSize(QSize(0, 25))
        self.lineEdit3.setMaximumSize(QSize(16777215, 25))
        self.lineEdit3.setFont(font)
        self.lineEdit3.setAlignment(Qt.AlignCenter)
        self.lineEdit3.setReadOnly(True)

        self.recolorLayout.addWidget(self.lineEdit3)

        self.label = QLabel(self.topwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.recolorLayout.addWidget(self.label)


        self.topLayout.addLayout(self.recolorLayout)

        self.lockbuttonsLayout = QVBoxLayout()
        self.lockbuttonsLayout.setObjectName(u"lockbuttonsLayout")
        self.linelockButton = QToolButton(self.topwidget)
        self.lockbuttonGroup = QButtonGroup(MainWindow)
        self.lockbuttonGroup.setObjectName(u"lockbuttonGroup")
        self.lockbuttonGroup.addButton(self.linelockButton)
        self.linelockButton.setObjectName(u"linelockButton")
        self.linelockButton.setMinimumSize(QSize(25, 25))
        self.linelockButton.setMaximumSize(QSize(25, 25))
        self.linelockButton.setIconSize(QSize(16, 16))

        self.lockbuttonsLayout.addWidget(self.linelockButton)

        self.line2lockButton = QToolButton(self.topwidget)
        self.lockbuttonGroup.addButton(self.line2lockButton)
        self.line2lockButton.setObjectName(u"line2lockButton")
        self.line2lockButton.setMinimumSize(QSize(25, 25))
        self.line2lockButton.setMaximumSize(QSize(25, 25))

        self.lockbuttonsLayout.addWidget(self.line2lockButton)

        self.line3lockButton = QToolButton(self.topwidget)
        self.lockbuttonGroup.addButton(self.line3lockButton)
        self.line3lockButton.setObjectName(u"line3lockButton")
        self.line3lockButton.setMinimumSize(QSize(25, 25))
        self.line3lockButton.setMaximumSize(QSize(25, 25))

        self.lockbuttonsLayout.addWidget(self.line3lockButton)

        self.windowlockButton = QToolButton(self.topwidget)
        self.lockbuttonGroup.addButton(self.windowlockButton)
        self.windowlockButton.setObjectName(u"windowlockButton")
        self.windowlockButton.setMinimumSize(QSize(25, 25))
        self.windowlockButton.setMaximumSize(QSize(25, 25))

        self.lockbuttonsLayout.addWidget(self.windowlockButton)


        self.topLayout.addLayout(self.lockbuttonsLayout)


        self.gridLayout.addWidget(self.topwidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Designer Hell", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438 \u043c\u0435\u043d\u044f", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435 1", None))
        self.lineEdit2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435 2", None))
        self.lineEdit3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435 3", None))
        self.label.setText("")
        self.linelockButton.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.line2lockButton.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.line3lockButton.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.windowlockButton.setText(QCoreApplication.translate("MainWindow", u"U", None))
    # retranslateUi

