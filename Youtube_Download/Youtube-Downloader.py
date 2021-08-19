from tkinter import *
import tkinter
from pytube import YouTube, Playlist

root = Tk()
root.geometry('300x200')
root.title("Youtube Downloader")
root.iconphoto(False, tkinter.PhotoImage(file='./Youtube_Download/icon.png'))
var = IntVar()
landString = tkinter.StringVar()


def PL(URL):
    playlist = Playlist(URL)
    nome = playlist.title
    for video in playlist:
        youtube = YouTube(video)
        youtube.streams.get_highest_resolution().download(output_path="./Youtube_Download/saida/"+nome)

def VD(URL):
    video = YouTube(URL)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path="./Youtube_Download/saida/")

def sel():
    cap = "Baixando"
    label.config(text = cap)
    if(str(var.get()) == "1"):
        PL(landString.get())
        selection = "Download Concluido "
        label.config(text = selection)
    elif(str(var.get())=="2"):
        
        VD(landString.get())
        selection = "Download Concluido "
        label.config(text = selection)
    

if __name__ == "__main__":
    R1 = Radiobutton(root, text="PlayList", variable=var, value=1)
    R1.pack(  anchor = W,expand=True, fill="both" )
    R2 = Radiobutton(root, text="Video", variable=var, value=2)
    R2.pack( anchor = W,expand=True, fill="both" )

    labelLand = tkinter.Label(root,text = "URL:")
    labelLand.pack( anchor = W,expand=True, fill="both" )
    entryLand = tkinter.Entry(root, width=40, textvariable=landString)
    entryLand.pack( anchor = W,expand=True, fill="both" )

    resultButton = tkinter.Button(root, text = 'DownLoad',command=sel)
    resultButton.pack( anchor = W,expand=True, fill="both")

    label = Label(root)
    label.pack(anchor = W,expand=True, fill="both")

    root.mainloop()