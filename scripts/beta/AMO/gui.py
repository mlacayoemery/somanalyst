import easygui, sys, amo, pickle

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
                            stemField='DC'
                
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
                    if len(app.collection.porter.stemCount)==0:
                        easygui.msgbox("There are no stems.")
                    else:
                        stems=map(app.collection.porter.stems.__getitem__,app.collection.porter.indexStems)
                        stems=zip(stems,app.collection.porter.stemFrequency)
                        stems=map(str,stems)
                        easygui.choicebox("Stems",title,collections)

                #filter documents                
                elif collectionChoice==collectionChoices[5]:
                    pass
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
                ifile.close()