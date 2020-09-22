#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:09:34 2020

@author: trabdlkarim
"""

import sys
from PyQt5 import Qt
from browserui import BrowserUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage, QWebEngineSettings


class VoceBrowser(QtWidgets.QMainWindow):
    def __init__(self, parent=None,*args,**kwargs):
        super(VoceBrowser, self).__init__(*args, **kwargs)

        QtWidgets.QWidget.__init__(self, parent)
        QWebEngineView.__init__(self)

        self.home_url = QUrl('https://duckduckgo.com/')
        self.appName = "Voce Browser"

        self.ui = BrowserUi()
        self.ui.setupUi(self)

        self.ui.urlbar.returnPressed.connect(self.goto_current_url)
        self.ui.goButton.clicked.connect(self.goto_current_url)

        self.ui.actionNewTab.triggered.connect(self.open_new_tab)
        self.ui.actionBack.triggered.connect(lambda:self.ui.tabWidget.currentWidget().back())
        self.ui.actionForward.triggered.connect(lambda:self.ui.tabWidget.currentWidget().forward())
        self.ui.actionReload.triggered.connect(lambda:self.ui.tabWidget.currentWidget().reload())
        self.ui.actionHome.triggered.connect(self.go_home)

        self.ui.tabWidget.currentChanged.connect(self.onchange_current_tab)
        self.ui.tabWidget.tabCloseRequested.connect(self.onclose_tab)

        self.setCentralWidget(self.ui.centralwidget)
        self.open_new_tab(self.home_url, 'Welcome page')


    def open_new_tab(self,url=None,title="New tab"):
        if not url:
            url = QUrl("about:blank")
        webView = QWebEngineView()
        webView.setUrl(url)
        webView.setFocus()
        index = self.ui.tabWidget.addTab(webView, title)
        self.ui.tabWidget.setCurrentIndex(index)
        webView.urlChanged.connect(lambda qurl, view = webView: self.update_address_bar(qurl, view))
        webView.loadFinished.connect(lambda _, i = index, view = webView:self.update_tab_title(i, view))
        webView.iconChanged.connect(lambda _,i=index,view=webView:self.update_favIcon(i,view))

    def update_favIcon(self,tabIndex,webView):
        self.ui.tabWidget.setTabIcon(tabIndex, webView.icon())


    def update_tab_title(self, tabIndex, webView):
        title = webView.page().title()
        self.ui.tabWidget.setTabText(tabIndex, title)
        self.setWindowTitle("%s - %s" % (title,self.appName))

    def onchange_current_tab(self, i):
        qurl = self.ui.tabWidget.currentWidget().url()
        self.update_address_bar(qurl, self.ui.tabWidget.currentWidget())
        self.update_browser_title(self.ui.tabWidget.currentWidget())

    def onclose_tab(self, i):
        if self.ui.tabWidget.count() < 2:
            return
        self.ui.tabWidget.removeTab(i)

    def onclick_new_tab(self,i):
        if i == -1:
            self.open_new_tab()
            self.update_browser_title(self.ui.tabWidget.currentWidget())

    def update_address_bar(self, new_url, view=None):
        if view != self.ui.tabWidget.currentWidget():
            return
        self.ui.urlbar.setText(new_url.toString())
        self.ui.urlbar.setCursorPosition(0)

    def update_browser_title(self, view):
        if view != self.ui.tabWidget.currentWidget():
            return
        title = self.ui.tabWidget.currentWidget().page().title()
        self.setWindowTitle("%s - %s" % (title,self.appName))

    def go_home(self):
        self.ui.tabWidget.currentWidget().setUrl(self.home_url)

    def goto_current_url(self):
        current_url = QUrl.fromUserInput(self.ui.urlbar.text())
        if current_url.isValid():
            if not '.' in self.ui.urlbar.text():
                current_url = self.create_search_query("https://duckduckgo.com",self.ui.urlbar.text())
        else:
            current_url = self.create_search_query("https://duckduckgo.com",self.ui.urlbar.text())

        self.ui.tabWidget.currentWidget().setUrl(current_url)

    def create_search_query(self,engine,keywords):
        query = engine + "?q="
        words = keywords.split()
        count = len(words)
        for w in words:
            if count>1:
                query += w + '+'
            else:
                query += w
            count -= 1
        return QUrl(query)




def main(argv):

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

    app = QtWidgets.QApplication(argv)
    app.setOrganizationName("Voce Browser Fundation")
    QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
    browser = VoceBrowser()
    app.setApplicationName(browser.appName)

    browser.show()
    sys.exit(app.exec_())

