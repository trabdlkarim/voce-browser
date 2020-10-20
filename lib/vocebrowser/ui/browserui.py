# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/browser.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
import vocebrowser

class UrlBar(QtWidgets.QLineEdit):
    def selectAll(self):
        super().selectAll()
        self.setFocus()



class BrowserUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"vocebrowser.png")),
                                     QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")

        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.urlbar = UrlBar(self.centralwidget)
        self.urlbar.setObjectName("urlbar")
        self.urlbar.setMinimumSize(QtCore.QSize(542, 30))
        self.urlbar.setClearButtonEnabled(True)
        self.horizontalLayout.addWidget(self.urlbar)
        QtWidgets.QShortcut("Ctrl+L", MainWindow, activated=self.urlbar.selectAll)

        self.goButton = QtWidgets.QPushButton(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())

        self.goButton.setSizePolicy(sizePolicy)
        self.goButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goButton.setAutoDefault(True)
        self.goButton.setDefault(True)
        self.goButton.setFlat(False)
        self.goButton.setMinimumSize(QtCore.QSize(80, 30))
        self.goButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.goButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")


        self.verticalLayout.addWidget(self.tabWidget)
        self.mainVerticalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.navigationToolBar = QtWidgets.QToolBar(MainWindow)
        self.navigationToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.navigationToolBar.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.navigationToolBar.setMovable(False)
        self.navigationToolBar.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.navigationToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.navigationToolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.navigationToolBar.setFloatable(False)
        self.navigationToolBar.setObjectName("navigationToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.navigationToolBar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 822, 22))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuWindow = QtWidgets.QMenu(self.menuBar)
        self.menuWindow.setObjectName("menuWindow")

        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")

        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuCommands = QtWidgets.QMenu(self.menuBar)
        self.menuCommands.setObjectName("menuCommands")

        MainWindow.setMenuBar(self.menuBar)

        self.actionUrlSelected = QtWidgets.QAction(self.urlbar)
        self.actionUrlSelected.setObjectName("actionUrlSelected")

        self.actionBack = QtWidgets.QAction(MainWindow)
        backIcon = QtGui.QIcon()
        backIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"previous.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(backIcon)
        self.actionBack.setObjectName("actionBack")

        self.actionForward = QtWidgets.QAction(MainWindow)
        forwardIcon = QtGui.QIcon()
        forwardIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(forwardIcon)
        self.actionForward.setObjectName("actionForward")

        self.actionReload = QtWidgets.QAction(MainWindow)
        reloadIcon = QtGui.QIcon()
        reloadIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"refresh.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReload.setIcon(reloadIcon)
        self.actionReload.setObjectName("actionReload")

        self.actionHome = QtWidgets.QAction(MainWindow)
        homeIcon = QtGui.QIcon()
        homeIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"flat-home.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(homeIcon)
        self.actionHome.setObjectName("actionHome")

        self.actionNewTab = QtWidgets.QAction(MainWindow)
        newTabIcon = QtGui.QIcon()
        newTabIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"tab-new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewTab.setIcon(newTabIcon)
        self.actionNewTab.setObjectName("actionNewTab")

        self.actionNewWindow = QtWidgets.QAction(MainWindow)
        newWinIcon = QtGui.QIcon()
        newWinIcon.addPixmap(QtGui.QPixmap(os.path.join(vocebrowser.QRC_ICON_DIR,"window-new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewWindow.setIcon(newWinIcon)
        self.actionNewWindow.setObjectName("actionNewWindow")

        self.actionIncognitoWindow = QtWidgets.QAction(MainWindow)
        self.actionIncognitoWindow.setObjectName("actionIncognitoWindow")

        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")

        self.actionDownloads = QtWidgets.QAction(MainWindow)
        self.actionDownloads.setObjectName("actionDownloads")

        self.actionBookmarks = QtWidgets.QAction(MainWindow)
        self.actionBookmarks.setObjectName("actionBookmarks")

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.actionAboutVoce = QtWidgets.QAction(MainWindow)
        self.actionAboutVoce.setObjectName("actionAboutVoce")

        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")

        self.actionAboutPlugins = QtWidgets.QAction(MainWindow)
        self.actionAboutPlugins.setObjectName("actionAboutPlugins")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.navigationToolBar.addAction(self.actionBack)
        self.navigationToolBar.addAction(self.actionForward)
        self.navigationToolBar.addAction(self.actionReload)
        self.navigationToolBar.addAction(self.actionHome)
        self.navigationToolBar.addSeparator()
        self.navigationToolBar.addAction(self.actionNewTab)
        self.navigationToolBar.addAction(self.actionNewWindow)

        self.menuFile.addAction(self.actionIncognitoWindow)
        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addAction(self.actionDownloads)
        self.menuFile.addAction(self.actionBookmarks)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)

        self.menuHelp.addAction(self.actionAboutVoce)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAboutPlugins)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCommands.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voce Browser"))
        self.urlbar.setPlaceholderText(_translate("MainWindow", "Search DuckDuckGo or type a URL"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.navigationToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "Browser"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCommands.setTitle(_translate("MainWindow", "Commands"))

        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionNewTab.setText(_translate("MainWindow", "New tab"))
        self.actionNewTab.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionNewWindow.setText(_translate("MainWindow", "New window"))
        self.actionNewWindow.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.actionIncognitoWindow.setText(_translate("MainWindow", "Incognito"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionDownloads.setText(_translate("MainWindow", "Downloads"))
        self.actionBookmarks.setText(_translate("MainWindow", "Bookmarks"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

        self.actionAboutVoce.setText(_translate("MainWindow", "About Voce"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAboutPlugins.setText(_translate("MainWindow", "About Plugins"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
