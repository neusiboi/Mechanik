from math import sin
import numpy as np

def dgl(y,t):
    q, p = y
    dydt = [p , -sin(q) ]
    return dydt

y_0 = [0 ,2]


t = [10, 10.001] #np.linspace(10, 10 ,100) 




from scipy.integrate import odeint
sol = odeint(dgl, y_0, t)

import matplotlib.pyplot as plt

plt.plot(sol[:, 0],sol[:, 1], 'b', label='theta(t)')
plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()

