"""
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.

    PSEUDO CODE - Wikipedia

    for each pixel (Px, Py) on the screen do
    x0 = scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
    y0 = scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
    x := 0.0
    y := 0.0
    iteration := 0
    max_iteration := 1000
    while (x*x + y*y ≤ 2*2 AND iteration < max_iteration) do
        xtemp := x*x - y*y + x0
        y := 2*x*y + y0
        x := xtemp
        iteration := iteration + 1

    color := palette[iteration]
    plot(Px, Py, color)

    Author: Harivinay V
    github: https://github.com/M87K452b

"""
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from timeit import default_timer as timer

N = 250
r = 4
nx = 2 * 1920
ny = 2 * 1080
xmin = -2.5  # -0.7721582 #Ocean#-0.7318744 #Snowflake#-0.37465401 #Default#-0.05
xmax = 1.0  # -0.7701566 #Ocean#-0.7318878 #Snowflake#-0.37332411 #Default##-0.55
ymin = -1.0  # 0.1143422 #Ocean#0.1845309 #Snowflake#0.659227668 #Default##0.5
ymax = 1.0  # 0.1163601 #Ocean#0.1845413 #Snowflake#0.66020767 #Default##1.0
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
fractal = np.zeros([nx, ny])


@jit(nopython=True)
def mandelbrot(x0, y0, N, r):
    xold = 0
    yold = 0
    z = 0
    rnew = x0**2 + y0**2
    while rnew < r and z < N:
        xnew = xold**2 - yold**2 + x0
        ynew = 2 * xold * yold + y0

        xold = xnew
        yold = ynew

        rnew = xnew**2 + ynew**2

        z += 1
    return z


@jit(nopython=True)
def fractal_plot(xmin, xmax, ymin, ymax, fractal, N, r):
    for i in range(nx):
        for j in range(ny):
            z = mandelbrot(x[i], y[j], N, r)
            fractal[i, j] = z


start = timer()
fractal_plot(xmin, xmax, ymin, ymax, fractal, N, r)
compute_time = timer() - start

print("Mandelbrot computed in %f s" % compute_time)
f = plt.figure(figsize=(12, 16))
plt.imshow(fractal.T, cmap='viridis')
plt.axis('off')
plt.show()

f.savefig("galaxy_spiral.png", bbox_inches='tight', dpi=800)
