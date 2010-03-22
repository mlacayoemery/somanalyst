Normalize by Variable
==================================
Creates a database file with values normalized by a column.

ArcGIS Reference
----------------

.. figure:: ../../_images/normalize.png

**Parameters**

input database file
  The database file to be normalized.
normalize by column
  The columns that contain the values by which to normalize other data.
output database file
  The ouput database file that will contain the normalized values.
division by zero value
  The value to assign when the resulting normalization requires a division by zero, as is the case when the column contains zeros.
decimal places to round to
  The number of decimal places to round the normaized values to.
columns to normalize
  The columns to normalize. If no columns are selected normalization will be performed on all columns that are numeric.

Code Reference
--------------

.. automodule:: uiNormVar
   :members:
   :undoc-members:
