import dynamic_one_track_model as dotm
import numpy as np


class TestSimDotm(object):
    def test_fun(self):
        x, y, psi, beta, r = 0, 0, 0, 0, 0
        t = 0
        v = 10
        state_x = [x, y, psi, beta, r]
        state_x_dot = dotm.fun(state_x, v, t)
        assert(state_x_dot == [0, 0, 0, 0, 0])

    def test_simulate_standstill(self):
        x0 = [0, 0, 0, 0, 0]
        ti = np.linspace(0, 1, 10)
        v = 0
        x_desired = np.zeros((len(ti), 5))
        x_actual = dotm.simulate(x0, v, ti)
        np.testing.assert_allclose(x_desired, x_actual)


    def test_simulate_const_velocity(self):
        x0 = [0, 0, 0, 0, 0]
        ti = np.linspace(0, 1, 10)
        v = 10
        x_desired = np.zeros((len(ti), 5))
        x_desired[:, 0] = ti*v
        x_actual = dotm.simulate(x0, v, ti)

        np.testing.assert_allclose(x_desired, x_actual, rtol=1e-5, atol=0)

    def test_simulate_const_velocity_diagonal(self):
        psi_const = np.pi/4
        x0 = [0, 0, psi_const, 0, 0]
        ti = np.linspace(0, 1, 10)
        v = 12
        s = ti*v
        x_desired = np.zeros((len(ti), 5))
        x_desired[:, 0] = s * np.cos(psi_const)
        x_desired[:, 1] = s * np.sin(psi_const)
        x_desired[:, 2] = np.ones(s.shape) * psi_const
        x_actual = dotm.simulate(x0, v, ti)

        np.testing.assert_allclose(x_desired, x_actual, rtol=1e-5, atol=0)
