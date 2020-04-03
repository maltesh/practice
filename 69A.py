#https://codeforces.com/problemset/problem/69/A
n = int(input())
k = 0
t = []
while k < n:
    t.extend( map(int, raw_input().split( ' ')))
    k = k +1
if sum(t) == 0 :
    print 'YES'

else:
    print 'NO'
    




