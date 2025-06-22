import matplotlib.pyplot as plt
import numpy as np

ROWS = 1000
COLOR = "#b20000"
FACECOLOR = "#000000"


def a(n):
    if n < 2:
        return n
    if n % 2 == 0:
        return a(n // 2)
    else:
        return a((n - 1) // 2) + a((n + 1) // 2)


y = [a(i) for i in range(2 ** (ROWS - 1) + ROWS - 2)]

fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
ax.set_facecolor(FACECOLOR)
plt.scatter(range(len(y)), y, s=0.5, color=COLOR, marker='.')
plt.axis('off')
plt.tight_layout()
plt.savefig("stern_sequence.jpg", dpi=300, bbox_inches='tight', pad_inches=0)
