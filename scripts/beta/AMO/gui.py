import easygui, sys, amo, pickle

def padNum(num,pad):
    return ("0"*(pad-len(str(num))))+str(num)
        
    

if __name__=="__main__":
    app=amo.AMO()

    choice=""
    title ="Abstract Map Open 1.0"
    mainChoices = ["Collection Manager", "Project Manager", "Viewer", "Save State", "Load State","Exit"]
    collectionChoices = ["List Collections","Insert Collection",\
               "Stem Collection","Save Stemmed Collection","Filter Stems","Filter Collection","Return to Main Menu"]

    while not (choice == "Exit"):
        choice = easygui.buttonbox("Main Menu", title, mainChoices)
        
        #Collection Manager Menu
        if choice == mainChoices[0]:
            collectionChoice=""
            while not (collectionChoice == collectionChoices[-1]):
                collectionChoice = easygui.buttonbox("Collection Manager", title, collectionChoices)

                #display collections
                if collectionChoice ==collectionChoices[0]:
                    collections=app.Collections()
                    collections.sort()
                    if len(collections)==0:
                        easygui.msgbox("There are no collections")
                    else:
                        easygui.choicebox("Collections",title,collections)

                #insert a collection
                elif collectionChoice ==collectionChoices[1]:
                    iName=easygui.fileopenbox(argInitialFile="d:/users/gregg/file1.txt")
                    if iName!=None:
                        iFile=open(iName)
                        cID,dictionary=app.collection.AMOparse(iFile)
                        iFile.close()
                        app.collection.Insert(cID,dictionary)

                #stem a collection
                elif collectionChoice==collectionChoices[2]:
                    collections=app.Collections()
                    collections.sort()
                    if len(collections)==0:
                        easygui.msgbox("There are no collections")
                    else:
                        collection=easygui.choicebox("Collections",title,collections)
                        if collection!=None:
                            app.collection.Stem(collection)

                #save a stemmed collection
                elif collectionChoice==collectionChoices[3]:
                    collections=app.StemmedCollections()
                    collections.sort()
                    if len(collections)==0:
                        easygui.msgbox("There are no stemmed collections.")
                    else:
                        collection=easygui.choicebox("Collections",title,collections)
                        if collection!=None:
                            #select the stem field to save
                            documentFieldKey=app.collection.collections[collection]["stems"].keys()[0]
                            fields=list(app.collection.collections[collection]["stems"][documentFieldKey].keys())
                            stemField=easygui.choicebox("Field",title,fields)
                
                            #select the ouput file for the vectors
                            easygui.msgbox("Choose an output file for the vectors.")
                            oDat=easygui.filesavebox(argInitialFile="d:/users/gregg/amo_dat.txt")
                            if oDat==None:
                               break


                            #select the output file for the stems                   
                            easygui.msgbox("Choose an output file for the stems.")
                            oStems=easygui.filesavebox(argInitialFile="d:/users/gregg/amo_stems.txt")
                            if oStems==None:
                                break


                            #construct the collection dictionary            
                            stems=set([])
                            for d in app.collection.collections[collection]['stems'].keys():
                                map(stems.add,app.collection.collections[collection]['stems'][d][stemField].keys())
                            stems=list(stems)
                            stems.sort()
                                
                            #write the dictionary
                            ofile=open(oStems,'w')
                            for s in stems:
                                ofile.write(app.collection.porter.indexStems[s])
                                ofile.write(' ')
                            ofile.close()

                            #write the data                
                            ofile=open(oDat,'w')
                            ofile.write(str(len(stems)))
                            ofile.write('\n')

                            #for each document in the collection
                            documents=app.collection.collections[collection]['stems'].keys()
                            documents.sort()
                            for d in documents:
                                #check for each stem in collection
                                for s in stems:
                                    if app.collection.collections[collection]['stems'][d][stemField].has_key(s):
                                        ofile.write(str(app.collection.collections[collection]['stems'][d][stemField][s]))
                                        ofile.write(' ')
                                    else:
                                        ofile.write('0 ')
                                ofile.write('\n')
                            ofile.close()

                #filter stems
                elif collectionChoice==collectionChoices[4]:
                    if len(app.collection.porter.stemFrequency)==0:
                        easygui.msgbox("There are no stems.")
                    else:
                        #get the stem indicies in frequency order
                        #assert len(app.collection.porter.stemFrequency)==len(app.collection.porter.indexStems)
                        stems=[]
                        pad=len(str(app.collection.porter.stemCount))
                        for i in app.collection.porter.stemFrequency.keys():
                            stems.append(padNum(app.collection.porter.stemFrequency[i],pad)+" "+
                                         app.collection.porter.indexStems[app.collection.porter.stems[i]])

                                
                        #select stems                        
                        stemFilter=easygui.multchoicebox("Select the stems to remove.",title,stems)

                        #delete selected stems                        
                        if stemFilter!=None:
                            stemFilter=[ s.split(' ')[1] for s in stemFilter]
                            easygui.msgbox("you selected "+str(stemFilter))

                            #delete from documents
                            #for each collection
                            for c in app.collection.collections.keys():
                                #for each document
                                for d in app.collection.collections[c]['stems'].keys():
                                    #for each field
                                    for f in app.collection.collections[c]['stems'][d].keys():
                                        #for each stem filter
                                        for s in stemFilter:
                                            if app.collection.collections[c]['stems'][d][f].has_key(app.collection.porter.stems[s]):
                                                app.collection.collections[c]['stems'][d][f].pop(app.collection.porter.stems[s])

                            #delete from porter
                            for s in stemFilter:
                                app.collection.porter.deleteStem(s)


                #filter documents                
                elif collectionChoice==collectionChoices[5]:
                    easygui.msgbox("Sorry. The Document Filter is currenly under development.")
        #Project Manager Menu
        elif choice == mainChoices[1]:
            easygui.msgbox("Sorry. The Project Manager is currenly under development.")

        #Viewer Menu
        elif choice == mainChoices[2]:
            easygui.msgbox("Sorry. The Viewer is currenly under development.")

        #Save State
        elif choice == mainChoices[3]:
            oState=easygui.filesavebox(argInitialFile="d:/users/gregg/amo.dat")
            if oState!=None:
                ofile=open(oState,'w')
                #store collection database
                pickle.dump(app.collection.collections,ofile)
                #store stemming data
                pickle.dump(app.collection.porter.stems,ofile)
                pickle.dump(app.collection.porter.indexStems,ofile)
                pickle.dump(app.collection.porter.stemCount,ofile)
                pickle.dump(app.collection.porter.stemFrequency,ofile)                          
                ofile.close()

        #Load State
        elif choice == mainChoices[4]:
            iState=easygui.fileopenbox(argInitialFile="d:/users/gregg/amo.dat")
            if iState !=None:
                ifile=open(iState)
                #store collection database
                app.collection.collections=pickle.load(ifile)
                #store stemming data
                app.collection.porter.stems=pickle.load(ifile)
                app.collection.porter.indexStems=pickle.load(ifile)
                app.collection.porter.stemCount=pickle.load(ifile)
                app.collection.porter.stemFrequency=pickle.load(ifile)  
                ifile.close()