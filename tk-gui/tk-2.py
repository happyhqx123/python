import tkinter as tk
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


