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


barWidth = 0.4
y1 = [1, 2, 4, 3]
y2 = [3, 4, 4, 3]
r1 = range(len(y1))
r2 = [x + barWidth for x in r1]

plt.bar(r1, y1, width = barWidth, color = ['yellow' for i in y1],
           edgecolor = ['blue' for i in y1], linewidth = 2)
plt.bar(r2, y2, width = barWidth, color = ['pink' for i in y1],
           edgecolor = ['green' for i in y1], linewidth = 2)
plt.xticks([r + barWidth for r in range(len(y1))], ['A', 'B', 'C', 'D'])
plt.show()
