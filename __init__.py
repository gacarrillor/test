"""
/***************************************************************************
Test
A QGIS plugin
Plugin for testing things
-------------------
begin : 2015-01-28
copyright : (C) 2015 by German Carrillo, GeoTux
email : gcarrillo@linuxmail.org
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
def classFactory(iface):
    # load Test class from file test.py
    from .test import Test
    return Test(iface)
