#test
import sys, string, os, base64

print "Importing ArcGIS Library... (This may take a momement.)"
import arcgisscripting

gp = arcgisscripting.create()
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")

#get this script's directory
path = os.path.dirname(sys.argv[0])

images=["dbf",
        "select",
        "dat",
        "mapinit",
        "vsom",
        "umatrix",
        "combine"]

print "Updating the toolbox images."

for image in images:
    #read xml file
    xml=path+"\\doc\\xml\\"+image+".xml"
    infile=open(xml,'r')
    l=infile.read()
    infile.close()

    #find begining and end of image source    
    i=l.find("vsrc=")
    j=l.find("/>\n",i)

    #open image and write to xml
    if image=="umatrix":
        infile=open(path+"\\doc\\sphinx\\_images\\tbxumatrix.jpg",'rb')
        outfile=open(xml,"w")
        outfile.write(l[:i+6]+"data:image/jpg;base64,"+base64.b64encode(infile.read())+l[j-1:])
    else:
        infile=open(path+"\\doc\\sphinx\\_images\\tbx"+image+".png",'rb')
        outfile=open(xml,"w")
        outfile.write(l[:i+6]+"data:image/png;base64,"+base64.b64encode(infile.read())+l[j-1:])
    infile.close()
    outfile.close()

tools=["bmushp",
       "codshp",
       "combine",
       "dat",
       "dbf",
       "divide",
       "email",
       "extent",
       "group",
       "mapinit",
       "minmax",
       "select",
       "umatrix",
       "visual",
       "vsom",
       "zscore"]

print "Updating the first tool is slow, but after that it is pretty quick."

for t in tools:    
    xml = path+"\\doc\\xml\\"+t+".xml"
    tool = path+"\\guiArcGIS93.tbx\\"+t    
    print "Writing updated metadata to tool "+t
    gp.MetadataImporter_conversion(xml, tool)