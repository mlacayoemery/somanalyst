import sys
from dbftool import dbfwriter

ifile=sys.argv[1]
ofile=sys.argv[2]

i=open(ifile,'r')
o=open(ofile,'wb')

fieldnames =i.readline().strip().split(',')
table=[l.strip().split(',') for l in i.readlines()]
i.close()
fieldwidth=map(len,table[0])

for l in table:
    for id,j in enumerate(l):
        if len(j)>fieldwidth[id]:
            fieldwidth[id]=len(j)

fieldspecs=[]
for w in fieldwidth:
    fieldspecs.append(('C', w, 0))

#set records
records = table

#write dbf
dbfwriter(o, fieldnames, fieldspecs, records)
o.close()


