# coding: utf-8

'''
Created on 2012/11/15

@author: tsurumi
'''
from Tkinter import *
import threading
import random

root = Tk()
root.title('おもしろアプリ')

column_data = (0, 1, 2, 0, 1, 2, 0, 1, 2)
row_data = (0, 0, 0, 1, 1, 1, 2, 2, 2)
buttonList = []

for x in range(9):
    buttonList.append(Button(root, text = '%d' % (x + 1), font=('ＭＳ 明朝', 20), bg = '#00FFFF', activebackground = '#00FF00'))
	buttonList[x].grid(column = column_data[x], row = row_data[x], sticky = 'nsew')

for x in range(3):
	root.grid_columnconfigure(x, weight = 1)
	root.grid_rowconfigure(x, weight = 1)

def buttonflash():
	#b.flash()
	#random.seed(1)
	buttonList[random.randint(0,8)].flash()
	ButtonFlashTimer()

def ButtonFlashTimer():
	t = threading.Timer(1, buttonflash)
	t.start()

ButtonFlashTimer()

root.mainloop()