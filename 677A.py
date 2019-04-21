# https://codeforces.com/contest/677/problem/A

hts  = []
temp = 0
sm = 0

n , h = map(int , raw_input().split( ' '))
hts = map(int, raw_input().split(' '))

for idx,ech_ht in enumerate(hts):
    if  ech_ht <= h:
        sm = sm + 1
    else:
        sm = sm + 2

print sm

