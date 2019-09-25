import tkinter as tk
windows =tk.Tk()
windows.title('我的gui')
windows.geometry('400x300')

var =tk.StringVar()
l=tk.Label(windows,textvariable=var,bg='green',font=('arial',12))
l.pack()

dian_anliu=False
def anliu():
    global dian_anliu
    if dian_anliu == False:
        dian_anliu=True
        var.set('点的好，送你一千万')
    else:
        dian_anliu=False
        var.set("一千万已经到账")
b=tk.Button(windows,text='点一下',command=anliu)
b.pack()
windows.mainloop()
