import struct, datetime
from math import sqrt

#convert cod to points minimizing memory used
print

#open files
codfile='Z:/arcSOM/states.cod'
shpfile='_'.join(codfile.split('.'))
inputCOD=open(codfile,'r')
shp=open(shpfile+"_point"+'.shp','wb') #main file
shx=open(shpfile+"_point"+'.shx','wb') #index file
dbf=open(shpfile+"_point"+'.dbf','wb') #dbf table

#read cod header

#parse file header
formatting=inputCOD.readline().split()
#number of columns in the cod
columns=int(formatting[0])
#the orientation of the SOM
topology=formatting[1]
#the number of neurons in the x direction
x=int(formatting[2])
#the number of neurons in the y direction
y=int(formatting[3])

#generate the column heading names
#begining with att1, they are numbered in sequence
names=[]
for i in range(columns):
    names.append('att'+str(i+1))

#write shp,shx,dbf headers
deci=6
version=1
shapeType=1
Xmin=0
Ymin=0
Xmax=0
Ymax=0
Zmin=0
Zmax=0
Mmin=0
Mmax=0
contentLength=10
neurons=x*y

if topology=="rect":
    Xmax=x-1
    Ymax=y-1

elif topology=='hexa':
    Ymax=(y-1)*sqrt(3.0/4)
    Xmax=x-0.5

########Main File Header##########
#This section corresponds directly to the whitepaper
#regarding main file creation
        
#BIG BYTE ORDER, integer
#byte 0, File Code
shp.write(struct.pack('>i', 9994))
#byte 4, Unused
shp.write(struct.pack('>i', 0))
#byte 8, Unused
shp.write(struct.pack('>i', 0))
#byte 12, Unused
shp.write(struct.pack('>i', 0))
#byte 16, Unused
shp.write(struct.pack('>i', 0))
#byte 20, Unused
shp.write(struct.pack('>i', 0))
#byte 24, File Length, total length of file in 16-bit words
shp.write(struct.pack('>i', 50+(contentLength*neurons)))
#byte 28, Version, integer
shp.write(struct.pack('<i', version))
#byte 32, shape type
shp.write(struct.pack('<i',shapeType))
#byte 36, Bounding Box Xmin
shp.write(struct.pack('<d',Xmin))
#byte 44 Bounding Box Ymin
shp.write(struct.pack('<d',Ymin))
#byte 52 Bounding Box Xmax
shp.write(struct.pack('<d',Xmax))
#byte 60 Bounding Box Ymax
shp.write(struct.pack('<d',Ymax))
#byte 68* Bounding Box Zmin
shp.write(struct.pack('<d',Zmin))
#byte 76* Bounding Box Zmax
shp.write(struct.pack('<d',Zmax))
#byte 84* Bounding Box Mmin
shp.write(struct.pack('<d',Mmin))
#byte 92* Bounding Box Mmax
shp.write(struct.pack('<d',Mmax))

##############Index File Header###########
#This section corresponds directly to the whitepaper
#regarding index file creation

#BIG BYTE ORDER, integer
#byte 0, File Code
shx.write(struct.pack('>i', 9994))
#byte 4, Unused
shx.write(struct.pack('>i', 0))
#byte 8, Unused
shx.write(struct.pack('>i', 0))
#byte 12, Unused
shx.write(struct.pack('>i', 0))
#byte 16, Unused
shx.write(struct.pack('>i', 0))
#byte 20, Unused
shx.write(struct.pack('>i', 0))
#byte 24, File Length, total length of file in 16-bit words
shx.write(struct.pack('>i', 50+(4*neurons)))
#byte 28, Version, integer
shx.write(struct.pack('<i', version))
#byte 32, shape type
shx.write(struct.pack('<i',shapeType))
#byte 36, Bounding Box Xmin
shx.write(struct.pack('<d',Xmin))
#byte 44 Bounding Box Ymin
shx.write(struct.pack('<d',Ymin))
#byte 52 Bounding Box Xmax
shx.write(struct.pack('<d',Xmax))
#byte 60 Bounding Box Ymax
shx.write(struct.pack('<d',Ymax))
#byte 68* Bounding Box Zmin
shx.write(struct.pack('<d',Zmin))
#byte 76* Bounding Box Zmax
shx.write(struct.pack('<d',Zmax))
#byte 84* Bounding Box Mmin
shx.write(struct.pack('<d',Mmin))
#byte 92* Bounding Box Mmax
shx.write(struct.pack('<d',Mmax))

#####################DBF header###############
# header info
ver = 3
now = datetime.datetime.now()
yr, mon, day = now.year-1900, now.month, now.day
numrec = neurons
numfields = columns
lenheader = numfields * 32 + 33
lenrecord = (numfields*(deci+2)) + 1
hdr = struct.pack('<BBBBLHH20x', ver, yr, mon, day, numrec, lenheader, lenrecord)
dbf.write(hdr)
                  
# field specs
for name in names:
    name = name.ljust(11, '\x00')
    fld = struct.pack('<11sc4xBB14x', name, 'N', deci+2, deci)
    dbf.write(fld)

# terminator
dbf.write('\r')
#dbf.write(struct.pack('>i',0xd))
dbf.write(struct.pack('>b',0x20))
#write records
deltaX=float(1)
deltaY=sqrt(3.0/4)

#read cod line
id=1
line=inputCOD.readline()
while(line):
    record = [round(float(i),deci) for i in line.split()]

    #write shp,shx,dbf entries
    shp.write(struct.pack('>i',id))
    #content length
    shp.write(struct.pack('>i',contentLength))
    #write record contents
    shp.write(struct.pack('<i',shapeType))

    #write coordinates
    if topology=="rect":
        shp.write(struct.pack('<d',float(id%y)))
        shp.write(struct.pack('<d',float(id/y)))

    elif topology=='hexa':
        hexX=id%y
        hexY=id/y
        if (hexY+1)%2:
            shp.write(struct.pack('<d',float((hexX+0.5)*deltaX)))
        else:
            shp.write(struct.pack('<d',float(hexX*deltaX)))
        shp.write(struct.pack('<d',float(hexY)))

    #write index records
    shx.write(struct.pack('>i',50+((contentLength+4)*(id-1))))
    shx.write(struct.pack('>i',contentLength))

    #dbf record
    #dbf.write(struct.pack('>i',0x0000))
    for value in record:
        
      
        value = str(round(value,6)).rjust(8, ' ')
        dbf.write(value)
    #print id
    #increment id
    id=id+1
    #read next line    
    line=inputCOD.readline()        


#close files
shp.close()
shx.close()
#eof
dbf.write('\x1A')
dbf.close()