from tkinter import *
root = Tk()
btn_1 = Button(root, text = 'ok', width = 10, height = 3, bg = 'blue', fg = 'black', font = 'arial 14')
btn_2 = Button(root, text = ':)', width = 10, height = 3, bg = 'yellow', fg = 'black', font = 'arial 16')
root.geometry('350x200')
btn_1.pack(anchor = 'se')
btn_2.pack(side = 'right')
root.mainloop()
