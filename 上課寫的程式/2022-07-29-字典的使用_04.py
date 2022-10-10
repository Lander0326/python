import 之寧模組

list1 = 之寧模組.新竹市重要遊憩據點

#  109年中 各據點加總後 人數最多及最少的是哪兩個?

dict1 = list1[0]

dict2 = dict.fromkeys( list(dict1.keys())[1:],0 )         # 練習一下fromkeys 的使用
# dict2 = { k : 0 for k,v in dict1.items() if k!='期別' }  # 累加用的小表格 此法讚啦 免多學一函式
# print(dict2)
print(dict2)

for dict_item in list1 :
    if dict_item['期別'].split('年')[0] == '109' :   # 如果期別開頭為109年
        for k,v in dict_item.items() :                  # 把key,value 傳出來去下面IF判別
            if k != '期別' :                               # 如果key是 期別 就不進入迴圈
                dict2[k] += int(v)                         # 累加

print(dict2)

ans1 = sorted(dict2.items(), key = lambda x : x[1] , reverse=True )
print(ans1)

ans2 = dict(ans1)
print(ans2)


def f1(d) :
    print(d)

dict4 = {'十八尖山': 1965616, '青青草原': 422134, '城隍廟': 2520746,
         '新竹漁港': 4831286, '賞蟹步道': 292292, '青草湖': 134932,
         '十七公里腳踏車道': 207628, '新竹公園': 516611}
print(dict4.items())
f1(dict4)

