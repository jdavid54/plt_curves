#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     20/08/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

xValues = [5, 3, 7, 9]
yValues = [6, 2, 9, 12]
xErrorValues = [1, 0.5, 2.5, 3]
yErrorValues = [0.5, 0.5, 2, 1.5]
plt.scatter(xValues, yValues, zorder = 2)
plt.errorbar(xValues, yValues, xerr = xErrorValues, yerr = yErrorValues,
  fmt = 'none', capsize = 10, ecolor = 'red', zorder = 1)
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
