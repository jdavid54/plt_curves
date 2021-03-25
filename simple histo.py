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
import matplotlib.patches as patches
import matplotlib.path as path
from random import *

x = [1, 2, 2, 5, 3, 4, 4, 4, 4, 4, 5, 5]
plt.hist(x, range = (0, 5), bins = 5, color = 'yellow',
            edgecolor = 'red')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
plt.show()
plt.close()

plt.bar(range(5), [1, 3, 3, 5, 4], width = 0.6, color = 'yellow',
  edgecolor = 'blue', linewidth = 2, yerr = [0.5, 1, 2, 1, 2],
  ecolor = 'magenta', capsize = 10)
plt.xticks([x + 0.6 / 2 for x in range(5)], ['A', 'B', 'C', 'D', 'E'],
  rotation = 45)
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
