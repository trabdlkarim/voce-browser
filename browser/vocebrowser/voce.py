#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:57:00 2020

@author: trabdlkarim
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
from PyQt5.QtWebEngineWidgets import  QWebEngineSettings
from vocebrowser.browser import VoceBrowser


class Voce(object):
      def __init__(self):
          pass

      def run(self,argv):
          pass

def main(argv=sys.argv):

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling

    app = QtWidgets.QApplication(argv)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    QtCore.QCoreApplication.setOrganizationName('Voce Browser Community')
    QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

    app.setApplicationName(VoceBrowser.appName)

    voce = VoceBrowser()
    voce.launch()


    return sys.exit(app.exec())

if __name__ == "__main__":
    main()
