#решение краевых задач мпп
#введение в питон 3 занятия
#потом прога 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# э
from math import sqrt


inp = input().split(" ")
for i,elem in enumerate(inp):
    inp[i] = int(elem)
print(inp,max(inp),min(inp),sum(inp),sorted(inp))

a = lambda x: x**2
print(type(a),a)

list1 = map(a,inp)
print(list(list1))#,*list1)

def isprostoe(a):
    if a==1:True
    if a==2:True
    if a==3:True
    if a==4:False
    for i in range(2,int(sqrt(a)+1)):
        if a%i==0:
            return False
    return True

list2 = [x for x in range(1,1000)]
#print(list2)
#isprostoe(6)
list2 = list(map(isprostoe,list2))
i=0
for elem in list2:
    if elem: i+=1
print(i)


import numpy as np

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c))

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()




