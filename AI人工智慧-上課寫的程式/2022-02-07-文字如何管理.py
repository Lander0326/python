
import matplotlib.pyplot as plt
import matplotlib

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams  設定整體參數

#A module for finding, managing, and using fonts across platforms.  設定文字管理
#https://matplotlib.org/stable/api/font_manager_api.html#
myfont_20 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=20)
myfont_15 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=15)
myfont_10 = matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=10)

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
fig.suptitle('Figure Title',fontproperties = myfont_20)

ax[0].set_facecolor('DimGray')
ax[0].set_title('Axes 1',fontproperties = myfont_15)
ax[0].set_xlabel('Axes 1 - Axis X',fontproperties = myfont_10)
ax[0].set_ylabel('Axes 1 - Axis Y',fontproperties = myfont_10)
ax[0].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_10)
ax[0].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_10)

ax[1].set_facecolor('DimGray')
ax[1].set_title('Axes 2',fontproperties = myfont_15)
ax[1].set_xlabel('Axes 2 - Axis X',fontproperties = myfont_10)
ax[1].set_ylabel('Axes 2 - Axis Y',fontproperties = myfont_10)
ax[1].set_xticks([0,1,2,3,4,5,6,7,8,9],labels=['a','b','c','d','e','f','g','h','i','j'],fontproperties = myfont_10)
ax[1].set_yticks([0,1,2,3,4,5,6,7,8],labels=[n for n in range(-40,41,10)],fontproperties = myfont_10)

'''
fig = plt.figure(figsize=[18,9],dpi=100, facecolor='#888888')

ax1,ax2 = fig.subplots(nrows=2, ncols=1)

fig.tight_layout()  #  add_axes 不適用

'''
fig.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()

'''
宋體SimSun
黑體SimHei
微軟雅黑Microsoft YaHei
微軟正黑體Microsoft JhengHei
新宋體NSimSun
新細明體PMingLiU
細明體MingLiU
標楷體DFKai-SB
仿宋FangSong
楷體KaiTi
隸書LiSu
幼圓YouYuan
華文細黑STXihei
華文楷體STKaiti
華文宋體STSong
華文中宋STZhongsong
華文仿宋STFangsong
方正舒體FZShuTi
方正姚體FZYaoti
華文彩雲STCaiyun
華文琥珀STHupo
華文隸書STLiti
華文行楷STXingkai
華文新魏STXinwei
'''