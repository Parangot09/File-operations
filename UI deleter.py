import os
from tkinter import *
from tkinter import  messagebox
win = Tk()
win.geometry("800x500")
win.title("File deleter")
win.config(bg="#FF6666")
img = PhotoImage(file="C:\\Users\\hp\\Documents\\tkinter\\bin2.png")
win.iconphoto(True,img)
e1 = Entry(win,font="monospace")
e1.place(x=150,y=350)
tex = Label(win,text="Enter path of file to be removed",
            font=("monospace",15),
            bg="#FF6666",
            fg="white")
note = Label(win,text="Deleted files will be moved to recycle bin",font=("monospace",15),fg="white",bg="#FF6666")
note.place(x=110,y=250)
tex.place(x=110,y=300)

photo = Label(win,image= img)
photo.pack()

def deleter():
    messagebox.showinfo("Delete file","Do you want to delete this file?")
    os.remove(e1.get())

b1 = Button(win,text="Delete",font="monospace",command= deleter,bg="#8080ff")
b1.place(x=150,y=400)




win.mainloop()