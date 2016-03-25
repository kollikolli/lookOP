from Tkinter import *

dummyData = {}
dummyData["neg"]={}
dummyData["pos"]={}
dummyData["neut"]={}

curItem=0
maxItems=1


def next():
    global curItem,maxItems
    if curItem <maxItems:
        curItem+=1
    updateContent()

def prev():
    global curItem,maxItems
    if curItem > 0:
        curItem-=1
    updateContent()

def updateContent():
    global curItem,dummyData
    posTitle.set(dummyData["pos"]["user"][curItem]+" on "+dummyData["pos"]["date"][curItem])
    posTweet.set(dummyData["pos"]["tweet"][curItem])
    neutTitle.set(dummyData["neut"]["user"][curItem]+" on "+dummyData["neut"]["date"][curItem])
    neutTweet.set(dummyData["neut"]["tweet"][curItem])
    negTitle.set(dummyData["neg"]["user"][curItem]+" on "+dummyData["neg"]["date"][curItem])
    negTweet.set(dummyData["neg"]["tweet"][curItem])

def query():
    global mainframe,posTitle,posTweet,neutTitle,neutTweet,negTitle,negTweet,dummyData
    if e.get().strip() == "IPad":
        dummyData = {}

        dummyData["neg"]={}
        dummyData["neg"]["user"]=["FrankerZZ1992","Tony"]
        dummyData["neg"]["tweet"]=["The IPad is troubling me so much","The IPad sucks ass"]
        dummyData["neg"]["rating"]=0.3
        dummyData["neg"]["date"]=["March 21 2016","October 31 1999"]

        dummyData["pos"]={}
        dummyData["pos"]["user"]=["Honker1234","Hero"]
        dummyData["pos"]["tweet"]=["The NEW IPad IS AMAZING!!","I LOOOVE the IPad"]
        dummyData["pos"]["rating"]=0.5
        dummyData["pos"]["date"]=["March 23 2015","December 11 2011"]

        dummyData["neut"]={}
        dummyData["neut"]["user"]=["Steven1231","Friend12"]
        dummyData["neut"]["tweet"]=["I am fine with the IPad","IPad is okayish"]
        dummyData["neut"]["rating"]=0.2
        dummyData["neut"]["date"]=["March 21 2016","April 1 2013"]


        if "rating" in dummyData["pos"] and "rating" in dummyData["neg"] and "rating" in dummyData["neut"]:            
            
            oplabel=Frame(mainframe)
            Label(oplabel, text=str(dummyData["pos"]["rating"]*100)+"%").pack(side=LEFT,padx=(0,0))
            Label(oplabel, text=str(dummyData["neut"]["rating"]*100)+"%").pack(side=LEFT,padx=(dummyData["pos"]["rating"]*500-30,300-500*dummyData["neg"]["rating"]))
            Label(oplabel, text=str(dummyData["neg"]["rating"]*100)+"%").pack(side=LEFT,padx=(0,0))
            oplabel.pack()            

            opinion = Frame(mainframe)
            pos=Frame(opinion,height=30,width=500*dummyData["pos"]["rating"],bg="green")
            pos.pack(side=LEFT)          

            neut=Frame(opinion,height=30,width=500*dummyData["neut"]["rating"],bg="grey")
            neut.pack(side=LEFT)          

            neg=Frame(opinion,height=30,width=500*dummyData["neg"]["rating"],bg="red")
            neg.pack(side=LEFT)          

            opinion.pack(pady=(0,20))

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
            negtxt.pack(pady=(10,15))

            prevB=Button(results,text="Previous Results",command=prev)
            nextB=Button(results,text="Next Results",command=next)
            prevB.pack(side=LEFT)
            nextB.pack(side=LEFT)
            results.pack()


app= Tk()
app.title("LookOP")
app.geometry("500x325+30+30")

posTitle=StringVar()
posTweet=StringVar()
neutTitle=StringVar()
neutTweet=StringVar()
negTitle=StringVar()
negTweet=StringVar()

mainframe=Frame(app)

queryframe = Frame(mainframe,borderwidth=1,height=15)
e=Entry(queryframe)
querybutton=Button(queryframe,text="Search",width=18,command=query)

e.pack(side=LEFT, fill=X, padx=5)
querybutton.pack(side=LEFT)

queryframe.pack()

Frame(mainframe,height=1,width=500,bg="black").pack(pady=10)
mainframe.pack()
app.mainloop()


