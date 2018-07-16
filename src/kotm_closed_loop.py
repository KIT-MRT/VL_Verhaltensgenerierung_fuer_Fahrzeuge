import numpy as np
from scipy.integrate import odeint
import kinematic_one_track_model as kotm
import kinematic_control as kc
import pseudo_projection as pro


class KotmClosedLoop(object):
    def __init__(self, initial_condition, curve):
        self.x0 = initial_condition
        self.curve = curve

    def simulate(self, t_vector):
        state_trajectory = odeint(self._f_system_dynamics, self.x0, t_vector)
        output_trajectory = np.array([self._g_system_output(x) for x in state_trajectory])
        return output_trajectory

    def _f_system_dynamics(self, x_, t):
        x, y, psi = x_
        _, _, _, d, theta_r, kappa_r = \
            pro.project2curve(self.curve['s'], self.curve['x'], self.curve['y'], self.curve['theta'], self.curve['kappa'],
                              x, y)
        delta = kc.feedback_law(d, psi, theta_r, kappa_r)
        v = 1  # const velocity
        x_dot = kotm.KinematicOneTrackModel().system_dynamics(x_, t, v, delta)
        return x_dot

    def _g_system_output(self, x_):
        x, y, psi = x_
        _, _, _, d, theta_r, kappa_r = \
            pro.project2curve(self.curve['s'], self.curve['x'], self.curve['y'], self.curve['theta'],
                              self.curve['kappa'],
                              x, y)
        delta = kc.feedback_law(d, psi, theta_r, kappa_r)

        return [x, y, psi, d, delta]



