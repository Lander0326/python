
import matplotlib.pyplot as plt
import matplotlib

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams  設定整體參數

#A module for finding, managing, and using fonts across platforms.  設定文字管理
#https://matplotlib.org/stable/api/font_manager_api.html#
myfont_20 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=20)
myfont_15 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=15)
myfont_10 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=10)
微軟正黑體_20 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\msjhbd.ttc',size=20)
微軟正黑體_15 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\msjhbd.ttc',size=15)

print( matplotlib.rcParams['figure.figsize'] )  # [6.4, 4.8] 英吋
print( matplotlib.rcParams['text.color'] )      # black
print( matplotlib.rcParams['font.family'] )     # ['sans-serif']

matplotlib.rcParams['figure.figsize'] = [18,9]
matplotlib.rcParams['text.color'] = 'LightGreen'   #  修改參數字典中，文字顏色的整體設定
matplotlib.rcParams['axes.labelcolor'] = 'white'
matplotlib.rcParams['xtick.color'] = 'Orange'
matplotlib.rcParams['xtick.labelcolor'] = 'white'
matplotlib.rcParams['ytick.color'] = 'Orange'
matplotlib.rcParams['ytick.labelcolor'] = 'white'

fig , ax = plt.subplots(nrows=2, ncols=1)

fig.set_facecolor('black')
fig.suptitle('這裡是圖紙的標題',fontproperties = 微軟正黑體_20)

ax[0].set_facecolor('DimGray')
ax[0].set_title('小圖一號',fontproperties = 微軟正黑體_15)
ax[0].set_xlabel('Axes 1 - Axis X',fontproperties = myfont_10)
ax[0].set_ylabel('Axes 1 - Axis Y',fontproperties = myfont_10)
ax[0].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_10)
ax[0].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_10)

ax[1].set_facecolor('DimGray')
ax[1].set_title('小圖二號',fontproperties = 微軟正黑體_15)
ax[1].set_xlabel('Axes 2 - Axis X',fontproperties = myfont_10)
ax[1].set_ylabel('Axes 2 - Axis Y',fontproperties = myfont_10)
ax[1].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_10)
ax[1].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_10)

fig.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()
