from tkinter import *
root = Tk()

canv = Canvas(root, width = 400, height = 400)
canv.pack()

from random import randint, choice
colors = ['red', 'green', 'yellow', 'blue']

R = randint(10, 40)
x = randint(R, 400 - R)
y = randint(R, 400 - R)
color = choice(colors)
canv.create_oval(x-R, y-R, x+R, y+R, fill = color)

root.mainloop()
