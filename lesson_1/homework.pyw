from tkinter import *
root = Tk()
root.geometry('500x500')

fr1 = Frame(root)
fr1.pack(side = 'top', fill = 'both')
bt1 = Button(fr1, text = '1', width = 5, height = 3, font = 'arial 14')
bt3 = Button(fr1, text = '3', width = 5, height = 3, font = 'arial 14')
bt1.pack(side = 'left')
bt3.pack(side = 'right')

fr2 = Frame(root)
fr2.pack(anchor = 'center')
bt2 = Button(fr2, text = '2', width = 5, height = 3, font = 'arial 14')
bt2.pack(side = 'top')

fr3 = Frame(root)
fr3.pack(side = 'bottom', fill = 'both')
bt4 = Button(fr3, text = '4', width = 5, height = 3, font = 'arial 14')
bt5 = Button(fr3, text = '5', width = 5, height = 3, font = 'arial 14')
bt5.pack(side = 'right')
bt4.pack(side = 'right', padx = 20)

root.mainloop()
