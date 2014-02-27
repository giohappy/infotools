# -*- coding: utf-8 -*-
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
        self.action1 = QAction(QIcon(QPixmap(":/infotools/info")),"&Infotools", self.iface.mainWindow())
        QObject.connect(self.action1, SIGNAL("triggered()"), self.runapp)
        self.iface.addToolBarIcon(self.action1)
        self.iface.addPluginToMenu("Infotools", self.action1)

    def unload(self):
        self.iface.removePluginMenu("Infotools",self.action1)
        self.iface.removeToolBarIcon(self.action1)
        if self.dialog:
            self.dialog.unLoad()
            self.dialog.close()
            self.dialog = None

    def runapp(self):
        if not self.dialog:
            self.dialog = InfoDialog(self.iface)
            self.dialog.show()
