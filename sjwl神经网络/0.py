import numpy as np


def S(x):  # 定义Sigmoid函数
    return 1 / (1 + np.exp(-x))


def R(x):  # 定义Relu函数
    return np.maximum(0, x)


x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
print("x", x.shape)
print("w1", w1.shape)
print("b1", b1.shape)
ai = np.dot(x, w1) + b1
z1 = S(ai)
print(ai)
print(z1)
w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
a2 = np.dot(z1, w2) + b2
z2 = S(a2)
print(z2)


w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
a3 = np.dot(z2, w3) + b3
z3 = S(a3)
print(z3)
