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

    def dropCollectionTable(self):
        self.cursor.execute("drop table collection cascade constraints;")
        self.commit()

    def dropProjectTable(self):
        self.cursor.execute("drop table project cascade constraints;")
        self.commit()

    def dropCollectionProjectTable(self):
        self.cursor.execute("drop table coll_proj cascade constraints;")
        self.commit()

    def recreateCollectionTables(self):
        self.dropCollectionTable()
        self.dropProjectTable()
        self.dropCollectionProjectTable()
        self.createCollectionTable()
        self.createProjectTable()
        self.createCollectionProjectTable()

    def dropCollectionDocumentTable(self):
        self.cursor.execute("drop table coll_document cascade constraints;")
        self.commit()

    def dropCollectionAuthorTable(self):        
        self.cursor.execute("drop table coll_author cascade constraints;")
        self.commit()

    def dropCollectionUniqueAuthorTable(self):        
        self.cursor.execute("drop table coll_uniqueauthor cascade constraints;")
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

    def recreateDocumentTables(self):
        self.dropCollectionDocumentTable()
        self.dropCollectionAuthorTable()
        self.dropCollectionUniqueAuthorTable()
        self.createCollectionDocumentTable()
        self.createCollectionUniqueAuthorTable()
        self.createCollectionAuthorTable()

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

    def recreateProjectTables():
        pass
        
        
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
        print stmt
        self.cursor.execute(stmt)
        self.commit()

    def deleteCollection(self,ID="Example-2007-1"):
        self.cursor.execute("DELETE FROM "+collectionTable+" WHERE "+collectionID+" = \'"+ID+"\'")
        self.commit()
        
    def insertDocument(self):
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

if __name__ == "__main__":
    am=AMmanager()
    am.open()
    for n in am.listCollections():
        print n[0]
    #am.close()
