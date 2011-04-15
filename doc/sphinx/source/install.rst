Quick Start Guide
=================

Install and Update
------------------

There are two options for installing and updating SOM Analyst. The preferred method is to download the latest release from http://somanalyst.googlecode.com. The download is available on the download page, which can be reached by click on the download tab. The available downloads are compressed into ZIP format and must be unzipped before using, but require no additional setup. Updating SOM Analyst only requires downloading the latest release and unzipping it to the same folder as the older release, overwriting the old files.

The other option for downloading SOM Analyst is to use a SVN client to retrieve the repository from http://somanalyst.googlecode.com/svn/trunk/. Unlike the ZIP of SOM Analyst, the SOM Analyst SVN repository no longer includes the shapefile classes needed, which must also be downloaded and is available from http://shapefile.googlecode.com. Updating SOM Analyst can be preformed by using the SVN update command. Note the SVN repository is where revisions to SOM Analyst are immediately available, and as such might be unstable. If necessary revert to an earlier revision.

Python must be installed on the computer in order for SOM Analyst to work. If you do have Python download it from http://www.python.org and follow the instructions for installation.

Direct Download
~~~~~~~~~~~~~~~

This is the preferred method of installation.

#. Go to http://somanalyst.googlecode.com
#. Click on the Downloads tab
#. Select the desired release and download
#. Unzip the download to the desired location. (Usually short names without spaces works best for folders).
#. Updates can be performed by repeating this process.

SVN Client
~~~~~~~~~~

This method should only be chosen by developers and testers.

#. Create or choose a folder to use to checkout SOM Analyst. (Usually short names without spaces works best for folders). 
#. Checkout the repository at http://somanalyst.googlecode.com/svn/trunk/ to the desired folder. 
#. The folder now contains SOM Analyst, but requires an additional library. 
#. The SOM Analyst folder contains a folder named lib, inside the lib folder create a folder called shp. 
#. Checkout the repository at http://shapefile.googlecode.com/svn/trunk/ to the folder called shp. 
#. Updates can be performed by calling the SVN update function on both the SOM Analyst folder and the shp folder.

Standalone GUI
~~~~~~~~~~~~~~

The standalone GUI for SOM Analyst does not support all the features of the ArcGIS GUI and requires an additional library called WxPython, if you do not plan on using the standalone GUI you do not need it.

#. Go to http://www.wxpython.org/
#. Select the download link and choose the appropriate version for your system.
#. Follow the installation instructions for your system.

ArcGIS GUI
~~~~~~~~~~

The ArcGIS GUI was created with ArcGIS 9.3 and exported into additional formats for ArcGIS versions 9.0-9.2.

#. In ArcMap, from the Window menu select toolbox. 
#. Right click the toolbox area and click on Add Toolbox.
#. Browse to the SOM Analyst folder and select the appropriate toolbox file (.tbx), then click open.
#. SOM Analyst Toolbox should now appear in the toolbox area. If desired right click the toolbox area and save the current setup.

Updates
-------
If you used the direct download installation method, repeat the installation process. If are using a SVN client see the instruction manual for your SVN client on how to perform a update. Remember when using SVN you must update both the SOM Analyst folder and the shp folder contained in its lib folder.