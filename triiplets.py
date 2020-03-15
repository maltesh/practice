# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python

from collections import defaultdict

def recoverSecret(triplets):
    all_chars = []
    biggera_ar = defaultdict(list)
    for triplr in triplets:
        all_chars.extend(triplr)
        for idx,val in enumerate(triplr):
            biggera_ar[val] =  list (set(biggera_ar[val]+triplr[idx+1:]))
    
    k= 0
    op = ''
    while biggera_ar:
        nn_cr = next(i for i, v in biggera_ar.items() if not v )
        print (nn_cr)
        del biggera_ar[nn_cr]
        for itm, arr in biggera_ar.items():
            if nn_cr in arr:
                arr.remove(nn_cr)
        op =  nn_cr + op
        k = k+1

    return op

triplets = [['t', 's', 'f'], ['a', 's', 'u'], ['m', 'a', 'f'], ['a', 'i', 'n'], ['s', 'u', 'n'], ['m', 'f', 'u'], ['a', 't', 'h'], ['t', 'h', 'i'], ['h', 'i', 'f'], ['m', 'h', 'f'], ['a', 'u', 'n'], ['m', 'a', 't'], ['f', 'u', 'n'], ['h', 's', 'n'], ['a', 'i', 's'], ['m', 's', 'n'], ['m', 's', 'u']]
#whatisup
recoverSecret(triplets)
