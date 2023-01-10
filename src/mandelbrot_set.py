import matplotlib.pyplot as plt
import numpy as np

"""
I Don't fully understand this one yet, it's pretty though. 

complex_matrix returns an array of real and imaginary numbers for is stable to work on
is_stable contains the definition of the mandelbrot function
"""


# Linearly spaced real and imaginary numbers between xmin, xmax and ymin, ymax, pixel density amount.
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    real = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2


if __name__ == '__main__':
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
    plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
