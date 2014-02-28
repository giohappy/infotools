# -*- coding: utf-8 -*-
template = '''
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
    <b>Bing Maps</b>:<br>
    <a href="http://bing.com/maps/default.aspx?cp={y}~{x}&lvl={z}">Bing Maps</a><br>
    <b>WMS parameters</b>:<br>
    SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={visiblelayers}&CRS={crs}&BBOX={xmin},{ymin},{xmax},{ymax}&WIDTH={grwidth},&HEIGHT={grheight}<br>
    <b>Wikipedia Search</b>:<br>
    <a href="http://api.geonames.org/wikipediaBoundingBox?north={yMaxWGS84}&south={yMinWGS84}&east={xMinWGS84}&west={xMaxWGS84}&username=demo">Wikipedia Search</a>
    <b>RealVista WMS Service (Italy only)</b>:<br>
    <a href="http://213.215.135.196/reflector/open/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.1.1&LAYERS=rv1&STYLES=&FORMAT=image/png&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&SRS=EPSG:4326&BBOX={xMinWGS84},{yMinWGS84},{xMaxWGS84},{yMaxWGS84}&WIDTH={grwidth}&HEIGHT={grheight}">RealVista Aerial photo</a><br>
'''
