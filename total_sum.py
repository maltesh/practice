# https://www.codewars.com/kata/great-total-additions-of-all-possible-arrays-from-a-list/train/python

import itertools as it
def gta(limit, *args):
    args = map(str,args)
    mx = max(args,key=len)
    arr = []
    t_l = len(str(mx))
    k = 0

    while k < limit:
        for itm in args:
            try:
                if itm[k] not in arr:
                    arr.append(itm[k])
                else:
                    continue
            except:
                pass
        k = k +1 
    print arr
    ll = 1
    sm =0 
    while ll <= limit:
        for item in  it.permutations(arr[0:limit], ll):
            aa = sum(map(int, item))
            sm = sm + aa
        ll = ll + 1
    return sm


# gta(7, 123489, 5, 67)
# print gta(7, 123489, 5, 67)
print gta(8, 12348, 47, 3639)