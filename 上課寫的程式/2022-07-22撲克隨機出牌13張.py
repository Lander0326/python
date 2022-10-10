import turtle
import random
import 之寧模組

#####################   主程式   ###########################

t1 = turtle.Turtle()  # 產生一個海龜物件
t1.hideturtle()

screen1 = turtle.Screen()
screen1.tracer(0) # 只看結果
screen1.setup( 1200, 800 )

list1 = [ str(x) for x in range(2,11) ] + ['J','Q','K','A']   # 文字的順序
list2 = ['S','H','D','C']   # 花色的順序
list_d = [  (row,col)  for row in list1  for col in list2    ] # 生成52張牌

list3 = []
x0,y0=-550,200
n = 0
while len(list3) < 26 :
    item = random.choice(list_d)  # 抽排
    if item not in list3 :        # 檢查有沒有重複
        list3.append(item)
        y0 = -y0                  # 上下發牌 1>-200 2>200 3>-200
        if item[1] == 'H'  :
            之寧模組.畫紅心(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, item[0])
        elif item[1] == 'D' :      # int(n/2) n=0>>0 n=1>>0 n=2>>1 n=3>>1 上下對齊X軸
            之寧模組.畫方塊(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, item[0])
        elif item[1] == 'S' :
            之寧模組.畫黑桃(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, item[0])
        else :
            之寧模組.畫梅花(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, item[0])
        n = n + 1

print(之寧模組.COLORS[:10])

screen1.mainloop()


