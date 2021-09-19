from tkinter import *
from pytube import YouTube
from tkinter import messagebox

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader")
root.resizable(width=False, height=False)
pic= PhotoImage(file= r'youtube.png')
root.iconphoto(False, pic)

Label(root,text = 'Youtube Video Downloader', font ='lota 20 bold',bg = 'red').pack()

link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'lota 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'lota 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'lota 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()
