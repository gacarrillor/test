# test
QGIS plugin for testing random things related to PyQGIS

**Installation**

* Download the zip file.
* Extract it in your QGIS plugins folder.
  * On GNU/Linux, probably: `/home/USER/.qgis2/python/plugins/`
  * On Windows, probably: `C:\Users\user_name\.qgis2\python\plugins\`
* Change the name of the extracted folder to "test".
* Start your QGIS and go to `Plugins->Manage and Install Plugins`.
* Type "test" and check the plugin. 

**Usage**

Open QGIS and you will see some message boxes that let you know when QGIS plugin
functions are being called. Particularly, you will be notified when `__init__()`, 
`initGui()`, `run()`, and `unload()` functions are called.

