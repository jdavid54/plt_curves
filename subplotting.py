#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:18:35 2019

@author: jeandavid

https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html
"""
import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.axes()  # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])  #[left, bottom, width, height] in percentage 
plt.show()


fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],   #bottom at 50% of total plot
                   xticklabels=[], ylim=(-1.2, 1.2))    # no x labels
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],   #bottom at 10% + height 40% = 50% to be under axe1
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x));
plt.show()

#array of subplots  - 2 rows of 3 subplots
for i in range(1, 7):
    plt.subplot(2, 3, i)    # i goes from 1 to 2*3 
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

plt.show()

#adjust space between 
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),  
           fontsize=16, ha='center')
plt.show()

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
#plt.show()

# axes are in a two-dimensional array, indexed by [row, col]
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
print(ax,fig)
plt.show()

#grid of different shapes of subplots
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0])   #first subplot takes one width at row 0, column 0
plt.subplot(grid[0, 1:])  #second subplot spans from column 1 to 2
plt.subplot(grid[1, :2])  #subplot 3 spans from column 0 to 1
plt.subplot(grid[1, 2]);   # subplot at row 1, column 2

plt.show()