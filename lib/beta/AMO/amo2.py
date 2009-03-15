
#Martin Lacayo-Emery
import cols

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
        return self.collection.Collections()

    def StemmedCollections(self):
        return self.collection.StemmedCollections()

    def ProjectManager(self):
        print "Project Manager"

    def Viewer(self):
        print "Viewer"
    
    
if __name__=="__main__":
    app=AMO()
    app.Menu()
            