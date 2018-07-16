import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_vehicle(ax, x, y, psi, delta=0, length = 4.899, width=2.094):
    geo = np.load('f10.npy')[()]
    x_offset = np.mean(geo["wheel3"][:, 0]) # find rear axis position
    length_data = np.max(geo["chassi"][:, 0]) - np.min(geo["chassi"][:, 0])
    width_data = np.max(geo["chassi"][:, 1]) - np.min(geo["chassi"][:, 1])
    length_scale = length/length_data
    width_scale = width/width_data

    for key, value in geo.items(): # make rear axis 0,0
        value[:, 0] -= x_offset
        value[:, 0] *= length_scale
        value[:, 1] *= width_scale

    for key, value in geo.items():

        if key == 'wheel1' or key == 'wheel2':
            #deltaX = max(value[:, 0]) - min(value[:, 0])
            #deltaY = max(value[:, 1]) - min(value[:, 1])
            centerX = np.mean(value[:,0])
            centerY = np.mean(value[:,1])

            polygon = Polygon(value, closed=True, alpha=0.5)
            c = ax.add_patch(polygon)
            transform = mpl.transforms.Affine2D().translate(-centerX, -centerY).rotate(delta).translate(centerX, centerY).translate(x,y).rotate(psi) + ax.transData
        else:
            transform = mpl.transforms.Affine2D().translate(x, y).rotate(psi) + ax.transData
            polygon = Polygon(value, closed=True, alpha=0.5)
            c = ax.add_patch(polygon)

        c.set_transform(transform)