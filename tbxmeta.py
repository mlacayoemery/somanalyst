import sys, string, os, base64

print "Importing ArcGIS Library... (This may take a momement.)"
import arcgisscripting

gp = arcgisscripting.create()
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Conversion Tools.tbx")

#get this script's directory
path = os.path.dirname(sys.argv[0])

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

print "Updating the toolbox images."

for tool in tools:
    #read xml file
    inName=path+"\\doc\\xml\\"+tool+".xml"
    inFile=open(inName,'r')
    xml=inFile.read()
    inFile.close()

    #find begining and end of image source    
    i=xml.find("toolIllust")
    if i!=-1:
        i=xml.find("alt=",i)
        j=xml.find("\"",i+5)

        image=xml[i+5:j]
        mime={
            "png":"image/png",
            "jpg":"image/jpg"
            }
        format=mime[image.split(".")[-1]]
        
        inFile=open(image,'rb')
        image=base64.b64encode(inFile.read())
        inFile.close()

        i=xml.find("vsrc=",i)
        j=xml.find("\"",i+6)
        xml=xml[:i+6]+"data:"+format+";base64,"+image+xml[j-1:]
    else:
        j=i
        
    l=j
    for lcv in range(xml.count("illust src=",j)):
        i=xml.find("illust src=",l)
        j=xml.find("\"",i+12)
        k=xml.find("alt=",j)
        l=xml.find("\"",k+5)

        image=xml[k+5:l]
        format=mime[image.split(".")[-1]]
        
        inFile=open(image,'rb')
        image=base64.b64encode(inFile.read())
        inFile.close()

        xml=xml[:i+12]+"data:"+format+";base64,"+image+xml[j:]

    outFile=open(inName,"w")
    outFile.write(xml)
    outFile.close()

print "Updating the first tool is slow, but after that it is pretty quick."

for t in tools:    
    xml = path+"\\doc\\xml\\"+t+".xml"
    tool = path+"\\guiArcGIS93.tbx\\"+t    
    print "Writing updated metadata to tool "+t
    gp.MetadataImporter_conversion(xml, tool)