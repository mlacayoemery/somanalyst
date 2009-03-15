
#input: a codebook file open for ascii reading, or explicit parameters
#paramters
#topo is the topology of the codebook
#x is the number of neurons in the x dimension
#y is the number of neurons in the y dimension
#hood is the neighborhood type
#nodes is the list of lists containg the dimenison weights
#name is the display name of the codebook
#rnd is the number of digits to which the dimension weights are rounded

class Codebook:
    def __init__ (self, dim, topo="", x=-1, y=-1, hood="", nodes=[],name=""):
        if type(dim)==int:
            self.dim=dim
            self.topo=topo
            self.x=x
            self.y=y
            self.hood=hood
            self.nodes=nodes
        elif type(dim)==file:
            format=dim.readline().split()
            self.dim=int(format[0])
            self.topo=format[1]
            self.x=int(format[2])
            self.y=int(format[3])
            self.hood=format[4]
            self.nodes=[map(float,i.split()) for i in dim.readlines()]
            
        #create name of parameters joined with spaces
        if name == "":
            self.name=" ".join(map(str,[self.dim,self.topo,self.x,self.y,self.hood]))
        else:
            self.name=name

    def __str__ (self):
        return self.name

    def __getitem__ (self,i):
        return self.nodes[i]

    def __len__ (self):
        return len(self.nodes)
    