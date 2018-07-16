import numpy as np
import pseudo_projection as pro
import kinematic_one_track_model as kotm


def feedback_law(d, psi, theta_r, kappa_r):
    axis_distance = 2.9680
    k_0 = 0.2
    k_1 = 1.

    # Stabilization
    u = kappa_r - k_0 * d - k_1 * normalize_angle(psi-theta_r)

    # Re-substitution
    delta = np.arctan(axis_distance*u)
    return delta


def normalize_angle(angle):
    return (angle+np.pi) % (2*np.pi) - np.pi




