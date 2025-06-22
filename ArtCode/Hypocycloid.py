import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
fig.patch.set_facecolor('ivory')
ax.set_facecolor('ivory')

for i, (R, r) in enumerate([(5, 3), (6, 4), (7, 2.5)]):
    theta = np.linspace(0, 2 * np.pi * R, 20000)
    k = R / r
    x = (R - r) * np.cos(theta) + r * np.cos((k - 1) * theta)
    y = (R - r) * np.sin(theta) - r * np.sin((k - 1) * theta)
    intensity = (np.sin(theta * 2 + i * np.pi / 3) + 1) / 2
    for alpha in np.linspace(0.02, 0.12, 5):
        ax.scatter(x, y, c=intensity, cmap='twilight_shifted',
                   s=0.2, alpha=alpha, edgecolors='none')
        ax.scatter(-x, -y, c=intensity, cmap='twilight_shifted',
                   s=0.2, alpha=alpha, edgecolors='none')

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("hypocycloid.jpg", format="jpg", dpi=300,
            facecolor='ivory', bbox_inches='tight', pad_inches=0)
plt.close()
