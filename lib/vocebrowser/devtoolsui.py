# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/devtoolswin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import os
import vocebrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

class DevToolsUi(QObject):
    def setupUi(self, DevToolsWindow):
        DevToolsWindow.setObjectName("DevToolsWindow")
        DevToolsWindow.setMinimumSize(QtCore.QSize(600, 400))
        DevToolsWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"vocebrowser.png")),
                                     QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DevToolsWindow.setWindowIcon(icon)
        DevToolsWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(DevToolsWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")

        self.devToolsWebView = QWebEngineView(DevToolsWindow)

        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.mainVerticalLayout.addWidget(self.devToolsWebView)

        DevToolsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DevToolsWindow)
        QtCore.QMetaObject.connectSlotsByName(DevToolsWindow)

    def retranslateUi(self, DevToolsWindow):
        _translate = QtCore.QCoreApplication.translate
        DevToolsWindow.setWindowTitle(_translate("DevToolsWindow", "DevTools"))
