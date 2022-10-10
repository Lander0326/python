# 只載入某支股票的一個月股價資料

import requests as r
import matplotlib.pyplot as plt
import matplotlib as mpl

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=00635U"
res = r.get(url)
stock_json = res.json()
標題 = stock_json['title']   #  '111年01月 00635U 期元大S&P黃金    各日成交資訊'
欄位 = stock_json['fields']  #  ['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data = stock_json['data']   #  [  ['111/01/03', '505,756', '12,255,065', '24.24', '24.27', '24.18', '24.18', '+0.33', '238'],...]

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

# 股票代號及股票名稱對照
dict_1 = {'00635U':'00635U 期元大S&P黃金','00738U':'00738U 期元大道瓊白銀'}
stock_no = '00635U'

mpl.rcParams['font.family'] = 'YouYuan'
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['figure.figsize'] = [18,9]
mpl.rcParams['text.color'] = 'LightGreen'   #  修改參數字典中，文字顏色的整體設定，會影響圖紙標題及小圖標題
mpl.rcParams['axes.labelcolor'] = 'yellow'  #  會影響小圖X軸及Y軸說明文字
mpl.rcParams['xtick.color'] = 'Orange'      #  會影響小圖X軸的尺標
mpl.rcParams['xtick.labelcolor'] = 'white'  #  會影響小圖X軸的尺標文字
mpl.rcParams['ytick.color'] = 'Orange'      #  會影響小圖Y軸的尺標
mpl.rcParams['ytick.labelcolor'] = 'white'  #  會影響小圖Y軸的尺標文字
myfont_10 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\ITCKRIST.TTF',size=10)

fig = plt.figure( facecolor='black' )
fig.suptitle(dict_1[stock_no],fontsize=20)

ax1 = fig.add_axes([0.05,0.42,0.9 ,0.48] ,facecolor='DimGray')
ax2 = fig.add_axes([0.05,0.05 ,0.9 ,0.25] ,facecolor='Black')

x = list(zip(*list_2D))[0]
y1 = list(zip(*list_2D))[6]
y2 = list(zip(*list_2D))[1]

ax1.set_title('走勢圖',fontsize=15)
ax1.set_xlabel('日期',fontsize=15)
ax1.set_ylabel('成交價格',fontsize=15)
ax1.fill_between(x, y1, color = 'LightGreen', alpha=1)    # 面積圖
ax1.plot(x, y1, color='Green', alpha=0.8)                 # 折線圖
#  設定日期出現的數量不要太多以免衝突
locations = ax1.get_xticks()
xtick_labels = ax1.get_xticklabels()
locs1 = [ n for n in range(0,len(locations),10)]
labels1 = [ x[n] for n in locs1]
ax1.set_xticks(locs1,labels=labels1,rotation=20,fontproperties=myfont_10)
ax1.grid(visible=True,axis='y')
ax1.set_ylim(min(y1)-1, max(y1))
y_t = ax1.get_yticklabels()
for item in y_t :
    item.set_fontproperties(myfont_10)  #class matplotlib.text.Text
ax1.margins(0.005, 0.005)

成交量顏色 = ['red']
成交量顏色 += [ "red" if y2[i]-y2[i-1] >= 0 else "green" for i in range(1,len(y2)) ]
ax2.set_title('成交量',color='red',fontsize=15)
ax2.set_ylabel('成交股數',fontsize=15)
ax2.bar(x, y2, alpha=1, color = 成交量顏色)            #  直條圖
ax2.set_xticks('',labels='')
y_t = ax2.get_yticklabels()
for item in y_t :
    item.set_fontproperties(myfont_10)
ax2.margins(0.005, 0.005)
ax2.grid(visible=True,axis='y')

plt.show()
