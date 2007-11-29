import sys
import xml.dom.ext
 

# create Reader object
reader = Sax2.Reader()

# parse the document
f = open("D:/data/example.xml",'r')
doc = reader.fromStream(f)
f.close()
xml.dom.ext.PrettyPrint(doc)

walker = doc.createTreeWalker(doc.documentElement,4294967295L, None, 0)

while 1:
    print walker.currentNode.tagName
    next = walker.nextNode()
    if next is None: break


