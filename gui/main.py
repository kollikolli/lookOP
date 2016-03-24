from Tkinter import *

dummyData = {}
dummyData["neg"]={}
dummyData["pos"]={}
dummyData["neut"]={}


def query():
    global mainframe
    if e.get().strip() == "IPad":
        dummyData = {}

        dummyData["neg"]={}
        dummyData["neg"]["user"]=["FrankerZZ1992"]
        dummyData["neg"]["tweet"]=["The IPad is troubling me so much"]
        dummyData["neg"]["rating"]=0.3
        dummyData["neg"]["date"]=["March 21 2016"]

        dummyData["pos"]={}
        dummyData["pos"]["user"]=["Honker1234"]
        dummyData["pos"]["tweet"]=["The NEW IPad IS AMAZING!!"]
        dummyData["pos"]["rating"]=0.5
        dummyData["pos"]["date"]=["March 23 2015"]

        dummyData["neut"]={}
        dummyData["neut"]["user"]=["Steven1231"]
        dummyData["neut"]["tweet"]=["I am fine with the IPad"]
        dummyData["neut"]["rating"]=0.2
        dummyData["neut"]["date"]=["March 21 2016"]


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
            Label(postxt, text=dummyData["pos"]["user"][0]+" on "+dummyData["pos"]["date"][0],background="lightgreen").pack()
            Label(postxt, text=dummyData["pos"]["tweet"][0],background="lightgreen").pack()
            postxt.pack(pady=(10,0))

            neuttxt = Frame(results,bd=1,relief=GROOVE,background="lightgrey")
            Label(neuttxt, text=dummyData["neut"]["user"][0]+" on "+dummyData["neut"]["date"][0],background="lightgrey").pack()
            Label(neuttxt, text=dummyData["neut"]["tweet"][0],background="lightgrey").pack()
            neuttxt.pack(pady=(10,0))

            negtxt = Frame(results,bd=1,relief=GROOVE,background="pink")
            Label(negtxt, text=dummyData["neg"]["user"][0]+" on "+dummyData["neg"]["date"][0],background="pink").pack()
            Label(negtxt, text=dummyData["neg"]["tweet"][0],background="pink").pack()
            negtxt.pack(pady=(10,0))

            results.pack()


app= Tk()
app.title("LookOP")
app.geometry("500x325+30+30")

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


