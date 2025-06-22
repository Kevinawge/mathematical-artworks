import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.set_facecolor('black')

TWO_PI = 2 * np.pi
PI = np.pi

for i in range(1, 361):
    angle_rad = np.radians(i)
    xi = np.sin(angle_rad)
    size = (np.tan(angle_rad) * PI * np.cos(angle_rad)
            * TWO_PI * np.cos(angle_rad) * PI) * 6

    rotation = (TWO_PI / 5) * i
    transform = Affine2D().rotate(rotation).translate(xi * 100, 0)

    square = Rectangle(
        (-size / 2, -size / 2), size, size,
        transform=transform + ax.transData,
        linewidth=0.3, edgecolor='white', facecolor='none'
    )
    ax.add_patch(square)

ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.axis('off')

plt.tight_layout()
plt.savefig("generative_squares.png", dpi=300,
            facecolor='black', bbox_inches='tight', pad_inches=0)
plt.close()
