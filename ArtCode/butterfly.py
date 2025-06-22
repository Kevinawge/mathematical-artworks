import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12 * np.pi, 10000)
r = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5
x = np.sin(t) * r
y = np.cos(t) * r
colors = plt.cm.twilight_shifted((t - t.min()) / (t.max() - t.min()))

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
for i in range(len(x) - 1):
    ax.plot(x[i:i + 2], y[i:i + 2], color=colors[i], linewidth=0.8)

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("butterfly.jpg", format="jpg", dpi=300,
            bbox_inches='tight', pad_inches=0)
