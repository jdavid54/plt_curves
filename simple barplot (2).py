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


plt.bar(range(5), [1, 3, 3, 5, 4], width = 0.6, color = 'yellow',
  edgecolor = 'blue', linewidth = 2, yerr = [0.5, 1, 2, 1, 2],
  ecolor = 'magenta', capsize = 10)
plt.xticks([x + 0.3 / 2  for x in range(5)], ['A', 'B', 'C', 'D', 'E'],
  rotation = 45)
plt.show()

