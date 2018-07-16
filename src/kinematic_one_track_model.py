import numpy as np
from scipy.integrate import odeint


class KinematicOneTrackModel(object):
    def __init__(self):
        self.params = self.params()

    def system_dynamics(self, x_, t, v, delta):  # x_dot = f(x,t)
        x, y, psi = x_

        x_dot = v*np.cos(psi)
        y_dot = v*np.sin(psi)
        psi_dot = v*np.tan(delta)/self.params['l']

        dxdt = [x_dot, y_dot, psi_dot]
        return dxdt

    @staticmethod
    def params():
        return {'l': 2.9680}

    def simulate(self, x0, v, delta, ti):
        sol = odeint(self.system_dynamics, x0, ti, args=(v, delta))
        return sol
