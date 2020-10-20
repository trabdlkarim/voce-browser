#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sept  22 14:41:31 2020

@author: trabdlkarim
"""

import os

from PyQt5.QtWebEngineCore import QWebEngineUrlSchemeHandler, QWebEngineUrlScheme, QWebEngineUrlRequestJob
from PyQt5.QtCore import QUrl, QFile, QIODevice, QByteArray

import vocebrowser

class VoceUrlSchemeHandler(QWebEngineUrlSchemeHandler):

    schemeName = QByteArray().append("voce")
    origin = QUrl("voce:")
    GET = QByteArray().append("GET")
    POST = QByteArray().append("POST")
    homeUrl = QUrl("voce://welcome")
    newtabUrl = QUrl("voce://newtab")
    settingsUrl = QUrl("voce://settings")
    bookmarksUrl = QUrl("voce://bookmarks")
    downloadsUrl = QUrl("voce://downloads")
    historyUrl = QUrl("voce://history")
    versionUrl = QUrl("voce://version")
    aboutUrl = QUrl("voce://about")

    def __init__(self,parent=None):
        super(VoceUrlSchemeHandler, self).__init__(parent)

    @classmethod
    def registerVoceUrlScheme(cls):
        voceUrlScheme = QWebEngineUrlScheme(cls.schemeName)
        voceUrlScheme.setFlags(QWebEngineUrlScheme.SecureScheme |
                               QWebEngineUrlScheme.LocalScheme |
                               QWebEngineUrlScheme.LocalAccessAllowed)
        QWebEngineUrlScheme.registerScheme(voceUrlScheme);


    def requestStarted(self, request):
        method = request.requestMethod()
        url = request.requestUrl()
        initiator = request.initiator()

        if method == self.GET and url.host() == self.homeUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'welcome.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.newtabUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'newtab/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.settingsUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'settings/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.downloadsUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'downloads/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.historyUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'history/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.bookmarksUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'bookmarks/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.versionUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'version/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        elif method == self.GET and url.host() == self.aboutUrl.host():
            file = QFile(os.path.join(vocebrowser.LOCAL_HTML_DIR,'about/index.html'), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/html", file)

        else:
            request.fail(QWebEngineUrlRequestJob.UrlNotFound)




class ResourceUrlSchemeHandler(QWebEngineUrlSchemeHandler):
    schemeName = QByteArray().append("voce-resources")
    origin = QUrl("voce-resources:")
    GET = QByteArray().append("GET")
    POST = QByteArray().append("POST")

    cssUrl = QUrl("voce-resources://css")
    jsUrl = QUrl("voce-resources://js")
    fontsUrl = QUrl("voce-resources://fonts")
    imagesUrl = QUrl("voce-resources://img")
    vendorsUrl = QUrl("voce-resources://vendors")
    globalUrl = QUrl("voce-resources://global")


    def __init__(self,parent=None):
        super(ResourceUrlSchemeHandler, self).__init__(parent)
        self.rsrc_dir = os.path.join(vocebrowser.LOCAL_HTML_DIR,"resources")

    @classmethod
    def registerVoceUrlScheme(cls):
        voceUrlScheme = QWebEngineUrlScheme(cls.schemeName)
        voceUrlScheme.setFlags(QWebEngineUrlScheme.SecureScheme |
                               QWebEngineUrlScheme.LocalScheme |
                               QWebEngineUrlScheme.LocalAccessAllowed)
        QWebEngineUrlScheme.registerScheme(voceUrlScheme);


    def getRelativePath(self,path):
        if not path:
            return None
        elif len(path) == 1:
            if path == '/':
                return None
            else:
                return path
        elif path[0] == '/':
            return path[1:]
        else:
            return path

    def requestStarted(self, request):
        url = request.requestUrl()
        relativePath  = self.getRelativePath(url.path())
        host = url.host()

        if host == self.cssUrl.host() and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,host,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/css", file)

        elif host == self.jsUrl.host() and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,host,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"text/javascript", file)

        elif host == self.imagesUrl.host()  and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,host,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"", file)

        elif host == self.fontsUrl.host()  and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,host,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"", file)

        elif host == self.globalUrl.host()  and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"", file)

        elif host == self.vendorsUrl.host()  and relativePath != None:
            file = QFile(os.path.join(self.rsrc_dir,host,relativePath), request)
            file.open(QIODevice.ReadOnly)
            request.reply(b"",file)

        else:
            request.fail(QWebEngineUrlRequestJob.UrlNotFound)