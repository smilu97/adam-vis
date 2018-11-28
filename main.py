#!/usr/bin/env python

#
# author: smilu97
# Visualization of comparison between SGD and Adam
#

import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def func_x2(x):
    return x**2

def draw_func(f, xrange):
    x = np.arange(xrange[0], xrange[1], 0.1)
    y = f(x)
    ln, = plt.plot(x, y)
    return ln

def sgd(g, lr):
    return g * lr

def main():

    xrange = (-5.0, 5.0)
    first_x = -4.0
    fig, ax = plt.subplots()
    xdata = [first_x]
    ydata = [func_x2(first_x)]
    ln = draw_func(func_x2, xrange)
    ln2, = plt.plot([], [], 'ro', animated=True)

    def init():
        ax.set_xlim(xrange[0], xrange[1])
        ax.set_ylim(-0.5, 20)
        return ln, ln2

    def update(frame):
        x = xdata[-1]
        g = 2 * x
        lr = 0.01
        x_ = x - sgd(g, lr)
        y_ = func_x2(x_)
        xdata.append(x_)
        ydata.append(y_)
        ln2.set_data(xdata, ydata)
        print('update: {}, {}'.format(x_, y_))
        return ln, ln2

    ani = FuncAnimation(fig, update, frames=100,
                        init_func=init, blit=True)

    plt.show()

if __name__ == '__main__':
    main()