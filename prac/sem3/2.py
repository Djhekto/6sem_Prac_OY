from math import sin
from scipy.integrate import odeint

a = lambda t: sin (t)
y0 = [0.0, -1.0]
t = [0,6.28]

sol = odeint(a, y0, t)
"""
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
"""