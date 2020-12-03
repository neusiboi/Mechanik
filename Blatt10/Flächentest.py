from math import sin
import numpy as np

def dgl(y,t):
    q, p = y
    dydt = [p , -sin(q) ]
    return dydt


number_of_points = 50
x_s = np.linspace(-1/2,1/2,number_of_points)
y_s = np.linspace(3,1,2*number_of_points)
L_points = []
for steps in y_s:
    for things in x_s:
        L_points.append([things,steps])


time = 100
stepsize = 100
t = np.linspace(0, time ,stepsize) 

from scipy.integrate import odeint

def Solutions(y):
    sol = odeint(dgl, y, t)
    return sol

k = 0
p=0
test = []

while k < 2*number_of_points**2:
    p += 1
    k = k +(2*number_of_points**2)/10
    test.append(k)

k = 0
solution = []
print("Starte mit Lösen der Dgl")
for points in L_points:
    solution.append(Solutions(points))
    k+=1
    if k in test:
        print(k, "gelöste Dgls,", 2*number_of_points**2-k, "noch zu lösen")



import matplotlib.pyplot as plt
L_x = []
for points in solution:
    L_x.append(points[stepsize-1:, 0])

L_y = []
for points in solution:
    L_y.append(points[stepsize-1:, 1])

plt.axis([-10, 10, -2, 2])
plt.plot(L_x,L_y,"bo", markersize = 1)
plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()
