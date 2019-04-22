from tkinter import *
root = Tk()

fr = Frame()
fr.pack(pady = 5)
canv = Canvas(root, width = 400, height = 400)
canv.pack()

from random import randint, choice
colors = ['blue','red', 'green', 'yellow', 'black', '#FF00CC', '#AA11aa']

def random_draw(event):
    count_mini = 0
    count_max = 0
    for i in range(20):
        R = randint(5, 90)
        x = randint(R, 400 - R)
        y = randint(R, 400 - R)
        color = choice(colors)
        canv.create_oval(x-R, y-R, x+R, y+R, fill = color)
        if R < 20 and color == 'red':
            count_mini += 1
        if R > 50 and color == 'blue':
            count_max += 1
    print(count_mini, 'red circle(s),', count_max, 'blue circle(s)')
    
def clear(event):
    canv.delete(ALL)

btn1 = Button(fr, text = 'Random 20, count little red and big blue')
btn1.pack(side = LEFT)
btn1.bind('<1>', random_draw)

btn2 = Button(fr, text = 'Clear')
btn2.pack(side = LEFT)
btn2.bind('<1>', clear)

root.mainloop()
        
