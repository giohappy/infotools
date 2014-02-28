QGIS Info Tools
=========

QGIS plugin for utility informations from maps. 

What is it?
-----------

It's a graphical plugin which exposes a bunch of map tools to grab useful informations from the underlying map. Simple, easy, extensible.

Features
--------

**Rectangular tool**

  * Show extent in original CRS and WGS84
  * Show geogrpahical dimensions
  * Show graphical dimensions
  * Show typical WMS GetMap request parameters, ready to me appended to your WMS request
  * OSM, Google Maps, Bing Maps, Wikipedia links
  * Realvista aerial photos (only for Italy)

**Point tool**

  * Show position in original CRS
  * Show WGS84 Lat/Lon position
  * ...
  * 
  
Install
-------

  1. Checkout the git repository or Download the zip file (https://github.com/giohappy/infotools/archive/master.zip).
  2. Unzip in your QGIS plugins folder
  3. Enable the plugin inside QGIS
 
NOTE: In case you download from the zip, rename the extracted folder to "**infotools**"

  
Customize it
------------
You can customize the output from the tools. Edit the templates under templates/ folder:

  * templates/rect.py: Template for rectangular tool
  * templates/point.py: Template for point tool

The following variables are available:

  * rect.py:
   * 'xmin': BBOX minimum X
   * 'ymin': BBOX minimum Y
   * 'xmax': BBOX maximum X
   * 'ymax': BBOB maximum Y
   * 'cx': BBOX center X
   * 'cy': BBOX center Y
   * 'geowidth': BBOX geographical width (in project CRS)
   * 'geoheight': BBOX geographical height (in project CRS)
   * 'grwidth':  Graphical width (pixels)
   * 'grheight': Graphical height (pixels)
   * 'mapunits': Map units
   * 'crs': Project CRS
   * 'visiblelayers' : List of visible layers
   * 'xMinWGS84': BBOX minimum X (EPSG:4326)
   * 'yMinWGS84': BBOX minimum Y (EPSG:4326)
   * 'xMaxWGS84': BBOX maximum X (EPSG:4326)
   * 'yMaxWGS84': BBOB maximum Y (EPSG:4326)
   * 'unitsperpixel': Map units per pixel
   * 'z': Slippy Maps/Google Mercator zoom level (best fit for BBOX)
   * 'x': BBOX center X (EPSG:3857)
   * 'y': BBOX center Y (EPSG:3857)
  
  * point.py:
   * 'cx': Point X
   * 'cy': Point Y 
   * 'lat': Point Latitude (EPSG:4326)
   * 'lon': Point Longitude (ESPG:4326)
   * 'z': Slippy Maps/Google Mercator zoom level (best fit for BBOX)
   * 'x': BBOX center X (EPSG:3857)
   * 'y': BBOX center Y (EPSG:3857)

Roadmap
-------

The next tools I will add are WKT from features, draw points/lines/polygons and get WKT and KML.
Anything useful will be added. If you want to add you own do not esitate to contribute ;)

![Infotools screenshot](https://raw.github.com/giohappy/files/master/infotools1.png)
