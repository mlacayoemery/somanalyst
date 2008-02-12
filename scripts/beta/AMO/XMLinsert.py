import cx_Oracle
from pprint import pprint

#constants
collectionTable="COLLECTION"
collectionID="COLLID"
collectionFullName="FULLNAME"
collectionShortName="SHORTNAME"
collectionYear="COLLYEAR"
collectionNumber="COLLNUM"
collectionPlace="COLLPLACE"

collectProjectTable="COLL_PROJ"

projectTable="PROJECT"
projectID="PROJID"
projectName="PROJNAME"
projectCreateTime="CREATETIME"
projectStatus="STATUS"

indexPostfix="_Index"
documentPostfix="_document"
uniqueAuthorPostfix="_uniqueauthor"
authorPostfix="_author"
somMetaPostfix="_sommeta"
somCodPostfix="_somcod"
somInputPostfix="_sominput"
somDocIDsPostfix="_somdocids"
somTermPostfix="_somterm"



class AMmanager:
    """Abstract Map Manager Class
    
    >>>am=AMmanager("Scott", "tiger", "abstract")
    >>>am.open()
    >>>am.deleteCollection()
    >>>number=len(am.collections())
    >>>am.insertCollection()
    >>>len(am.collections())-number
    1
    >>>am.deleteCollection()
    >>>len(am.collections())-number
    0
    >>>am.close()
    """    
    def __init__(self,user="scott",password="tiger",database="abstract"):
        self.user=user
        self.password=password
        self.database=database

    #basic I/O
    def open(self):
        self.connection=cx_Oracle.Connection("%s/%s@%s" % (self.user,self.password,self.database))
        self.cursor=cx_Oracle.Cursor(self.connection)

    def close(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.cursor.execute("COMMIT")

     
    #table creation
    #creates all the tables for a document
    def createDocumentTables(shortName, ID):
        self.createDocumentTable(shortName, ID)
        self.createUniqueAuthorTable(shortName)
        self.createAuthorTable(shortName)

    #creates the index table for a collection    
    def createIndexTable(self, shortName):
        tableName=shortName+indexPostfix
        self.cursor.execute("CREATE TABLE "+tableName+" ( docidsAfterFilt CLOB,\
                            keywordsAfterFilt CLOB, \
                            FilteredIndex CLOB, \
                            shortname VARCHAR2(40) NOT NULL)")
        self.commit()

    #creates the doucment table for a collection
    def createDocumentTable(self, shortName, ID):
        tableName = shortName + documentPostfix
        self.cursor.execute("CREATE TABLE "+tableName+" \
                            (docid VARCHAR2(50) NOT NULL, \
                            collid VARCHAR2(40) NOT NULL, \
                            title VARCHAR2(300), \
                            stmtitle VARCHAR2(300), \
                            absttext CLOB, \
                            stmabsttext CLOB, \
                            fulltext CLOB, \
                            stmfulltext CLOB, \
                            keywords VARCHAR2(200), \
                            stmkeywords VARCHAR2(200), \
                            primary key(docid), \
                            foreign key(collid) references collection(collid)\
                            ON DELETE CASCADE)")
        self.commit()

    #creates the unique author table for a collection
    def createUniqueAuthorTable(self, shortName):
        tableName = shortName + uniqueAuthorPostfix
        self.cursor.execute("CREATE TABLE " + tablename +\
                            "(uniqueid NUMBER NOT NULL,\
                            fname VARCHAR2(50), lname VARCHAR2(50), \
                            primary key(uniqueid))")
        self.commit()

    #creates the author table for a collection
    def createAuthorTable(self, shortName):
         tablename = shortname + authorPostfix
         #for some reason it wouldn't let me use line continuations
         stmt="CREATE TABLE " + tablename
         stmt+="(docid VARCHAR2(50) NOT NULL, uniqueid NUMBER NOT NULL, "
         stmt+="name VARCHAR2(100), address VARCHAR2(500), "
         stmt+="email VARCHAR2(100), primary key(docid, uniqueid), "
         stmt+="foreign key(docid) references "
         stmt+=shortname + documentPostfix
         stmt+="(docid) ON DELETE CASCADE, foreign key(uniqueid) references "
         stmt+=shortname + uniqueauthorPostfix +"(uniqueid))"
         
         self.cursor.execute(stmt)

    #creates all the tables for a project
    def createProjectTables(self,ID):
        self.createSomMetaTable(ID+somMetaPostfix)
        self.createSomCodTable(ID)
        self.createSomInputTable(ID)
        self.createSomDocIDsTable(ID)
        self.createSomTermTable(ID)

    #deletes all the tables for a project
    def deleteProjectTables(self,ID):
        self.deleteTable(ID+somMetaPostfix)
        self.deleteTable(ID+somCodPostfix)
        self.deleteTable(ID+somInputPostfix)
        self.deleteTable(ID+somDocIDsPostfix)
        self.deleteTable(ID+somTermPostfix)
        self.deleteTable(ID+indexPostfix)

    #deletes a single table
    def deleteTable(self,ID):
        self.cursor.execute("DROP TABLE " + ID + " CASCADE CONSTRAINTS")
        self.commit()

    def deleteTableEntry(self,tableName,fieldID,ID):
        self.cursor.execute("DELETE FROM TABLE " + tableName + " WHERE "+fieldID+" = " +  "\'" + ID + "\'")
        self.commit()

    def createSomMetaTable(self,ID):
        self.cursor.execute("CREATE TABLE " + ID + somMetaPostfix +\
                            " (somid VARCHAR2(15) NOT NULL, \
                            dimen NUMBER, \
                            topo VARCHAR2(100), \
                            nrow NUMBER, \
                            ncol NUMBER, \
                            tform VARCHAR2(10), \
                            creatime DATE)")
        self.commit()

    def createSomCodTable(self):
        self.commit()

    def createSomInputTable(self):
        self.commit()

    def createSomDocIDsTable(self):
        self.commit()

    def createSomTermTable(self):
        self.commit()

      
    #accessors
    def collections(self):
        self.cursor.execute("SELECT "+collectionID+" FROM "+collectionTable)
        return [i[0] for i in self.cursor.fetchall()]

    def projects(self):
        self.cursor.execute("SELECT "+projectID+" FROM "+projectTable)
        return [i[0] for i in self.cursor.fetchall()]

    #modifiers
    
    def insertCollection(self,shortName="Example",year=2007,number=1,fullName="NULL",place="NULL"):
        ID=str(shortName)+"-"+str(year)+"-"+str(number)
        self.cursor.execute("INSERT INTO "+collectionTable+" values "+\
                            str((ID,shortName,year,number,fullName,place)))
        self.commit()

    def deleteCollection(self,ID="Example-2007-1"):
        self.cursor.execute("DELETE FROM "+collectionTable+" WHERE "+collectionID+" = \'"+ID+"\'")
        self.commit()
        
    def insertDocument(self):
        self.commit()

    def deleteDocument(self):
        self.commit()

    #order dependent insertion
    def insertProject(self,ID,name="NULL",time="NULL",status="NULL"):
        self.cursor.execute("INSERT INTO "+projectTable+" values "+str((ID,name,time,status)))
        self.commit()

    def deleteProject(self,ID="Example"):
        self.cursor.execute("DELETE FROM "+projectTable+" WHERE "+projectID+" = \'"+ID+"\'")
        self.commit()

if __name__ == "__main__":
    pass
##    am=AMmanager()
##    am.open()
##    am.createIndexTable("IndexTableTest")
##    am.close()
