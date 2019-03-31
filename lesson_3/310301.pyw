from tkinter import *
root = Tk()

def hello():
    print('Hello, kids!')

btn = Button(root, text='press me!', command=hello)
btn.pack()


root.mainloop()
