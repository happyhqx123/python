def ycq():  #定义一个预测器
    a=100
    b=62.137
    c=0.5
    while True:
        c=c+0.00001
        print(c)
        if c*a >=b:
           # print(c)
            break
ycq()
