from scipy.integrate import quad
from math import cos, exp, pi, sin, sqrt
from scipy.misc import derivative


def curve (x): #Die Kurve welche die Bahn beschreibt
    return -sqrt(1/2*x)

def Nenner(x): #Nenner des Integrals 
    return 1/sqrt(2*-(curve(x))*9.81)

def deriv (x, h=0.00000001): #differential quotient für die Ableitung (hier ensteht ein Fehler da es nicht die ableitung ist sondern nur eine annäherung)
    return curve(x+h)/h-curve(x)/h

def Zähler(x): #Zähler des integrals
    return sqrt(1+( deriv(x) )**2)

def integrator (y): #Zusammengesetzte Funktion für das Integral
    return Zähler(y)*Nenner(y)

if curve(0)==0 and curve(2)==-1: #Prüft ob die Funktion die gegebenen Vorraussetzungen erüllt
    print("Die Kurve erfüllt die Vorraussetzungen und die benötigte Zeit ist (Wert [s], Fehler[s])")
    print(quad(integrator,0,2)) #Integral von Nenner mal Zähler welches die benötigte Zeit ist
else:
    print("Die Kurve erfüllt nicht die Vorraussetzungen") #Falls die Vorraussetzungen nicht erfüllt werden bekommen wir als output einen Fehler


#f(x)=-1/2*x                                     time:(1.0096375544955325, 1.7783297057150094e-09)
#f(x)=-1*x+1/4*x**2                              time:(0.8624548063069947, 4.309375745137345e-09)
#f(x)=(1/(x+1)-1)*3/2                            time:(0.8355438465062506, 1.1712219194492945e-08)
#f(x)=-sin(1/4*pi*x)                             time:(0.8924637063678499, 8.189575684269812e-10)
#f(x)=(exp(-x+1)-exp(1))*exp(1)/(-1 + exp(2))    time:(0.8527180257272348, 4.494299155055614e-09)
#f(x)=-sqrt(1/2*x)                               time:(0.8248173097914494, 1.464707588549885e-08)