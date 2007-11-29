#!/usr/bin/python
#
# This generates a set of random values and 
import pylab
import random

# Fill an list of random values
data=[]
for v in pylab.arange(1,1000):
    data.append(random.gauss(0,1))

# Make a histogram out of the data in x and prepare a bar plot.
vals, bins, patchs = pylab.hist(data)

# Show the plot.
pylab.show()

