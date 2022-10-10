import random

list1 = []
while True :
    n = random.randint(1,49)
    if not ( n in list1 ) :
        list1.append(n)
    if len(list1) == 7 :
        break

print(f"開出順序 : {list1[:6]}   特別號 : {list1[-1]}")
print(f"大小順序 : {sorted(list1[:6])}   特別號 : {list1[-1]}")

list1 = [ "温孟芳" , "吳芝儀", "張家翊", "劉家銘"]
print( random.choice(list1) )

list1 = [2,5,9,1,0,2,3,6,4,9,7,8,5,6,2]
print(list1)
list1.sort()
print(list1)
random.shuffle(list1)
print(list1)



