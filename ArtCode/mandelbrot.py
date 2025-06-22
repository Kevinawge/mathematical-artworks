import numpy as np
import matplotlib.pyplot as plt

try:
    xrange
except NameError:
    xrange = range


def count_iterations(c, thresh):
    z = 0+0j
    for i in xrange(thresh):
        z = z*z + c
        if abs(z) > 4:
            return i
    return thresh


def mandelbrot(thresh, res):
    re = np.linspace(-0.235125, -0.234875, res)
    im = np.linspace(0.8275, 0.82775, res)
    atlas = np.empty((len(re), len(im)))
    for ix in xrange(len(re)):
        for iy in xrange(len(im)):
            atlas[ix, iy] = count_iterations(re[ix] + 1j*im[iy], thresh)
    plt.figure(figsize=(8, 8), dpi=300)
    plt.imshow(atlas.T, interpolation='nearest', cmap='hot', origin='lower')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig("mandelbrot_deep_zoom.png", dpi=300,
                bbox_inches='tight', pad_inches=0)
    plt.close()


mandelbrot(thresh=300, res=1500)
