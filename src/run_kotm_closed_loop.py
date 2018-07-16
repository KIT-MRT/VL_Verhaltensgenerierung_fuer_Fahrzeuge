import numpy as np
import matplotlib.pyplot as plt
import kotm_closed_loop as cl
import generate_reference_curve as ref


def main():
    print('Running simulation...')
    radius = 20
    x0 = [0.0, -radius, 0.0]
    curve = ref.generate_reference_curve([0, radius, 0, -radius, 0], [-radius, 0, radius, 0, radius], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    sol = model.simulate(ti)
    x = sol[:, 0]
    y = sol[:, 1]
    plt.plot(curve['x'], curve['y'], 'r-')
    plt.plot(x, y, 'b-')
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    main()
