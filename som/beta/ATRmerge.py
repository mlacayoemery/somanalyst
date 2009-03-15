folder="Z:/svn/data/census/norm/noakhi/year/"
files=map(str,range(1900,2000,10))
o=open(folder+'all.txt','w')
o.write('9\n')
for i in files:
    i=open(folder+i+'.txt','r')
    i.readline()
    for l in i.readlines():
        o.write(l)
o.close()
    