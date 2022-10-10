import pandas as pd
list1 = []

start_year = 2020
start_month = 7

end_year = 2022
end_month = 1

for y in range(start_year,end_year+1) :
    if y == start_year :
        s_m = start_month
        if y == end_year :
            e_m = end_month
        else :        
            e_m = 12
    elif y == end_year :
        s_m = 1
        e_m = end_month
    else :
        s_m = 1
        e_m = 12
    for m in range(s_m,e_m+1) :
        str1 = str(m).zfill(2)
        str2 = f"D:\\python教學\\2022尖兵六班\\股票資料\\STOCK_DAY_00635U_{y}{str1}.csv"
        df = pd.read_csv(str2,encoding='big5',header=1,skipfooter=5,engine='python',
                     usecols=[0,1,2,3,4,5,6,7,8])
        list1.append(df)
    
    
縱向合併 = pd.concat(list1)
stock_table = 縱向合併.reset_index(drop=True)
#print(stock_table.dtypes)
stock_table['成交股數'] = (stock_table['成交股數'].str.split(',')).str.join("") 
stock_table['成交股數'] = stock_table['成交股數'].astype('int')
#print(stock_table.dtypes)

import statistics
window5 = 5  # 绘制5日移动平均线
mean5 = [ statistics.mean(stock_table['收盤價'][i: i+window5]) for i in range(len(stock_table['收盤價']) - window5 + 1)]
window20 = 20  # 绘制5日移动平均线
mean20 = [ statistics.mean(stock_table['收盤價'][i: i+window20]) for i in range(len(stock_table['收盤價']) - window20 + 1)]
window60 = 60  # 绘制5日移动平均线
mean60 = [ statistics.mean(stock_table['收盤價'][i: i+window60]) for i in range(len(stock_table['收盤價']) - window60 + 1)]

import matplotlib.pyplot as plt
import matplotlib as mpl

微軟正黑體 = mpl.font_manager.FontProperties(fname=r"c:\windows\fonts\msjhbd.ttc",size = 12)
喜歡的英數字體 = mpl.font_manager.FontProperties(fname=r"c:\windows\fonts\ITCKRIST.TTF",size = 12)

#mpl.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# The list of rcParams  https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=matplotlib%20rcparams#matplotlib.rcParams

mpl.rcParams['xtick.color'] = 'Orange'      #  會影響小圖X軸的尺標
mpl.rcParams['xtick.labelcolor'] = 'white'  #  會影響小圖X軸的尺標文字
mpl.rcParams['ytick.color'] = 'Orange'      #  會影響小圖Y軸的尺標
mpl.rcParams['ytick.labelcolor'] = 'white'  #  會影響小圖Y軸的尺標文字

fig1 = plt.figure()  # 產生figure
fig1.set_facecolor('#222222')
fig1.set_size_inches(16,8)

x = stock_table['日期']
y1 = stock_table['收盤價']
y2 = stock_table['成交股數']
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html#sphx-glr-gallery-lines-bars-and-markers-fill-between-alpha-py
# https://qinqianshan.com/python/matplotlib/matplotlib-stacked-area/
成交量顏色 = ['red']
成交量顏色 += [ "red" if y2[i]-y2[i-1] >= 0 else "green" for i in range(1,len(y2)) ]

axes_1 = fig1.add_axes([0.05,0.37,0.9,0.53],facecolor='#222222') #  [left, bottom, width, height]

axes_1.set_title('期元大S&P黃金',fontsize=18, color='white',fontproperties = 微軟正黑體)
axes_1.plot(x, y1, label='收盤價', color = 'Magenta')
axes_1.plot(x[window5-1:],mean5,alpha=0.5,label='MA 5',color = 'Cyan')
axes_1.plot(x[window20-1:],mean20,alpha=0.5,label='MA 20',color = 'Lime')
axes_1.plot(x[window60-1:],mean60,alpha=0.5,label='MA 60',color = 'Gold')
axes_1.legend(prop = 微軟正黑體)
axes_1.fill_between(x, y1, interpolate=True, color='#efbbff', alpha=0.2)
axes_1.set_ylim(min(y1)-1, max(y1))
axes_1.get_xaxis().set_visible(False)
axes_1.margins(0.005, 0.005)

y_t = axes_1.get_yticklabels()
for item in y_t :
    item.set_fontproperties(喜歡的英數字體)

    
#axes_1.spines['left'].set_color('#800080')
#axes_1.spines['right'].set_color('#800080')
#axes_1.spines['top'].set_color('#800080')
#axes_1.spines['left'].set_color('#800080')

axes_2 = fig1.add_axes([0.05,0.1,0.9,0.23],facecolor='#222222')
axes_2.bar(x, y2, label='成交股數', color = 成交量顏色)
axes_2.legend(prop = 微軟正黑體)
axes_2.margins(0.005, 0.005)
locations = axes_2.get_xticks()
xtick_labels = axes_2.get_xticklabels()
locs1 = [ n for n in range(0,len(locations),15)]
labels1 = [ x[n] for n in locs1]
axes_2.set_xticks(locs1)
axes_2.set_xticklabels(labels1,rotation=20,fontproperties=喜歡的英數字體)
y_t = axes_2.get_yticklabels()
for item in y_t :
    item.set_fontproperties(喜歡的英數字體)
    
#axes_2.spines['left'].set_color('#800080')
#axes_2.spines['right'].set_color('#800080')
#axes_2.spines['top'].set_color('#800080')
#axes_2.spines['left'].set_color('#800080')

plt.show()

'''
matplotlib提供了三个模块用于对图表的颜色进行操控：

matplotlib.cm
matplotlib.colorbar
matplotlib.colors
在matplotlib中，有三种给图表配色的方法：

直观的指定颜色，如，在对象的参数中指定,color='red'；
使用colormap，将数据映射为颜色模型。注意，需要支持 cmap 参数的图表类型；
通过y值，使用蒙版数组按y值绘制具有不同颜色的线。





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