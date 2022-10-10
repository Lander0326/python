
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

myfont_20 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\impact.TTf',size=20)
myfont_15 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\impact.TTf',size=15)
myfont_10 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\impact.TTf',size=10)
微軟正黑體_20 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\impact.TTf',size=20)

print(matplotlib.rcParams['figure.figsize']) #  print出得知圖畫紙大小為[6.4, 4.8]英吋
print(matplotlib.rcParams['text.color'])     #  black
print(matplotlib.rcParams['xtick.color'])
print(matplotlib.rcParams['xtick.labelcolor'])
print(matplotlib.rcParams['font.family'])

matplotlib.rcParams['figure.figsize'] = [13,6]
matplotlib.rcParams['text.color'] = 'LightGreen'  #  修改參數字典顏色設定
matplotlib.rcParams['xtick.labelcolor'] = 'white'
matplotlib.rcParams['xtick.color'] = 'Orange'
matplotlib.rcParams['ytick.labelcolor'] = 'white'
matplotlib.rcParams['ytick.color'] = 'Orange'
matplotlib.rcParams['axes.labelcolor'] = 'white'



fig , ax = plt.subplots(nrows=2, ncols=1)

fig.set_facecolor('black')
fig.suptitle('Figure Title',fontproperties = myfont_20)

ax[0].set_facecolor('DimGray')
ax[0].set_title('Axes 1',fontproperties = myfont_15)
ax[0].set_xlabel('Axes 1 - Axes X',fontproperties = myfont_10)
ax[0].set_ylabel('Axes 1 - Axes Y',fontproperties = myfont_10)
ax[0].set_xticklabels(xtick_labels,fontproperties = myfont_10)


ax[1].set_facecolor("DimGray")
ax[1].set_title('Axes 2',fontproperties = myfont_15)
ax[1].set_xlabel('Axes 2 - Axes X',fontproperties = myfont_10)
ax[1].set_ylabel('Axes 2 - Axes Y',fontproperties = myfont_10)
ax[0].set_yticklabels(fontproperties = myfont_10)


fig.tight_layout()
plt.subplots_adjust(hspace=0.6)   #  兩張小圖上下間格的"比例"


plt.show()

