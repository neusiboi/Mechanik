from math import sin, cos
from scipy.integrate import solve_ivp
def rhs(s, v): 
    return [-12*v[2]**2, 12*v[2]**2, 6*v[0]*v[2] - 6*v[2]*v[1] - 36*v[2]]

res = solve_ivp(rhs, (0, 0.1), [2, 3, 4])
print(res)