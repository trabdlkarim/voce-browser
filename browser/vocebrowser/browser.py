#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:09:34 2020

@author: trabdlkarim
"""

import sys

from browserui import BrowserUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage, QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

class WebView(QWebEngineView):
    def __init__(self,parent=None):
        self.parent = parent
        super(WebView,self).__init__(parent)

    def createWindow(self, winType):
        if winType == QWebEnginePage.WebBrowserTab:
           return self.parent.open_new_tab()
        elif winType == QWebEnginePage.WebBrowserWindow:
            return VoceBrowser.create_browser_window()



class BrowserWindow(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(BrowserWindow, self).__init__(*args, **kwargs)

        self.home_url = QUrl('https://duckduckgo.com/')
        self.appName = "Voce Browser"

        self.profile = QWebEngineProfile(self)

        self.ui = BrowserUi()
        self.ui.setupUi(self)

        self.ui.urlbar.returnPressed.connect(self.goto_current_url)
        self.ui.goButton.clicked.connect(self.goto_current_url)
        self.ui.actionNewWindow.triggered.connect(VoceBrowser.create_browser_window)
        self.ui.actionNewTab.triggered.connect(self.open_new_tab)
        self.ui.actionBack.triggered.connect(lambda:self.ui.tabWidget.currentWidget().back())
        self.ui.actionForward.triggered.connect(lambda:self.ui.tabWidget.currentWidget().forward())
        self.ui.actionReload.triggered.connect(lambda:self.ui.tabWidget.currentWidget().reload())
        self.ui.actionHome.triggered.connect(self.go_home)
        self.ui.actionUrlSelected.triggered.connect(self.ui.urlbar.selectAll)
        self.ui.tabWidget.currentChanged.connect(self.onchange_current_tab)
        self.ui.tabWidget.tabCloseRequested.connect(self.onclose_tab)

        self.setCentralWidget(self.ui.centralwidget)


    def open_new_tab(self,url=None, title="New Tab"):

        webView = WebView(self)
        if url:
             webView.setUrl(url)

        webPage = QWebEnginePage(self.profile,webView)
        webView.setPage(webPage)
        webView.setFocus()

        index = self.ui.tabWidget.addTab(webView, title)
        self.ui.tabWidget.setCurrentIndex(index)
        webView.urlChanged.connect(lambda qurl, view = webView: self.update_address_bar(qurl, view))
        webView.titleChanged.connect(lambda _, i = index, view = webView:self.update_tab_title(i, view))
        webView.iconChanged.connect(lambda _,i=index,view=webView:self.update_favIcon(i,view))

        return webView

    def update_favIcon(self,tabIndex,webView):
        self.ui.tabWidget.setTabIcon(tabIndex, webView.icon())

    def update_tab_title(self, tabIndex, webView):
        title = webView.page().title()
        self.setWindowTitle("%s | %s" % (title,self.appName))
        self.ui.tabWidget.setTabText(tabIndex, title)

    def onchange_current_tab(self, i):
        qurl = self.ui.tabWidget.currentWidget().url()
        self.update_address_bar(qurl, self.ui.tabWidget.currentWidget())
        self.update_browser_title(self.ui.tabWidget.currentWidget())

    def onclose_tab(self, i):
        if self.ui.tabWidget.count() < 2:
             return #QtWidgets.QApplication.quit()
        self.ui.tabWidget.removeTab(i)

    def onclick_new_tab(self,i):
        if i == -1:
            webView = self.open_new_tab()
            self.update_browser_title(webView)

    def update_address_bar(self, new_url, view=None):
        if view != self.ui.tabWidget.currentWidget():
            return
        self.ui.urlbar.setText(new_url.toString())
        #self.ui.urlbar.selectAll()

    def update_browser_title(self, view):
        if view != self.ui.tabWidget.currentWidget():
            return
        title = self.ui.tabWidget.currentWidget().page().title()
        if not title.strip():
            self.setWindowTitle(self.appName)
        else:
            self.setWindowTitle("%s | %s" % (title,self.appName))

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

    def closeEvent(self, event):
        answer = QMessageBox.question(self,"QUIT", "Are you sure want to stop process?",
                            QMessageBox.Yes | QMessageBox.No)

        if answer == QMessageBox.Yes:
            event.accept()
            self.deleteLater()
           # QtWidgets.QApplication.quit()

        else:
            event.ignore()


class VoceBrowser(object):
    home_url = QUrl('https://duckduckgo.com/')
    appName = "Voce Browser"

    @staticmethod
    def create_browser_window(url=None, offRecord=False):
        window = BrowserWindow()
        if not url :
            url = VoceBrowser.home_url
        webView = window.open_new_tab(url=url)
        window.show()
        return webView

    def launch(self):
        VoceBrowser.create_browser_window(VoceBrowser.home_url)

