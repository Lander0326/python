import 之寧模組

list1 = 之寧模組.新竹市重要遊憩據點

# 109年1月 青青草原 來客數為?

t = input("請輸入期別:")
p = input("請輸入據點:")


for item in list1 :
    if item['期別'] == t :
        print( f'{t} {p} 來客人數為 {item[p]} 人' )

