class Document:
    def __init__(self, ID, contents):
        self.ID=ID
        self.contents=contents

    def __getitem__(self,index):
        return self.contents.__getitem__(index)

class Collection    

class ISIdocument(Document):    

    