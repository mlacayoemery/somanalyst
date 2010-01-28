Tutorial
========

This tutorial covers the basic steps of going froma dataset to visualizing SOM and data using the SOM Analyst toolbox for ArcGIS 9.3. This process is the same basic process that would be applied to any dataset.

Connecting the Folder
---------------------

Adding the Toolbox
------------------

1. Open the ArcToolbox panel by clicking on the **Window** menu and select **ArcToolbox**. Alternatively, click on the toolbox icon on the meun bar.

.. image:: ../../_images/tutorial/ArcToolbox.png

2. Right click in the ArcToolbox panel and select **Add Toolbox...**.

.. image:: ../../_images/tutorial/AddToolbox.png

3. Browse to the location of SOM Analyst and select **guiArcGIS93.tbx** and click **Open**.

.. image:: ../../_images/tutorial/guiArcGIS93.png

.. note:: Double click on a toolbox opens it as a folder and allows you to add toolboxes it contains.

The SOM Analyst toolbox is now acessible throught the ArcToolbox panel.

.. image:: ../../_images/tutorial/SOManalyst.png

Browse through the toolbox to familarize your self with the tools.

.. image:: ../../_images/tutorial/ToolList.png

Convert Data Format
-------------------

.. image:: ../../_images/tutorial/toXbase.png

.. image:: ../../_images/tutorial/census.png

.. image:: ../../_images/tutorial/censusfields.png

Select Variables
----------------

.. image:: ../../_images/tutorial/select.png

.. image:: ../../_images/tutorial/demographics.png

.. image:: ../../_images/tutorial/demographicfields.png

Normalize Data
--------------

.. image:: ../../_images/tutorial/normalize.png

.. image:: ../../_images/tutorial/normalizevalues.png

Delete the population field.

.. image:: ../../_images/tutorial/Zscore.png

.. image:: ../../_images/tutorial/Zscorevalues.png

Export Data
-----------

.. image:: ../../_images/tutorial/somdat.png

Create Initial SOM
------------------

.. image:: ../../_images/tutorial/mapinit.png

.. image:: ../../_images/tutorial/training.png

Train SOM
---------

.. image:: ../../_images/tutorial/stage1.png

.. image:: ../../_images/tutorial/stage2.png

Project Data onto SOM
---------------------

.. image:: ../../_images/tutorial/bmu.png

Create SOM Shapefile
--------------------

.. image:: ../../_images/tutorial/somshape.png

Create Data Shapefile
---------------------

.. image:: ../../_images/tutorial/bmushape.png

Group Data Shapefile
--------------------

.. image:: ../../_images/tutorial/trajectory.png

Visualization
-------------