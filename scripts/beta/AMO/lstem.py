import porter

class Lstem:
    def __init__(self):
        self.p=porter.PorterStemmer()
        #do not put a " " in the ignoreChars
        self.ignoreChars=['~', '!', '@', '#', '$', '%', '^', '&', '*', '*', '*', \
                          '(', ')', '_', '+', '`', '1', '2', '3', '4', '5', '6', \
                          '7', '8', '9', '0', '0', '-', '=', '{', '}', '|', '[', \
                          ']', '\\', ':', '\"', ';', '\'', '<', '>', '?', ',', '.', '/',\
                          '\x85', '\x91', '\x92', '\x93', '\x94', '\x96', '\x97', \
                          '\x9c', '\xa3', '\xa7', '\xab', '\xbb', '\xc7', '\xe0', \
                          '\xe1', '\xe3', '\xe7', '\xe8', '\xe9', '\xea', '\xed', \
                          '\xf3', '\xf5', '\xf6', '\xfa', '\xfc', '\t']
        self.stopWords = set(['', 'all', 'six', 'less', 'being', 'indeed', 'over', 'move',\
             'anyway', 'cross', 'four', 'not', 'own', 'through', 'yourselves',\
             'fify', 'where', 'mill', 'only', 'find', 'before', 'one', 'whose',\
             'how', 'somewhere', 'much', 'thick', 'show', 'had', 'enough',\
             'should', 'to', 'must', 'whom', 'seeming', 'under', 'ours', 'has',\
             'might', 'thereafter', 'latterly', 'do', 'them', 'his', 'around',\
             'than', 'get', 'very', 'de', 'none', 'cannot', 'every', 'whether',\
             'they', 'front', 'during', 'thus', 'now', 'him', 'nor', 'name',\
             'several','hereafter', 'always', 'who', 'cry', 'whither', 'this',\
             'someone', 'either','each', 'become', 'thereupon', 'sometime',\
             'side', 'two', 'therein', 'twelve', 'because', 'often', 'ten',\
             'our', 'eg', 'some', 'back', 'up', 'go', 'namely', 'towards',\
             'are','further', 'beyond', 'ourselves', 'yet', 'out', 'even',\
             'will','what', 'still', 'for', 'bottom', 'mine', 'since', 'please',\
             'forty', 'per', 'its', 'everything', 'behind', 'un', 'above',\
             'between', 'it', 'neither', 'seemed', 'ever', 'across', 'she',\
             'somehow', 'be', 'we', 'full', 'never', 'sixty', 'however', 'here',\
             'otherwise', 'were', 'whereupon', 'nowhere', 'although', 'found',\
             'alone', 're', 'along', 'fifteen', 'by', 'both', 'about', 'last',\
             'would', 'anything', 'via', 'many', 'could', 'thence', 'put',\
             'against', 'keep', 'etc', 'amount', 'became', 'ltd', 'hence',\
             'onto', 'or', 'con', 'among', 'already', 'co', 'afterwards',\
             'formerly', 'within', 'seems', 'into', 'others', 'while',\
             'whatever', 'except', 'down', 'hers', 'everyone', 'done', 'least',\
             'another', 'whoever', 'moreover', 'couldnt', 'throughout', 'anyhow',\
             'yourself', 'three', 'from', 'her', 'few', 'mid', 'top', 'there',\
             'due', 'been', 'next', 'anyone', 'eleven', 'fought', 'call',\
             'therefore', 'interest', 'then', 'thru', 'themselves', 'hundred',\
             'was', 'sincere', 'empty', 'more', 'himself', 'elsewhere', 'mostly',\
             'on', 'fire', 'am', 'becoming', 'hereby', 'amongst', 'else', 'part',\
             'everywhere', 'too', 'herself', 'former', 'those', 'he', 'me',\
             'myself', 'made', 'twenty', 'these', 'bill', 'cant', 'us', 'until',\
             'besides', 'nevertheless', 'below', 'anywhere', 'nine', 'can', 'of',\
             'toward', 'my', 'something', 'and', 'whereafter', 'whenever', 'give',\
             'almost', 'wherever', 'is', 'describe', 'beforehand', 'herein', 'an',\
             'as', 'itself', 'at', 'have', 'in', 'seem', 'whence', 'ie', 'any',\
             'fill', 'again', 'hasnt', 'inc', 'thereby', 'thin', 'no', 'perhaps',\
             'latter', 'meanwhile', 'when', 'detail', 'same', 'wherein', 'beside',\
             'also', 'that', 'other', 'take', 'which', 'becomes', 'you', 'if',\
             'nobody', 'see', 'though', 'may', 'after', 'upon', 'most',\
             'hereupon', 'eight', 'but', 'serious', 'nothing', 'such', 'your',\
             'why', 'a', 'off', 'whereby', 'third', 'together', 'i', 'whole',\
             'noone', 'sometimes', 'well', 'amoungst', 'yours', 'their',\
             'rather', 'without', 'so', 'five', 'the', 'first', 'with',\
             'whereas', 'se', 'once'])
        #stores index value by stems
        self.stems={}
        #stores stems by index value
        self.indexStems={}
        self.stemCount=0
        self.stemFrequency={}
        
    def deleteStem(self,stem):
        #remove stem from dictioanry
        stemIndex=self.stems.pop(stem)
        #remove stem index
        self.indexStems.pop(stemIndex)
        #remove stem frequency
        self.stemFrequency.pop(stem)
  
    def charStrip(self,l):
        clean=""
        for c in l:
            if not (c in self.ignoreChars):
                clean+=c
            else:
                clean+=" "
        return clean

    def Stem(self,l):
        #the vector to store the stem count
        #stored as a stem key key: count
        v={}
        #loop through each word after stripping ignore Chars
        for word in [w.lower() for w in self.charStrip(l).split(" ")]:

            #if it is not a stop word stem it
            if not self.stopWords.issuperset(set([word])):
                s=self.p.stem(word,0,len(word)-1)

                #if it is a new stem then enumerate it
                if not self.stems.has_key(s):
                    self.stems[s]=self.stemCount
                    self.indexStems[self.stemCount]=s
                    self.stemCount+=1
                    self.stemFrequency[s]=0
                self.stemFrequency[s]+=1    
                #if the local vector does not have the stem
                if not v.has_key(self.stems[s]):
                    v[self.stems[s]]=1
                else:
                    v[self.stems[s]]+=1
        return v

    def stemList(self,stemKeys):
        words=[]
        for k in stemKeys:
            words.append(self.indexStems[k])
        return words

    def amStemList(self,stemDict):
        words=[]
        for k in stemDict.keys():
            for i in range(stemDict[k]):
                words.append(self.indexStems[k])
        return words

if __name__ == "__main__":
    l=Lstem()
    v=l.Stem("participate. introduction participate")
    print
    for k in l.stems.keys():
        print k
    print
    #l.deleteStem('particip')
    for k in l.stems.keys():
        print k
    print
    for k in v.keys():
        print l.indexStems[k], v[k]