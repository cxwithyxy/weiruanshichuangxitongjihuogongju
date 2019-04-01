#coding:utf-8

from workThreading.regWin import RegWin

import tkinter

mainW = tkinter.Tk()
t = tkinter.Text()

t.pack()

def word_show(word):
    t.insert(tkinter.END, word + "\n")

RegWin(word_show).do_reg()

mainW.mainloop()
