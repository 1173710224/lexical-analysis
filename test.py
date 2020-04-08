# import tkinter
# from tkinter import *
#
# win = tkinter.Tk()
# win.title("表格数据")
# win.geometry("800x600+600+100")
# check = IntVar()
# b = Checkbutton(win,variable=check,text='dfa');b.pack()
# print(check.get())
# Button(win,text='check',command=lambda:print(check.get())).pack()
# win.mainloop()

# file = open('test.c','r')
# data = file.readlines()
# file.close()
# print('(' != '\n')
file = open('test.c','r')
data = file.readlines()
file.close()
#
from gg import *
a = core(readExcel("dfa.xlsx"), data)
analyses,ret = a.parse()
print(analyses)
print(ret)
dfa = readExcel("dfa.xlsx")

# import pandas as pd
# df = pd.read_excel('dfa.xlsx')
# print(len(df.columns))
# lis = [1,2]
# print(tuple(lis))
# wb = openpyxl.load_workbook('dfa.xlsx')
# sheet = wb['Sheet1']
# print(sheet)