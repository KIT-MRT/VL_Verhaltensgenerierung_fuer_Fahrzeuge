import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class KammsCircle(object):
    def __init__(self, ax, x=0, y=0, r=1, a_max=10):
        self.x = x
        self.y = y
        self.r = r
        self.a_max = a_max
        c = Circle((x, y), r, facecolor='grey', edgecolor='k')
        ax.add_patch(c)
        self.a = plt.Line2D([], [], color='k', marker='P')
        ax.add_line(self.a)

    def update(self, a_vec):
        self.a.set(xdata=[self.x, self.x + a_vec[0]/self.a_max*self.r], ydata=[self.y, self.y + a_vec[1]/self.a_max*self.r])


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')

kc = KammsCircle(ax1, 3, 5)
kc.update((-2, 5))
plt.margins(.5)
plt.show()
