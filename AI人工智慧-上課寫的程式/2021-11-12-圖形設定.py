import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.font_manager import FontProperties
喜歡的英數字體 = FontProperties(fname=r"c:\windows\fonts\ITCKRIST.TTF")
#mpl.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# The list of rcParams  https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=matplotlib%20rcparams#matplotlib.rcParams
fig1 = plt.figure()  # 產生figure
fig1.set_facecolor('#222222')
fig1.set_size_inches(16,8)
x = np.linspace(0, 10, 1000)

axes_1 = fig1.add_axes([0.1,0.4,0.8,0.5],facecolor='#222222')
axes_1.set_title('axes_1',{'fontsize' : 20,'color' : 'white'})
axes_1.plot(x, np.sin(x), label='line 1')
axes_1.plot(x, np.cos(x), label='line 2')
axes_1.legend()
axes_1.fill_between(x, np.sin(x), np.cos(x), interpolate=True, color='green', alpha=0.5)

x_t = axes_1.get_xticklabels()
for item in x_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_fontsize(16)
    item.set_color("white")
    
y_t = axes_1.get_yticklabels()
for item in y_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_fontsize(16)
    item.set_color("white")

axes_2 = fig1.add_axes([0.1,0.1,0.8,0.2],facecolor='#222222')
axes_2.set_title('axes_2',{'fontsize' : 20,
                           'color' : 'white'})  
axes_2.plot(x, np.sin(x), label='line 1')
axes_2.plot(x, np.cos(x), label='line 2')
axes_2.legend()
axes_2.fill_between(x, np.sin(x), np.cos(x), interpolate=True, color='green', alpha=0.5)

x_t = axes_2.get_xticklabels()
for item in x_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_fontsize(16)
    item.set_color("white")
    
y_t = axes_2.get_yticklabels()
for item in y_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_fontsize(16)
    item.set_color("white")

plt.show()


'''
#製作figure
fig = plt.figure(figsize=(14,8))

# 2x3的矩陣的第1個位置中設定axes
ax_1 = fig.add_subplot(2, 3, 1)
ax_1.set_title('Final Term')  #圖的標題
ax_1.set_facecolor('#b2d8d8')
bar_1 = ax_1.bar([0,1,2],[100,150,75],0.3,label='BNT')
bar_2 = ax_1.bar([0+0.3,1+0.3,2+0.3],[85,130,85],0.3,label='MDN')
bar_3 = ax_1.bar([0+0.6,1+0.6,2+0.6],[105,90,95],0.3,label='AZ')
ax_1.set_xticks([0+0.3,1+0.3,2+0.3])
ax_1.set_xticklabels(['Jan','Feb','Mar'])
ax_1.legend()
#ax_1.bar_label(bar_1, padding=3)
#ax_1.bar_label(bar_2, padding=3)
#ax_1.bar_label(bar_3, padding=3)

x_t = ax_1.get_xticklabels()
for item in x_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_color("red")
    
y_t = ax_1.get_yticklabels()
for item in y_t :
    item.set_fontproperties(喜歡的英數字體)
    item.set_color("red")

# 2x3的矩陣的第2個位置中設定axes
ax_2 = fig.add_subplot(2, 3, 2)
ax_2.set_title('2')  #圖的標題
ax_2.set_facecolor('#66b2b2')

# 2x3的矩陣的第3個位置中設定axes
ax_3 = fig.add_subplot(2, 3, 3)
ax_3.set_title('3')  #圖的標題
ax_3.set_facecolor('#008080')

# 2x3的矩陣的第4個位置中設定axes
ax_4 = fig.add_subplot(2, 3, 4)
ax_4.set_title('4')  #圖的標題
ax_4.set_facecolor('#006666')

# 2x3的矩陣的第5個位置中設定axes
ax_5 = fig.add_subplot(2, 3, 5)
ax_5.set_title('5')  #圖的標題
ax_5.set_facecolor('#004c4c')

# 2x3的矩陣的第6個位置中設定axes
ax_6 = fig.add_subplot(2, 3, 6)
ax_6.set_title('6')  #圖的標題
ax_6.set_facecolor('#b2d8d8')

#顯示圖
plt.show()
'''