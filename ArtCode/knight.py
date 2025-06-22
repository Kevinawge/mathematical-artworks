import numpy as np
import cv2
import math

board_size = 61
center_cell = board_size // 2
cell_width = 10
board = np.zeros([board_size, board_size], np.int32)

leaps = np.resize(np.repeat(np.arange(1, board_size + 1), 2),
                  board_size * 2 - 1)
direction = np.array([[0, 1], [-1, 0], [0, -1], [1, 0]])
steering = np.zeros([sum(leaps), 2], np.int32)
count = 0
for i in range(len(leaps)):
    for _ in range(leaps[i]):
        steering[count] = direction[i % 4]
        count += 1

pos = np.array([center_cell, center_cell])
count = 1
for turn in steering:
    board[tuple(pos)] = count
    count += 1
    pos += turn


def check_nbros(pos, board, limit):
    nbors = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2],
                     [2, 1], [2, -1], [-2, 1], [-2, -1]])
    nbors_pos = pos + nbors
    nbors_pos = nbors_pos[(nbors_pos[:, 0] >= 0) & (nbors_pos[:, 1] >= 0) &
                          (nbors_pos[:, 0] < limit) & (nbors_pos[:, 1] < limit)]
    nbors_pos = np.array(
        [p for p in nbors_pos if board[tuple(p)] != limit**2 + 1])
    if len(nbors_pos) > 0:
        nbors_values = np.array([board[tuple(p)] for p in nbors_pos])
        return nbors_pos[np.argmin(nbors_values)]
    else:
        return pos


pos = np.array([center_cell, center_cell])
path = np.zeros([board_size**2, 2], np.uint32)
for i in range(board_size**2):
    path[i] = pos
    board[tuple(pos)] = board_size**2 + 1
    pos = check_nbros(pos, board, board_size)

img = np.zeros((board_size * cell_width, board_size * cell_width, 3), np.uint8)

path = path * cell_width
color = [0, 255, 0]
for n, coord in enumerate(path[:-1]):
    if n % 10 == 0:
        color[1] = max(color[1] - 1, 50)
    if n % 5 == 0:
        color[2] = min(color[2] + 2, 255)
    img = cv2.line(img, tuple(coord), tuple(path[n + 1]), color, 2)

cv2.imwrite("knight_path.jpg", img)
