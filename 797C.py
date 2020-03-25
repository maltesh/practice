# https://codeforces.com/contest/797/problem/C  
import Queue
import string
from collections import Counter

s = raw_input()
stk, res = [] , []

qu = Queue.Queue(maxsize=len(s))
dct = dict( zip(string.ascii_lowercase, [0 for _ in range(1,27)]) )

def get_cr():
    for cr in string.ascii_lowercase:
        if dct.get(cr):
            return cr

for each_cr in s:
    qu.put(each_cr)
    dct[each_cr.lower()] = dct[each_cr.lower()]+1

while not qu.empty():
    min_cr = get_cr()
    if len(stk) == 0:
        cr = qu.get()
        stk.append(cr)
        dct[cr] = dct[cr]-1
    else:
        if stk[ len(stk)-1] <= min_cr  :
            res.append(stk.pop())
        else:
            qfrnt = qu.get()
            stk.append(qfrnt)
            dct[qfrnt] = dct[qfrnt]-1

while len(stk)>0:
    res.append(stk.pop())

print (''.join(res))