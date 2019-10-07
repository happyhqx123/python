import numpy as np


def Nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    y = 0.7
    tmp = np.sum(x * w) + y
    if tmp <= 0:
        return 0
    else:
        return 1


def And(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    pz = -0.7
    sc = np.sum(w * x) + pz
    if sc <= 0:
        return 0
    else:
        return 1


def Or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    y = -0.2
    tmp = np.sum(x * w) + y
    if tmp <= 0:
        return 0
    else:
        return 1


def Xor(x1, x2):
    s1 = Nand(x1, x2)
    s2 = Or(x1, x2)
    y = And(s1, s2)
    return y


print("1,0 ---", And(1, 0))
print("1,1 ---", And(1, 1))
print("0,0 ---", And(0, 0))
print("0,1 ---", And(0, 1))


print("-" * 70)


print("0,1 ---", Nand(0, 1))
print("1,1 ---", Nand(1, 1))
print("0,0 ---", Nand(0, 0))
print("1,0 ---", Nand(1, 0))


print("0,1 ---", Xor(0, 1))
print("1,1 ---", Xor(1, 1))
print("0,0 ---", Xor(0, 0))
print("1,0 ---", Xor(1, 0))
