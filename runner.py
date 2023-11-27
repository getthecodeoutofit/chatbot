import sys
import os
import tkinter
# import tkMessageBox
top=tkinter.Tk()

def helloCallBack():
    os.system("gnome-terminal -- bash -c \"python3 listen.py\"")
def close():
    os.system("gnome-terminal -- bash -c \"kill -9 $(pgrep bash)\"")

B=tkinter.Button(top,text="Start the Bot",command= helloCallBack)
c = tkinter.Button(top,text="Stop the Bot",command= close)

B.pack()
c.pack()
top.mainloop()