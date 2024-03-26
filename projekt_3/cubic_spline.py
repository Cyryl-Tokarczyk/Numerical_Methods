import numpy as np
import matplotlib.pyplot as plt

def calc_cubic_splines(xs, ys):

    n = len(xs) - 1
    
    A = np.zeros((n*4, n*4))

    # initializing splines

    for i in range(n):
        # h - delta x
        h = xs[i + 1] - xs[i]

        # 1 0 0 0
        A[i*2][i*4] = 1

        # h^0 h^1 h^2 h^3
        for j in range(4):
            A[i*2 + 1][i*4 + j] = h ** j    

    for i in range(n - 1):
        h = xs[i + 1] - xs[i]

        # first row:
        # 0 1 2h 3h^2 0 -1 0 0
        A[n*2 + i*2][i*4 + 1] = 1
        A[n*2 + i*2][i*4 + 2] = 2*h
        A[n*2 + i*2][i*4 + 3] = 3*(h**2)

        A[n*2 + i*2][i*4 + 5] = -1

        # second row:
        # 0 0 2 6h 0 0 -2 0
        A[n*2 + i*2 + 1][i*4 + 2] = 2
        A[n*2 + i*2 + 1][i*4 + 3] = 6*h

        A[n*2 + i*2 + 1][i*4 + 6] = -2

    h = xs[-1] - xs[-2]

    A[-1][-2] = 2
    A[-1][-1] = h*6
    A[-2][2] = 1

    # initializng vector b

    b = np.zeros(n*4)

    for i in range(n):

        # starting point of the spline
        b[i*2] = ys[i]

        # the end point
        b[i*2 + 1] = ys[i + 1]

    r = np.linalg.solve(A, b)

    return r

def cubic_splines_interpolation(splines, xs, x):
    
    # Determine which spline

    for i in range(len(xs) - 1):
        if xs[i] <= x and x <= xs[i + 1]:

            result = 0
            dx = x - xs[i]

            for j in range(4):
                result += splines[i*4 + j] * (dx ** j)

            break

    return result

if __name__ == '__main__':
    xs = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    ys = [6, -2, 4, 8, -5, 1, 6, 7, 10]
    splines = calc_cubic_splines(xs, ys)

    linspace = np.linspace(xs[0], xs[-1])
    results = []
    for x in linspace:
        results.append(cubic_splines_interpolation(splines, xs, x))

    plt.plot(xs, ys, 'o')
    plt.plot(linspace, results)
    plt.show()