#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:09:34 2020

@author: trabdlkarim
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl, QObject, QFile, QIODevice
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage, QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

import vocebrowser
from vocebrowser.ui.browserui import BrowserUi
from vocebrowser.ui.devtoolsui import DevToolsUi
from vocebrowser.assistant.voce import VoceAssistant, AssistantRunnable


class WebView(QWebEngineView):

    devToolsRequested = QtCore.pyqtSignal(QWebEnginePage)

    def __init__(self, parent=None):
        self.parent = parent
        super(WebView,self).__init__(parent)

    def contextMenuEvent(self, event):
        menu  = self.page().createStandardContextMenu()
        actions = menu.actions()
        inspectElement =  self.page().action(QWebEnginePage.InspectElement)
        if inspectElement not in actions:
            action = QtWidgets.QAction()
            action.setText("Inspect element")
            action.triggered.connect(lambda: self.devToolsRequested.emit(self.page()) )
            menu.addAction(action)
        menu.exec_(event.globalPos())

    def createWindow(self, winType):
        if winType == QWebEnginePage.WebBrowserTab:
           return self.parent.open_new_tab()
        elif winType == QWebEnginePage.WebBrowserWindow:
            return self.parent.parent.create_browser_window()

    def reload(self):
        super().reload()
        self.parent.update_address_bar(self.page().url(),self)



class WebPage(QWebEnginePage):
    pass


class DevToolsWindow(QtWidgets.QMainWindow):
    def __init__(self,parent,*args, **kwargs):
        self.parent = parent
        super(DevToolsWindow, self).__init__(*args, **kwargs)
        self.ui = DevToolsUi()
        self.ui.setupUi(self)

    def getDevToolsView(self):
        return self.ui.devToolsWebView

    def update_win_title(self,url):
        self.setWindowTitle("DevTools - " + url.toString())

    def closeEvent(self, event):
        self.parent.devToolsView.page().setInspectedPage(None)
        event.accept()
        self.deleteLater()

