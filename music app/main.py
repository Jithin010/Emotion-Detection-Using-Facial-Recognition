
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("1600x1000")
canvas.config(bg = 'white')
rootpath=''

my_canvas= tk.Canvas(canvas,width=323,height = 576)

hrootpath = "C:\\Users\Dell\Documents\Emotion-Detection-Using-Facial-Recognition\songs\happy"
srootpath = "C:\\Users\Dell\Documents\Emotion-Detection-Using-Facial-Recognition\songs\sad"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")



def button_command():
    global rootpath
    text= un_entry.get()
    if text == 'happy':
       rootpath = hrootpath
       for root, dirs, files in os.walk(rootpath):
            for filename in fnmatch.filter(files, pattern):
                listBox.insert('end', filename)
    elif text == 'sad':
        rootpath = srootpath
        for root, dirs, files in os.walk(rootpath):
            for filename in fnmatch.filter(files, pattern):
                listBox.insert('end', filename)

  
def select():
        label.config(text = listBox.get("anchor"))
        mixer.music.load( rootpath + "\\" + listBox.get("anchor"))
        mixer.music.play()
   

def stop():
    mixer.music.stop()
    listBox.select_clear('active') 

def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_sname = listBox.get(next_song)
    label.config(text = next_sname) 
    mixer.music.load(rootpath + "\\" + next_sname)
    mixer.music.play()      
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_sname = listBox.get(next_song)
    label.config(text = next_sname) 
    mixer.music.load(rootpath + "\\" + next_sname)
    mixer.music.play()      
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song) 

def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"      


        

top = tk.Frame(canvas, bg = "white")
top.pack(padx = 10, pady = 5, anchor = 'n')

un_entry = tk.Entry(canvas, font=('poppins',24), width =14,bg = 'grey', bd=7)
un_entry.pack(pady = 2, side = 'top')


emoButton = tk.Button(canvas, text='Submit',font = ('poppins', 14), bg = 'blue', borderwidth = 5, command = button_command )
emoButton.pack(pady = 2, side = 'top')

prevButton = tk.Button(canvas, image = prev_img, bg = 'white', borderwidth = 0, command = prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, image = stop_img, bg = 'white', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, image = pause_img, bg = 'white', borderwidth = 0, command = pause)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, image = play_img, bg = 'white', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas,  image = next_img, bg = 'white', borderwidth = 0, command = next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

listBox = tk.Listbox(canvas, fg = "yellow", bg = "purple", width = 300, font = ('poppins', 14))
listBox.pack(padx = 15, pady = 10)
label = tk.Label(canvas, text = '', bg = "black", fg = "cyan", font = ('poppins', 14))
label.pack(pady = 15)






canvas.mainloop()