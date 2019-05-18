import numpy as np  #导入numpy模块
def np0():           #numpy数组
    x=np.array([1.0,2.0,3.0,5.0])
    #array方法接受一个列表，生成数组
    y=np.array([5.0,9.0,8,12,])
    print(x+y,x-y,x*y,x/y)  #数组之间的算术运算
    #注意，数组之间的元素个数相等才可以进行算术运算，
    #元素个数不同，程序就会报错

def np1():          #numpy生成多维数组
    x=np.array([9,11,13],[7,9,6])
    #.array接收多个列表就可以生成多维数组(矩阵),注意：.array最多只能接收俩列表，只能生成二维数组
    print(x)        #打印数组x
    print('矩阵x形状',x.shape)  
    #.shape方法可以查看矩阵形状
    print('矩阵x元素的数据类型',x.dtype)  
    #.dtype方法查看矩阵元素的数据类型

def np2():          #矩阵的算术运算
    x=np.array([4,5,6],[7,8,9])
    y=np.array([9,16,4],[7,6,15])
    #定义矩阵x,y 
    print('数组的加法',x+y)
    print('数组的减法',x-y)
    print('数组的乘法',x*y)
    print('数组的除法',x/y)
    #矩阵的算术运算也可以在相同的矩阵间以对应元素的
    #方法进行，
    #也可以通过标量（单一数）值对矩阵进行算术运算
    #这是基于广播的功能
    print('通过标量(单一数值)对矩阵进行算术运算')
    print('矩阵x乘以3',x*3)

def AND(x1,x2):
     w1,w2,theta=0.5,0.5,0.7
     tmp=x1*w1+x2*w2
     if tmp<=theta:
         return 0
     elif tmp>theta:
         return 1
print(AND(0,0))
def yum():
    x=np.array([0,1])   #输入
    w=np.array([0.5,0.5])   #权重

a=np0()
b=np1()
c=np2()
