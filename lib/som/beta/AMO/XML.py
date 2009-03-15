import xml.dom.minidom, string

TEXT_NODE = xml.dom.minidom.DocumentType.TEXT_NODE

#gets value from a leaf node list
#skips text node leafs
def getXMLValue(nodes):
    #ignore preceeding whitespace and get value
    if not nodes:
        return None
    if nodes[0].nodeType==TEXT_NODE:
        nodes.pop(0)
    node=nodes.pop(0).childNodes
    if len(node)==0:
        return None
    else:
        return node[0].nodeValue
    
class Date:
    def __init__(self,year=None,month=None,day=None):
        self.year=year
        self.month=month
        self.day=day

    def __str__(self):
        return "/".join(map(str,(self.month,self.day,self.year)))

    def getXMLValue(self,nodes):
        try:
            return int(getXMLValue(nodes))
        #if value not integer return None
        except (TypeError, ValueError):
            return None

    def XMLnode(self,dateNode):
        nodes=dateNode.childNodes

        self.year=self.getXMLValue(nodes)
        self.month=self.getXMLValue(nodes)        
        self.day=self.getXMLValue(nodes)     

class Misc:
    def __init__(self,description=None,webpage=None,contact=None):
        self.description=description
        self.webpage=webpage
        self.contact=contact

    def __str__(self):
        return "\n".join(map(str,[self.description,self.webpage,self.contact]))

    def getXMLValue(self,nodes):
        try:
            value = getXMLValue(nodes).strip(string.whitespace)
        except AttributeError:
            return None
        
        if len(value):
            return value
        else:
            return None
                  
    def XMLnode(self,miscNode):
        nodes=miscNode.childNodes

        self.description=self.getXMLValue(nodes)
        self.webpage=self.getXMLValue(nodes)
        self.contact=self.getXMLValue(nodes)

class Author:
    def __init__(self,id=None,name=None,address=None,email=None):
        self.id=id
        self.name=name
        self.address=address
        self.email=email

    def getXMLValue(self,nodes):
        value = getXMLValue(nodes)
        #if not None, strip it and change to none if blank
        if value:
            #strip out the whitespace
            value=value.strip(string.whitespace)
            if not len(value):
                value=None
        return value

    def XMLnode(self,authorNode):
        nodes=authorNode.childNodes
        self.id=self.getXMLValue(nodes)
        self.name=self.getXMLValue(nodes)
        self.address=self.getXMLValue(nodes)
        self.email=self.getXMLValue(nodes)        
        
class Keywords:
    def __init__(self,keywords=None):
        self.keywords=keywords


    def XMLnode(self,keywordsNode):
        nodes=keywordsNode.childNodes
        words=[]

        #get a list of the keywords, ignoring blanks
        for i in range(len(nodes)):
            if nodes[0].nodeType==TEXT_NODE:
                nodes.pop(0)
            else:
                try:
                    value = nodes.pop(0).childNodes[0].nodeValue.strip(string.whitespace)
                    if len(value):
                        words.append(value)
                except:
                    #empty keyword tag
                    pass

        if len(words):
            self.keywords=words
        else:
            self.keywords=None

class Text:
    def __init__(self,abstract=None,fulltext=None):
        self.abstract=abstract
        self.fulltext=fulltext

    def XMLnode(self,textNode):
        nodes=textNode.childNodes

        self.abstract=getXMLValue(nodes)
        self.fulltext=getXMLValue(nodes)
        
class Document:
    def __init__(self,id=None,date=None,other=None,authors=None,
                 title=None,keywords=None,text=None,references=None):
        self.id=id
        self.date=date
        self.other=other
        self.title=title
        self.authors=authors
        self.keywords=keywords
        self.text=text
        self.references=references

    def XMLnode(self,documentNode):
        nodes=documentNode.childNodes

        self.id=getXMLValue(nodes)

        #skip text node and get date
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)        
        self.date=Date()
        self.date.XMLnode(nodes.pop(0))

        #skip text node and get other info
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)        
        self.other=Misc()
        self.other.XMLnode(nodes.pop(0))
        
        self.title=getXMLValue(nodes)

        #skip text node and create a list of all authors
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)
        authorsNode=nodes.pop(0).childNodes
        authors=[]
        for i in range(len(authorsNode)):
            if authorsNode[0].nodeType==TEXT_NODE:
                authorsNode.pop(0)
            else:
                author=Author()
                author.XMLnode(authorsNode.pop(0))
                authors.append(author)
        if len(authors):
            self.authors=authors
        else:
            self.authors=None

        #skip text node and create a list of keywords
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)            
        self.keywords=Keywords()
        self.keywords.XMLnode(nodes.pop(0))
        
       
        #skip text node and create text
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)            
        self.text=Text()
        self.text.XMLnode(nodes.pop(0))

        self.references=getXMLValue(nodes)

class Collection:
    def __init__(self,shortname=None,longname=None,id=None,place=None,date=None,other=None,documents=None):
        self.shortname=shortname
        self.longname=longname
        self.id=id
        self.place=place
        self.date=date
        self.other=other
        self.documents=documents

    def XMLnode(self,collectionNode):
        nodes=collectionNode.childNodes

        self.shortname=getXMLValue(nodes)
        self.longname=getXMLValue(nodes)
        self.id=getXMLValue(nodes)
        self.place==getXMLValue(nodes)
        
        #skip text node and get date
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)        
        self.date=Date()
        self.date.XMLnode(nodes.pop(0))
        
        #skip text node and get other info
        if nodes[0].nodeType==TEXT_NODE:
            nodes.pop(0)        
        self.other=Misc()
        self.other.XMLnode(nodes.pop(0))
        
        #skip text node and create documents
        docs=[]
        try:
            for i in range(len(nodes)):
                if nodes[0].nodeType==TEXT_NODE:
                    nodes.pop(0)
                else:
                    doc=Document()
                    doc.XMLnode(nodes.pop(0))
                    docs.append(doc)
        except:
            print "Document parsing error"
        if len(docs):
            self.documents=docs
        else:
            self.documents=None         

def parse(file):
    c=Collection()
    doc=xml.dom.minidom.parse(file)
    c.XMLnode(doc.childNodes[0].childNodes[0])
    return c


if __name__=="__main__":
    c=Collection()
    doc=xml.dom.minidom.parse("Z:/ISIfromEndNote/AMsewer.xml")
    c.XMLnode(doc.childNodes[0].childNodes[0])


##d=Document()
##d.XMLnode(doc.childNodes[0].childNodes[1].childNodes[19])