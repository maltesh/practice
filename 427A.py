# http://codeforces.com/contest/427/problem/A

no = int(raw_input())
arr = map(int,raw_input().split( ' '))
i = 0
crim = 0
poli = 0
while i < no:
    if arr[i]< 0:
        crim = crim + arr[i]
        if poli > 0 :
            crim =     -(abs(crim) - 1) if crim< 0 else abs(crim)-1
            poli = poli -1 
        
    else:
        poli = poli + arr[i]
    i = i + 1
print abs(crim)