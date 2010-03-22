import pickle

name="E:/test.txt"
outfile=open(name,'w')

a=[1,2,3]
print a
pickle.dump(a,outfile)
outfile.close()
del a
try:
    print a
except:
    print "does not exist"

infile=open(name)
a=pickle.load(infile)
infile.close()
print a