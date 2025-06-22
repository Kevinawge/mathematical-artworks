import math


def lorenz(xyz, t, sigma, beta, rho):
    x, y, z = xyz
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz


def halvorsen(xyz, t, a):
    x, y, z = xyz
    dx = - a * x - 4 * (y + z) - y ** 2
    dy = - a * y - 4 * (z + x) - z ** 2
    dz = - a * z - 4 * (x + y) - x ** 2
    return dx, dy, dz


def aizawa(xyz, t, alpha, beta, gamma, delta, epsilon, zeta):
    x, y, z = xyz
    dx = x * (z - beta) - delta * y
    dy = y * (z - beta) + delta * x
    dz = gamma + alpha * z - z ** 3 / 3 - \
        (x ** 2 + y ** 2) * (1 + epsilon * z) + zeta * z * (x ** 3)
    return dx, dy, dz


def rossler(xyz, t, a, b, c):
    x, y, z = xyz
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz


def thomas(xyz, t, b):
    x, y, z = xyz
    dx = math.sin(y) - b * x
    dy = math.sin(z) - b * y
    dz = math.sin(x) - b * z
    return dx, dy, dz


def chen(xyz, t, a, c, b):
    x, y, z = xyz
    dx = a * (y - x)
    dy = (c - a) * x - x * z + c * y
    dz = x * y - b * z
    return dx, dy, dz


def dadras(xyz, t, a, b, c, d, e):
    x, y, z = xyz
    dx = y - a * x + b * y * z
    dy = c * y - x * z + z
    dz = d * x * y - e * z
    return dx, dy, dz
