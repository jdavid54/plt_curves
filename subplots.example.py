import numpy as np
import matplotlib.pyplot as plt

#First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

#Creates just a figure and only one subplot
fig, ax = plt.subplots()
fig.suptitle('one subplot')
ax.plot(x, y)
ax.set_title('Simple plot')
plt.show()

#Creates two subplots and unpacks the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig.suptitle('sharey=true')
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
plt.show()

#Creates four polar axes, and accesses them through the returned array
fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
fig.suptitle('subplot_kw=dict(polar=true)')
axes[0, 0].plot(x, y)
axes[1, 0].scatter(x, y)
axes[0, 1].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()

#Share a X axis with each column of subplots
fig, axes = plt.subplots(2, 2, sharex='col')
fig.suptitle('sharex=col')
axes[0, 0].plot(x, y)
axes[1, 0].scatter(x, y)
axes[0, 1].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()


#Share a Y axis with each row of subplots
fig, axes = plt.subplots(2, 2, sharey='row')
fig.suptitle('sharey=row')
axes[0, 0].plot(x, y)
axes[1, 0].scatter(x, y)
axes[0, 1].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()


#Share both X and Y axes with all subplots
fig, axes = plt.subplots(2, 2, sharex='all', sharey='all')
fig.suptitle('sharex=all,sharey=all')
axes[0, 0].plot(x, y)
axes[1, 0].scatter(x, y)
axes[0, 1].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()


#Note that this is the same as
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
fig.suptitle('sharex=true,sharey=true')
axes[0, 0].plot(x, y)
axes[1, 0].scatter(x, y)
axes[0, 1].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()

#Creates figure number 10 with a single subplot
#and clears it if it already exists.
fig.title('fig number & clear')
fig, ax=plt.subplots(num=10, clear=True)
ax.plot(x, y)

plt.show()