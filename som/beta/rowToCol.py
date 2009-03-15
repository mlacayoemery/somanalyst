import dbftool

infile='E:/Aude/CA_tab.dbf'
outfile='E:/Aude/CA_tab_rev.dbf'

file = open(infile,'rb')

table = dbftool.dbfreader(file)
#file.close()

fieldnames=table.next()
fieldspecs=table.next()

d={}
for l in table:
    if d.has_key(l[1]):
        d[l[1]][l[2]]=l[3]
    else:
        d[l[1]]={l[2]:l[3]}
    
file.close()

newtable=[]
newfnames=[fieldnames[1],'GRIDCODE10','GRIDCODE11','GRIDCODE12',
           'GRIDCODE13','GRIDCODE14','GRIDCODE15','GRIDCODE16','GRIDCODE17',
           'GRIDCODE20','GRIDCODE30','GRIDCODE40','GRIDCODE50','GRIDCODE60','GRIDCODE70','GRIDCODE80','GRIDCODE90']
newfspecs=[fieldspecs[1]]*17
records=[]

cid={10:1,11:2,12:3,13:4,14:5,15:6,16:7,17:8,20:9,30:10,40:11,50:12,60:13,70:14,80:15,90:16}

ks=d.keys()
ks.sort()

for i in ks:
    line=[0]*17
    line[0]=i
    for k in d[i].keys():
        line[cid[int(float(k))]]=float(d[i][k])
    records.append(line)

file = open(outfile,'wb')
dbftool.dbfwriter(file, newfnames, newfspecs, records)
file.close()
    
        
