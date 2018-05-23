#YouTube Video Downloader Program

from pytube import YouTube
from tkinter import *

def youtubedl():
	try:
		status.set("Download in progress")
		yt = YouTube(url.get())
		yt.streams.filter(file_extension="mp4").first().download()
		status.set("Download complete for {}".format(yt.title))
	except:
		status.set("Download failed.")

root = Tk()
root.title("My YouTube Downloader")

f = Frame()
f.grid(column=0,row=3)

url = StringVar()
status = StringVar()

Label(f,text="Enter YouTube video URL: ",width=60,fg="green").grid(column=0,row=0)
Entry(f,textvariable=url,width=60,bg="yellow").grid(column=0,row=1)
Label(f,textvariable=status,width=60).grid(column=0,row=2)
Button(f,text="Download",command=youtubedl,width=20,bg="purple",fg="white").grid(column=0,row=3)
root.mainloop()
