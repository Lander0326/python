import csv  #  python 的內建模組
import matplotlib.pyplot as plt

def 整理股票資料CSV檔(file) :

    with open(file, 'r') as f :
        data = list(csv.reader(f, delimiter=","))

    標題 = data[0][0]
    欄位 = data[1][:-1]
    data = data[2:-5]

    list_2D = []
    for r,row in enumerate(data) :
        list_1D = []
        for n,item in enumerate(row) :
            if n == 0 :                      #  日期
                list_1D.append(item)
            elif n in (1,2) :                #  成交股數  成交金額
                list_1D.append( int(''.join(item.split(','))) )
            elif n in (3,4,5,6) :            #  開 高 低 收
                list_1D.append( float(item) )
        list_2D.append(list_1D)
    return 標題 , 欄位 , list_2D

start_year = 2020  # 起始年份
start_month = 7    # 起始月份

end_year = 2022    # 結束年份
end_month = 1      # 結束月份

# 股票代號及股票名稱對照
dict_1 = {'00635U':'00635U 期元大S&P黃金','00738U':'00738U 期元大道瓊白銀'}
stock_no = '00738U'

list_2D = []
for y in range(start_year,end_year+1) :
    for m in range(1,13) :
        if y == start_year and m < start_month :
            continue
        elif y == end_year and m > end_month :
            break
        else :
            file = f'.\股票資料\STOCK_DAY_{stock_no}_{y}{str(m).zfill(2)}.csv'
            標題 , 欄位 , list_2D_t = 整理股票資料CSV檔(file)
            list_2D += list_2D_t

# 準備開始畫圖，圖紙上的統一設定可用rc先設好
# matplotlib.pyplot -->  https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#module-matplotlib.pyplot

plt.rc('font', family = 'Microsoft JhengHei' , size = 10 )
plt.rc('text', color='#ffffff')                        #  會影響標題
plt.rc('xtick',labelcolor='#ffffff',color='#55ff55')   #  會影響單位文字及尺標
plt.rc('ytick',labelcolor='#ffffff',color='#55ff55')

x = list(zip(*list_2D))[0]
y1 = list(zip(*list_2D))[6]
y2 = list(zip(*list_2D))[1]

fig = plt.figure(figsize=(24,9),dpi=72,facecolor='DarkMagenta')  # 產生一張圖畫紙

細部文字設定 = {'fontsize': 16, 'color': '#ffff00'}

ax1 = plt.subplot(2, 1, 1,
                  facecolor='DarkMagenta',
                  xmargin = 0.01,
                  frameon = False)   #  2 * 1 的畫面，ax1 小圖畫在一號位置，利用這種方式設定小圖，圖都是均分大小
ax1.set_title(dict_1[stock_no],fontdict =  {'fontsize': 24})
ax1.fill_between(x, y1, color = 'Pink', alpha=1)    # 面積圖
ax1.plot(x, y1, color='Red', alpha=0.8)             # 折線圖

#  設定日期出現的數量不要太多以免衝突
locations = ax1.get_xticks()
xtick_labels = ax1.get_xticklabels()
locs1 = [ n for n in range(0,len(locations),10)]
labels1 = [ x[n] for n in locs1]
ax1.set_xticks(locs1,labels=labels1,rotation=20)

ax1.grid(visible=True,axis='y')
ax1.set_ylim(min(y1)-3, max(y1))
ax1.set_ylabel('收盤價', fontdict = 細部文字設定)
ax1.set_xlabel('成交日期', fontdict = 細部文字設定)

ax2 = plt.subplot(2, 1, 2,
            facecolor='DarkMagenta',
            xmargin = 0.01,
            frameon = False   )                #  2 * 1 的畫面，小圖畫在二號位置
ax2.bar(x, y2, color = 'Violet', alpha=1)      #  直條圖
ax2.set_xticks('',labels='')                   #  隱藏日期及尺標出現
ax2.grid(visible=True,axis='y')                #  設定格線
ax2.set_ylabel('成交股數', fontdict = 細部文字設定)


fig.tight_layout()
plt.show()  #  依照上面的設定，把圖畫出來

'''

matplotlib.pyplot.subplot(*args, **kwargs)
Add an Axes to the current figure or retrieve an existing Axes.

A dictionary controlling the appearance of the title text,
the default fontdict is:

{'fontsize': rcParams['axes.titlesize'],
 'fontweight': rcParams['axes.titleweight'],
 'color': rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}


宋體SimSun
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