Introduction
============

SOM Analyst is software written in the Python language and was created to make the use of self-organizing maps (SOMs) more accessible for users of geographic information systems (GIS). The broader impact of this work is to contribute to geographic information science, the science behind GIS, by incorporating a method that is usable with datasets that challenge current methods. These challenges include the sear volume of data as well as the number of variables that can cause some methods, or at least their implementation, to fail altogether or become unusable because of the amount of time need for computation. SOMs are by no means a cure all, they have several limitations and can be difficult to interpret. The following is a brief introduction to SOMs and a quick start guide to using SOM Analyst.

Method
------

Self-organizing maps (SOMs) are artificial neural networks created using a method originally developed for signal processing. However, the use of this method is not limited to signal processing, it can be used for any dataset, especially those that contain many variables and/or instances. Essentially the method approximates an “optimal” spatial arrangement such that spatial distances are related to data similarity. As with all reductions of the number of independent variables distortions are produced. This means that spatial distances are consequently not strictly proportional to data similarity, however there is a tendency towards proportionality and as such can demonstrate qualities similar to geographic space. This is especially true since SOMs typically create two-dimensional spaces, although more dimensions and different shapes can be used. The space a SOM creates can have widely differing results from producing only clusters to producing only hierarchies and everything in between. 

Overview of Parameters
----------------------

The results of a SOM depend on both the parameters specified by the user as well as qualities of the data. I will begin by defining each of the parameters of a SOM as well as some of the qualities of data that are important to keep in mind. 

SOMs have the following variables:
  * x-dimension: the resolution in the x direction
  * y-dimension: the resolution in the y direction
  * number of variables: the number of variables from the data
  * topology: the arrangement of the units in the SOM
  * neighborhood type: the relationship between units in the SOM 

Dimensions of the SOM
~~~~~~~~~~~~~~~~~~~~~

The user has complete control of the x and y dimensions of the SOM and this greatly affects what kind of results will be achieved. It can be helpful to think of the size of the dataset and what you want the results to be. For example, if you are more interested in a classification you might choose to use 7 times as many units in the SOM as you have in your data. In this way, a perfectly even distribution would yield a single neuron for each of the input data with no adjacency. If you wanted to use the SOM more for clustering then you might only use 9 units in total. Once you have chosen the number of units, then the question of what ratio between the x and y dimensions is relevant. The easiest solution is to have both dimensions be the same, however varying their ratio changes the shape of the achievable topology. For example, if you were interested in a simple ordering you might choose one of the dimensions to only have a length of 1, which would result in a linear SOM and each unit would represent a place on a scale. Ultimately, the decision must be based on the desired results and the compatibility of SOM topology with that of the data topology.

Characteristics of SOM Training
-------------------------------

SOM training has the variables:
* run length: the total number of times data is present to the SOM
* neighborhood size: the distance over which the training acts
* learning rate: the rate at which the training changes values 

Run Length
~~~~~~~~~~

The run length of the training is the number of times data is presented to the SOM. For example, if your data had 10 vectors in it and you chose a run length of 100, each of the vectors would be presented 10 times. The vectors are presented in the order they appear in the data, so a run length of 102 would present the first two vectors more than the rest.

Neighborhood Size
~~~~~~~~~~~~~~~~~

The neighborhood size is the distance over which the neighborhood area is selected. This affects the resolution at which the data acts and is what directly defines area over which the lateral cohesion of the SOM forms. If the neighborhood size is too small, the SOM will result in little areas that are overspecialized surround by large areas that are not specialized. If the neighborhood size is too big then the SOM will be one large area that doesn't distinguish data into different classes. In many instances the SOM is first trained with a large neighborhood and trained a second time with a smaller neighborhood.

Learning Rate
~~~~~~~~~~~~~

The learning rate is the rate at which the SOM changes its values to correspond with the input data. A rate too high will produce areas that are overspecialized. A rate too low will produce areas that are not specialized enough.

Choosing Parameters
-------------------

Determining the correct parameters for your data can be difficult to determine, however that are several guidelines that can be helpful. Small numbers of neurons produces clusters, while large numbers produce hierarchies. Small neighborhood sizes will yield spatially small clusters or hierarchies that can be widely dispersed, while large neighborhood sizes yield large clusters and little hierarchy. High learning rates yield a more specialized SOM, but this can also be overspecialized, while low learning rates yield a more generalized SOM that may have a clear structure.