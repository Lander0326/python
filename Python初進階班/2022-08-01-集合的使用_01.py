
#set1 = { [1,2],[3,4],[5,6] }
set1 = { (1,2),(3,4),(5,6) }
# set2 = { list('aiushdauisdh') } >>> TypeError
set2 = { *tuple('aiushdauisdh') } # 解包把()拿掉 但集合中元素不可重複> 為消除重複項
print(set1)
print(set2)

print(dir(set1))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

set3 = set()  # 創建空集合唯一方法