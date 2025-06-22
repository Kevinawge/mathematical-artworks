import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

style.use('dark_background')

scale = 350
decay = -0.3
arms_cfg = [
    (scale, 1, 1.5), (scale, 0.91, 1.5),
    (-scale, 1, 1.5), (-scale, -1.09, 1.5),
    (-scale, 0.5, 1.5), (-scale, 0.4, 1.5),
    (-scale, -0.5, 1.5), (-scale, -0.6, 1.5),
]


def generate_spiral_stars(b, r, rot, fuzz_scale):
    points = []
    fuzz = int(abs(r) * 0.03)
    for i in range(1000):
        theta = math.radians(i)
        radius = r * math.exp(b * theta)
        x = radius * math.cos(theta - math.pi * rot) + \
            random.randint(-fuzz, fuzz) * fuzz_scale
        y = radius * math.sin(theta - math.pi * rot) + \
            random.randint(-fuzz, fuzz) * fuzz_scale
        z = random.uniform(-1, 1) * (scale / (scale * 3))
        points.append((x, y, z))
    return points


def generate_arms(b, cfg):
    lead, trail = [], []
    for idx, (r, rot, fuzz) in enumerate(cfg):
        arm = generate_spiral_stars(b, r, rot, fuzz)
        (lead if idx % 2 else trail).extend(arm)
    return lead, trail


def spherical_distribution(n, radius, z_factor=0.02):
    pts = np.random.normal(0, 1, (n, 3)) * radius
    pts[:, 2] *= z_factor
    return pts


def generate_core(s):
    outer = spherical_distribution(3000, s / 15)
    inner = spherical_distribution(750, s / 37.5)
    return np.vstack([outer, inner])


def generate_haze(s, r_div, z_mult, density):
    pts = []
    for _ in range(int(s * density)):
        theta = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.random()) * s / r_div
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        z = random.uniform(-1, 1) * z_mult
        pts.append((x, y, z))
    return np.array(pts)


def generate_background(n, limit):
    return np.random.uniform(-limit, limit, (n, 3))


lead_arm, trail_arm = generate_arms(decay, arms_cfg)
core = generate_core(scale)
haze1 = generate_haze(scale, 2, 0.5, 5)
haze2 = generate_haze(scale * 2, 0.8, 2, 4)
stars_bg = generate_background(1000, scale * 1.8)

fig = plt.figure(figsize=(12, 12), dpi=100)
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
ax.set_xlim(-scale * 1.5, scale * 1.5)
ax.set_ylim(-scale * 1.5, scale * 1.5)
ax.set_zlim(-15, 15)

ax.scatter(*zip(*lead_arm), c='white', s=5, alpha=0.7)
ax.scatter(*zip(*trail_arm), c='white', s=2, alpha=0.5)
ax.scatter(core[:, 0], core[:, 1], core[:, 2], c='white', s=1, alpha=0.8)
ax.scatter(haze1[:, 0], haze1[:, 1], haze1[:, 2], c='white', s=1, alpha=0.3)
ax.scatter(haze2[:, 0], haze2[:, 1], haze2[:, 2],
           c='lightgrey', s=1, alpha=0.15)
ax.scatter(stars_bg[:, 0], stars_bg[:, 1],
           stars_bg[:, 2], c='white', s=0.5, alpha=0.2)

plt.savefig("final_spiral_galaxy.png", bbox_inches='tight',
            pad_inches=0, facecolor='black')
