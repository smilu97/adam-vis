#!/usr/bin/env python

#
# author: smilu97
# Visualization of comparison between SGD and Adam
#

import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

def func_x2(x):
    return x**2

def draw_func(f, xrange):
    x = np.arange(xrange[0], xrange[1], 0.1)
    y = f(x)
    plt.plot(x, y)

def main():
    draw_func(func_x2, (-10.0, 10.0))
    plt.show()

if __name__ == '__main__':
    main()