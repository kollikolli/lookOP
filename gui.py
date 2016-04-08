from Tkinter import *
from indexer import *

dummyData = {}
dummyData["neg"]={}
dummyData["pos"]={}
dummyData["neut"]={}

curPos=0
curNeut=0
curNeg=0
done = True


def next():
    global curPos,curNeut,curNeg
    if curPos < len(dummyData["pos"]["user"])-1:
        curPos+=1
    if curNeut < len(dummyData["neut"]["user"])-1:
        curNeut+=1
    if curNeg < len(dummyData["neg"]["user"])-1:
        curNeg+=1
    updateContent()

def prev():
    global curPos,curNeut,curNeg
    if (curPos > 0):
        curPos-=1
    if (curNeut > 0):
        curNeut-=1
    if (curNeg > 0):
        curNeg-=1
    updateContent()

def updateContent():
    global curItem,dummyData
    if(len(dummyData["pos"]["user"]) < 1):
        posTitle.set("No Results available")
        posTweet.set("--------------------")
    else:    
        posTitle.set(dummyData["pos"]["user"][curPos]+" on "+dummyData["pos"]["date"][curPos])
        posTweet.set(dummyData["pos"]["tweet"][curPos])
    if(len(dummyData["neut"]["user"]) < 1):
        neutTitle.set("No Results available")
        neutTweet.set("--------------------")
    else:
        neutTitle.set(dummyData["neut"]["user"][curNeut]+" on "+dummyData["neut"]["date"][curNeut])
        neutTweet.set(dummyData["neut"]["tweet"][curNeut])
    if(len(dummyData["neg"]["user"]) < 1):
        negTitle.set("No Results available")
        negTweet.set("--------------------")
    else:
        negTitle.set(dummyData["neg"]["user"][curNeg]+" on "+dummyData["neg"]["date"][curNeg])
        negTweet.set(dummyData["neg"]["tweet"][curNeg])
    posTxt=" "
    for i in range(int(dummyData["pos"]["rating"]*45)):
        posTxt=posTxt+" ";
    posTxt=posTxt+str(int(dummyData["pos"]["rating"]*100))+"%";
    for i in range(int(dummyData["pos"]["rating"]*45)):
        posTxt=posTxt+" ";
    neutTxt=" "
    for i in range(int(dummyData["neut"]["rating"]*45)):
        neutTxt=neutTxt+" ";
    neutTxt=neutTxt+str(int(dummyData["neut"]["rating"]*100))+"%";
    for i in range(int(dummyData["neut"]["rating"]*45)):
        neutTxt=neutTxt+" ";
    negTxt=" "
    for i in range(int(dummyData["neg"]["rating"]*45)):
        negTxt=negTxt+" ";
    negTxt=negTxt+str(int(dummyData["neg"]["rating"]*100))+"%";
    for i in range(int(dummyData["neg"]["rating"]*45)):
        negTxt=negTxt+" ";
    posLab.set(posTxt)
    neutLab.set(neutTxt)
    negLab.set(negTxt)

def query():
    global mainframe,posTitle,posTweet,neutTitle,neutTweet,negTitle,negTweet,dummyData,posLab,neutLab,negLab,done,curPos,curNeut,curNeg
   
    #print dummyData
    curPos=0
    curNeut=0
    curNeg=0
    dummyData["neg"]={}
    dummyData["pos"]={}
    dummyData["neut"]={}


    dummyData = lookop.query(e.get())
    if not done:
        updateContent()

    if "rating" in dummyData["pos"] and "rating" in dummyData["neg"] and "rating" in dummyData["neut"] and done:            
        done=False
        oplabel=Frame(mainframe)
        leftPad=dummyData["pos"]["rating"]*500-30
        if(leftPad<0):
            leftPad=0
        Label(oplabel, textvariable=posLab,bg="green").pack(side=LEFT,padx=(2,0))
        Label(oplabel, textvariable=neutLab,bg="grey").pack(side=LEFT,padx=(0,0))
        Label(oplabel, textvariable=negLab,bg="red").pack(side=LEFT,padx=(0,2))
        oplabel.pack(pady=(0,25))            



        results = Frame(mainframe)

        postxt = Frame(results,bd=1,relief=GROOVE,background="lightgreen")

        updateContent()

        Label(postxt, textvariable=posTitle,background="lightgreen").pack()
        Label(postxt, textvariable=posTweet,background="lightgreen").pack()
        postxt.pack(pady=(10,0))

        neuttxt = Frame(results,bd=1,relief=GROOVE,background="lightgrey")
        Label(neuttxt, textvariable=neutTitle,background="lightgrey").pack()
        Label(neuttxt, textvariable=neutTweet,background="lightgrey").pack()
        neuttxt.pack(pady=(10,0))

        negtxt = Frame(results,bd=1,relief=GROOVE,background="pink")
        Label(negtxt, textvariable=negTitle,background="pink").pack()
        Label(negtxt, textvariable=negTweet,background="pink").pack()
        negtxt.pack(pady=(10,20))

        prevB=Button(results,text="Previous Results",command=prev)
        nextB=Button(results,text="Next Results",command=next)
        prevB.pack(side=LEFT,padx=(170,0))
        nextB.pack(side=LEFT)
        results.pack()


app= Tk()
app.title("LookOP")
app.geometry("550x350+30+30")

posTitle=StringVar()
posTweet=StringVar()
neutTitle=StringVar()
neutTweet=StringVar()
negTitle=StringVar()
negTweet=StringVar()
posLab=StringVar()
negLab=StringVar()
neutLab=StringVar()

mainframe=Frame(app)

queryframe = Frame(mainframe,borderwidth=1,height=15)
e=Entry(queryframe)
querybutton=Button(queryframe,text="Search",width=18,command=query)

e.pack(side=LEFT, fill=X, padx=5)
querybutton.pack(side=LEFT)

queryframe.pack()

Frame(mainframe,height=1,width=550,bg="black").pack(pady=10)
mainframe.pack()

lookop=LookOP()
lookop.index("testdata.manual.2009.06.14.csv")

app.mainloop()


