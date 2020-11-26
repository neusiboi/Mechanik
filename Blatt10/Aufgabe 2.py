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


time = 10
stepsize = 1000
t = np.linspace(0, time ,stepsize) 


from scipy.integrate import odeint

def Solutions(y):
    sol = odeint(dgl, y, t)
    return sol

sol1 = Solutions(y1)
sol2 = Solutions(y2)
sol3 = Solutions(y3)
sol4 = Solutions(y4)

import matplotlib.pyplot as plt
L_x = [sol1[stepsize-1:, 0],sol2[stepsize-1:, 0],sol3[stepsize-1:, 0],
sol4[stepsize-1:, 0],sol1[stepsize-1:, 0]]
L_y = [sol1[stepsize-1:, 1],sol2[stepsize-1:, 1],sol3[stepsize-1:, 1],
sol4[stepsize-1:, 1],sol1[stepsize-1:, 1]]

plt.plot(L_x,L_y)
"""
plt.plot(sol1[stepsize-1:, 0],sol1[stepsize-1:, 1], 'bo')
plt.plot(sol2[stepsize-1:, 0],sol2[stepsize-1:, 1], 'go')
plt.plot(sol3[stepsize-1:, 0],sol3[stepsize-1:, 1],'ro')
plt.plot(sol4[stepsize-1:, 0],sol4[stepsize-1:, 1], 'yo')
"""

plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()
