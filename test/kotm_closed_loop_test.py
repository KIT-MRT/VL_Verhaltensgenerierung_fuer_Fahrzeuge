import numpy as np
import kotm_closed_loop as cl
import generate_reference_curve as ref

def test_closed_loop_straight_without_initial_error():
    x0 = [0.0, 0.0, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    output_trajectory = model.simulate(ti)
    y_end = output_trajectory[-1, 1]
    np.testing.assert_almost_equal(0.0, y_end)


def test_closed_loop_straight_with_initial_error():
    x0 = [0.0, .1, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    output_trajectory = model.simulate(ti)
    y_end = output_trajectory[-1, 1]
    np.testing.assert_almost_equal(0.0, y_end, decimal=3)


def test_closed_loop_circle_without_initial_error():
    radius = 20
    curve = ref.generate_reference_curve([0, radius, 0, -radius, 0], [-radius, 0, radius, 0, radius], 1.0)
    x0 = [curve['x'][0], curve['y'][0], curve['theta'][0]]
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    output_trajectory = model.simulate(ti)
    d_end = output_trajectory[-1, 3]
    np.testing.assert_almost_equal(0.0, d_end, decimal=2)


def test_closed_loop_circle_with_initial_error():
    radius = 15
    curve = ref.generate_reference_curve([0, radius, 0, -radius, 0], [-radius, 0, radius, 0, radius], 1.0)
    initial_error = 0.2
    x0 = [curve['x'][0], curve['y'][0] + initial_error, curve['theta'][0]]
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    output_trajectory = model.simulate(ti)
    d_end = output_trajectory[-1, 3]
    np.testing.assert_almost_equal(0.0, d_end, decimal=2)
