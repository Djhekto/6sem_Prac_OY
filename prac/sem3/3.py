from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def fun(x,t):
    return [x[1], -np.sin(t)]

y0 = [0.0,1.0]
#t = [0.0,3.14]
t= np.linspace(0,np.pi)

sol = odeint(fun, y0, t)
print(sol)
plt.plot(t, sol[:, 0])
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

