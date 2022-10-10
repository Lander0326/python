squares = [1, 4, 9, 16, 25]

print(type(squares))

print(dir(squares))

# 'append', 'clear', 'copy', 'count', 'extend', 'index'
# 'insert', 'pop', 'remove', 'reverse', 'sort'

print(squares[-3:])

list1 = squares[:] # 全切=拷貝(淺拷貝)

cubes = [1,8,27,65,125] # 串列為可變資料型別 可改變串列中元素內容
cubes[3] = 64 # 3號位65 改為64

print(cubes)
