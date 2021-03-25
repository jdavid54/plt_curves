#-------------------------------------------------------------------------------
# Name:        module2
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


barWidth = 0.8
y1 = [1, 2, 4, 3]
y2 = [3, 4, 4, 3]
r = range(len(y1))

plt.bar(r, y1, width = barWidth, color = ['yellow' for i in y1],
           edgecolor = ['blue' for i in y1], linestyle = 'solid', hatch ='/',
           linewidth = 3)
plt.bar(r, y2, width = barWidth, bottom = y1, color = ['pink' for i in y1],
           edgecolor = ['green' for i in y1], linestyle = 'dotted', hatch = 'o',
           linewidth = 3)
plt.xticks([r + barWidth / 2 for r in range(len(y1))], ['A', 'B', 'C', 'D'])
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
