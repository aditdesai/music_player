from tkinter import *
import pygame
import os

def startsong():
    track = playlist.get(ACTIVE)
    for widget in frame2.winfo_children():
        widget.destroy()
    Label(frame2, text = track).place(x = 150, y = 25, anchor = "center")
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

def playsong():
    pygame.mixer.music.unpause()

def pausesong():
    pygame.mixer.music.pause()



root = Tk()
root.geometry("700x200")
root.title("Music Player")
root.iconbitmap("music.ico")

pygame.init()
pygame.mixer.init()

frame1 = LabelFrame(root, text = "Playlist", padx = 10, pady = 10)
frame2 = LabelFrame(root, text = "Song Playing- ", padx = 10, pady = 10)
frame3 = LabelFrame(root, text = "Control Panel", padx = 10, pady = 10)

play_img = PhotoImage(file = r"play.png")
pause_img = PhotoImage(file = r"pause.png")
power_img = PhotoImage(file = r"power.png")


Button(frame3, image = power_img, command = startsong).place(x = 105, y = 20)
Button(frame3, image = play_img, command = playsong).place(x = 138, y = 20)
Button(frame3, image = pause_img, command = pausesong).place(x = 170, y = 20)




scrol_y = Scrollbar(frame1, orient=VERTICAL)
playlist = Listbox(frame1, yscrollcommand=scrol_y.set, selectmode=SINGLE, bd=5, relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command = playlist.yview)
playlist.pack(fill = BOTH)

os.chdir("songs")
songs = os.listdir()

track = StringVar()

for track in songs:
    playlist.insert(END,track)


frame1.place(x = 0, y = 0, width = 400, height = 200)
frame2.place(x = 400, y = 0, width = 300, height = 100)
frame3.place(x = 400, y = 100, width= 300, height = 100)

root.mainloop()