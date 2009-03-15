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

    #table recreation (ie drop then add)
    def recreateCollectionTables(self):
        self.dropCollectionTable()
        self.dropProjectTable()
        self.dropCollectionProjectTable()
        self.createCollectionTable()
        self.createProjectTable()
        self.createCollectionProjectTable()

    def recreateDocumentTables(self):
        self.dropCollectionDocumentTable()
        self.dropCollectionAuthorTable()
        self.dropCollectionUniqueAuthorTable()
        self.createCollectionDocumentTable()
        self.createCollectionUniqueAuthorTable()
        self.createCollectionAuthorTable()

    def recreateProjectTables(self):
        self.dropProjectSOMMetaTable()
        self.dropProjectSOMCODTable()
        self.dropProjectSOMTermTable()
        self.dropProjectSOMDocumentTable()
        self.dropProjectSOMInputTable()
        self.createProjectSOMMetaTable()
        self.createProjectSOMCODTable()
        self.createProjectSOMTermTable()
        self.createProjectSOMDocumentTable()
        self.createProjectSOMInputTable()
     
    #table creation
    #base tables
    def createCollectionTable(self):
        stmt="""create table collection(
            collid varchar2(40) not null,
            shortname varchar2(20) not null,
            collyear number not null,
            collnum number not null,
            fullname varchar2(200),
            collplace varchar2(200),
            primary key(collid)
        );"""
        self.cursor.execute(stmt)
        self.commit()
        
    def createProjectTable(self):
        stmt="""create table project(
            projid varchar2(20) not null,
            projname varchar2(100),
            creatime date,
            status varchar2(20),
            primary key(projid)
        );"""
        self.cursor.execute(stmt)
        self.commit()

    #paired tables
    def createCollectionProjectTable(self):
        stmt="""create table coll_proj(
            collid varchar2(40) not null,
            projid varchar2(20) not null,
            primary key(collid, projid),
            foreign key(collid) references collection(collid),
            foreign key(projid) references project(projid) on delete cascade
        );"""
        self.cursor.execute(stmt)
        self.commit()

    def createCollectionDocumentTable(self):
        stmt="""create table coll_document(
            docid varchar2(12) not null,
            collid varchar2(20) not null,
            title varchar2(300),
            stmtitle varchar2(300),
            absttext clob,
            stmabsttext clob,
            fulltext clob,
            stmfulltext clob,
            keywords varchar2(200),
            stmkeywords varchar2(200),
            primary key(docid),
            foreign key(collid) references collection(collid) on delete cascade
        );"""
        self.cursor.execute(stmt)
        self.commit()

    def createCollectionUniqueAuthorTable(self):
        stmt="""create table coll_uniqueauthor(
            uniqueid number not null,
            fname varchar2(50),
            lname varchar2(50),
            primary key(uniqueid)
        );"""
        self.cursor.execute(stmt)
        self.commit()

    def createCollectionAuthorTable(self):
        stmt="""create table coll_author(
            docid varchar2(12) not null,
            uniqueid number not null,
            name varchar2(100),
            address varchar2(500),
            email varchar2(100),
            primary key(docid, uniqueid),
            foreign key(docid) references coll_document(docid) on delete cascade,
            foreign key(uniqueid) references coll_uniqueauthor(uniqueid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()

    def createProjectSOMMetaTable(self):
        stmt="""create table proj_sommeta(
                somid varchar2(15) not null,
                dimen number,
                topo varchar2(10),
                nrow number,
                ncol number,
            tform varchar2(10),
            creatime date;
                primary key(somid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()

    def createProjectSOMCODTable(self):   
        stmt="""create table proj_somcod(
            somid varchar2(15) not null,
            nind number not null,
            rowdata clob,
            primary key(somid, nind),
            foreign key(somid) references proj_sommeta(somid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()

    def createProjectSOMTermTable(self):      
        stmt="""create table proj_sominput(
            somid varchar2(25) not null,
            dind number not null,
            docid varchar2(12) not null,
            rowdata clob,
            primary key(somid, dind),
            foreign key(somid) references proj_sommeta(somid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()
    def createProjectSOMDocumentIDTable(self):
        stmt="""create table proj_somdocids(
            somid varchar2(15) not null,
            docids clob,
            primary key(somid),
            foreign key(somid) references proj_sommeta(somid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()
        
    def createProjectSOMInputTable(self):    
        stmt="""create table proj_somterm(
            somid varchar2(15) not null,
            termdata clob,
            primary key(somid),
            foreign key(somid) references proj_sommeta(somid)
        );"""        
        self.cursor.execute(stmt)
        self.commit()

    #table dropping
    #base tables
    def dropCollectionTable(self):
        self.cursor.execute("drop table collection cascade constraints;")
        self.commit()

    def dropProjectTable(self):
        self.cursor.execute("drop table project cascade constraints;")
        self.commit()

    #paired tables
    def dropCollectionProjectTable(self):
        self.cursor.execute("drop table coll_proj cascade constraints;")
        self.commit()

    def dropCollectionDocumentTable(self):
        self.cursor.execute("drop table coll_document cascade constraints;")
        self.commit()

    def dropCollectionAuthorTable(self):        
        self.cursor.execute("drop table coll_author cascade constraints;")
        self.commit()

    def dropCollectionUniqueAuthorTable(self):        
        self.cursor.execute("drop table coll_uniqueauthor cascade constraints;")
        self.commit()

    def dropProjectSOMMetaTable(self):
        self.cursor.execute("drop table proj_sommeta cascade constraints;")
        self.commit()

    def dropProjectSOMCODTable(self):        
        self.cursor.execute("drop table proj_somcod cascade constraints;")
        self.commit()

    def dropProjectSOMTermTable(self):      
        self.cursor.execute("drop table proj_somterm cascade constraints;")
        self.commit()

    def dropProjectSOMDocumentIDTable(self):
        self.cursor.execute("drop table proj_somdocids cascade constraints;")
        self.commit()

    def dropProjectSOMInputTable(self):        
        self.cursor.execute("drop table proj_sominput cascade constraints;")
        self.commit()


   
        
    #creates all the tables for a document
    def createDocumentTables(self, shortName, ID):
        self.__createDocumentTable(shortName, ID)
        self.__createUniqueAuthorTable(shortName)
        self.__createAuthorTable(shortName)

    def dropDocumentTables(self, shortName):
        self.__dropDocumentTable(shortName)
        self.__dropUniqueAuthorTable(shortName)
        self.__dropAuthorTable(shortName)

    def __dropDocumentTable(self,shortName):
        try:
            self.cursor.execute("drop table "+str(shortName + documentPostfix)+" cascade constraints")
            self.commit()
        except cx_Oracle.DatabaseError:
            pass

    def __dropUniqueAuthorTable(self,shortName):
        try:
            self.cursor.execute("drop table "+str(shortName + uniqueAuthorPostfix)+" cascade constraints")
            self.commit()
        except cx_Oracle.DatabaseError:
            pass

    def __dropAuthorTable(self, shortName):
        try:
            self.cursor.execute("drop table "+str(shortName + authorPostfix)+" cascade constraints")
            self.commit()
        except cx_Oracle.DatabaseError:
            pass
        
    #creates the index table for a collection    
    def createIndexTable(self, shortName):
        tableName=shortName+indexPostfix
        print tableName
        self.cursor.execute("CREATE TABLE "+tableName+" ( docidsAfterFilt CLOB,\
                            keywordsAfterFilt CLOB, \
                            FilteredIndex CLOB, \
                            shortname VARCHAR2(40) NOT NULL)")
        self.commit()

    #creates the doucment table for a collection
    def __createDocumentTable(self, shortName, ID):
        tableName = shortName + documentPostfix
        self.cursor.execute("CREATE TABLE "+str(tableName)+" \
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
    def __createUniqueAuthorTable(self, shortName):
        tableName = shortName + uniqueAuthorPostfix
        self.cursor.execute("CREATE TABLE " + tableName +\
                            "(uniqueid NUMBER NOT NULL,\
                            fname VARCHAR2(50), lname VARCHAR2(50), \
                            primary key(uniqueid))")
        self.commit()

    #creates the author table for a collection
    def __createAuthorTable(self, shortName):
         tablename = shortName + authorPostfix
         #for some reason it wouldn't let me use line continuations
         stmt="CREATE TABLE " + tablename
         stmt+="(docid VARCHAR2(50) NOT NULL, uniqueid NUMBER NOT NULL, "
         stmt+="name VARCHAR2(100), address VARCHAR2(500), "
         stmt+="email VARCHAR2(100), primary key(docid, uniqueid), "
         stmt+="foreign key(docid) references "
         stmt+=shortName + documentPostfix
         stmt+="(docid) ON DELETE CASCADE, foreign key(uniqueid) references "
         stmt+=shortName + uniqueAuthorPostfix +"(uniqueid))"
         
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
        stmt="INSERT INTO "+collectionTable+" values (\'"+ID+"\', "
        stmt+="\'"+str(shortName)+"\', "+str(year)+", "+str(number)+", "
        if fullName==None:
            stmt+="NULL, "
        else:
            stmt+="\'"+str(fullName)+"\', "
        if place==None:
            stmt+="NULL)"
        else:
            stmt+="\'"+str(place)+"\')"
        self.cursor.execute(stmt)
        self.commit()

    def deleteCollection(self,ID="Example-2007-1"):
        self.cursor.execute("DELETE FROM "+collectionTable+" WHERE "+collectionID+" = \'"+ID+"\'")
        self.commit()
        
    def insertDocument(self,table,documentID,collectionID,title=None,stemTitle=None,abstract=None,stemAbstract=None,text=None,stemText=None,keywords=None,stemKeywords=None):      
        stmt="INSERT INTO "+table+" values(:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8,:v9,:v10)"
        self.cursor.execute(stmt,
                            v1=documentID,
                            v2=collectionID,
                            v3=title,v4=stemTitle,
                            v5=abstract,v6=stemAbstract,
                            v7=text,v8=stemText,
                            v9=keywords,v10=stemKeywords)
        self.commit()

    def deleteDocument(self):
        self.commit()

    def listCollections(self):
        self.cursor.execute("SELECT collid FROM collection")
        return self.cursor.fetchall()

    #order dependent insertion
    def insertProject(self,ID,name="NULL",time="NULL",status="NULL"):
        self.cursor.execute("INSERT INTO "+projectTable+" values "+str((ID,name,time,status)))
        self.commit()

    def deleteProject(self,ID="Example"):
        self.cursor.execute("DELETE FROM "+projectTable+" WHERE "+projectID+" = \'"+ID+"\'")
        self.commit()

    #returns a list where any None values are replaced with "NULL"
    def formatValueString(self,values):
        stmt="("
        if values[0]==None:
            stmt+="NULL"
        else:
            if type(values[0])==str:
                stmt+="\'"+values[0]+"\'"
            else:
                stmt+=values[0]
            
        for v in values[1:]:
            if v==None:
                stmt+=",NULL"
            else:
                stmt+=","
                if type(v)==str:
                    stmt+="\'"+v+"\'"
                else:
                    stmt+=v

        stmt+=")"
        return stmt
        
        

if __name__ == "__main__":
    am=AMmanager()
    am.open()
    for n in am.listCollections():
        print n[0]
    #am.close()
