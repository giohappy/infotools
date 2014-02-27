# -*- coding: utf-8 -*-
def classFactory(iface):
    from infotoolsplugin import InfoToolsPlugin
    return InfoToolsPlugin(iface)