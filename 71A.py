# http://codeforces.com/contest/71/problem/A
from __future__ import print_function

fw = lambda x: '{fc}{cnt}{lc}'.format(fc=x[0],cnt=len(x[1:-1]),lc=x[-1])
pnt = lambda x: print (x)

n = int(raw_input())
i = 0
temp = []
while i < n:
    wrd = raw_input()
    fm_wrd = wrd if len(wrd) < 10 else fw(wrd)
    i = i + 1
    temp.append(fm_wrd)
map(pnt,temp)