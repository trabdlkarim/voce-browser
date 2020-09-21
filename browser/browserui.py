# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/browser.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage

class BrowserUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(822, 695)
        MainWindow.setMinimumSize(QtCore.QSize(650, 450))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.urlbar = QtWidgets.QLineEdit(self.centralwidget)
        self.urlbar.setObjectName("urlbar")
        self.urlbar.setMinimumSize(QtCore.QSize(542, 30))
        self.horizontalLayout.addWidget(self.urlbar)

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

        #self.tab = QtWidgets.QWidget()
        #self.tab.setObjectName("tab")
        #self.tabWidget.addTab(self.tab, "")

        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.navigationToolBar = QtWidgets.QToolBar(MainWindow)
        self.navigationToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.navigationToolBar.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.navigationToolBar.setMovable(False)
        self.navigationToolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.navigationToolBar.setFloatable(False)
        self.navigationToolBar.setObjectName("navigationToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.navigationToolBar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 822, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuCommands = QtWidgets.QMenu(self.menuBar)
        self.menuCommands.setObjectName("menuCommands")
        MainWindow.setMenuBar(self.menuBar)

        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")

        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName("actionBack")

        self.actionForward = QtWidgets.QAction(MainWindow)
        self.actionForward.setObjectName("actionForward")

        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")

        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")

        self.actionNewTab = QtWidgets.QAction(MainWindow)
        self.actionNewTab.setObjectName("actionNewTab")

        self.actionNew_window = QtWidgets.QAction(MainWindow)
        self.actionNew_window.setObjectName("actionNew_window")

        self.actionIncognito_window = QtWidgets.QAction(MainWindow)
        self.actionIncognito_window.setObjectName("actionIncognito_window")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionDownloads = QtWidgets.QAction(MainWindow)
        self.actionDownloads.setObjectName("actionDownloads")
        self.actionBookmarks = QtWidgets.QAction(MainWindow)
        self.actionBookmarks.setObjectName("actionBookmarks")
        self.actionAbout_Voce = QtWidgets.QAction(MainWindow)
        self.actionAbout_Voce.setObjectName("actionAbout_Voce")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout_Plugins = QtWidgets.QAction(MainWindow)
        self.actionAbout_Plugins.setObjectName("actionAbout_Plugins")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.navigationToolBar.addAction(self.actionBack)
        self.navigationToolBar.addAction(self.actionForward)
        self.navigationToolBar.addAction(self.actionReload)
        self.navigationToolBar.addAction(self.actionHome)
        self.navigationToolBar.addSeparator()
        self.navigationToolBar.addAction(self.actionNewTab)
        self.navigationToolBar.addAction(self.actionNew_window)
        self.menuFile.addAction(self.actionIncognito_window)

        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addAction(self.actionDownloads)
        self.menuFile.addAction(self.actionBookmarks)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_Voce)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout_Plugins)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCommands.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voce Browser"))
        self.urlbar.setPlaceholderText(_translate("MainWindow", "http://"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.navigationToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "Browser"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCommands.setTitle(_translate("MainWindow", "Commands"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionNewTab.setText(_translate("MainWindow", "New tab"))
        self.actionNew_window.setText(_translate("MainWindow", "New window"))
        self.actionIncognito_window.setText(_translate("MainWindow", "Incognito Mode"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionDownloads.setText(_translate("MainWindow", "Downloads"))
        self.actionBookmarks.setText(_translate("MainWindow", "Bookmarks"))
        self.actionAbout_Voce.setText(_translate("MainWindow", "About Voce"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout_Plugins.setText(_translate("MainWindow", "About Plugins"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
