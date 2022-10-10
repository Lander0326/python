

def perm1(l):

# Compute the list of all permutations of l
    if len(l) <= 1:
        return [l]
    r = []
    # print(r)
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm1(s)
        print(s)
        print(l)
        print(p)
        for x in p:
            r.append(l[i:i + 1] + x)
            print(r)

    return r


# print(perm1(a))
print(perm1([4,7]))



# list1 = [1]
# list2 = [1,2]     #  [1,2] [2,1]
# list3 = [1,2,3]   #  [1,2,3] [1,3,2] [2,1,3] [3,1,2] [3,2,1]
#
# for item1 in list3 :
#     for item2 in list3 :
#         for item3 in list3 :
#             if len(set([item1,item2,item3])) == 3 :
#                 print([item1,item2,item3])


n = int(input('give me a int number :'))


# 5! = 1 * 2 * 3 * 4 * 5
# 3! = 1 * 2 * 3

t = 1
for i in range(1,n+1) :
    t *= i

print(t)











