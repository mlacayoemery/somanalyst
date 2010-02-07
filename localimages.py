import sys, string, os

print "Importing ArcGIS Library... (This will take a momement.)"
import arcgisscripting

gp = arcgisscripting.create()
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")

#get this scripts directory
path = os.path.dirname(sys.argv[0])
imagepath= path + "/"

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

for t in tools:

    xml = path+"\\doc\\xml\\"+t+".xml"
    script = path+"\\guiArcGIS93.tbx\\"+t
    
    print "Creating updated metadata for tool "+t
    infile=open(xml,'r')
    l=infile.read()
    infile.close()
    i=l.find("vsrc=")
    j=l.find("doc",i)
    outfile=open(xml,"w")
    outfile.write(l[:i+6]+imagepath+l[j:])
    outfile.close()
    
    print "Writing updated metadata to tool "+t
    gp.MetadataImporter_conversion(xml, script)

