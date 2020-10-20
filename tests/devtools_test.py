#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:34:49 2020

@author: trabdlkarim
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView

class DevToolsUi(QObject):
    def setupUi(self, DevToolsWindow):
        DevToolsWindow.setObjectName("DevToolsWindow")
        DevToolsWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(DevToolsWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")

        self.devToolsWebView = QWebEngineView(DevToolsWindow)
        self.devToolsWebView.load(QUrl('https://google.com'))

        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.mainVerticalLayout.addWidget(self.devToolsWebView)

        DevToolsWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(DevToolsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        DevToolsWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(DevToolsWindow)
        self.statusbar.setObjectName("statusbar")
        DevToolsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DevToolsWindow)
        QtCore.QMetaObject.connectSlotsByName(DevToolsWindow)

    def retranslateUi(self, DevToolsWindow):
        _translate = QtCore.QCoreApplication.translate
        DevToolsWindow.setWindowTitle(_translate("DevToolsWindow", "DevTools"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    devToolsUi = DevToolsUi()
    devToolsUi.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())