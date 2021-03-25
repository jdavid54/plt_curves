'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = R**2

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
#surf = ax.contour(X, Y, Z)#, cmap=cm.coolwarm,linewidth=0, antialiased=False)
# Customize the z axis.
ax.set_zlim(0.01, 50.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
theta = np.linspace(0 * np.pi, 2 * np.pi, 100)  
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1

#r = np.arange(-5, 5, 0.1)
for z  in range(10,60,10):
    r = np.sqrt(z)
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, zorder=2.5,color='red',label=str(z))
ax.legend()

plt.show()
