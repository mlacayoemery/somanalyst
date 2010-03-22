import xml.dom.minidom

path="E:/somanalyst/doc/xml/"
files=["bmushp",
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

for f in files:
    doc=xml.dom.minidom.parse(path+f+".xml")
    outfile=open(path+f+".rst",'w')
    summary=doc.getElementsByTagName("summary")[0].getElementsByTagName("para")[0].childNodes[0].data
    parameters=doc.getElementsByTagName("parameters")
    outfile.write(summary+"\n\n**Parameters**\n")
    for parameter in parameters[0].getElementsByTagName("param"):
        name = parameter.getAttribute("displayname")
        try:
            text = parameter.getElementsByTagName("dialogReference")[0].getElementsByTagName("para")[0].childNodes[0].data
            outfile.write("\n"+name+"\n  "+text)
        except:
            outfile.write("\n"+name+"\n  ")
    outfile.write("\n\nCode Reference\n--------------\n")
    outfile.close()