"""
/***************************************************************************
 Test
                                 A QGIS plugin
 Plugin for testing things
                              -------------------
        begin                : 2015-01-28
        copyright            : (C) 2015-2017 by German Carrillo, GeoTux
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
from qgis.core import QgsApplication, QgsRasterLayer, QgsRaster
from qgis.gui import QgsMapToolEmitPoint
from PyQt4.QtCore import QObject, SIGNAL, QTimer
from PyQt4.QtGui import ( QMessageBox, QIcon, QAction, QMenu, QActionGroup,
                          QWidgetAction, QToolTip )

class Test:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.tooltipRaster = TooltipRasterMapTool( self.iface )

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) +
            "/icon_default.png" ), "Tooltip for Raster Values", self.iface.mainWindow() )
        # connect the action to the run method
        self.action.triggered.connect( self.run )
        self.action.setCheckable( True )

        self.iface.mapCanvas().mapToolSet.connect( self.mapToolWasSet )

        # Add toolbar button to the Plugins toolbar
        self.iface.addToolBarIcon(self.action)
        # Add menu item to the Plugins menu
        self.iface.addPluginToMenu("&Tooltip for Raster Values", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu( "&Tooltip for Raster Values", self.action )
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self, checked):
        if checked:
            self.iface.mapCanvas().setMapTool( self.tooltipRaster )
        else:
            self.iface.mapCanvas().unsetMapTool( self.tooltipRaster )

    def mapToolWasSet( self, newTool ):
        if type(newTool) != TooltipRasterMapTool:
            self.action.setChecked( False )


class TooltipRasterMapTool(QgsMapToolEmitPoint):
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.timerMapTips = QTimer( self.canvas )
        self.timerMapTips.timeout.connect(self.showMapTip)

    def canvasPressEvent(self, e):
        pass

    def canvasReleaseEvent(self, e):
        pass

    def canvasMoveEvent(self, e):
        if self.canvas.underMouse(): # Only if mouse is over the map
            QToolTip.hideText()
            self.timerMapTips.start( 700 ) # time in milliseconds

    def deactivate(self):
        self.timerMapTips.stop()

    def showMapTip( self ):
        self.timerMapTips.stop()
        if self.canvas.underMouse():
            rLayer = self.iface.activeLayer()
            if type(rLayer) is QgsRasterLayer:
                ident = rLayer.dataProvider().identify( self.toMapCoordinates(self.canvas.mouseLastXY()), QgsRaster.IdentifyFormatValue )
                if ident.isValid():
                    text = ", ".join(['{0:g}'.format(r) for r in ident.results().values() if r is not None] )
                else:
                    text = "Non valid value"
                QToolTip.showText( self.canvas.mapToGlobal( self.canvas.mouseLastXY() ), text, self.canvas )


