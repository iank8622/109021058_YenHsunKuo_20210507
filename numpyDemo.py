import numpy as np
import random as rand

a = np.array([1, 2, 3, 4]) # 一維陣列建立
# print(a)
b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype=float) #二維陣列建立
# print(b)
c = np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [
    (2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype=float) # 三維陣列建立
# print(c)
zeros = np.zeros((2, 3)) # 建立2*3全為0的陣列
ones = np.ones((2, 3, 4)) * 128 #建立一個2*3*4全為1(*n)陣列
# np128 = [[[[128] for i in range(4)]for j in range(3)]for k in range(2)]

d = np.arange(1, 10, 2) # 建立一個從1開始,不超過10,間格為2的均勻數值陣列

x1 = np.linspace(0, 10, 5) # 建立一個0到10之間 均勻的5個數值陣列
fileName = "out.npy"
with open(fileName, "wb") as fp:
    np.save(fp, x1)

f = np.full((3, 2), 8) # 建立一個3*2全為8的陣列

print("--------------------")
np.random.seed(1723)
ran = np.random.randint(2, 135, (2, 3)) # 建立一個2*3 亂數2~135的陣列
z_ran = ran.reshape(3, 2) # 重塑(切割)ran為1*6的ran亂數範圍陣列
z_ran.sort() # 由小到大排列
#z_mid = ((z_ran[len(z_ran)//2 - 1][len(z_ran[len(z_ran)//2 - 1])//2 -1]) + (z_ran[len(z_ran)//2][len(z_ran[len(z_ran)//2])//2])) / 2
print(z_ran)
#print(z_mid)

r = np.random.shuffle(z_ran) #shuffle()打亂順序

data = list("This is a book")
print(data)
rand.seed(1723)
rand.shuffle(data)
print("".join(data))

