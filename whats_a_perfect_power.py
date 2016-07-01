# https://www.codewars.com/kata/whats-a-perfect-power-anyway/train/python
#Sieve Algorithms for Perfect Power Testin

import  math

def isPP(n):
    primes = int (math.log(n,2))
    temp = 2
    while  temp <= primes :
        lgn = round(math.pow(n,1.0/temp),1)
        if abs(math.pow(lgn,temp)) == float(n):
            return [int(lgn),temp]
        temp = temp +1

pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
# pp = [128,256,222]
for item in pp:
    print item ,isPP(item)
