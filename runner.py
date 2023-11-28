import os
import tkinter
# import tkMessageBox
top=tkinter.Tk()

def helloCallBack():
    os.system("gnome-terminal -- bash -c \"python3 listen.py\"")

B=tkinter.Button(top,text="Start the Bot",command= helloCallBack)

B.pack()
top.mainloop()