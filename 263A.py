# https://codeforces.com/problemset/problem/263/A
n = 5
k = 0
rw = 0
col = 0
while k < n:
    rws = map(int, raw_input().split(' '))
    if rws.count(1)>0 :
        rw = k
        col = rws.index(1)
    k = k+1

print (abs(2-rw) + abs(2- col))