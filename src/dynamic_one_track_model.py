import numpy as np
from scipy.integrate import odeint


def params():
    return {'l': 2.9680}


def fun(x, t, v): # x_dot = f(x,t)
    x, y, psi, r, beta = x

    x_dot = v*np.cos(psi + beta)
    y_dot = v*np.sin(psi + beta)
    psi_dot = r
    r_dot = 0
    beta_dot = 0

    dxdt = [x_dot, y_dot, psi_dot, r_dot, beta_dot]
    return dxdt


def simulate(x0, v, ti):
    sol = odeint(fun, x0, ti, args=(v,))
    return sol
