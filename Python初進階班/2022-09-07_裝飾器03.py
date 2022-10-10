# coding: utf8
import collections


學生 = collections.namedtuple('學生',("學號",'姓名','生日'))

表格 = [ 學生('A01','孟芳','10/10'),學生('A02','虹文','10/11'),學生('A03','家翊','10/12') ]

print(表格[0].姓名) # 表格[0][1]

for item in 表格[0] :
    print(item)


class 學生1 :
    def __init__(self,*args) :
        self.學號 = args[0]
        self.姓名 = args[1]
        self.生日 = args[2]

        self.資料 = [self.學號,self.姓名,self.生日]

    # def __iter__(self):
    #     return self
    def __getitem__(self,item): # item 傳遞索引
        return self.資料[item]

表格1 = [ 學生1('A01','孟','10/10'),學生1('A02','虹','10/11'),學生1('A03','家','10/12') ]

print(表格1[0].學號)
print(表格1[0].姓名)
print(表格1[0].生日)

print(表格1[0][0])

for item in 表格1[0] :
    print(item)
