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
                stmAbstract=self.stemmer.amStemList(self.stemmer.Stem(str(d.text.abstract)))
                stmAbstract.sort()
                stmAbstract=' '.join(stmAbstract)[:4000]            

            #full text
            text=str(d.text.fulltext).replace("\'","\'\'").replace("\"","\'\'\'\'")[:4000]
            stmtext=None
            if d.text.fulltext:
                stmText=self.stemmer.stemList(self.stemmer.Stem(str(d.text.fulltext)).keys())
                stmText.sort()
                stmText=' '.join(stmText)[:4000]       

##            #keywords comma delimited
##            keywords=', '.join(d.keywords.keywords)
##            stmKeywords=None
##            if d.keywords.keywords:
##                stmKeywords=[]
##                for k in d.keywords.keywords:
##                    stmKeywords.append(' '.join(self.stemmer.stemList(self.stemmer.Stem(str(k)).keys())))
##                stmKeywords=', '.join(stmKeywords)
            
            self.dbase.insertDocument(str(self.collection.shortname)+"_document",str(docID),COLLID,title,stmTitle,abstract,stmAbstract,text,stmText)

    def close(self):
        self.dbase.close()

if __name__=="__main__":
    m=Manager()
    m.insertCollection(fileName="d:/data/08-02-23/cositUnique03032007.xml")
    m.insertCollection(fileName="d:/data/08-02-23/cositUnique10142007.xml")    
    m.close()



##connection = cx_Oracle.Connection("user/pw@tns")
##cursor = connection.cursor()
##cursor.setinputsizes(value = cx_Oracle.CLOB)
##cursor.execute("insert into xmltable values (:value)",
##value = "A very long XML string")
##>>> m.dbase.cursor.execute("select absttext from ISIWOS_document where docid=\'845\'")
##[<cx_Oracle.CLOB with value None>]
##>>> f=m.dbase.cursor.fetchmany()
##>>> q=f[0][0].read()
##>>> len(q)