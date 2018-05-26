
#! /usr/bin/python
# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_liner(n):
    test = [1]
    a = 1
    b = 1
    while len(sorted(set(test))) < n+1:
        test.append(2*a+1)
        test.append(3*b+1)
        a=test[b]
        b=b +1

    t =  sorted(set(test))
    print t , n , len(t)
    print t[n]

if __name__   == '__main__':
    dbl_liner(20)
