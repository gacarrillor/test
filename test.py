"""
/***************************************************************************
 Test
                                 A QGIS plugin
 Plugin for testing things
                              -------------------
        begin                : 2015-01-28
        copyright            : (C) 2015 by German Carrillo, GeoTux
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
"""
import os

# Import the PyQt and QGIS libraries
from qgis.core import QgsApplication
from PyQt4.QtCore import ( QObject, SIGNAL )
from PyQt4.QtGui import QMessageBox, QIcon, QAction, QMenu, QActionGroup, QWidgetAction

class Test:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
            "/icon_default.png" ), "Test", self.iface.mainWindow() )
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button to the Plugins toolbar
        self.iface.addToolBarIcon(self.action)
        # Add menu item to the Plugins menu
        self.iface.addPluginToMenu("&Test", self.action)
        
        # Make sure your action can be toggled 
        self.action.setCheckable( True )

        # Build an action (button) list from QGIS navigation toolbar
        actionList = self.iface.mapNavToolToolBar().actions()

        # Add actions from QGIS attributes toolbar (handling QWidgetActions)
        tmpActionList = self.iface.attributesToolBar().actions()        
        for action in tmpActionList:
            if isinstance(action, QWidgetAction):
                actionList.extend( action.defaultWidget().actions() )
            else:
                actionList.append( action ) 
        # ... add other toolbars' action lists...
        
        # Build a group with the nav toolbar and add your own action
        group = QActionGroup( self.iface.mainWindow() )
        group.setExclusive(True)
        for action in actionList:
            group.addAction( action )
        group.addAction( self.action )
                
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu( "&Test", self.action ) 
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        QMessageBox.information( self.iface.mainWindow(), "Test", 
            "The plugin button was clicked!", QMessageBox.Ok )
            
