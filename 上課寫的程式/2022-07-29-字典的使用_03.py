import 之寧模組

list1 = 之寧模組.新竹市重要遊憩據點

dict1 = { "期別": "109年1月","十八尖山": "192081","青青草原": "58063",
          "城隍廟": "241389","新竹漁港": "452276","賞蟹步道": "15147",
          "青草湖": "32690","十七公里腳踏車道": "27195","新竹公園": "111424" }

'''
dict2 = {}
# dict2["十八尖山"] = 192081
# dict2["青青草原"] = 58063
# dict2["城隍廟"] = 241389

dict1.keys()  # 取得字典dict1 中的所有key值
list2 = list(dict1.keys())[1:] # 切開期別 取得後面key 值
print(list2)
# dict2[list2[0]] = 192081
# dict2[list2[1]] = 58063
# dict2[list2[2]] = 241389

list3 = list(dict1.values())[1:] # 取得字典dict1 中的所有value值
print(list3)
# dict2[list2[0]] = int(list3[0])
# dict2[list2[1]] = int(list3[0])
# dict2[list2[2]] = int(list3[0])
# dict2[list2[3]] = int(list3[0])
# dict2[list2[4]] = int(list3[0])
# dict2[list2[5]] = int(list3[0])
# dict2[list2[6]] = int(list3[0])
# dict2[list2[7]] = int(list3[0])

for n in range(len(list2)) :
    dict2[list2[n]] = 0
'''

# 使用迴圈產生字典
dict2 = { k : 0 for k,v in dict1.items() if k!='期別' }

# 比較兩方法差別
del dict1["期別"] # 直接刪除後 字典中value無法轉型int

print(dict1)
print(dict2)