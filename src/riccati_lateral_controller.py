from scipy import linalg
import numpy as np

class RiccatiLatControl:
    def __init__(self, Q, R):

        A = np.array([[1, 2, 3],
                      [1, 2, 3],
                      [1, 2, 3]])

        B = np.array([[0],
                      [0],
                      [1]])

        P = linalg.solve_continuous_are(A, B, Q, R)
        self.gain = 1.0 / R + np.dot(B.transpose(),P)