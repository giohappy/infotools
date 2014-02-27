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
from infotools.utils import RESOLUTIONS

class InfoTool(object):
    def __init__(self,window):
        self.window = window
        self.iface = window.iface
        self.canvas = window.canvas
        self.maptool = None
        self.result = ''
        
    def run(self):
        self.window.hideme()
        
    def done(self):
        if self.maptool:
            self.canvas.unsetMapTool(self.maptool)
        self.window.setResult(self.result)
        self.window.showme()
    
    def setMapTool(self,tool):
        pass

    def getVisibleLayers(self):
        layers = []
        legendiface = self.iface.legendInterface()
        for layer in legendiface.layers():
            if legendiface.isLayerVisible(layer):
                layers.append(layer)
        return layers
    
    def unitsPerPixel(self):
            return self.canvas.getCoordinateTransform().mapUnitsPerPixel()
        
    def viewExtent(self):
        return self.canvas.extent()
        
    def matchRes(self,targetRes):
        for i,res in enumerate(RESOLUTIONS):
            if res<targetRes:
                diff1 = targetRes-res
                diff2 = abs(targetRes-RESOLUTIONS[i-1])
                if diff1<diff2:
                    return i
                else:
                    return i-1
                
    def pointToWGS84(self,point):
        coordtransform = self.makeCoordTransform()
        return coordtransform.transform(point)
                
    def centerWGS84(self,rect):
        rectWGS84 = self.rectToWGS84(rect)
        return rectWGS84.center()
    
    def rectToWGS84(self,rect):
        coordtransform = self.makeCoordTransform()
        return coordtransform.transform(rect)
        
    def makeCoordTransform(self,toCrsEPSG='EPSG:4326'):
        fromCrs = self.canvas.mapRenderer().destinationCrs()
        toCrs = QgsCoordinateReferenceSystem()
        toCrs.createFromString(toCrsEPSG)
        coordtransform = QgsCoordinateTransform()
        coordtransform.setSourceCrs(fromCrs)
        coordtransform.setDestCRS(toCrs)
        return coordtransform
