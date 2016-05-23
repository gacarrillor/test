# test
QGIS plugin for testing a variety of aspects related to PyQGIS

**Tags**

Go to [Tags](https://github.com/gacarrillor/test/tags) to see all versions of the plugin (each version tackles a different aspect). This is a summary:

* [Attribute value changed](https://github.com/gacarrillor/test/tree/attribute_value_changed)

  Open QGIS, load a vector layer, and click on the plugins icon.
  Start editing and edit any existing attribute value of the 1st layer in the QGIS ToC.
  You should see a message box after that change.

  See this [post](http://gis.stackexchange.com/a/132194/4972) for more context.

* [Function notifications](https://github.com/gacarrillor/test/tree/function_notifications)

  Open QGIS and you will see some message boxes that let you know when QGIS plugin functions are being called. Particularly, you will be notified when __init__(), initGui(), run(), and unload() functions are called.

  See this [post](http://gis.stackexchange.com/a/132604/4972) for more context.

* [Mutually exclusive buttons](https://github.com/gacarrillor/test/tree/mutually_exclusive_buttons)

  Open QGIS and you should notice that the plugin button (identified by an icon of a directory) is mutually exclusive with QGIS buttons from Navigation and Attributes toolbars. For instance, if you click on Pan tool and then click on the plugin button, the Pan tool is deactivated. 

  See this [post](http://gis.stackexchange.com/a/132389/4972) for context.

* [QGIS GUI customization](https://github.com/gacarrillor/test/tree/qgis_gui_customization)

  Open QGIS and you should notice:

      A new menu "My tools"
      A new toolbar "My tools"
      A missing Edit menu
      A missing File toolbar

  See this [post](http://gis.stackexchange.com/a/132238/4972) for context.

**Installation**

* Download the zip file.
* Extract it in your QGIS plugins folder.
  * On GNU/Linux, probably: `/home/USER/.qgis2/python/plugins/`
  * On Windows, probably: `C:\Users\user_name\.qgis2\python\plugins\`
* Change the name of the extracted folder to "test".
* Start your QGIS and go to `Plugins->Manage and Install Plugins`.
* Type "test" and check the plugin. 
