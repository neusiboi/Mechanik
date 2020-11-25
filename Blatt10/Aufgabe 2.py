from math import sin
import numpy as np

def dgl(y,t):
    q, p = y
    dydt = [p , -sin(q) ]
    return dydt



y1 = [-1/2,3]
y2 = [1/2, 3]
y3 = [1/2 , 1]
y4 = [-1/2 ,1]







t = np.linspace(1, 1.1 ,100) 

from scipy.integrate import odeint
def Solutions(y):
    sol = odeint(dgl, y, t)
    return sol

sol1 = Solutions(y1)
sol2 = Solutions(y2)
sol3 = Solutions(y3)
sol4 = Solutions(y4)

import matplotlib.pyplot as plt

plt.plot(sol1[:, 0],sol1[:, 1], linewidth = 5)
plt.plot(sol2[:, 0],sol2[:, 1], linewidth = 5)
plt.plot(sol3[:, 0],sol3[:, 1], linewidth = 5)
plt.plot(sol4[:, 0],sol4[:, 1], linewidth = 5)

plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()
