'''
list1 = [ "温孟芳" , "吳芝儀", "張家翊", "劉家銘"]

for item in list1 :
    print(item)

for i in range( len(list1) ) :
    print(f"第 {i+1} 個人是 {list1[i]}" )

for i,item in enumerate(list1) :
    print(f"第 {i+1} 個人是 {item}" )
'''

list1 = [ "温孟芳 24 93 77 82" ,
          "吳芝儀 22 89 81 86" ,
          "張家翊 19 91 79 84" ,
          "劉家銘 25 95 75 80"   ]

for item in list1 :
    print( f"{item.split(' ')[0]} 今年 {item.split(' ')[1]} 歲")

list2 = []
for item in list1 :
    a = item.split(' ')  # "温孟芳 24 93 77 82"  -->  ['温孟芳', '24', '93', '77', '82']
    list2.append(a)

print(list2)

for item in list2 :
    print(f"{item[0]} 今年 {item[1]} 歲")



















'''
dfgfhshgf
sdfhfhfhfh
shfhhhdsfhdfh
'''

str1 = 'gngngngn'
str2 = "dfgfhfhfnfgngfn"
str3 = 'bbcjhdscvdkvj;KDV;ldvdlkvnbld' \
       'kbvLKDVNLKDVBLDKFVBN/LKDFVBLDKVNB/' \
       'LDKVBN/DLKVBLDKVB/DLKVB/DLKVBD/LKVB/DL' \
       'KVB/DLKVB/DLKVB/DLKVB/DLFVD/FBLVKB/VIAERV;'

STR4 = '''\
FGHBGFNGFNGFNGN
FNGGFNGFNGFN
FGNGFNFGN
SFNSGFNGFNGFNGFNGFNGN
'''











