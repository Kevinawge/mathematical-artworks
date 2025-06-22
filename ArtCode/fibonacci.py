import cv2
import numpy as np

N_SQUARES = 13
WIN_SCALE = 2
RECT_COLOR = (100, 200, 255)       # soft light blue
RECT_WIDTH = 1
ARC_COLOR = (200, 200, 200)        # soft metallic silver
ARC_THICKNESS = 2


def fibo(n):
    return fibo(n - 2) + fibo(n - 1) if n > 2 else 1


def win_dimensions(n):
    return WIN_SCALE * fibo(n) + 1, WIN_SCALE * fibo(n + 1) + 1


def get_pts(pt, leapsize, dir_modulo):
    sq_dirs = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    el_dirs = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    sq_vertex = tuple(pt + leapsize * sq_dirs[dir_modulo])
    el_center = tuple(pt + leapsize * el_dirs[dir_modulo])
    return sq_vertex, el_center


def draw_arc(img, pt, iter_num, squares=False):
    mod = (iter_num - N_SQUARES) % 4
    leap = fibo(iter_num) * WIN_SCALE
    newpt, el_center = get_pts(pt, leap, mod)
    angle = [90, 180, 270, 0][mod]
    cv2.ellipse(img, el_center, (leap, leap), angle,
                0, 90, ARC_COLOR, ARC_THICKNESS)
    if squares:
        cv2.rectangle(img, pt, newpt, RECT_COLOR, thickness=RECT_WIDTH)
    return newpt


img = np.zeros((*win_dimensions(N_SQUARES), 3), dtype=np.uint8)
origin = (0, 0)

for i in np.arange(N_SQUARES, 1, -1):
    origin = draw_arc(img, origin, i, squares=True)

cv2.imwrite("fibonacci_spiral.jpg", img)
