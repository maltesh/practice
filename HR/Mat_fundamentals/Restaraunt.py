#https://www.hackerrank.com/challenges/restaurant?h_r=next-challenge&h_v=zen

import sys
import math

def gcd(a,b):
    if b ==0:
        return a
    elif  a >= b and b > 0:
        return gcd ( b , a % b );
    else:
        return gcd ( b , a );

lines = sys.stdin.readlines()
test_cases = lines[0]
for params in lines[1:]:
    a,b = map(int,params.split( ' '))
    if a == b:
        print 1
    else:
        gc = gcd(a,b)
        print b*a/math.pow(gc,2)


