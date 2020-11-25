from math import sin
import numpy as np

def dgl(y,t):
    q, p = y
    dydt = [p , -sin(q) ]
    return dydt

y_0 = [0 ,2]


t = np.linspace(0, 10 ,100) 

"""
t = 0
T = 10
dt = 0.2
L_t = []
while t<T:
    t +=dt
    L_t.append(t)
"""





from scipy.integrate import odeint
sol = odeint(dgl, y_0, t)

import matplotlib.pyplot as plt

plt.plot(sol[:, 0],sol[:, 1], 'b', label='theta(t)')
plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()

