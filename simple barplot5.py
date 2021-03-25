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


values = [5, 3, 7, 9]
errorValues = [1, 0.5, 2.5, 3]
plt.bar(range(len(values)), values, color = 'skyblue')
plt.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 2, capthick = 8)
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
