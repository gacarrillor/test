# test
QGIS plugin for testing a variety of aspects related to PyQGIS

**Tags**

Go to [Tags](https://github.com/gacarrillor/test/tags) to see all versions of the plugin (each version tackles a different aspect). This is a summary:


* [QGIS GUI customization](https://github.com/gacarrillor/test/tree/qgis_gui_customization_v3) (QGIS 3)

  Open QGIS and you should notice:

      A new menu "My tools"
      A new toolbar "My tools"
      A missing Edit menu
      A missing File toolbar (i.e., no New/Open/Save project buttons, among others)

  See this [post](http://gis.stackexchange.com/a/132238/4972) for context.
  Download [plugin ZIP file](https://github.com/gacarrillor/test/archive/refs/tags/qgis_gui_customization_v3.zip).


* [Function notifications](https://github.com/gacarrillor/test/tree/function_notifications_v3) (QGIS 3)

  Open QGIS and you will see some message boxes that let you know when QGIS plugin functions are being called. Particularly, you will be notified when **\__init__()**, **initGui()**, **run()**, and **unload()** functions are called.

  See this [post](http://gis.stackexchange.com/a/132604/4972) for more context. 
  Download [plugin ZIP file](https://github.com/gacarrillor/test/archive/refs/tags/function_notifications_v3.zip).


* [Attribute value changed](https://github.com/gacarrillor/test/tree/attribute_value_changed) (QGIS 2)

  Open QGIS, load a vector layer, and click on the plugins icon.
  Start editing and edit any existing attribute value of the 1st layer in the QGIS ToC.
  You should see a message box after that change.

  See this [post](http://gis.stackexchange.com/a/132194/4972) for more context.
  Download [plugin ZIP file](https://github.com/gacarrillor/test/archive/refs/tags/attribute_value_changed.zip).


* [Mutually exclusive buttons](https://github.com/gacarrillor/test/tree/mutually_exclusive_buttons) (QGIS 2)

  Open QGIS and you should notice that the plugin button (identified by an icon of a directory) is mutually exclusive with QGIS buttons from Navigation and Attributes toolbars. For instance, if you click on Pan tool and then click on the plugin button, the Pan tool is deactivated.

  See this [post](http://gis.stackexchange.com/a/132389/4972) for context.
  Download [plugin ZIP file](https://github.com/gacarrillor/test/archive/refs/tags/mutually_exclusive_buttons.zip).


* [Tooltip for Raster Value](https://github.com/gacarrillor/test/tree/tooltip_raster_values) (QGIS 2)

  By toggling the plugin's button you can enable tooltips displaying raster cell values for the active layer (if it's a raster).
  (Icon by http://www.webalys.com/)

  See this [post](https://gis.stackexchange.com/a/245398/4972) for context.
  Download [plugin ZIP file](https://github.com/gacarrillor/test/archive/refs/tags/tooltip_raster_values.zip).
  
  ![image](https://user-images.githubusercontent.com/652785/236654966-952f3f9e-e328-434f-92b8-4890a82156a1.png)


**Installation**

* Download the ZIP file.
* Install it via Plugins --> Manage and Install Plugins... --> Install from ZIP.
