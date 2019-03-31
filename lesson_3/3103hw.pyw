from tkinter import *
root = Tk()

def summa(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1+x2)

def difference(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1-x2)

def multiplication(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1*x2)

def division(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1/x2)

def clean(event):
    e1.delete(0, END)
    e2.delete(0, END)
    t3['text'] = ''    

t1 = Label(root, text = 'Entry fist number')
t1.pack()

e1 = Entry(root)
e1.pack(pady = 5)

t2 = Label(root, text = 'Entry second number')
t2.pack(pady = 5)

e2 = Entry(root)
e2.pack(pady = 5)

btnA = Button(root, text = 'Add', width = 10, font = 'Arial 14')
btnA.pack(pady = 5)
btnA.bind("<Button-1>", summa)

btnD = Button(root, text = 'Deduct', width = 10, font = 'Arial 14')
btnD.pack(pady = 5)
btnD.bind("<Button-1>", difference)

btnM = Button(root, text = 'Multiply', width = 10, font = 'Arial 14')
btnM.pack(pady = 5)
btnM.bind("<Button-1>", multiplication)

btnDi = Button(root, text = 'Divide', width = 10, font = 'Arial 14')
btnDi.pack(pady = 5)
btnDi.bind("<Button-1>", division)

btnC = Button(root, text = 'Clean', width = 10, font = 'Arial 14')
btnC.pack(pady = 5)
btnC.bind("<Button-1>", clean)

t3 = Label(root, font = 'Arial 20')
t3.pack()

root.mainloop()
