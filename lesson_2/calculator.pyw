from tkinter import *
root = Tk()
root.title('Калькулятор')

ent = Entry(root, width = 28)
ent.grid(row = 0, rowspan = 2, columnspan = 5, pady = 5, padx = 5)

btn_mc = Button(root, text = 'MC', width = 3, height = 1)
btn_mc.grid(row = 2, column = 0, padx = 5)
btn_mr = Button(root, text = 'MR', width = 3, height = 1)
btn_mr.grid(row = 2, column = 1)
btn_ms = Button(root, text = 'MS', width = 3, height = 1)
btn_ms.grid(row = 2, column = 2, padx = 5)
btn_m1 = Button(root, text = 'M+', width = 3, height = 1)
btn_m1.grid(row = 2, column = 3)
btn_m2 = Button(root, text = 'M-', width = 3, height = 1)
btn_m2.grid(row = 2, column = 4, padx = 5)

btn_01 = Button(root, text = '<-', width = 3, height = 1)
btn_01.grid(row = 3, column = 0, padx = 5, pady = 5)
btn_ce = Button(root, text = 'CE', width = 3, height = 1)
btn_ce.grid(row = 3, column = 1, pady = 5)
btn_c = Button(root, text = 'C', width = 3, height = 1)
btn_c.grid(row = 3, column = 2, padx = 5, pady = 5)
btn_02 = Button(root, text = '+\-', width = 3, height = 1)
btn_02.grid(row = 3, column = 3, pady = 5)
btn_sqrt = Button(root, text = 'SQRT', width = 3, height = 1)
btn_sqrt.grid(row = 3, column = 4, padx = 5, pady = 5)

btn_7 = Button(root, text = '7', width = 3, height = 1)
btn_7.grid(row = 4, column = 0, padx = 5)
btn_8 = Button(root, text = '8', width = 3, height = 1)
btn_8.grid(row = 4, column = 1)
btn_9 = Button(root, text = '9', width = 3, height = 1)
btn_9.grid(row = 4, column = 2, padx = 5)
btn_03 = Button(root, text = '/', width = 3, height = 1)
btn_03.grid(row = 4, column = 3)
btn_per = Button(root, text = '%', width = 3, height = 1)
btn_per.grid(row = 4, column = 4, padx = 5)

btn_4 = Button(root, text = '4', width = 3, height = 1)
btn_4.grid(row = 5, column = 0, padx = 5, pady = 5)
btn_5 = Button(root, text = '5', width = 3, height = 1)
btn_5.grid(row = 5, column = 1, pady = 5)
btn_6 = Button(root, text = '6', width = 3, height = 1)
btn_6.grid(row = 5, column = 2, padx = 5, pady = 5)
btn_04 = Button(root, text = '*', width = 3, height = 1)
btn_04.grid(row = 5, column = 3, pady = 5)
btn_05 = Button(root, text = '1/x', width = 3, height = 1)
btn_05.grid(row = 5, column = 4, padx = 5)

btn_1 = Button(root, text = '1', width = 3, height = 1)
btn_1.grid(row = 6, column = 0, padx = 5)
btn_2 = Button(root, text = '2', width = 3, height = 1)
btn_2.grid(row = 6, column = 1)
btn_3 = Button(root, text = '3', width = 3, height = 1)
btn_3.grid(row = 6, column = 2, padx = 5)
btn_06 = Button(root, text = '-', width = 3, height = 1)
btn_06.grid(row = 6, column = 3)
btn_07 = Button(root, text = '=', width = 3, height = 3)
btn_07.grid(rowspan = 2, row = 6, column = 4, padx = 5, pady = 5)

btn_0 = Button(root, text = '0', width = 8, height = 1)
btn_0.grid(row = 7, column = 0, columnspan = 2, padx = 5, pady = 5)
btn_08 = Button(root, text = ',', width = 3, height = 1)
btn_08.grid(row = 7, column = 2, pady = 5)
btn_09 = Button(root, text = '+', width = 3, height = 1)
btn_09.grid(row = 7, column = 3, pady = 5)

root.mainloop()
