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
from PyQt4.QtGui import QMessageBox
from qgis.core import QGis,QgsMessageLog

zooms = range(0,21)
RADIUS_GOOGLE_EARTH = 6378137
res = lambda x:RADIUS_GOOGLE_EARTH*3.14*2/(256*(2**x))
RESOLUTIONS = [res(z) for z in zooms]

UNITS = {
   0 : 'meters',
   1 : 'feet',
   2 : 'deegrees',
   3 : 'unknown',
   4 : 'decimal deegrees',
   5 : 'degrees minutes seconds',
   6 : 'deegrees decimal minutes',
   7 : 'nautical miles'
}

def log(msg):
    logger = QgsMessageLog.instance()
    logger.logMessage(msg,'InfoTools')
    
def message(msg,parent=None):
    QMessageBox.information(parent, "InfoTools", msg)
    
def confirm(title,msg,parent=None):
    box = QMessageBox(QMessageBox.Question,title,msg,QMessageBox.Yes|QMessageBox.No)
    #reply = QMessageBox.question(parent,title,msg,QMessageBox.Yes|QMessageBox.No)
    box.setButtonText(QMessageBox.Yes, u"Yes");
    box.setButtonText(QMessageBox.No, u"No");
    return (box.exec_() == QMessageBox.Yes)