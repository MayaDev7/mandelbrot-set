import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Calculate the number of iterations required for a complex number c to diverge under the function z^2 + c.

    Args:
        c (complex): The complex number to calculate the number of iterations for.
        max_iter (int): The maximum number of iterations.

    Returns:
        int: The number of iterations required for c to diverge, or max_iter if c does not diverge.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return max_iter

width = 300
height = 300
max_iter = 256

x_min = -2.0
x_max = 1.0
y_min = -1.0
y_max = 1.0

real = np.linspace(x_min, x_max, width)
imag = np.linspace(y_min, y_max, height)

mandelbrot_set = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        c = complex(real[j], imag[i])
        mandelbrot_set[i, j] = mandelbrot(c, max_iter)

plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.show()
