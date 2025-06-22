import numpy as np
import matplotlib.pyplot as plt

a, b, c, d = -1.4, 1.6, 1.0, 0.7
n_points = 1_000_000

x = np.zeros(n_points)
y = np.zeros(n_points)

for i in range(1, n_points):
    x[i] = np.sin(a * y[i - 1]) + c * np.cos(a * x[i - 1])
    y[i] = np.sin(b * x[i - 1]) + d * np.cos(b * y[i - 1])

intensity = np.sqrt(x**2 + y**2)
intensity = (intensity - intensity.min()) / (intensity.max() - intensity.min())

x_full = np.concatenate([x, -x])
y_full = np.concatenate([y, -y])
intensity_full = np.concatenate([intensity, intensity])

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

for alpha in np.linspace(0.02, 0.15, 6):
    ax.scatter(
        x_full, y_full,
        s=0.02,
        c=intensity_full,
        cmap='twilight_shifted',
        alpha=alpha,
        edgecolors='none'
    )

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("clifford.jpg", format="jpg", dpi=300,
            facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
