# http://codeforces.com/contest/227/problem/B

n = int(input())
arr = map(int , raw_input().split())

arr = dict(zip(arr,xrange(1,len(arr)+1 )))
m = int(input())
sq = map(int , raw_input().split())

x, y = 0,0
for item in sq:
    x = x + arr[item]
    y =  y+ n - arr[item] + 1
print x, y,