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

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (QMessageBox,
                                 QAction,
                                 QMenu)


class Test:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)),
            "icon_default.png")), "Test", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button to the Plugins toolbar
        self.iface.addToolBarIcon(self.action)

        # Add menu item to the Plugins menu
        self.iface.addPluginToMenu("&Test", self.action)

        # Add a custom toolbar
        self.toolbar = self.iface.addToolBar("My tools")
        self.toolbar.addAction(self.action)

        # Remove a QGIS toolbar
        fileToolBar = self.iface.fileToolBar()
        self.iface.mainWindow().removeToolBar(fileToolBar)

        # Add a custom menu
        self.menu = QMenu("&My tools", self.iface.mainWindow().menuBar())
        actions = self.iface.mainWindow().menuBar().actions()
        lastAction = actions[-1]
        self.iface.mainWindow().menuBar().insertMenu(lastAction, self.menu)
        self.menu.addAction(self.action)

        # Remove a QGIS menu
        editMenu = self.iface.editMenu()
        editMenu.menuAction().setVisible(False)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Test", self.action)
        self.iface.removeToolBarIcon(self.action)

        # Remove custom menu
        menu_action = [a for a in self.iface.mainWindow().menuBar().actions() if a.text() == '&My tools']
        if len(menu_action) == 1:
            self.iface.mainWindow().menuBar().removeAction(menu_action[0])

    # run method that performs all the real work
    def run(self):
        QMessageBox.information(self.iface.mainWindow(), "Test",
            "The plugin button was clicked!", QMessageBox.Ok)
        # Add your useful stuff here...
