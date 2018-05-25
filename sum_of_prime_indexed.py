from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def total(arr):
    return sum([val for index,val in enumerate(arr) if isPrime(index)])



if __name__ == '__main__':
    total([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


