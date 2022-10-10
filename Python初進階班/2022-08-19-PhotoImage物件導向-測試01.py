# class LL():
class LL(list):
    pass

obj1 = LL()
obj2 = LL()
# print(obj1) # <__main__.LL object at 0x0000022F0AF4A400> 產生了LL類別的物件

obj1.append(1)
obj1.append(2)
obj2.append(10)
obj2.append(20)
print(obj1+obj2) # 繼承