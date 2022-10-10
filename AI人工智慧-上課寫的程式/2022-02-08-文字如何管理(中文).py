
import matplotlib.pyplot as plt
import matplotlib as mpl

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams  設定整體參數

mpl.rcParams['font.family'] = 'YouYuan'
# 解決中文字體下坐標軸負數的負號顯示問題
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['figure.figsize'] = [18,9]
mpl.rcParams['text.color'] = 'white'   #  修改參數字典中，文字顏色的整體設定
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['xtick.color'] = 'Orange'
mpl.rcParams['xtick.labelcolor'] = 'white'
mpl.rcParams['ytick.color'] = 'Orange'
mpl.rcParams['ytick.labelcolor'] = 'white'

#A module for finding, managing, and using fonts across platforms.  設定文字管理
#https://matplotlib.org/stable/api/font_manager_api.html#
myfont_20 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=20)

fig , ax = plt.subplots(nrows=2, ncols=1)

fig.set_facecolor('black')
fig.suptitle('這裡是圖紙的標題',fontsize=50)

ax[0].set_facecolor('DimGray')
ax[0].set_title('小圖一號',fontsize=30,rotation=-20)
ax[0].set_xlabel('Axes 1 - Axis X',fontproperties = myfont_20)
ax[0].set_ylabel('Axes 1 - Axis Y',fontproperties = myfont_20)
ax[0].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_20)
ax[0].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_20)

ax[1].set_facecolor('DimGray')
ax[1].set_title('小圖二號',fontsize=30,rotation=20)
ax[1].set_xlabel('Axes 2 - Axis X',fontproperties = myfont_20)
ax[1].set_ylabel('Axes 2 - Axis Y',fontproperties = myfont_20)
ax[1].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_20)
ax[1].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_20)

fig.tight_layout()
plt.subplots_adjust(hspace=0.7)
plt.show()

'''
宋體SimSun  ok
微軟雅黑Microsoft YaHei  ok
微軟正黑體Microsoft JhengHei  ok
細明體MingLiU  ok
標楷體DFKai-SB  ok
隸書LiSu  ok
幼圓YouYuan   ok(好)
華文細黑STXihei   ok
華文楷體STKaiti   ok
華文宋體STSong    ok
華文中宋STZhongsong   ok(好)
華文仿宋STFangsong    ok
方正舒體FZShuTi       ok
方正姚體FZYaoti       ok
'''