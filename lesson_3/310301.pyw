from tkinter import *
root = Tk()

def hello(event):
    print('Hello, kids!')

btn = Button(root, text='press me!', width=10, height=5)
btn.pack()
btn.bind("<Button-1>", hello)

root.mainloop()
