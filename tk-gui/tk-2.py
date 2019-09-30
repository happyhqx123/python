import tkinter as tk
<<<<<<< HEAD
windows=tk.Tk()
windows.title('我的第一个gui程序')
windows.geometry('500x300')
i=tk.Label(windows,text='我要打死你')
i.pack()

def anniu():

    pass
b=tk.Button(windows,text='点一下',commend=anniu)
windows.mainloop()
=======
windows = tk.Tk()
windows.title("my windows")
windows.geometry('200x100')

var =tk.StringVar()
l=tk.Label(windows,textvariable=var,bg="green",font=("Arial",12),width=15,height=2)
l.pack()

on_hit=False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit=True
        var.set('点一下')
    else:
        on_hit=False
        var.set('')
b=tk.Button(windows,text='点一下',width=15,height=2,command=hit_me)
b.pack()
windows.mainloop()


>>>>>>> a7d653de04629bfe09e0734e8867de39e46109dd
