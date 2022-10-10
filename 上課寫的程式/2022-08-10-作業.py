

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