# https://www.hackerrank.com/challenges/possible-path?h_r=next-challenge&h_v=zen

def gcd(a,b):
    if b ==0:
        return a
    elif  a >= b and b > 0:
        return gcd ( b , a % b );
    else:
        return gcd ( b , a );


import sys
lines = sys.stdin.readlines()
for line in lines[1:]:
    a,b,c,d = map(int,line.split(" "))
    if gcd(a,b) == gcd(c,d):
        print 'YES'
    else:
        print  'NO'

# A geometric view[edit]>
# "Tall, slender rectangle divided into a grid of squares. The rectangle is two squares wide and five squares tall."
# A 24-by-60 rectangle is covered with ten 12-by-12 square tiles, where 12 is the GCD of 24 and 60. More generally, an a-by-b rectangle can be covered with square tiles of side length c only if c is a common divisor of a and b.
# For example, a 24-by-60 rectangular area can be divided into a grid of: 1-by-1 squares, 2-by-2 squares, 3-by-3 squares, 4-by-4 squares, 6-by-6 squares or 12-by-12 squares. Therefore, 12 is the greatest common divisor of 24 and 60.
# A 24-by-60 rectangular area can be divided into a grid of 12-by-12 squares, with two squares along one edge (24/12 = 2) and five squares along the other (60/12 = 5).