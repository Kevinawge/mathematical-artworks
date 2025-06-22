import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def trans_1(x, y): return (0., 0.16 * y)
def trans_2(x, y): return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)
def trans_3(x, y): return (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)
def trans_4(x, y): return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)


transformations = [trans_1, trans_2, trans_3, trans_4]
probas = [0.01, 0.85, 0.07, 0.07]


def barnsley_fern(num_points, width, height):
    x, y = 0, 0
    image = np.zeros((width, height))

    for _ in range(num_points):
        trans = np.random.choice(transformations, p=probas)
        x, y = trans(x, y)
        px, py = int(width / 2 + x * width / 10), int(y * height / 11)
        if 0 <= px < width and 0 <= py < height:
            image[px, py] = 1
    return image


width, height = 1200, 1200
num_points = width * height

fern = barnsley_fern(num_points, width, height)

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
fig.patch.set_facecolor('ivory')
ax.set_facecolor('ivory')
ax.axis('off')
ax.imshow(fern[::-1, :], cmap='Greens')
plt.tight_layout()
plt.savefig("fern_ivory.jpg", format='jpg', dpi=300,
            bbox_inches='tight', pad_inches=0, facecolor='ivory')
plt.close()
