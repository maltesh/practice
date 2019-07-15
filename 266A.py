# http://codeforces.com/contest/266/problem/A

n = int(raw_input())
colors  = list(raw_input())
ct = 0
k = 1
temp = colors[0]
while k < n:
    m = colors[k]
    if temp == m :
        ct = ct + 1
    temp = m
    k = k + 1

print ct