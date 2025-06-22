import math
from random import random
import matplotlib as mpl
import matplotlib.pyplot as plt

c1 = (0, 0, 0)
c2 = (0.7, 0.7, 0.75)

mpl.rcParams['savefig.facecolor'] = c1
mpl.rcParams['axes.facecolor'] = c1

fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis("off")


def Circ(n):
    xPrev, yPrev = 0, 0
    for i in range(n):
        fac = random()
        x = math.cos(fac * math.pi * 2)
        y = math.sin(fac * math.pi * 2)
        ax.plot((xPrev, x), (yPrev, y), c=c2, lw=0.4, alpha=0.2)
        xPrev, yPrev = x, y


Circ(500)
plt.savefig("metallic_circle_lines_zoomed.jpg",
            dpi=300, bbox_inches='tight', pad_inches=0)
