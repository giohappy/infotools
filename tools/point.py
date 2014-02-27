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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from infotools.tools import InfoTool
from infotools.ui.templates import pointInfos

class PointInfoTool(InfoTool):
    def __init__(self,window):
        super(PointInfoTool,self).__init__(window)
        
    def run(self):
        super(PointInfoTool,self).run()
        self.maptool = PointTool(self.canvas)
        QObject.connect(self.maptool,SIGNAL('canvasClicked(const QgsPoint &, Qt::MouseButton)'),self.grabPoint)
        self.canvas.setMapTool(self.maptool)

    def grabPoint(self,point,button):
        x_destCrs = point.x()
        y_destCrs = point.y()
        pointWGS84 = self.pointToWGS84(point)
        z,x,y = self.getTileParamsForPoint(point)
        results = {
           'x_destCrs':x_destCrs,
           'y_destCrs':y_destCrs,
           'lat': pointWGS84.x(),
           'lon': pointWGS84.y(),
           'z': z,
           'x': x,
           'y': y
        }
        self.result = pointInfos.format(**results)
        super(PointInfoTool,self).done()
        
    def getTileParamsForPoint(self,point):
        coordtransform = self.makeCoordTransform('EPSG:3857')
        vextent = self.canvas.extent()
        vextent3857 = coordtransform.transformBoundingBox(vextent)
        dX = vextent3857.width()
        dY = vextent3857.height()
        if dX>dY:
            targetRes = dX/self.canvas.width()
        else:
            targetRes = dY/self.canvas.height()
        matchedRes = self.matchRes(targetRes)
        pointWGS84 = self.pointToWGS84(point)
        return matchedRes,pointWGS84.x(),pointWGS84.y()


class PointTool(QgsMapToolEmitPoint):   
    def __init__(self, canvas):
        QgsMapToolEmitPoint.__init__(self, canvas)
        self.setCursor(QCursor(QPixmap(":/infotools/pointcursor")))
#         self.setCursor(QCursor(QPixmap(["16 16 3 1",
#                                       " »     c None",
#                                       ".»     c #000000",
#                                       "+»     c #FFFFFF",
#                                       "                ",
#                                       "       +.+      ",
#                                       "      ++.++     ",
#                                       "     +.....+    ",
#                                       "    +.     .+   ",
#                                       "   +.   .   .+  ",
#                                       "  +.    .    .+ ",
#                                       " ++.    .    .++",
#                                       " ... ...+... ...",
#                                       " ++.    .    .++",
#                                       "  +.    .    .+ ",
#                                       "   +.   .   .+  ",
#                                       "   ++.     .+   ",
#                                       "    ++.....+    ",
#                                       "      ++.++     ",
#                                       "       +.+      "])))
