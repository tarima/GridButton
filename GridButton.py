# coding: utf-8

'''
Created on 2012/11/15

@author: tsurumi
'''
from Tkinter import *
import threading
import random
import tkMessageBox
import time

root = Tk()
root.title('おもしろアプリ')
BUTTONLIST = []
RANDOMNUM = 0

class ButtonPush:
	def __init__(self, buttonNum):
		self.buttonNum = buttonNum

	def __call__(self, event=None):
		if RANDOMNUM == self.buttonNum:
			tkMessageBox.showinfo('showinfo', 'OK!')
		else:
			tkMessageBox.showerror('showerror', 'ERROR!')

class ButtonMake:
	column_data = (0, 1, 2, 0, 1, 2, 0, 1, 2)
	row_data = (0, 0, 0, 1, 1, 1, 2, 2, 2)

	for x in range(9):
		BUTTONLIST.append(Button(root, text = '%d' % (x + 1), font=('ＭＳ 明朝', 20),
			bg = '#00FFFF', activebackground = '#00FF00', command=ButtonPush(x)))
		BUTTONLIST[x].grid(column = column_data[x], row = row_data[x], sticky = 'nsew')

	for x in range(3):
		root.grid_columnconfigure(x, weight = 1)
		root.grid_rowconfigure(x, weight = 1)

class ButtonFlash:
	def __init__(self):
		self.ButtonFlashTimer()

	def buttonflash(self):
		global RANDOMNUM
		RANDOMNUM = random.randint(0,8)
		#BUTTONLIST[RANDOMNUM].flash()
		BUTTONLIST[RANDOMNUM].configure(bg = '#00FF00')
		time.sleep(0.1)
		BUTTONLIST[RANDOMNUM].configure(bg = '#00FFFF')
		self.ButtonFlashTimer()

	def ButtonFlashTimer(self):
		t = threading.Timer(0.3, self.buttonflash)
		t.start()

##------------------------------------------------
if __name__ == '__main__':
	ButtonMake()
	ButtonFlash()
	root.mainloop()
