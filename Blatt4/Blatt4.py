
from scipy.integrate import odeint
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp, sin, cos
from numpy import log as ln

t = 0 #Startzeit
T = 20 #Simulationsdauer
dt = 0.01 #Schrittgröße der Zeit

#Anfangsbedingungen
x = 1
y = 1

v_x = 0
v_y = 1

lx = [] #Zwei Listen damit man später einen Plot erstellen kann 
ly = []

while t <= T:
    t = t+dt #Zählt die einzelenen Schritte in der Zeit in Abstand dt hoch

    #Hie sind die einzelen zu lösenden dgls aufgelistet 
    """
    a_y = (-y)/((x**2+y**2)**(3/2))
    a_x = (-x)/((x**2+y**2)**(3/2))

    v_x += a_x*dt
    v_y += a_y*dt

    x += v_x * dt
    y += v_y*dt
    """

    """
    a_x = (-x)/(x**2+y**2)
    a_y = (-y)/(x**2+y**2)

    v_x += a_x*dt
    v_y += a_y*dt

    x += v_x * dt
    y += v_y*dt

    """
    """
    a_x = -x
    a_y = -2*y

    v_x += a_x*dt
    v_y += a_y*dt

    x += v_x * dt
    y += v_y*dt
    """
    """
    a_x = (20*exp(5+10*sin(x)**2*sin(y)**2)*cos(x)*sin(x)*sin(y)**2)/(exp(5)+exp(10*sin(x)**2*sin(y)**2))**2
    a_y = (20*exp(5+10*sin(x)**2*sin(y)**2)*cos(y)*sin(x)**2*sin(y))/(exp(5)+exp(10*sin(x)**2*sin(y)**2))**2

    v_x += a_x*dt
    v_y += a_y*dt

    x += v_x * dt
    y += v_y*dt
    """
    a_x = -2*x
    a_y = -2*y

    v_x += a_x*dt
    v_y += a_y*dt

    x += v_x * dt
    y += v_y*dt
    lx.append(x) #Hier werden die Listen erzeugt die wir für die Plots brauchen 
    ly.append(y) 

plt.axis([0, 10, -30, 50]) #hier werden die Plots erzeugt
plt.plot(lx,ly, linewidth=2.0)
plt.show()