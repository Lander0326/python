str1 = '刁虹文'
str2 = '張家翊'
str3 = '歐明軒'
# print(str1+str2+str3)

# 使用字串相關方法
# 'count', 'format', 'replace','join', 'split', 'strip', 'zfill'

# print( str1.count('刁') )

str4 = '''\
Return the number of non-overlapping occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.
'''

print(len(str4))
print( str4.count('t') )

no = 0
for item in str4 :
    if item == 't' :
        print('索引位置:',no)
    no = no + 1

# 注意迴圈控制區塊
no = 0
for item in str4 :
    if item == 't' :
        print('索引位置:',no)
        no = no + 1