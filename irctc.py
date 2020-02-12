from tkinter import*
import requests


class Irctc:

    def __init__(self):
        
        self.root=Tk()
        self.root.title("IRCTC")
        self.root.minsize(500,600)
        self.root.minsize(500,600)

        self.root.configure(background="#0089ae")
        #F9250E

        self.label1=Label(self.root,text="Train Route",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(20,20))


        self.trainNo=Entry(self.root)
        self.trainNo.pack(ipadx=45,ipady=10)


        self.click=Button(self.root,text="Fetch Station", width=30,height=2,command=lambda:self.fetch())
        self.click.pack(pady=(15,15))


        self.result=Label(self.root,bg="#0089ae",fg="#ffffff")
        self.result.configure(font=("Constantia",12))
        self.result.pack(pady=(5,10))


        self.root.mainloop()



    def fetch(self):
        train_no=self.trainNo.get()
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/vtvzydta4l/".format(train_no)
        data=requests.get(url)
        response=data.json()
        stations=""
        for i in response['route']:
            stations=stations+i['station']['name']+" | " + i['scharr']+" | " + " | " + i['schdep']+" | " + str(i['distance'])+ "\n"


        self.result.configure(text=stations)

        

#vtvzydta4l
obj=Irctc()
