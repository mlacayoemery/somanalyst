import pylab

data=[1,1,1,1,1,1,5,5,1,1,1,1,1,1,5,5,1,1,1,1,1,1,5,5,1,1,1,1,1,1,5,5,1,1,1,1,1,1,5,5,1,1,1,1,1,1,5,5]
data.sort()
vals, bins, patchs = pylab.hist(data, [1,6], width=1, align='center')
pylab.show()