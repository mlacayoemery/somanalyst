class RecordHeader:
    def __init__ (self,location,length):
        self.location=location
        self.length=length

    def __str__ (self):
        return struct.pack('>i',location)+struct.pack('>i',length)
    