class BrowserWindow(QtWidgets.QMainWindow):

    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        super(BrowserWindow, self).__init__(*args, **kwargs)

        self.ui = BrowserUi()
        self.ui.setupUi(self)

        self.ui.urlbar.returnPressed.connect(self.goto_current_url)
        self.ui.goButton.clicked.connect(self.goto_current_url)

        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionIncognitoWindow.triggered.connect(lambda offMode =True: self.parent.create_browser_window(offRecord=offMode))
        self.ui.actionHistory.triggered.connect(lambda _, qurl=VoceBrowser.history_url : self.open_new_tab(url=qurl))
        self.ui.actionDownloads.triggered.connect(lambda _, qurl=VoceBrowser.downloads_url : self.open_new_tab(url=qurl))
        self.ui.actionBookmarks.triggered.connect(lambda  _, qurl=VoceBrowser.bookmarks_url : self.open_new_tab(url=qurl))
        self.ui.actionSettings.triggered.connect(lambda  _, qurl=VoceBrowser.settings_url : self.open_new_tab(url=qurl))

        self.ui.actionNewWindow.triggered.connect(self.parent.create_browser_window)
        self.ui.actionNewTab.triggered.connect(self.open_new_tab)

        self.ui.actionBack.triggered.connect(lambda:self.ui.tabWidget.currentWidget().back())
        self.ui.actionForward.triggered.connect(lambda:self.ui.tabWidget.currentWidget().forward())
        self.ui.actionReload.triggered.connect(lambda:self.ui.tabWidget.currentWidget().reload())
        self.ui.actionHome.triggered.connect(self.go_home)


        self.ui.tabWidget.currentChanged.connect(self.onchange_current_tab)
        self.ui.tabWidget.tabCloseRequested.connect(self.onclose_tab)

        self.setCentralWidget(self.ui.centralwidget)

        self.parent.assistant.signals.search.connect(self.search)
        self.parent.assistant.signals.openNewTab.connect(self.open_new_tab)
        self.parent.assistant.signals.closeCurrentTab.connect(lambda: self.onclose_tab(self.ui.tabWidget.currentIndex()))
        self.parent.assistant.signals.openNewWindow.connect(self.parent.create_browser_window)
        self.parent.assistant.signals.closeCurrentWindow.connect(self.close)


    def readFile(self,filename):
        file = QFile(filename)
        file.open(QIODevice.ReadOnly)
        barray = file.readAll()
        file.close()
        return barray


    def open_new_tab(self,url=None, title="New Tab"):
        webView = WebView(self)
        profile = QWebEngineProfile.defaultProfile()
        webPage = WebPage(profile, self)
        webView.setPage(webPage)

        if not url:
            url = VoceBrowser.newtab_url

        elif type(url) == str:
            url = QUrl(url)

        webView.page().setUrl(url)
        webView.setFocus()

        index = self.ui.tabWidget.addTab(webView, title)
        self.ui.tabWidget.setCurrentIndex(index)
        webView.urlChanged.connect(lambda qurl, view = webView: self.update_address_bar(qurl, view))
        webView.titleChanged.connect(lambda title, i = index,view=webView:self.update_tab_title(title,i,view))
        webView.iconChanged.connect(lambda icon,i=index:self.update_favIcon(icon,i))
        webView.devToolsRequested.connect(self.parent.create_devtools_window)

        webView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        webView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        webView.settings().setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
        webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        webView.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        webView.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)

        return webView


    def update_favIcon(self,icon, tabIndex):
        self.ui.tabWidget.setTabIcon(tabIndex,icon)

    def update_tab_title(self, title, tabIndex,webView):
        self.update_browser_title(title,webView)
        self.ui.tabWidget.setTabText(tabIndex, title)

    def onchange_current_tab(self, i):
        qurl = self.ui.tabWidget.currentWidget().url()
        self.update_address_bar(qurl, self.ui.tabWidget.currentWidget())
        title = self.ui.tabWidget.tabText(i)
        self.update_browser_title(title,self.ui.tabWidget.currentWidget())

    def onclose_tab(self, i):
        if self.ui.tabWidget.count() < 2:
            self.close()
        else:
            self.ui.tabWidget.removeTab(i)

    def update_address_bar(self, new_url, view=None):
        if view != self.ui.tabWidget.currentWidget():
            return
        if view.page().url() == VoceBrowser.home_url or view.page().url() == VoceBrowser.newtab_url :
            self.ui.urlbar.clear()
        else:
            self.ui.urlbar.setText(new_url.toString())


    def update_browser_title(self,title="Untitled", view=None):
        if view != self.ui.tabWidget.currentWidget():
            return
        self.setWindowTitle("%s - %s" % (title,self.parent.appName))

    def go_home(self):
        self.ui.tabWidget.currentWidget().page().setUrl(VoceBrowser.home_url)
        self.update_address_bar(VoceBrowser.home_url,self.ui.tabWidget.currentWidget())

    def goto_current_url(self):
        current_url = QUrl.fromUserInput(self.ui.urlbar.text())

        if current_url.isValid():
            if (current_url.scheme() not in  ["voce","voce-resources"]) and ('.' not in self.ui.urlbar.text()):
                current_url = self.create_search_query(self.parent.search_engine,self.ui.urlbar.text())
        else:
            current_url = self.create_search_query(self.parent.search_engine,self.ui.urlbar.text())

        if current_url:
            self.ui.tabWidget.currentWidget().page().setUrl(current_url)
            self.update_address_bar(current_url,self.ui.tabWidget.currentWidget())

    def create_search_query(self,engine,keywords):
        query = engine + "?q="
        words = keywords.split()
        if not words:
            return None
        count = len(words)
        for w in words:
            if count>1:
                query += w + '+'
            else:
                query += w
            count -= 1
        return QUrl(query)

    def search(self,keywords):
        query = self.create_search_query(self.parent.search_engine,keywords)
        self.open_new_tab(url=query)


    def showDevToolsPage(self,page):
        devToolsView = QWebEngineView()
        page.setDevToolsPage(devToolsView.page()) # same as devToolsView.page().setInspectedPage(page)
        i = self.ui.tabWidget.addTab(devToolsView, page.title())
        self.ui.tabWidget.setCurrentIndex(i)

    def closeEvent(self, event):
        if self.parent.windows < 2:
            answer = QMessageBox.question(self,
                                          "Quit", "Are you sure you want to close this window?",
                                          QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.Yes:
                self.parent.stop_assistant()
                event.accept()
                self.deleteLater()
            else:
                event.ignore()
        else:
            event.accept()
            self.parent.windows -= 1



class VoceBrowser(QObject):
    home_url = QUrl('voce://welcome')
    newtab_url = QUrl('voce://newtab')
    history_url = QUrl('voce://history')
    downloads_url = QUrl('voce://downloads')
    settings_url = QUrl('voce://settings')
    bookmarks_url = QUrl('voce://bookmarks')

    def __init__(self):
        super().__init__()
        self.appName = "Voce Browser"
        self.search_engine ="https://duckduckgo.com/"
        self.profile = QWebEngineProfile()
        self.assistant = VoceAssistant()
        self.windows = 0
        self.downloadManager = None



    def create_browser_window(self,url=None, offRecord=False):
        window = BrowserWindow(self)
        self.windows += 1
        webView = window.open_new_tab(url)
        window.show()
        return webView

    def create_devtools_window(self,page):
        self.devToolsWin = DevToolsWindow(self)
        self.devToolsView = self.devToolsWin.getDevToolsView()
        profile = QWebEngineProfile.defaultProfile()
        webPage = WebPage(profile, self)
        self.devToolsView.setPage(webPage)
        page.setDevToolsPage(self.devToolsView.page())
        self.windows += 1
        self.devToolsView.page().inspectedPage().urlChanged.connect(self.devToolsWin.update_win_title)
        self.devToolsWin.update_win_title(page.url())
        self.devToolsWin.show()

    def get_download_manager(self):
        pass

    def launch(self):
        self.create_browser_window(VoceBrowser.home_url)
        self.run_assistant()


    def run_assistant(self):
        if  not self.assistant.isRunning:
            assistant_process = AssistantRunnable(self.assistant.run_forever)
            assistant_process.start()
            self.assistant.isRunning = True

    def stop_assistant(self):
        if  self.assistant.isRunning:
            self.assistant.stop_event.set()
            self.assistant.isRunning = False


class DownloadManger(QObject):
    def downloadRequestHandler(self, downloadItem):
        qurl, path = QtWidgets.QFileDialog.getSaveFileName(
            self,"Save as",
            QtCore.QDir(downloadItem.downloadDirectory()).filePath(downloadItem.downloadFileName()))

        if not path:
            return

        downloadItem.setDownloadDirectory(QtCore.QFileInfo(path).path())
        downloadItem.setDownloadFileName(QtCore.QFileInfo(path).fileName())
        downloadItem.accept()


class DownloadWidget(QtWidgets.QWidget):
    def __init__(self,downloadItem,parent):
        pass
