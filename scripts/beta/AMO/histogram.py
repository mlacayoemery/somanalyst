import pylab

fName="D:/users/ryan/dat.txt"
iFile=open(fName)
lines=iFile.readlines()
iFile.close()

termDocumentMatrix=[map(int,l.strip().split(" ")) for l in lines[1:]]
#demonstrates the breadth of vocabulary in a document
sumDocument=map(sum,termDocumentMatrix)

documentTermMatrix=[[i] for i in termDocumentMatrix[0]]
for i in termDocumentMatrix[1:]:
    for id,j in enumerate(i):
        documentTermMatrix[id].append(j)
#demontrates word usage/frequency
sumTerm=map(sum,documentTermMatrix)

#determin bins
b=list(set(sumTerm))
b.sort()
b=map(b.__getitem__,range(0,len(b),len(b)/20))


# Make a histogram out of the data in x and prepare a bar plot.
vals, bins, patchs = pylab.hist(sumTerm, b)

# Show the plot.
pylab.show()


##def bin(
##delta=(max(sumTerm)-min(sumTerm)-.1)/10.0
##hist=[0]*10
##for n in sumTerm:
##    i=int(math.floor(n/delta))
##    hist[i]+=1

##def squared(i):
##    return i**2
##
##N=float(len(sumTerm))
##mean=sum(sumTerm)/float(N)

###std dev, sqrt of difference squared
##stdDev=0
##for i in sumTerm:
##    stdDev+=((i-mean)**2)/N
##stdDev=stdDev**0.5
##
##min=mean-stdDev
##max=mean+stdDev
###%68 of data with 1 std dev
