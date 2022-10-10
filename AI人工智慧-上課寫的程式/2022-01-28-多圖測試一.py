
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=3, ncols=3,)
# Create a figure and a set of subplots.

print(fig) # Figure(640x480)
# class matplotlib.figure.Figure       查 Figure 物件的方法與屬性
print(axs) # <class 'numpy.ndarray'>
# class matplotlib.axes.Axes           查 Axes 物件的方法與屬性

fig.set_facecolor('#999900')
fig.set_size_inches(18, 9)

axs[0, 0].set_facecolor('#222222')
axs[0, 1].set_facecolor('#444444')
axs[0, 2].set_facecolor('#666666')
axs[1, 0].set_facecolor('#888888')
axs[1, 1].set_facecolor('#AAAAAA')
axs[1, 2].set_facecolor('#CCCCCC')
axs[2, 0].set_facecolor('#EEEEEE')
axs[2, 1].set_facecolor('#FF0000')
axs[2, 2].set_facecolor('#00FF00')

####   0,0 圖  多條折線圖
x = np.linspace(0, 10)
# Fixing random state for reproducibility
np.random.seed(19680801)
axs[0, 0].plot(x, np.sin(x) + x + np.random.randn(50))
axs[0, 0].plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
axs[0, 0].plot(x, np.sin(x) + 2 * x + np.random.randn(50))
axs[0, 0].plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
axs[0, 0].plot(x, np.sin(x) - 2 * x + np.random.randn(50))
axs[0, 0].plot(x, np.sin(x) + np.random.randn(50))

####  群組直條圖
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = axs[1, 0].bar(x - width/2, men_means, width, label='Men')
rects2 = axs[1, 0].bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
axs[1, 0].set_xticks(x, labels)
axs[1, 0].legend()
axs[1, 0].bar_label(rects1, padding=3)
axs[1, 0].bar_label(rects2, padding=3)

####  堆疊直條圖
N = 5
menMeans = (20, 35, 30, 35, -27)
womenMeans = (25, 32, 34, 20, -25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = axs[2, 0].bar(ind, menMeans, width, yerr=menStd, label='Men')
p2 = axs[2, 0].bar(ind, womenMeans, width,
            bottom=menMeans, yerr=womenStd, label='Women')

axs[2, 0].axhline(0, color='grey', linewidth=0.8)
axs[2, 0].set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
axs[2, 0].legend()

# Label with label_type 'center' instead of the default 'edge'
axs[2, 0].bar_label(p1, label_type='center')
axs[2, 0].bar_label(p2, label_type='center')
axs[2, 0].bar_label(p2)

####  折線面積圖  三個
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

axs[0, 1].fill_between(x, y1)
axs[1, 1].fill_between(x, y1, 1)
axs[2, 1].fill_between(x, y1, y2)

#### 環圈圖
size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

axs[0, 2].pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

axs[0, 2].pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

axs[0, 2].set(aspect="equal", title='Pie plot with `ax.pie`')

#### 圓餅圖

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

axs[1, 2].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
axs[1, 2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#### 橫向直條圖
# Fixing random state for reproducibility
np.random.seed(19680801)

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

axs[2, 2].barh(y_pos, performance, xerr=error, align='center')
axs[2, 2].set_yticks(y_pos, labels=people)
axs[2, 2].invert_yaxis()  # labels read top-to-bottom
axs[2, 2].set_title('How fast do you want to go today?')

fig.tight_layout()

plt.show() # Display all open figures.

