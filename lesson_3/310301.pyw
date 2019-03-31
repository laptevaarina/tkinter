from tkinter import *
root = Tk()

def hello(event):
    text = e.get()
    e.delete(0, END)
    lbl['text'] = text

btn = Button(root, text='press me!')
btn.pack()
btn.bind("<Button-1>", hello)

e = Entry(root)
e.pack()

lbl = Label(root, text = 'Hello, kids!')
lbl.pack()

root.mainloop()
