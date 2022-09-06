from cProfile import label
from tkinter import *
from pytube import YouTube
from tkinter import filedialog

# Function 
def downloadFunc():
    url = YouTubelink.get())
    print(url.title(（


def Location():
    locationLabel = Label(root)
    locationLabel.grid(row=5, column=2, pady=(20, 0))
    locationlol = filedialog.askdirectory()
    locationLabel.insert(END, locationlol)


root = Tk()
root.geometry('500x300') 
root.title('Youtube Video/Music Downloader')
root.resizable(False, False)


link = StringVar()

title = Label(root, text="Youtube to Mp4/Mp3", font=('Helvetica', 20))
title.grid(row=0, column=2, pady=(20,50))

labelText = Label(root, text="Paste Link:", font=('Helvetica', 15))
labelText.grid(row=1,column=2)
urlEntry = Entry(root, textvariable=link)
urlEntry.grid(row=2, column=2)

submitBtn = Button(root, text="Process", command=downloadFunc)
submitBtn.grid(row=3, column=2, pady=(20,0))

choose = Button(root, text="Choose Location", command=Location)
choose.grid(row=4, column=2)

author = Label(root, text="Made by Hayden Bradford", font=('Helvetica', 10))
author.grid(row=5, column=0, columnspan=1, pady=(75,0), padx=(10,0))


root.update_idletasks()
root.mainloop()