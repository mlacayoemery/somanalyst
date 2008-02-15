import XML, XMLinsert



collection = XML.parse("d:/data/COSITunique.xml")
am=XMLinsert.AMmanager("scott","tiger","abstract")
am.open()
COLLID=str(collection.shortname)+"-"+str(collection.date.year)+"-"+str(1)
am.deleteCollection(COLLID)
am.insertCollection(collection.shortname,collection.date.year,1,collection.longname,collection.place)
am.dropDocumentTables(str(collection.shortname))
am.createDocumentTables(str(collection.shortname),COLLID)

for docID,d in enumerate(collection.documents):
    am.insertDocument("ISIWOS_document",str(docID),"ISIWoS-2007-1",str(d.title).replace("\'","\'\'").replace("\"","\'\'\'\'")[:300])
    