from tkinter import *

root = Tk()
root.geometry("800x600")
root.title('Project PSIT \"Get A\"')

class Subject():
    def __init__(self, root):
        self.root = root

    def print_box(self):
        top = Toplevel()
        self.e = Entry(top)
        self.e.pack()

        button_ok = Button(top, text='OK', command=self.add_subject)
        button_ok.pack()
    def add_subject(self):
        print (self.e.get())
        self.b = Button(self.root, text=self.e.get())
        self.b.pack()
        """button_subject = Button(root, text='e')
        button_subject.pack()
        top.destroy()"""


    
s = Subject(root)
button_test = Button(root, text='New Subject', command = s.print_box)
button_test.pack()
# button_test.grid(row = 0, column =0)
