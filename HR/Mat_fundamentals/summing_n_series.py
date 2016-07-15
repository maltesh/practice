#https://www.hackerrank.com/challenges/summing-the-n-series

import sys
lines = sys.stdin.readlines()
for no in lines[1:]:
    print int(no)**2 % (10**9+7)