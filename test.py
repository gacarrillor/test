"""
/***************************************************************************
 Test
                                 A QGIS plugin
 Plugin for testing things
                              -------------------
        begin                : 2015-01-28
        copyright            : (C) 2015 by German Carrillo, GeoTux
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

# Import the PyQt and QGIS libraries
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (QMessageBox, QAction)

class Test:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        QMessageBox.information(self.iface.mainWindow(), "Test", 
            "__init__(self, iface) was called!", QMessageBox.Ok)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(os.path.dirname(os.path.realpath(__file__)) + 
            "/icon_default.png" ), "Test", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button to the Plugins toolbar
        self.iface.addToolBarIcon(self.action)
        # Add menu item to the Plugins menu
        self.iface.addPluginToMenu("&Test", self.action)
        
        QMessageBox.information(self.iface.mainWindow(), "Test", 
            "initGui(self) was called!\n\nYour plugin GUI has been set up.", 
            QMessageBox.Ok)
                            
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Test", self.action) 
        self.iface.removeToolBarIcon(self.action)
        
        QMessageBox.information(self.iface.mainWindow(), "Test", 
            "unload(self) was called!\n\nYour plugin widgets were removed from QGIS GUI.", 
            QMessageBox.Ok)

    # run method that performs all the real work
    def run(self):
        QMessageBox.information( self.iface.mainWindow(), "Test", 
            "run(self) was called!\n\nIt's time to learn more PyQGIS!", QMessageBox.Ok)
            

