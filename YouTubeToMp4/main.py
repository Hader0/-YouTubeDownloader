from cProfile import label
from tkinter import *
from pytube import YouTube
import yt_dlp
from tkinter import filedialog

# Function


def Location():
    global dirText
    locationlol = filedialog.askdirectory()
    dirText = str(locationlol)
    locationLabel.config(text=str(locationlol))
    return dirText


def downloadFunc():
    url = YouTube(link.get())
    if selected.get() == "Audio":
        url = link.get()
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'paths': {'temp': f'{str(dirText)}', "home": f'{str(dirText)}'},
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)

    elif selected.get() == "Video":
        urlDown = url.streams.get_highest_resolution()
        urlDown.download(str(dirText))
        print(str(dirText))
    else:
        selected.set("SELECT a Format")
    print(str(dirText))


root = Tk()
root.geometry('500x350')
root.title('Youtube Video/Music Downloader')
root.resizable(False, False)

root.columnconfigure(2, weight=1)

link = StringVar()

# Drop Down Selection
selected = StringVar()
selected.set("Video")

# Widgets


locationLabel = Label(root)
locationLabel.grid(row=6, column=2, pady=(20, 0))

title = Label(root, text="Youtube to Mp4/Mp3", font=('Helvetica', 20))
title.grid(row=0, column=2, pady=(20, 50))

labelText = Label(root, text="Paste Link:", font=('Helvetica', 15))
labelText.grid(row=1, column=2)

urlEntry = Entry(root, textvariable=link, width=25)
urlEntry.grid(row=2, column=2)

ddm = OptionMenu(root, selected, "Audio", "Video")
ddm.grid(row=3, column=2, pady=(10, 0))

submitBtn = Button(root, text="Download", command=downloadFunc)
submitBtn.grid(row=4, column=2, pady=(10, 0))

choose = Button(root, text="Choose Location", command=Location)
choose.grid(row=5, column=2, pady=(10, 0))

author = Label(root, text="Made by Hayden Bradford", font=('Helvetica', 7))
author.grid(row=7, column=2, pady=(20, 0), padx=(10, 0))


root.update_idletasks()
root.mainloop()
