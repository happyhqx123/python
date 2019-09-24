import tkinter as tk
windows=tk.Tk()
windows.title('我的第一个gui程序')
windows.geometry('500x300')
i=tk.Label(windows,text='我要打死你')
i.pack()

def anniu():

    pass
b=tk.Button(windows,text='点一下',commend=anniu)
windows.mainloop()
