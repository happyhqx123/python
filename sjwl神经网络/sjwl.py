def ycq():  #定义一个预测器
    a=100
    b=62.137
    c=0.5
    while True:
        c=c+0.00001
        #print(c)
        if c*a >=b:
            print(c)
            break
ycq()


def flq():  #定义一个分类器
    y1=3.0
    x1=1.0

    y2=1.0
    x2=3.0
    a=0.25
    y=x2*a
    e=y2-y
    while True:
        a=e / x2/4+a 
        print(a)
        if a*x2 >y2 :
            break
    #print(a)
    y=x1*a
    e=2.9-y
    a=e/x1*0.5+a
    print(a)
flq()


def s(x):    #定义S函数
    e=2.71828
    y=1/((1/e)**x+1)
    return y
#print('s函数的返回值是:',s(0.3))
for i in range(-100, 100):
    x=i/10
    print(x,'---',s(x))



def yumen(x1,x2):    #定义一个与门
    #w:权重，x:参数，theta:阀值
    w1,w2,theta=0.6,0.6,0.7
    y=w1*x1+w2*x2
    if y>theta:
        return  x1,x2,"---",1
    elif y<=theta:
        return x1,x2,"---",0
print(yumen(1,0))
print(yumen(0,0))
print(yumen(0,1))
print(yumen(1,1))
