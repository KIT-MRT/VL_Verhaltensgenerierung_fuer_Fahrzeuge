import numpy as np
from numpy import linalg as LA
import pytest
import pseudo_projection as pp


class TestPseudoProjection(object):

    def test_two_points(self):
        x_c = [0, 1]
        y_c = [0, 0]
        s_c = [0, 1]
        theta_c = [0, 0]
        kappa_c = [0, 0]

        x = .5
        y = 1
        proj_desired = [0.5, 0, 0.5, 1.0, 0.0, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        assert proj_desired == proj_actual

    def test_two_points_diagonal(self):
        x_c = [0, 1]
        y_c = [0, 1]
        s_c = [0, np.sqrt(2)]
        theta_c = [np.pi/4, np.pi/4]
        kappa_c = [0, 0]

        x = 0.
        y = 1.
        proj_desired = [0.5, 0.5, 0.5*np.sqrt(2), 0.5*np.sqrt(2), np.pi/4, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual)

    def test_three_points(self):
        x_c = [-1, 0, 1]
        y_c = [0, 0, 0]
        s_c = [0, 1, 2]
        theta_c = [0, 0, 0]
        kappa_c = [0, 0, 0]

        x = .5
        y = 1
        proj_desired = [0.5, 0, 1.5, 1.0, 0.0, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual)

    def test_three_points_variable_distance(self):
        x_c = [-1, 0, 2]
        y_c = [0, 0, 0]
        s_c = [0, 1, 3]
        theta_c = [0, 0, 0]
        kappa_c = [0, 0, 0]

        x = .6
        y = 1
        proj_desired = [0.6, 0, 1.6, 1.0, 0.0, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual)

    def test_three_points_variable_distance_special_case(self):
        x_c = [-1, 1, 2]
        y_c = [0, 0, 0]
        s_c = [0, 2, 3]
        theta_c = [0, 0, 0]
        kappa_c = [0, 0, 0]

        x = .6
        y = 1
        proj_desired = [0.6, 0, 1.6, 1.0, 0.0, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual)

    def test_inverse_problem_zero_distance(self):
        x_c = [1.2, 2.1]
        y_c = [3.2, 4.1]
        s_c = [5.2, 5.2 + np.sqrt((x_c[1] - x_c[0])**2 + (y_c[1] - y_c[0])**2)]
        theta_c = [0.9*np.pi/4., 1.2*np.pi/4.]
        kappa_c = [3.3, 4.4]

        lambda_ = 0.9
        d_desired = -1.3

        x_desired, y_desired, s_desired, theta_desired, kappa_desired = \
            (1.0 - lambda_) * np.array([x_c[0], y_c[0], s_c[0], theta_c[0], kappa_c[0]]) \
                  + lambda_ * np.array([x_c[1], y_c[1], s_c[1], theta_c[1], kappa_c[1]])

        # Linear interpolation of tangent vector
        tangent_vector = (1.0 - lambda_) * np.array([np.cos(theta_c[0]), np.sin(theta_c[0])]) \
                                                     + lambda_ * np.array([np.cos(theta_c[1]), np.sin(theta_c[1])])
        tangent_vector = tangent_vector / LA.norm(tangent_vector)
        normal_vector = np.array([- tangent_vector[1], tangent_vector[0]])

        # Forward generation of point to be projected
        x, y = np.array([x_desired, y_desired]) + d_desired * normal_vector

        proj_desired = [x_desired, y_desired, s_desired, d_desired, theta_desired, kappa_desired]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual, atol=0.001)





