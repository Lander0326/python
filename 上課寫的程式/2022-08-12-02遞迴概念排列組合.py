

def perm(L):

# Compute the list of all permutations of l
    if len(L) <= 1:
        return [L]
    if len(L) == 2:
        return [ [ L[0],L[1] ] , [ L[1],L[0] ] ]

    r = []
    for i in range(len(L)):
        s = L[  : i ] + L[ i + 1 : ]
        p = perm(s)
        for x in p:
            r.append(L[i:i + 1] + x)
    return r

print(perm([3,4,5]))
#perm([3,4,5]     --->

# [3] perm([4,5]) ---> [3]  [4,5] [5,4]
# [4] perm([3,5]) ---> [4]  [3,5] [5,3]
# [5] perm([3,4]) ---> [5]  [3,4] [4,3]

# perm 正式結束


