from tkinter import *

root = Tk()
root.title('Get A')
root.geometry('600x700')

def new_project(root):
    w = Frame(root, width = 200, height = 400, bg = 'Blue')
    w.grid(row=0,column=0)
        
    new = Button(w, text=('clickMe'))
    new.pack(anchor = NW, pady = 180, padx = 100)

Frame(width = 400, height = 400, bg = 'Red').grid(row=0,column=1)
Frame(width = 600, height = 300, bg = 'Yellow').grid(row=1,columnspan=2)

new_project(root)
