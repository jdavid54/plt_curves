from pylab import *

axes = figure().add_subplot(111)
t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
axes.plot(t, s)
# choose Y axis side
right = True
left = not right

# all yticks
maj = axes.yaxis.get_major_ticks()
for tick in maj:
    tick.label1.set_visible(left)   # left side Y axis
    tick.label1.set_color('blue')
    tick.label2.set_visible(right)     # right side Y axis
    tick.label2.set_color('green')
    print(tick, tick.label1.get_color(),tick.label2.get_color())

# axis Y
import matplotlib.ticker as ticker
formatter = ticker.FormatStrFormatter('$%1.2f')
axes.yaxis.set_major_formatter(formatter)

# .label = label1, .label2 = label2
if left :
    title='left'
    axes.yaxis.tick_left()
    label = axes.yaxis.get_major_ticks()[2].label  # second ytick left label
else:
    title='right'
    axes.yaxis.tick_right()
    label = axes.yaxis.get_major_ticks()[2].label2  # second ytick right label
label.set_fontsize(10)
label.set_rotation('vertical')
label.set_color('red')
plt.title(title)
# axis X
a=axes.get_xticks().tolist()
a[1]='change'
axes.set_xticklabels(a)


plt.show()