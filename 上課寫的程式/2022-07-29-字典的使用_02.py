import 之寧模組

list1 = 之寧模組.新竹市重要遊憩據點

t = input("請輸入年份:")
p = input("請輸入據點:")

n = 0
for item in list1 :
    if item['期別'].split('年')[0] == t :
        n += int(item[p])

print( f'{t}年 {p} 總共來客人數為 {n} 人' )


