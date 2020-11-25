from math import sin
import numpy as np

def dgl(y,t):
    q, p = y
    dydt = [p , -sin(q) ]
    return dydt


x_s = np.linspace(-1/2,1/2,1000)
L_xs = []
L_xs2 = []
for steps in x_s:
    L_xs.append([steps, 3])
    L_xs2.append([steps*-1 ,1 ])

y_s = np.linspace(3,1,1000)
L_ys = []
L_ys2 = []
for steps in y_s:
    L_ys.append([1/2,steps])

y_s2 = np.linspace(1,3,1000)
for steps in y_s2:
    L_ys2.append([-1/2,steps])

time = 0
stepsize = 100
t = np.linspace(0, time ,stepsize) 


from scipy.integrate import odeint

def Solutions(y):
    sol = odeint(dgl, y, t)
    return sol


sol_xs = []
sol_xs2 = []
for points in L_xs:
    sol_xs.append(Solutions(points))
for points in L_xs2:
    sol_xs2.append(Solutions(points))


sol_ys = []
sol_ys2 = []
for points in L_ys:
    sol_ys.append(Solutions(points))
for points in L_ys2:
    sol_ys2.append(Solutions(points))



import matplotlib.pyplot as plt
L_x = []
for points in sol_xs:
    L_x.append(points[stepsize-1:, 0])
for points in sol_ys:
    L_x.append(points[stepsize-1:, 0])
for points in sol_xs2:
    L_x.append(points[stepsize-1:, 0])
for points in sol_ys2:
     L_x.append(points[stepsize-1:, 0])


L_y = []
for points in sol_xs:
    L_y.append(points[stepsize-1:, 1])
for points in sol_ys:
    L_y.append(points[stepsize-1:, 1])
for points in sol_xs2:
    L_y.append(points[stepsize-1:, 1])
for points in sol_ys2:
    L_y.append(points[stepsize-1:, 1])



L_x2 = []
L_y2 = []
for points in L_x:
    L_x2.append(points[0])
for points in L_y:
    L_y2.append(points[0])


plt.plot(L_x2,L_y2)


plt.xlabel('q')
plt.ylabel('p')
plt.grid() 
plt.show()
