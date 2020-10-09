#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:57:00 2020

@author: trabdlkarim
"""

import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import  QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

from vocebrowser.browser import VoceBrowser
from vocebrowser.schemes import VoceUrlSchemeHandler, ResourceUrlSchemeHandler

def main(argv=sys.argv):

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling

    VoceUrlSchemeHandler.registerVoceUrlScheme()
    ResourceUrlSchemeHandler.registerVoceUrlScheme()

    app = QtWidgets.QApplication(argv)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    QtCore.QCoreApplication.setOrganizationName('Voce Browser Fundation')
    QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

    app.setApplicationName(VoceBrowser.appName)
    browser = VoceBrowser()

    voceUrlSchemeHandler = VoceUrlSchemeHandler()
    resourceUrlSchemeHandler = ResourceUrlSchemeHandler()

    QWebEngineProfile.defaultProfile().installUrlSchemeHandler(VoceUrlSchemeHandler.schemeName, voceUrlSchemeHandler)
    QWebEngineProfile.defaultProfile().installUrlSchemeHandler(ResourceUrlSchemeHandler.schemeName, resourceUrlSchemeHandler)


    browser.launch()

    return sys.exit(app.exec())


if __name__ == "__main__":
    main()
