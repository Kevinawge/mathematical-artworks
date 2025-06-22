import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import random

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('white')
ax.axis('off')

# Parameters
n_lines = 500
frames = 150
max_length = 120
step_range = (2, 6)

# Theme-based color palette
theme_colors = [
    "#203239", "#3C6E71", "#70A9A1", "#B8D8BA", "#557B83", "#D4E09B"
]
cmap = ListedColormap(theme_colors)

# Data structure for lines
lines_data = []
for _ in range(n_lines):
    start_x = random.uniform(-200, 200)
    start_y = random.uniform(-200, 200)
    angle = random.uniform(0, 2 * np.pi)
    curvature = random.choice([0, 0.01, -0.01, 0.005, -0.005])
    speed = random.uniform(*step_range)
    color = cmap(np.random.rand())
    lw = random.uniform(0.2, 1.8)
    lines_data.append({
        'x': [start_x],
        'y': [start_y],
        'angle': angle,
        'curve': curvature,
        'speed': speed,
        'color': color,
        'lw': lw
    })

# Line artists
artists = []
for line in lines_data:
    ln, = ax.plot(line['x'], line['y'], color=line['color'],
                  lw=line['lw'], alpha=0.4)
    artists.append(ln)

# Update function


def update(frame):
    for i, data in enumerate(lines_data):
        if len(data['x']) < max_length:
            data['angle'] += data['curve']
            new_x = data['x'][-1] + np.cos(data['angle']) * data['speed']
            new_y = data['y'][-1] + np.sin(data['angle']) * data['speed']
            data['x'].append(new_x)
            data['y'].append(new_y)
            artists[i].set_data(data['x'], data['y'])
    return artists


# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=80, blit=True)

# Save to file
ani.save("pollock_lines.gif", writer='pillow', fps=10)
