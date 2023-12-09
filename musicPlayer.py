# Music Player
from tkinter import *
from tkinter import filedialog
# filedialog: modal dialog box, when shown blocks the rest application until user has chosen a file
# provides classes and factory funcs for creating file/directory selection window
from pygame import mixer  # to play music
import os  # to open folder in our local system

root=Tk()
root.title("Music Player")
root.geometry("1100x670+270+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)  # not-resizable

mixer.init()

def open_folder():
    path=filedialog.askdirectory()  # askdirectory: to select a folder and save its path in a 'path' variable
    if path:
        os.chdir(path)
        # os.chdir method changes the current working directory to a specific path
        # os.getcwd() used to print current working directory
        songs=os.listdir(path)
        # os.listdir() method is used to get list of all files and directories in the specified directory
        #print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(music_name)
    mixer.music.play()
    music.config(text=music_name[0:-4])

#icon
image_icon=PhotoImage(file="music_logo.png")
root.iconphoto(False,image_icon)
# iconphoto() method is used to set the titlebar icon of any tkinter/toplevel window
# should be the object of PhotoImage class

Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="#0f1a2b").pack()

# logo
Logo=PhotoImage(file="music_logo.png")
Label(root,image=Logo,bg="white").place(x=110,y=115)

# buttons
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0,command=play_song).place(x=118,y=280)

stop_button=PhotoImage(file="stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=22,y=415)

resume_button=PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=230,y=415)

pause_button=PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=118,y=540)

#label
music=Label(root,text="",font=("arial",18),fg="black",bg="#7DF9FF")
music.place(x=420,y=250,anchor="center")

#music
Menu=PhotoImage(file="menu.png")
Label(root,image=Menu,bg="#0f1a2b").pack(padx=35,pady=10,side=RIGHT)

music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=420,y=350,width=610,height=280)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de"
       ,command=open_folder).place(x=420,y=300)
scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",18),bg="#333333",fg="white",
                 selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()