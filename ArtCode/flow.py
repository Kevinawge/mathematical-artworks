import math
from random import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from noise import pnoise3

c1 = (0, 0, 0)
c2 = (0.7, 0.7, 0.75)

mpl.rcParams['savefig.facecolor'] = c1
mpl.rcParams['axes.facecolor'] = c1

fig, ax = plt.subplots(figsize=(8, 8), dpi=300)  # zoomed out canvas
ax.set_xlim(-1.5, 1.5)  # expanded visible area
ax.set_ylim(-1.5, 1.5)
ax.axis("off")


def EmmitParticle(x, y, z, c, iterations, speed):
    xCur, yCur = x, y
    xPrev, yPrev = x, y
    for i in range(iterations):
        eff = pnoise3(xCur, yCur, z, octaves=1)
        angleEff = math.pi * 2 * eff
        xCur += math.cos(angleEff) * speed
        yCur += math.sin(angleEff) * speed
        if math.fabs(xCur) > 1.5 or math.fabs(yCur) > 1.5:
            return
        ax.plot((xPrev, xCur), (yPrev, yCur), c=c, lw=0.4, alpha=0.4, ls='-')
        xPrev, yPrev = xCur, yCur


def LineParticles(x1, y1, x2, y2, z, n):
    xDiff = x2 - x1
    yDiff = y2 - y1
    for i in range(n):
        off = i / n
        x = x1 + xDiff * off
        y = y1 + yDiff * off
        EmmitParticle(x, y, z, c2, 40, 0.01)


z = random() * 1000
nLines = 5
for i in range(nLines):
    off = i / (nLines - 1)
    x = ((off - 0.5) * 2) * 0.8
    LineParticles(x, -1, x, 1, z, 100)

plt.savefig("metallic_flow_zoomed.jpg", dpi=300,
            bbox_inches='tight', pad_inches=0)
