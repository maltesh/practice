# https://codeforces.com/contest/9/problem/A

from fractions import Fraction
y, w = map(int,raw_input().split( ' '))
t = sorted([y,w], reverse=True)
rng = len(range(t[0], 7))
if rng == 6:
    print '1/1'
else:
    print str(Fraction(rng,6))