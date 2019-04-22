from tkinter import *
root = Tk()

fr = Frame()
fr.pack(pady = 5)
canv = Canvas(root, width = 400, height = 400)
canv.pack()

from random import randint, choice
colors = ['red', 'yellow', 'black', '#FF00CC', '#AA11aa']

def random_draw(event):
    count = 0
    for i in range(20):
        R = randint(10, 40)
        x = randint(R, 400 - R)
        y = randint(R, 400 - R)
        color = choice(colors)
        canv.create_oval(x-R, y-R, x+R, y+R, fill = color)
        if color == 'red':
            count += 1
    print(count, 'circle(s)')

def clear(event):
    canv.delete(ALL)

btn1 = Button(fr, text = 'Random 20 and count')
btn1.pack(side = LEFT)
btn1.bind('<1>', random_draw)

btn2 = Button(fr, text = 'Clear')
btn2.pack(side = LEFT)
btn2.bind('<1>', clear)

root.mainloop()
        
