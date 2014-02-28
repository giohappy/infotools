# -*- coding: utf-8 -*-
template = '''
    <b>Coordinates</b> (X,Y):<br>
    {cx},{cy}<br>
    <b>Lat/Lon</b> (WGS84):<br>
    {lat},{lon}<br>
    <b>OpenStreetMap</b>:<br>
    <a href="http://www.openstreetmap.org/#map={z}/{y}/{x}">OSM map</a><br>
    <b>Google Maps</b>:<br>
    <a href="https://www.google.com/maps?ll={y},{x}&z={z}">Google Maps</a><br>
'''