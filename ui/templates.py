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
rectInfos = '''
    <b>BBOX</b> (xmin,ymin,xmax,ymax):<br>
    {xmin},{ymin},{xmax},{ymax}<br>
    <b>Centroid</b> (X,Y):<br>
    {cx},{cy}<br>
    <b>Geographic dimensions</b> (widht,height):<br>
    {geowidth},{geoheight}<br>
    <b>Graphic dimensions</b> (widht,height):<br>
    {grwidth},{grheight}<br>
    <b>Units per pixel</b> ({mapunits}):<br>
    {unitsperpixel}<br>
    <b>Slippy Maps Tile parameters</b> (z/y/x):<br>
    {z}/{y}/{x}<br>
    <b>OpenStreetMap</b>:<br>
    <a href="http://www.openstreetmap.org/#map={z}/{y}/{x}">OSM map</a><br>
    <b>Google Maps</b>:<br>
    <a href="https://www.google.com/maps?ll={y},{x}&z={z}">Google Maps</a><br>
    <b>WMS parameters</b>:<br>
    SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={visiblelayers}&CRS={crs}&BBOX={xmin},{ymin},{xmax},{ymax}&WIDTH={grwidth},&HEIGHT={grheight}<br>
    <b>Wikipedia Search</b>:<br>
    <a href="http://api.geonames.org/wikipediaBoundingBox?north={yMaxWGS84}&south={yMinWGS84}&east={xMinWGS84}&west={xMaxWGS84}&username=demo">Wikipedia Search</a>
'''

pointInfos = '''
    <b>Coordinates</b> (X,Y):<br>
    {x_destCrs},{y_destCrs}<br>
    <b>Lat/Lon</b> (WGS84):<br>
    {lat},{lon}<br>
    <b>OpenStreetMap</b>:<br>
    <a href="http://www.openstreetmap.org/#map={z}/{y}/{x}">OSM map</a><br>
    <b>Google Maps</b>:<br>
    <a href="https://www.google.com/maps?ll={y},{x}&z={z}">Google Maps</a><br>
'''