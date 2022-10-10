import csv  #  python 的內建模組
import matplotlib.pyplot as plt
import matplotlib as mpl

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

start_year = 2021  # 起始年份
start_month = 5    # 起始月份

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

#A module for finding, managing, and using fonts across platforms.  設定文字管理
#https://matplotlib.org/stable/api/font_manager_api.html#
myfont_10 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=10)
微軟正黑體_20 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\msjhbd.ttc',size=20)
微軟正黑體_15 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\msjhbd.ttc',size=15)

mpl.rcParams['figure.figsize'] = [18,9]
mpl.rcParams['text.color'] = 'LightGreen'   #  修改參數字典中，文字顏色的整體設定，會影響圖紙標題及小圖標題
mpl.rcParams['axes.labelcolor'] = 'yellow'  #  會影響小圖X軸及Y軸說明文字
mpl.rcParams['xtick.color'] = 'Orange'      #  會影響小圖X軸的尺標
mpl.rcParams['xtick.labelcolor'] = 'white'  #  會影響小圖X軸的尺標文字
mpl.rcParams['ytick.color'] = 'Orange'      #  會影響小圖Y軸的尺標
mpl.rcParams['ytick.labelcolor'] = 'white'  #  會影響小圖Y軸的尺標文字

fig , ax = plt.subplots(nrows=2, ncols=1)

fig.set_facecolor('black')
fig.suptitle(dict_1[stock_no],fontproperties = 微軟正黑體_20)

x = list(zip(*list_2D))[0]
y1 = list(zip(*list_2D))[6]
y2 = list(zip(*list_2D))[1]

ax[0].set_facecolor('DimGray')
ax[0].set_title('走勢圖',fontproperties = 微軟正黑體_15)
ax[0].set_xlabel('日期',fontproperties = 微軟正黑體_15)
ax[0].set_ylabel('成交價格',fontproperties = 微軟正黑體_15)
ax[0].fill_between(x, y1, color = 'LightGreen', alpha=1)    # 面積圖
ax[0].plot(x, y1, color='Green', alpha=0.8)                 # 折線圖
#  設定日期出現的數量不要太多以免衝突
locations = ax[0].get_xticks()
xtick_labels = ax[0].get_xticklabels()
locs1 = [ n for n in range(0,len(locations),10)]
labels1 = [ x[n] for n in locs1]
ax[0].set_xticks(locs1,labels=labels1,rotation=20,fontproperties=myfont_10)
ax[0].grid(visible=True,axis='y')
ax[0].set_ylim(min(y1)-3, max(y1))
y_t = ax[0].get_yticklabels()
for item in y_t :
    item.set_fontproperties(myfont_10)  #class matplotlib.text.Text
ax[0].margins(0.005, 0.005)

成交量顏色 = ['red']
成交量顏色 += [ "red" if y2[i]-y2[i-1] >= 0 else "green" for i in range(1,len(y2)) ]
ax[1].set_facecolor('black')
ax[1].set_title('成交量',color='red',fontproperties = 微軟正黑體_15)
ax[1].set_ylabel('成交股數',fontproperties = 微軟正黑體_15)
ax[1].bar(x, y2, alpha=1, color = 成交量顏色)            #  直條圖
ax[1].set_xticks('',labels='')
y_t = ax[1].get_yticklabels()
for item in y_t :
    item.set_fontproperties(myfont_10)
ax[1].margins(0.005, 0.005)
ax[1].grid(visible=True,axis='y')

fig.tight_layout()
plt.subplots_adjust(hspace=0.4)
plt.show()

