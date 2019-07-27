# https://codeforces.com/contest/136/problem/A
from __future__ import print_function

pp = lambda x: print(x[1])

n = int(raw_input())
arr = []
arr = map(int,raw_input().split( ' '))
z = zip(arr, range(1,len(arr)+1))
k = sorted(z,key = lambda x:x[0])
map(pp ,k)
