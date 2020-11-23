import matplotlib.pyplot as plt
from math import exp

#define starting parameters
h = 0.1
x = 1
y = 1

n = 0
N = 10

Jan 


L_x = []
L_y = []
#Setting up functions
def first_order_diff(y,x):
    dy_dx = 3*x**2
    return dy_dx

def d_1(x,y):
    return h*first_order_diff(x,y)

def d_2(x,y):
    return h*first_order_diff(x+h/2,y+d_1(x,y)/2)

def d_3(x,y):
    return h*first_order_diff(x+h/2,y+d_2(x,y)/2)

def d_4(x,y):
    return h*first_order_diff(x+h,y+d_3(x,y))


#solving the differential equations 
while n<N:
    n+=1
    print(n)
    y = y + d_1(x,y)/6 + d_2(y,x)/3 + d_3(x,y)/3 + d_4(x,y)/6
    x = x + h
    L_x.append(x)
    L_y.append(y)


plt.grid("on")
plt.plot(L_x, L_y,
         linewidth = 0.5)
plt.show()
