import numpy as np
def S(x):    #定义Sigmoid函数
    return 1/(1+np.exp(-x))


def R(x):    #定义Relu函数
    return np.maximum(0,x)

x=np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7])
print("S--",S(x))
print("R--",R(x))
