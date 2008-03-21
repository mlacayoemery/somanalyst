import XML, XMLinsert, lstem

def LongStem(manager,value,length):
    base=value
    stmBase=None
    #non empty string
    if base:
        #convert quotes to SQL formatting, unneccesary for varialbe binding
        base=str(base)#.replace("\'","\'\'").replace("\"","\'\'\'\'")
        #if not empty
        if base:
            stmBase=manager.stemmer.stemList(manager.stemmer.Stem(base).keys())
            stmBase.sort()
            stmBase=' '.join(stmBase)
            return base[:length],stmBase[:length]
        else:
            base=None
    #empty string or None
    else:
        base=None
    return base,stmBase
    

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
            #get value and construct stemed value
            title,stmTitle=LongStem(self,d.title,300)
            abstract,stmAbstract=LongStem(self,d.text.abstract,2147483647)
            text,stmText=LongStem(self,d.text.fulltext,2147483647)
            if d.keywords.keywords:
                keywords,stmKeywords=LongStem(self,' '.join(d.keywords.keywords),200)
            else:
                keywords=None
                stmKeywords=None

##            #keywords comma delimited
##            keywords=', '.join(d.keywords.keywords)
##            stmKeywords=None
##            if d.keywords.keywords:
##                stmKeywords=[]
##                for k in d.keywords.keywords:
##                    stmKeywords.append(' '.join(self.stemmer.stemList(self.stemmer.Stem(str(k)).keys())))
##                stmKeywords=', '.join(stmKeywords)
            #print "Keywords: ", stmKeywords
            self.dbase.insertDocument(str(self.collection.shortname)+"_document",str(docID+1),COLLID,title,stmTitle,abstract,stmAbstract,text,stmText,keywords,stmKeywords)

    def close(self):
        self.dbase.close()

if __name__=="__main__":
    m=Manager()
    fName="Z:/XML/AMsewer.xml"
    m.insertCollection(fileName=fName)
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