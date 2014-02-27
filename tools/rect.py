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
from infotools.ui.templates import rectInfos
from infotools import utils

class RectInfoTool(InfoTool):
    def __init__(self,window):
        super(RectInfoTool,self).__init__(window)
        
    def run(self):
        super(RectInfoTool,self).run()
        self.maptool = RectangleMapTool(self.canvas)
        QObject.connect(self.maptool,SIGNAL('rectangleCreated ()'),self.grabRectSel)
        self.canvas.setMapTool(self.maptool)
        
    def grabRectSel(self):
        if not self.maptool:
            return
        rect = self.maptool.rectangle()
        xMin = rect.xMinimum()
        yMin = rect.yMinimum()
        xMax = rect.xMaximum()
        yMax = rect.yMaximum()
        cx = rect.center().x()
        cy = rect.center().y()
        geowidth = rect.width()
        geoheight = rect.height()
        unitsperpixel = self.unitsPerPixel()
        grwidth = geowidth/unitsperpixel
        grheight = geoheight/unitsperpixel
        mapunits = utils.UNITS[self.canvas.mapUnits()]
        visiblelayers = self.makeVisibleLayersString()
        crs = self.canvas.mapRenderer().destinationCrs().authid()
        rectWGS84 = self.rectToWGS84(rect)
        xMinWGS84 = rectWGS84.xMinimum()
        yMinWGS84 = rectWGS84.yMinimum()
        xMaxWGS84 = rectWGS84.xMaximum()
        yMaxWGS84 = rectWGS84.yMaximum()
        z,x,y = self.getTileParamsForRect(rect,grwidth,grheight)
        results = {
               'xmin':xMin,
               'ymin':yMin,
               'xmax':xMax,
               'ymax':yMax,
               'cx': cx,
               'cy': cy,
               'geowidth': geowidth,
               'geoheight': geoheight,
               'grwidth': grwidth,
               'grheight': grheight,
               'mapunits': mapunits,
               'crs': crs,
               'visiblelayers' : visiblelayers,
               'xMinWGS84':xMinWGS84,
               'yMinWGS84':yMinWGS84,
               'xMaxWGS84':xMaxWGS84,
               'yMaxWGS84':yMaxWGS84,
               'unitsperpixel': unitsperpixel,
               'z': z,
               'x': x,
               'y': y
        }
        self.result = rectInfos.format(**results)
        self.maptool.reset()
        super(RectInfoTool,self).done()
        
    def makeVisibleLayersString(self):
        layers = self.getVisibleLayers()
        return ','.join([l.name() for l in layers])
    
    def getTileParamsForRect(self,rect,width,height):
        coordtransform = self.makeCoordTransform('EPSG:3857')
        vextent = self.canvas.extent()
        vextent3857 = coordtransform.transformBoundingBox(vextent)
        rect3857 = coordtransform.transformBoundingBox(rect)
        dX = rect3857.width()
        dY = rect3857.height()
        if dX>dY:
            extratio = dX/vextent3857.width()
            targetRes = (dX/width)*extratio
        else:
            extratio = dY/vextent3857.height()
            targetRes = (dY/height)*extratio
        matchedRes = self.matchRes(targetRes)
        centerWGS84 = self.pointToWGS84(rect.center())
        return matchedRes,centerWGS84.x(),centerWGS84.y()


class RectangleMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

        self.rubberBand = QgsRubberBand( self.canvas, QGis.Polygon )
        self.rubberBand.setColor( QColor(255,0,0,80) )
        self.rubberBand.setWidth( 1 )

        self.reset()

    def reset(self):
        self.startPoint = self.endPoint = None
        self.isEmittingPoint = False
        self.rubberBand.reset( QGis.Polygon )

    def canvasPressEvent(self, e):
        self.startPoint = self.toMapCoordinates( e.pos() )
        self.endPoint = self.startPoint
        self.isEmittingPoint = True

        self.showRect(self.startPoint, self.endPoint)

    def canvasReleaseEvent(self, e):
        self.isEmittingPoint = False
        if self.rectangle() != None:
            self.emit( SIGNAL("rectangleCreated()") )

    def canvasMoveEvent(self, e):
        if not self.isEmittingPoint:
            return
    
        self.endPoint = self.toMapCoordinates( e.pos() )
        self.showRect(self.startPoint, self.endPoint)

    def showRect(self, startPoint, endPoint):
        self.rubberBand.reset( QGis.Polygon )
        if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
            return

        point1 = QgsPoint(startPoint.x(), startPoint.y())
        point2 = QgsPoint(startPoint.x(), endPoint.y())
        point3 = QgsPoint(endPoint.x(), endPoint.y())
        point4 = QgsPoint(endPoint.x(), startPoint.y())

        self.rubberBand.addPoint( point1, False )
        self.rubberBand.addPoint( point2, False )
        self.rubberBand.addPoint( point3, False )
        self.rubberBand.addPoint( point4, True )    # true to update canvas
        self.rubberBand.show()

    def rectangle(self):
        if self.startPoint == None or self.endPoint == None:
            return None
        elif self.startPoint.x() == self.endPoint.x() or self.startPoint.y() == self.endPoint.y():
            return None

        return QgsRectangle(self.startPoint, self.endPoint)

    def setRectangle(self, rect):
        if rect == self.rectangle():
            return False

        if rect == None:
            self.reset()
        else:
            self.startPoint = QgsPoint(rect.xMaximum(), rect.yMaximum())
            self.endPoint = QgsPoint(rect.xMinimum(), rect.yMinimum())
            self.showRect(self.startPoint, self.endPoint)
        return True
