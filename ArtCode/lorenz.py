import numpy as np
import matplotlib.pyplot as plt

sigma = 10
rho = 28
beta = 8 / 3
dt = 0.005
steps = 100000

xs = np.empty(steps + 1)
ys = np.empty(steps + 1)
zs = np.empty(steps + 1)
xs[0], ys[0], zs[0] = (0., 1., 1.05)

for i in range(steps):
    dx = sigma * (ys[i] - xs[i])
    dy = xs[i] * (rho - zs[i]) - ys[i]
    dz = xs[i] * ys[i] - beta * zs[i]
    xs[i + 1] = xs[i] + dx * dt
    ys[i + 1] = ys[i] + dy * dt
    zs[i + 1] = zs[i] + dz * dt

colors = np.linspace(0, 1, steps)
cmap = plt.cm.plasma

fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
fig.patch.set_facecolor('ivory')
ax.set_facecolor('ivory')
ax.axis('off')

for i in range(1, steps):
    ax.plot(xs[i-1:i+1], ys[i-1:i+1], color=cmap(colors[i]),
            alpha=0.05, linewidth=0.5)

plt.savefig("lorenz_ivory.png", dpi=300, bbox_inches='tight',
            pad_inches=0, facecolor='ivory')
plt.close()
