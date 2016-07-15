#https://www.hackerrank.com/challenges/diwali-lights/forum
# http://en.wikipedia.org/wiki/Modular_exponentiation

#https://www.hackerrank.com/challenges/summing-the-n-series

# Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.

import sys
import math
lines = [1,100000,21111]
for no in lines[1:]:
    num = 2**int(no)-1
    den = 10**5
    re  = num%den
    print  re