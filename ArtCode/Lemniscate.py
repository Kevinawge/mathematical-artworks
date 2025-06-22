import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 12), dpi=400)
fig.patch.set_facecolor('ivory')
ax.set_facecolor('ivory')

theta = np.linspace(0, 2 * np.pi, 2000)
n_lemniscates = 120
a = 1.5

for i in range(n_lemniscates):
    phase = 2 * np.pi * i / n_lemniscates
    r = a * np.sqrt(np.abs(np.cos(2 * theta)))
    x = r * np.cos(theta + phase)
    y = r * np.sin(theta + phase)
    color_intensity = (np.sin(3 * theta + phase) + 1) / 2
    for alpha in np.linspace(0.02, 0.12, 5):
        ax.scatter(x, y, c=color_intensity, cmap='twilight_shifted',
                   s=0.3, alpha=alpha, edgecolors='none')

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("lemniscate_field.jpg", format="jpg", dpi=400,
            bbox_inches='tight', pad_inches=0, facecolor='ivory')
plt.close()
