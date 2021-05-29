#Importing necessary modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#Creating applicatin window
musicplayer = tkr.Tk()

#Setting the title name
musicplayer.title("roli Music Player")

#Setting the dimesions
musicplayer.geometry("450x350")

#Asking for music directory
directory = askdirectory()

#Setting music directory to the current working directory
os.chdir(directory)

#Creating our songlist
#os.listdir() returns a list containing the names of the entries in the directory given by the path
songlist = os.listdir()

#Creating the playlist
playlist = tkr.Listbox(musicplayer, font = "Cambria 16 bold", bg = "cyan2" , selectmode = tkr.SINGLE)

#Adding songs from songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1

#Initializing modules
pygame.init()
pygame.mixer.init()

#Function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#Function for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()

#Function for pause button
def pause():
    pygame.mixer.music.pause()

#Function for resume button
def resume():
    pygame.mixer.music.unpause()

#Creating Buttons
Button_play = tkr.Button(musicplayer,height=3,width=5,text="Play Music",font="Cambria 14 bold",command=play,bg="lime green",fg="black")
Button_stop = tkr.Button(musicplayer,height=3,width=5,text="Stop Music",font="Cambria 14 bold",command=ExitMusicPlayer ,bg="red",fg="black")
Button_pause = tkr.Button(musicplayer,height=3,width=5,text="Pause Music",font="Cambria 14 bold",command=pause ,bg="yellow",fg="black")
Button_resume = tkr.Button(musicplayer,height=3,width=5,text="Resume Music",font="Cambria 14 bold",command=resume ,bg="yellow",fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font = "Cambria 14 bold", textvariable = var)
songtitle.pack()
musicplayer.mainloop()