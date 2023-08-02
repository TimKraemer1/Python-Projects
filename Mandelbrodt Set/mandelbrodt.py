import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def draw_mandelbrot(x_min, x_max, y_min, y_max, width, height, max_iter):
    while True:
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        mandelbrot_set = np.zeros((height, width))

        for i in range(height):
            for j in range(width):
                c = x[j] + 1j * y[i]
                mandelbrot_set[i, j] = mandelbrot(c, max_iter)

        plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap='hot', aspect='auto')
        plt.title("Mandelbrot Set")
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.colorbar()
        plt.draw()
        plt.pause(0.1)  # Pause for a short time to allow for user input

        # Get new coordinates from user input to zoom into
        print("Click on the two corners of the region you want to zoom into.")
        points = plt.ginput(2, timeout=-1)

        # Update the range with the new coordinates
        x_min, y_min = points[0]
        x_max, y_max = points[1]


if __name__ == "__main__":

    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    width, height = 1000, 1000
    max_iter = 100

    draw_mandelbrot(x_min, x_max, y_min, y_max, width, height, max_iter)
