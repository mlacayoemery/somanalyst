#Martin Lacayo-Emery
import lstem

class CollectionManager:
    def __init__(self):
        self.collections={}
        self.porter=lstem.Lstem()

    def Collections(self):\
        return self.collections.keys()

    def StemmedCollections(self):
        collections=self.collections.keys()
        stemmed=[]
        for collection in collections:
            if self.collections[collection].has_key('stems'):
                stemmed.append(collection)
        return stemmed

    def Insert(self,name,dictionary):
        self.collections[name]=dictionary

    #parsers ISI style data
    #first field data is collection identifier
    #first block is collection data
    #subsequent blocks documents
    #first field data is document identifier
    def ISIparse(self,iFile):
        blocks=''.join(iFile.readlines()).split("\n\n")
        id,d=self.ISIblockParse(blocks[0].split("\n"))

        d['docs']={}
        for b in blocks[1:]:
            i,b=self.ISIblockParse(b.split("\n"))
            d['docs'][i]=b
            
        return id,d

    #ISIparse helper function that parses a text block
    def ISIblockParse(self,block):
        d={}
        id=block[0][3:]
        for l in block:
            d[l[:2]]=l[3:].strip()
        return id,d
    
    #entries are separated by blank lines
    #the first entry is the collections name
    def AMOparse(self,iFile):
        d={}
        #separate the file out into blocks delimited by '\n\n', and lines within
        #blocks are delimited by '\n'
        blocks=[b.split('\n') for b in ''.join(iFile.readlines()).split('\n\n')]

        #remove the collection data from the document list
        col=blocks[0]
        blocks=blocks[1:]

        #set the collection id to the value from the first field
        cID=col[0][3:]

        #store the collection fields
        for i in col:
            d[i[:2]]=i[3:].strip()
     
        docs={}
        #separate out document data
        for b in blocks:
            #create a dictionary for the document
            bID=b[0][3:]
            docs[bID]={}
            #store each field in the document dictionary
            for l in b:
                docs[bID][l[:2]]=l[3:].strip()
        d['docs']=docs

        return cID,d        
                
        

    #stems a document in the collection
    #creates a new field in the dictionary called stem
    def Stem(self,name):
        s={}
        for k in self.collections[name]['docs'].keys():
            s[k]={}
            for l in self.collections[name]['docs'][k].keys():
                s[k][l]=self.porter.Stem(self.collections[name]['docs'][k][l])
        self.collections[name]["stems"]=s

def ISIvalidate(lines):
    for l in lines:
        if len(l) > 1:
            if l[2] != ' ':
                return False
        elif l != "\n":
            return False
    return True    