import tkinter as tk
windows=tk.Tk()
windows.title('第一个tkinter程序')
windows.geometry('500x300')
i=tk.Label(windows,text="我要打死你",bg='green',font=("Arial",12),width=30,height=2)
i.pack()
windows.mainloop()

