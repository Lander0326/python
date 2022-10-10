import turtle
import math
import random
import 家翊模組


##############################    主程式    ###############################

t1 = turtle.Turtle()  # 產生一個海龜物件
t1.hideturtle()

screen1 = turtle.Screen()
screen1.tracer(0)  # 只看結果
screen1.setup(1200, 800)

list1 = [ str(x) for x in range(2,11) ] + ['A','J','Q','K']
list2 = ['H','D','S','C']
list_d = [ (row,col) for row in list1 for col in list2 ]

list3 = []
n = 0
while len(list3) < 5 :
    item = random.choice(list_d)
    if item not in list3 :
        list3.append(item)
        if item[1] == 'H' :
            家翊模組.畫紅心(t1, screen1, -450 + 225 * n, 0, 1, item[0])
        elif item[1] == 'D' :
            家翊模組.畫方塊(t1, screen1, -450 + 225 * n, 0, 1, item[0])
        elif item[1] == 'S' :
            家翊模組.畫黑桃(t1, screen1, -450 + 225 * n, 0, 1, item[0])
        else:
            家翊模組.畫梅花(t1, screen1, -450 + 225 * n, 0, 1, item[0])
        n = n + 1

print(家翊模組.COLORS[:10])
screen1.mainloop()