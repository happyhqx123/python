import numpy as np 
x= np.array([1,2,3,4,5,6])
y= np.array([7,8,9,6,5,2])
z=np.array([[1,3,5],[2,4,6],[7,9,11]])
f=np.array([2,4,1])
print("x+y=:",x+y)
print("x-y=:",x-y)
print("x*y=:",x*y)
print("x/y=:",x/y)
print("x/2=:",x/2.0)


x=np.array([[1,2,3],[7,8,5],[5,8,9],[5,5,9]])
print('z=:\n',z)
print('f=:\n',f)
print("z+f=:\n",z+f)
print("z-f=:\n",z-f)
print("z*f=:\n",z*f)
print("z/f=:\n",z/f)
print('-'*9,'x=:\n',x,"x转换为一维数组后\n",x.flatten())
print(x[0])
print(x[0][1])
print(x[x>3])
print('*'*90)







import matplotlib.pyplot as plt
x= np.arange(0,9,0.1)
y=np.sin(x)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label='sin')
plt.plot(x,y2,linestyle='--',label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()

plt.show()
