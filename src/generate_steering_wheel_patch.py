import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection


class SteeringWheel(object):
    def __init__(self, ax, diameter=1):
        thickness_horizontal = 0.22
        thickness_vertical = 0.15
        thickness_ring = 0.2
        diameter_center = .4
        epsilon = thickness_horizontal / 5.
        bmw_diameter = .12

        patches = [
            Circle((0, 0), diameter_center, color='k'),             # Full circle
            Wedge((0, 0), 1., 0, 360, width=thickness_ring, color='k'),
            Polygon([[thickness_horizontal, 0], [thickness_horizontal, -1 + epsilon], [-thickness_horizontal, -1 + epsilon],
                     [-thickness_horizontal, 0]], closed=True, color='k'),
            Polygon([[-1 + epsilon, thickness_vertical], [1 - epsilon, thickness_vertical], [1 - epsilon, -thickness_vertical],
                     [-1 + epsilon, -thickness_vertical]], closed=True, color='k'),
            Wedge((0, 0), bmw_diameter, 0, 360, color='white'),
            Wedge((0, 0), bmw_diameter, 90, 180, color='blue'),
            Wedge((0, 0), bmw_diameter, 270, 360, color='blue')]

        self.p = PatchCollection(patches, match_original=True)
        tf = transforms.Affine2D().scale(diameter) + ax.transData
        self.p.set_transform(tf)
        ax.add_collection(self.p)

    def update_pose(self, x, y, angle):
        tf = transforms.Affine2D().rotate(angle).translate(x, y) + ax.transData
        self.p.set_transform(tf)


fig, ax = plt.subplots()
sw = SteeringWheel(ax)
ax.margins(0.05)
ax.axis('equal')
sw.update_pose(.2, .5, 3.14 / 8)
plt.show()
