import XML, XMLinsert, lstem

class Manager:
    def __init__(self,user="scott",password="tiger",database="abstract"):
        self.dbase=XMLinsert.AMmanager(user,password,database)
        self.dbase.open()
        self.collection=None
        self.stemmer=lstem.Lstem()

    def insertCollection(self,fileName="d:/data/COSITunique.xml"):
        collectionCount=1
        self.collection=XML.parse(fileName)
        COLLID=str(self.collection.shortname)+"-"+str(self.collection.date.year)+"-"+str(collectionCount)

        #delete collection if already there        
        self.dbase.deleteCollection(COLLID)
        self.dbase.insertCollection(self.collection.shortname,self.collection.date.year,collectionCount,self.collection.longname,self.collection.place)

        #delete document table if already exists
        self.dbase.dropDocumentTables(str(self.collection.shortname))
        self.dbase.createDocumentTables(str(self.collection.shortname),COLLID)

        #insert collections
        for docID,d in enumerate(self.collection.documents):
            #stem the title and get the stem list
            title=str(d.title).replace("\'","\'\'").replace("\"","\'\'\'\'")[:300]
            stmTitle=None
            if d.title:
                stmTitle=self.stemmer.stemList(self.stemmer.Stem(str(d.title)).keys())
                stmTitle.sort()
                stmTitle=' '.join(stmTitle)[:300]

            #stem abstract and get stem list, string longer than 4000 only possible with variable binding
            abstract=str(d.text.abstract).replace("\'","\'\'").replace("\"","\'\'\'\'")[:4000]
            stmAbstract=None
            if d.text.abstract:
                stmAbstract=self.stemmer.stemList(self.stemmer.Stem(str(d.text.abstract)).keys())
                stmAbstract.sort()
                stmAbstract=' '.join(stmAbstract)[:4000]            
            
            self.dbase.insertDocument("ISIWOS_document",str(docID),"ISIWoS-2007-1",title,stmTitle,abstract,stmAbstract)

    def close(self):
        self.dbase.close()

if __name__=="__main__":
    m=Manager()
    m.insertCollection()