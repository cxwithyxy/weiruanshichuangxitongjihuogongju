#coding:utf-8

from workThreading.regWin import RegWin

import tkinter

mainW = tkinter.Tk()
mainW.title("系统激活")
mainW.geometry("400x600")

t = tkinter.Text(mainW)

t.pack(fill = "both", expand = 1)

def word_show(word):
    t.insert(tkinter.END, word + "\n\n")

RegWin(word_show).thread_do_reg()

mainW.mainloop()
