import numpy as np
import riccati_lateral_controller as riccati


class TestRiccati(object):
    def test_size(self):
        Q = np.diag([1, 1, 1])
        R = np.array([1])
        controller = riccati.RiccatiLatControl(Q, R)
        assert(controller.gain.shape == (1, 3))
