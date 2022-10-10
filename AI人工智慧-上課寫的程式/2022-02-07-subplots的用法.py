
import matplotlib.pyplot as plt

fig , ax = plt.subplots(nrows=2, ncols=1)

fig.set_facecolor('red')
fig.suptitle('Figure Title')

ax[0].set_facecolor('yellow')
ax[0].set_title('Axes 1')
ax[0].set_xlabel('Axes 1 - Axis X')
ax[0].set_ylabel('Axes 1 - Axis Y')

ax[1].set_facecolor('green')
ax[1].set_title('Axes 2')
ax[1].set_xlabel('Axes 2 - Axis X')
ax[1].set_ylabel('Axes 2 - Axis Y')

plt.subplots_adjust(hspace=0.6)  #  二張小圖，上下就部會太擠了

plt.show()

#pyplot  matplotlib.pyplot is a state-based interface to matplotlib.
#https://matplotlib.org/stable/api/pyplot_summary.html#

#class matplotlib.figure.Figure
#https://matplotlib.org/stable/api/figure_api.html#

#class matplotlib.axes.Axes
#https://matplotlib.org/stable/api/axes_api.html#

#class matplotlib.axis.Axis
#https://matplotlib.org/stable/api/axis_api.html

