# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# InfoTools
# Copyright (C) 2014  Giovanni Allegri
# EMAIL: giovanni.allegri (at) gmail.com
# WEB  : https://github.com/giohappy/infotools
#
# A collection of tools to grab utiliy informations from maps
#
#-----------------------------------------------------------
from PyQt4.QtCore import QObject,SIGNAL,Qt
from PyQt4.QtGui import QMainWindow,QDesktopServices
from qgis.core import *
from ..tools.rect import RectInfoTool
from ..tools.point import PointInfoTool
from .mainwindow import Ui_MainWindow
from .about import aboutText

class InfoDialog(QMainWindow,Ui_MainWindow):
    def __init__(self,iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        super(InfoDialog, self).__init__(self.canvas)
        self.setupUi(self)
        self.actionRect.triggered.connect(self.runRectTool)
        self.actionPoint.triggered.connect(self.runPointTool)
        self.actionAbout.triggered.connect(self.showAbout)
        self.textarea.setOpenLinks(False)
        self.textarea.anchorClicked.connect(self.openLink)
        
    def runRectTool(self):
        self.tool = RectInfoTool(self)
        self.tool.run()
        
    def runPointTool(self):
        self.tool = PointInfoTool(self)
        self.tool.run()
        
    def showAbout(self):
        self.textarea.setHtml(aboutText)
        
    def openLink(self,url):
        QDesktopServices.openUrl(url)
        
    def closeEvent(self, event):
        self.tool = None
        event.accept()
        
    def setResult(self,text):
        self.textarea.setHtml(text)
        
    def hideme(self):
        self.showMinimized()
        
    def showme(self):
        if self.windowState() != Qt.WindowMaximized:
            self.showMaximized()
            self.showNormal()
        else:
            self.showNormal()
            self.showMaximized()
        