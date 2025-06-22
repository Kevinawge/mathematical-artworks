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

fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
ax.set_xlim(-1.5, 1.5)
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


z = random() * 1000
t = np.linspace(-1, 1, 150)
y = np.sin(t * math.pi)
for pX, pY in zip(t, y):
    EmmitParticle(pX, pY, z, c2, 60, 0.01)

plt.savefig("metallic_sinwave_zoomed.jpg", dpi=300,
            bbox_inches='tight', pad_inches=0)
