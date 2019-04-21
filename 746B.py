# https://codeforces.com/contest/746/problem/B#
from math import ceil
n = int(raw_input())
enc_str = raw_input()
size = len(enc_str)


t = ''
for idx, val in enumerate(enc_str):
    if idx % 2 == 1:
        t = val + t
    else:
        t = t+val 

if size % 2 ==0:
    print t[::-1]
else:
    print t
    
