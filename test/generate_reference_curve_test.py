import numpy as np
import generate_reference_curve as rc


class TestGenerateReferenceCurve(object):
    def test_straight_line(self):
        x = np.arange(0, 110, 10)
        y = np.zeros(x.shape)
        delta = 1
        curve_desired = {"x": np.arange(0, 101, 1), "y": np.zeros(101)}
        curve_actual = rc.generate_reference_curve(x, y, delta)
        for key, value in curve_desired.items():
            np.testing.assert_allclose(curve_actual[key], curve_desired[key])

    def test_diagonal_line(self):
        # Input and actual
        alpha = np.pi / 4.
        s = np.arange(0, 60, 10)
        x = s * np.cos(alpha)
        y = s * np.sin(alpha)
        delta = 0.5
        curve_actual = rc.generate_reference_curve(x, y, delta)

        # Desired
        s_ = np.arange(0, 50 + delta, delta)
        x_desired = s_ * np.cos(alpha)
        y_desired = s_ * np.cos(alpha)
        theta_desired = np.full(101, alpha)
        kappa_desired = np.zeros(101)
        curve_desired = {'x': x_desired, 'y': y_desired, 'theta': theta_desired, 'kappa': kappa_desired}

        for key, value in curve_desired.items():
            np.testing.assert_allclose(curve_actual[key], curve_desired[key], rtol=1e-7, atol=1e-7)

    def test_curvature(self):
        alpha = np.linspace(0, 2*np.pi, 100)
        r = 10.
        x = r * np.cos(alpha)
        y = r * np.sin(alpha)
        delta = 1
        curve_actual = rc.generate_reference_curve(x, y, delta)
        kappa_desired = 1/r
        np.testing.assert_almost_equal(np.min(np.max(curve_actual['kappa'])), kappa_desired, decimal=3)

    def test_negative_curvature(self):
        alpha = np.linspace(0, -np.pi, 30)
        r = 20.
        x = r * np.cos(alpha)
        y = r * np.sin(alpha)
        delta = 0.8
        curve_actual = rc.generate_reference_curve(x, y, delta)
        kappa_desired = -1/r
        np.testing.assert_allclose(np.min(np.max(curve_actual['kappa'])), kappa_desired, atol=1e-3)


    def test_distance(self):
        alpha = np.linspace(0, -np.pi, 30)
        r = 20.
        x = r * np.cos(alpha)
        y = r * np.sin(alpha)
        delta = 0.8
        curve_actual = rc.generate_reference_curve(x, y, delta)
        x_actual = curve_actual['x']
        y_actual = curve_actual['y']
        s_actual = curve_actual['s']
        delta_s_from_postions = np.sqrt(np.diff(x_actual)**2 + np.diff(y_actual)**2)
        delta_s_actual = np.diff(s_actual)

        assert s_actual[0] == 0.0
        np.testing.assert_allclose(delta_s_actual, delta_s_from_postions)
