import numpy as np

def AND(x1,x2):     #与门
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b= -0.7     #偏置大于权重
    tmp=np.sum(w*x)+b
    print(tmp)
    if tmp<=0:
        return 0
    else:
        return 1
print('1,0,---',AND(1,0))
print('1,1,---',AND(1,1))
print('0,0,---',AND(0,1))
print('0,1,---',AND(0,0))



def NAND(x1,x2):    #与非门
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7   #设偏置为正，权重则为负
    tmp=np.sum(x*w)+b
    print(tmp)
    if tmp <=0:
        return 0
    else:
        return 1
print("1,0,---",NAND(1,0))
print("1,1,---",NAND(1,1))
print("0,0,---",NAND(0,0))
print("0,1,---",NAND(0,1))
