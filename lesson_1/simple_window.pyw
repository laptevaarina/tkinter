from tkinter import *
root = Tk()
root.geometry('500x300')
fr_up = Frame(root)
btn_1 = Button(fr_up, text = 'ok_1', width = 5, height = 2, bg = 'blue', fg = 'black', font = 'arial 14')
btn_2 = Button(fr_up, text = 'ok_2', width = 5, height = 2, bg = 'yellow', fg = 'black', font = 'arial 16')
fr_up.pack(side = 'top', fill = 'both') 
btn_1.pack(side = 'left')
btn_2.pack(side = 'right')

fr_down = Frame(root)
btn_3 = Button(fr_down, text = 'ok_3', width = 5, height = 2, bg = 'red', fg = 'black', font = 'arial 14')
btn_4 = Button(fr_down, text = 'ok_4', width = 5, height = 2, bg = 'green', fg = 'black', font = 'arial 16')
fr_down.pack(side = 'bottom', fill = 'both') 
btn_3.pack(side = 'left')
btn_4.pack(side = 'right')

root.mainloop()
