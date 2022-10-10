
import matplotlib.pyplot as plt

# Create a new figure, or activate an existing figure.
fig = plt.figure( figsize=[18, 9], dpi=100, facecolor='DarkGreen' )

#ax1 = fig.add_subplot(2,2,1)
#ax2 = fig.add_subplot(2,2,2)
#ax3 = fig.add_subplot(2,2,3)
#ax4 = fig.add_subplot(2,2,4)

ax1 = fig.add_axes([0.05,0.45,0.9 ,0.5] ,facecolor='LightGreen')
ax2 = fig.add_axes([0.05,0.1 ,0.5 ,0.3] ,facecolor='YellowGreen')
ax3 = fig.add_axes([0.6 ,0.1 ,0.35,0.3] ,facecolor='LimeGreen')

#ax1,ax2 = fig.subplots(nrows=2, ncols=1)

#fig.tight_layout()  #  add_axes 不適用

plt.show()

'''
add_axes(*args, **kwargs)  
#  可在呼叫函式時直接設定小圖參數，一定要輸入
#  The dimensions [left, bottom, width, height] of the new Axes.
#  All quantities are in fractions of figure width and height.
Add an Axes to the figure.

subplots(nrows=1, ncols=1, *, sharex=False, 
sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None)
Add a set of subplots to this figure.

add_subplot(*args, **kwargs)  #  可在呼叫函式時直接設定小圖參數
Add an Axes to the figure as part of a subplot arrangement.

'''