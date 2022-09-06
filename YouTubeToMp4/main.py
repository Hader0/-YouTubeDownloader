from cProfile import label
from tkinter import *
from pytube import YouTube
from tkinter import filedialog

# Function 

def Location():
    global dirText
    locationLabel = Label(root)
    locationLabel.grid(row=5, column=2, pady=(20, 0))
    locationlol = filedialog.askdirectory()
    dirText = str(locationlol)
    locationLabel.config(text=str(locationlol))
    return dirText

def downloadFunc():
    url = YouTube(link.get())
    urlDown = url.streams.get_highest_resolution()
    urlDown.download(str(dirText))
    print(str(dirText))


root = Tk()
root.geometry('500x350') 
root.title('Youtube Video/Music Downloader')
root.resizable(False, False)

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)

link = StringVar()

title = Label(root, text="Youtube to Mp4/Mp3", font=('Helvetica', 20))
title.grid(row=0, column=2, pady=(20,50))

labelText = Label(root, text="Paste Link:", font=('Helvetica', 15))
labelText.grid(row=1,column=2)
urlEntry = Entry(root, textvariable=link, width=25)
urlEntry.grid(row=2, column=2)

submitBtn = Button(root, text="Download", command=downloadFunc)
submitBtn.grid(row=3, column=2, pady=(30,0))

choose = Button(root, text="Choose Location", command=Location)
choose.grid(row=4, column=2, pady=(30, 0))

author = Label(root, text="Made by Hayden Bradford", font=('Helvetica', 7))
author.grid(row=5, column=2, pady=(100,0), padx=(10,0))


root.update_idletasks()
root.mainloop()
