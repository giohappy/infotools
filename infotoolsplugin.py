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
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui.mainDialog import InfoDialog

class InfoToolsPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
        self.action1 = QAction(QIcon(QPixmap(":/infotools/info")),"&Info Tools", self.iface.mainWindow())
        QObject.connect(self.action1, SIGNAL("triggered()"), self.runapp)
        self.iface.addToolBarIcon(self.action1)
        self.iface.addPluginToMenu("Info Tools", self.action1)

    def unload(self):
        self.iface.removePluginMenu("Info Tools",self.action1)
        self.iface.removeToolBarIcon(self.action1)
        if self.dialog:
            self.dialog.unLoad()
            self.dialog.close()
            self.dialog = None

    def runapp(self):
        if not self.dialog:
            self.dialog = InfoDialog(self.iface)
            self.dialog.show()
