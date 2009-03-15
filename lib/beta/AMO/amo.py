
#Martin Lacayo-Emery
import cols, pickle

class AMO:
    def __init__(self):
        self.collection=cols.CollectionManager()

    def Menu(self):        
        print "Welcome to Abstract Map Open 1.0"
        task=""
        
        while task != "4":
            print
            print "Select a task:"
            print "[1]Collection Manager"
            print "[2]Project Manager"
            print "[3]Viewer"
            print "[4]Exit"
            print "option: ",
            task=raw_input()

            if task == "1":
                self.CollectionManager()
            elif task == "2":
                self.ProjectManager()
            elif task == "3":
                self.Viewer()
        print
        print "Thank you for using Abstract Map Open"

    def CollectionManager(self):
        print "Collection Manager"
        task=""
        exit="6"

        #save a list of the collections
        c=self.Collections()
        c.sort()
     
        while task != exit:
            print
            print "Select a task:"
            print "[1]List Collections"
            print "[2]Insert Collection"
            print "[3]Stem Collection"
            print "[4]Print Collections"
            print "[5]Save Stemmed Collection"
            print "["+exit+"]Return to Main Menu"
            print "option: ",
            task=raw_input()

            if task == "1":
                c=self.Collections()
                if len(c)==0:
                    print "There are no collections"
                else:
                    print "collections: ",
                    for i in c:
                        print i+" ",
            elif task == "2":
                print "Enter in the path for the ISI formatted file:"
                print "The example document will be inserted"
                iName="d:/gregg/file1.txt"
                iFile=open(iName)
                cID,dictionary=self.collection.AMOparse(iFile)
                iFile.close()
                self.collection.Insert(cID,dictionary)

                #update the list of collections
                c=self.Collections()
                c.sort()                
            elif task == "3":
                print "Select a collection:"
                for id,n in enumerate(c):
                    print "["+str(id)+"]"+n
                print "option: ",
                i=int(raw_input())
                self.collection.Stem(c[i])
            elif task == "4":
                print self.collection.collections
            elif task == "5":
                print "Select a collection:"
                for id,n in enumerate(c):
                    print "["+str(id)+"]"+n
                print "option: ",
                i=int(raw_input())
                oDat="d:/gregg/amo_dat.txt"
                oStems="d:/gregg/amo_stems.txt"
                stemField='DC'
                #construct the collection dictionary            
                stems=set([])
                for d in self.collection.collections[c[i]]['stems'].keys():
                    map(stems.add,self.collection.collections[c[i]]['stems'][d][stemField].keys())
                stems=list(stems)
                stems.sort()
                    
                #write the dictionary
                ofile=open(oStems,'w')
                for s in stems:
                    ofile.write(self.collection.porter.indexStems[s])
                    ofile.write(' ')
                ofile.close()

                #write the data                
                ofile=open(oDat,'w')
                ofile.write(str(len(stems)))
                ofile.write('\n')

                #for each document in the collection                
                for d in self.collection.collections[c[i]]['stems'].keys():
                    #check for each stem in collection
                    for s in stems:
                        if self.collection.collections[c[i]]['stems'][d][stemField].has_key(s):
                            ofile.write(str(self.collection.collections[c[i]]['stems'][d][stemField][s]))
                            ofile.write(' ')
                        else:
                            ofile.write('0 ')
                    ofile.write('\n')
                ofile.close()
                
                
    def Collections(self):
        collectionNames = self.collection.Collections()
        collectionNames.sort()
        return collectionNames

    def StemmedCollections(self):
        collectionNames= self.collection.StemmedCollections()
        collectionNames.sort()
        return collectionNames

    def ProjectManager(self):
        print "Project Manager"

    def Viewer(self):
        print "Viewer"

    def Save(self,fileName):
        ofile=open(fileName,'w')
        #store collection database
        pickle.dump(self.collection.collections,ofile)
        #store stemming data
        pickle.dump(self.collection.porter.stems,ofile)
        pickle.dump(self.collection.porter.indexStems,ofile)
        pickle.dump(self.collection.porter.stemCount,ofile)
        pickle.dump(self.collection.porter.stemFrequency,ofile)                          
        ofile.close()

    def Load(self,fileName):
        ifile=open(fileName)
        #store collection database
        self.collection.collections=pickle.load(ifile)
        #store stemming data
        self.collection.porter.stems=pickle.load(ifile)
        self.collection.porter.indexStems=pickle.load(ifile)
        self.collection.porter.stemCount=pickle.load(ifile)
        self.collection.porter.stemFrequency=pickle.load(ifile)  
        ifile.close()

    def InsertCollection(self,fileName):
        iFile=open(fileName)
        cID,dictionary=self.collection.AMOparse(iFile)
        iFile.close()
        self.collection.Insert(cID,dictionary)

    def StemCollection(self,collectionName):
        self.collection.Stem(collectionName)

    def StemFields(self,collectionName):
        documentFieldKey=self.collection.collections[collectionName]["stems"].keys()[0]
        return list(self.collection.collections[collectionName]["stems"][documentFieldKey].keys())

    def ExportStemmedCollection(self,oStems,oDat,collectionName,stemField):
        stems=set([])
        for d in self.collection.collections[collectionName]['stems'].keys():
            map(stems.add,self.collection.collections[collectionName]['stems'][d][stemField].keys())
        stems=list(stems)
        stems.sort()
        
        ofile=open(oStems,'w')
        for s in stems:
            ofile.write(self.collection.porter.indexStems[s])
            ofile.write(' ')
        ofile.close()        

        #write the data                
        ofile=open(oDat,'w')
        ofile.write(str(len(stems)))
        ofile.write('\n')

        #for each document in the collection
        documents=self.collection.collections[collectionName]['stems'].keys()
        documents.sort()
        for d in documents:
            #check for each stem in collection
            for s in stems:
                if self.collection.collections[collectionName]['stems'][d][stemField].has_key(s):
                    ofile.write(str(self.collection.collections[collectionName]['stems'][d][stemField][s]))
                    ofile.write(' ')
                else:
                    ofile.write('0 ')
            ofile.write('\n')
        ofile.close()

    def StemCount(self):
        return self.collection.porter.stemCount

    def StemFrequency(self,i):
        return self.collection.porter.stemFrequency[i]

    def StemKeys(self):
        return self.collection.porter.stemFrequency.keys()                      

    def DeleteStem(self,stemName):
        self.collection.porter.deleteStem(stemName)
        
    
    
if __name__=="__main__":
    app=AMO()
    app.Menu()
            