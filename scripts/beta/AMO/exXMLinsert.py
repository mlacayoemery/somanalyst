import XML, XMLinsert

collection = XML.parse("d:/data/COSITunique.xml")
am=XMLinsert.AMmanager("scott","tiger","abstract")
am.open()
am.deleteCollection(str(collection.shortname)+"-"+str(collection.date.year)+"-"+str(1))
am.insertCollection(collection.shortname,collection.date.year,1,collection.longname,collection.place)