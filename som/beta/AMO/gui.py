import easygui, sys, amo, pickle

def padNum(num,pad):
    return ("0"*(pad-len(str(num))))+str(num)
      

    

if __name__=="__main__":
    app=amo.AMO()

    choice=""
    title ="Abstract Map Open 1.0"
    mainChoices = ["Collection Manager", "Project Manager", "Viewer", "Save State", "Load State","Exit"]
    collectionChoices = ["List Collections","Insert Collection",\
               "Stem Collection","Export Stemmed Collection","Filter Stems","Filter Collection","Return to Main Menu"]

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
                    if len(collections)==0:
                        easygui.msgbox("There are no collections")
                    else:
                        easygui.choicebox("Collections",title,collections)

                #insert a collection
                elif collectionChoice ==collectionChoices[1]:
                    iName=easygui.fileopenbox(argInitialFile="d:/users/gregg/file1.txt")
                    if iName!=None:
                        app.InsertCollection(iName)

                #stem a collection
                elif collectionChoice==collectionChoices[2]:
                    collections=app.Collections()
                    if len(collections)==0:
                        easygui.msgbox("There are no collections")
                    else:
                        collection=easygui.choicebox("Collections",title,collections)
                        if collection!=None:
                            app.StemCollection(collection)

                #save/export a stemmed collection
                elif collectionChoice==collectionChoices[3]:
                    collections=app.StemmedCollections()
                    if len(collections)==0:
                        easygui.msgbox("There are no stemmed collections.")
                    else:
                        collectionName=easygui.choicebox("Collections",title,collections)
                        if collectionName!=None:
                            #select the stem field to save
                            fields=app.StemFields(collection)
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

                            #write the stems and data
                            app.ExportStemmedCollection(oStems,oDat,collectionName,stemField)

                #filter stems
                elif collectionChoice==collectionChoices[4]:
                    if len(app.collection.porter.stemFrequency)==0:
                        easygui.msgbox("There are no stems.")
                    else:
                        #get the stem indicies in frequency order
                        #assert len(app.collection.porter.stemFrequency)==len(app.collection.porter.indexStems)
                        stems=[]
                        pad=len(str(app.StemCount()))
                        for k in app.StemKeys():
                            stems.append(padNum(app.StemFrequency(k),pad)+" "+k)

                        #select stems                        
                        stemFilter=easygui.multchoicebox("Select the stems to remove.",title,stems)

                        #delete selected stems                        
                        if stemFilter!=None:
                            stemFilter=[ s.split(' ')[1] for s in stemFilter]
                            #easygui.msgbox("you selected "+str(stemFilter))

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
                                app.DeleteStem(s)


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
                app.Save(oState)

        #Load State
        elif choice == mainChoices[4]:
            iState=easygui.fileopenbox(argInitialFile="d:/users/gregg/amo.dat")
            if iState !=None:
                app.Load(iState)