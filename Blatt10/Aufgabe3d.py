from math import sin, cos, pi, sqrt
import numpy as np

a = 1
m = 1
g = 1

def Energy(y):
    T = -(g*a*2*m*cos(y[0])+g*a*m*cos(y[2]))

    V_Zähler = m*y[1]**2+2*m*y[3]**2-2*m*y[1]*y[3]*cos(y[0]-y[2])
    V_Nenner = a**2*m*(3*m-m*cos(2*(y[0]-y[2])))
    
    return T+V_Zähler/V_Nenner


ys = 0 ,0 ,0 ,0
print(Energy(ys))
Given_Value = -2.9

if Energy(ys) == Given_Value:
    def differentialeq(y, t):
        theta1, p_theta1, theta2, p_theta2 = y

        c, s = cos(theta1 - theta2), sin(theta1 - theta2)
        den = 16*m - 9 * m * c**2

        theta1dot = 6 / a**2 * (2*p_theta1 - 3  * c * p_theta2) / den
        theta2dot = 6 / m / a**2 * (
                        (2 * p_theta2 * 4*m - 3 * m / 1 * c * p_theta1) / den)
        term = m * a**2 / 2 * theta1dot * theta2dot * s
        p_theta1dot = -term - (m/2 + m) * g * a * sin(theta1)
        p_theta2dot = term - m/2 * g * a * sin(theta2)

        return theta1dot, p_theta1dot, theta2dot, p_theta2dot

    time = 3000
    t = np.linspace(0,time,10000)

    from scipy.integrate import odeint

    def Solutions(y):
        sol = odeint(differentialeq, y, t)
        return sol

    print("Starting with solving the Differential-equation")
    Points = Solutions(ys) #Note its a list of Lists 
    print("Finished with solving the Differential-equation")

    PlotPoints_q = []
    PlotPoints_p = []
    for things in Points:
        if -0.1<things[2]<0.1 and things[3]>0:
            PlotPoints_q.append(things[0])
            PlotPoints_p.append(things[1])


    PlotPoints_q2 = []
    for things in PlotPoints_q:
        if things not in PlotPoints_q2:
            PlotPoints_q2.append(things)

    PlotPoints_p2 = []
    for things in PlotPoints_p:
        if things not in PlotPoints_p2:
            PlotPoints_p2.append(things)


    import matplotlib.pyplot as plt


    plt.plot(PlotPoints_q2,PlotPoints_p2,'bo',  markersize = 3)
    plt.xlabel('q1')
    plt.ylabel('p1')
    plt.grid() 
    plt.show()
else:
    print("does not fulfill the given conditions" )
        

 