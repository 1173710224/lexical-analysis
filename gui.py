#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/31 11:45
@Author  : cbz
@Site    : https://github.com/1173710224/brain-computing/blob/cbz
@File    : gui.py
@Software: PyCharm
@Descripe:
"""
global programs
from tkinter import *
from tkinter import ttk

top = Tk()
top.title('词法分析器 C32')
top.geometry('600x600')
top.update()

entry = Text(top);entry.pack()
entry.place(width=0.4*top.winfo_width(),height=0.9*top.winfo_height(),
            x=0.05*top.winfo_width(),y=0.03*top.winfo_height())

tree= ttk.Treeview(top,show='headings');tree.pack()
tree.place(width=0.4*top.winfo_width(),height=0.7*top.winfo_height(),
            x=0.55*top.winfo_width(),y=0.03*top.winfo_height())
#定义列
tree["columns"]=("行号","word","token")
#设置列属性，列不显示
tree.column("行号",width=int(0.33*tree.winfo_width()))
tree.column("word",width=int(0.33*tree.winfo_width()))
tree.column("token",width=int(0.33*tree.winfo_width()))
# tree.column("code",width=int(0.25*tree.winfo_width()))

#设置表头
tree.heading("行号",text="行号")
tree.heading("word",text="word")
tree.heading("token",text="token")
# tree.heading("code",text="code")

def show_table(dfa):
    tmpwin = Toplevel()
    tmpwin.title('dfa 转换表')
    tmpwin.geometry('1254x700')
    tmpwin.update()
    tmptree = ttk.Treeview(tmpwin, show='headings');tmptree.pack()
    import pandas as pd
    df = pd.read_excel('dfa.xlsx')
    tmptree.place(width=tmpwin.winfo_width(), height=tmpwin.winfo_height(),x=0, y=0)
    tmptree.update()
    # 定义列
    titles = list(df.columns)
    tmptree["columns"] = titles

    # # 设置列属性，列不显示
    # tree.column("行号", width=int(0.33 * tree.winfo_width()))
    # tree.column("word", width=int(0.33 * tree.winfo_width()))
    # tree.column("token", width=int(0.33 * tree.winfo_width()))
    # tree.column("code",width=int(0.25*tree.winfo_width()))
    print(tmptree.winfo_width() / len(titles))
    print(tmptree.winfo_width())
    print(len(titles))
    print(titles)
    for tmp in titles:
        tmptree.column(tmp,width=int(tmptree.winfo_width() / len(titles)))
    for tmp in titles:
        tmptree.heading(tmp,text=str(tmp))
    # # 设置表头
    # tree.heading("行号", text="行号")
    # tree.heading("word", text="word")
    # tree.heading("token", text="token")
    # tree.heading("code",text="code")
    index = -1
    for tmp in df.values:
        index += 1
        # print(tmp)
        from math import isnan
        value = []
        for unit in tmp:
            if isnan(unit):
                value.append('')
            else:
                value.append(str(unit))
        tmptree.insert("",index,values=value)
    tmpwin.mainloop()
    return
def openfile():
    file = open('test.c','r')
    data = file.readlines()
    file.close()
    # print(data)
    entry.delete("0.0","end")
    for i in range(len(data)):
        entry.insert(INSERT,data[i])
    return
fromfile = Button(top,text='open',command=openfile);fromfile.pack()
fromfile.place(width=0.4*top.winfo_width(),height=0.1*top.winfo_height(),
            x=0.55*top.winfo_width(),y=0.75*top.winfo_height())

check = IntVar()
b = Checkbutton(top,variable=check,text='dfa');b.pack()
b.place(x=0.9*top.winfo_width(),y=0.9*top.winfo_height())
def parse():
    text = entry.get("0.0", "end")
    from gg import back_parse
    analyses, dfa = back_parse(text)
    index = -1
    for tmp in analyses:
        index += 1
        tree.insert("",index,values = tmp)
    if check.get() == 1:
        show_table(dfa)
    return
fromfile = Button(top,text='parse',command=parse);fromfile.pack()
fromfile.place(width=0.35*top.winfo_width(),height=0.1*top.winfo_height(),
            x=0.55*top.winfo_width(),y=0.87*top.winfo_height())


top.mainloop()
