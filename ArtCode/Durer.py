import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10), dpi=400)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

n_spirals = 100
theta = np.linspace(0, 10 * np.pi, 2000)


def generate_spiral_group(n, a, b, twist=1, reverse=False, colormap='plasma'):
    for i in range(n):
        offset = 2 * np.pi * i / n * twist
        r = a + b * theta
        if reverse:
            x = r * np.cos(-theta + offset)
            y = r * np.sin(-theta + offset)
        else:
            x = r * np.cos(theta + offset)
            y = r * np.sin(theta + offset)
        intensity = (np.sin(theta * 2 + offset) + 1) / 2
        for alpha in np.linspace(0.02, 0.12, 6):
            ax.scatter(x, y, c=intensity, cmap=colormap,
                       s=0.3, alpha=alpha, edgecolors='none')


generate_spiral_group(n=80, a=0.01, b=0.14, twist=1,
                      reverse=False, colormap='twilight_shifted')
generate_spiral_group(n=60, a=0.02, b=0.10, twist=1.5,
                      reverse=True, colormap='magma')

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("durer.jpg", format="jpg", dpi=400,
            facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
