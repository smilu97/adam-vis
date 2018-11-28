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
import math

'''
Constants for optimizer
'''
beta1 = 0.9
beta2 = 0.999
eps = 1e-08
lr = 0.1
'''
Memory variables for ADAM optimizer
'''
m = 0
v = 0

def func_x2(x):
    '''
    The target function.
    You can modify the graph by
    defining target function here
    '''
    return x**2

def draw_func(f, xrange):
    x = np.arange(xrange[0], xrange[1], 0.1)
    y = f(x)
    ln, = plt.plot(x, y)
    return ln

def sgd(g):
    return g * lr

def adam(g):
    global lr, m, v
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g * g
    m_ = m / (1 - beta1)
    v_ = v / (1 - beta2)
    return lr * m_ / (np.sqrt(v_) + eps)

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
        '''
        You can choose which algorithm we use ADAM, or SGD, here
        '''
        if True:
            x_ = x - adam(g)
        else:
            x_ = x - sgd(g)
        y_ = func_x2(x_)
        if False:
            xdata.append(x_)
            ydata.append(y_)
        else:
            xdata[0] = x_
            ydata[0] = y_
        ln2.set_data(xdata, ydata)
        print('update: {}, {}'.format(x_, y_))
        return ln, ln2

    if True:
        ani = FuncAnimation(fig, update, interval=0, frames=180,
                            init_func=init, blit=True)
        if True:  # Show the animation instantly
            plt.show()
        else:  # Save the animation
            ani.save('out.gif', writer='imagemagick', fps=20)
    else:
        while True:
            update(None)

if __name__ == '__main__':
    main()