"""
/***************************************************************************
 RemoveEmptyLayers
                                 A QGIS plugin
 This plugin 'cleans' the layer list widget by removing empty layers
                             -------------------
        begin                : 2011-03-06
        copyright            : (C) 2011 by German Carrillo, GeoTux
        email                : geotux_tuxman@linuxmail.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Test"
def description():
    return "For testing purposes"
def version():
    return "Version 1.0"
def icon():
    return "icon_default.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load RemoveEmptyLayers class from file RemoveEmptyLayers
    from test import Test
    return Test(iface)
