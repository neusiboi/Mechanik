import matplotlib.pyplot as plt
from math import sin
T=100
dt=0.001
t=0.1
k=0
x=0
L_t = []
L_x = []

while t<T:
    t +=dt
    dx = -sin(t)
    x+= dx*dt   
    L_t.append(t)
    L_x.append(x)


plt.plot(L_t, L_x,
         linewidth=0.5)
plt.show()