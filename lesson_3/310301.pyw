from tkinter import *
root = Tk()

def hello(event):
    e.delete(0, END)
    e.insert(0, "Hello, kids!")

btn = Button(root, text='press me!')
btn.pack()
btn.bind("<Button-1>", hello)

e = Entry(root)
e.pack()

root.mainloop()
