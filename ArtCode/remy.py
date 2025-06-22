import matplotlib.pyplot as plt
import numpy as np

COLOR = "#FFFFFF"
FACECOLOR = "#000000"
N_POINTS = 3000


def seq(arr, n):
    people = arr[[x for x in range(1, n) if x & n != 0]]
    taotry = 0
    while taotry in people:
        taotry += 1
    arr[n] = taotry


y = np.zeros(N_POINTS)
for n in range(1, N_POINTS):
    seq(y, n)

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
plt.scatter(range(N_POINTS), y, s=0.5, color=COLOR, marker='.')
ax.set_facecolor(FACECOLOR)
plt.axis('off')
plt.tight_layout()
plt.savefig("remy_sequence.jpg", dpi=300, bbox_inches='tight', pad_inches=0)
