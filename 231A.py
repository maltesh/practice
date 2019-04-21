# https://codeforces.com/contest/231/problem/A

n = int(raw_input())
t = 0
ct = 0 
while t < n:
    temp = raw_input().split(' ')
    k = 0
    for _ , val in enumerate(temp):
        if int(val):
            k = k + 1
    if k >= 2:
        ct = ct+1    
    t = t + 1
print ct