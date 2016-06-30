# https://www.codewars.com/kata/54129112fb7c188740000162/train/python
def prefill(n,v=[]):
    #your code here
    temp=[]
    try:
        if n is not None and int(n)>0:
            for i in range(int(n)):
                temp.append(v)
            return temp
        if n is None:
            return temp
        if n == 0 or int(n) ==0 :
            return temp
    except ValueError :
        raise TypeError(n +" is invalid")

from unittest import TestCase

# print prefill(3,1)
# print prefill(2,"abc")
# print prefill(3, prefill(2,'2d'))
# print prefill("xyz", 1)
# print prefill('3',1)
# print prefill(0,2)
# print prefill(0,[])
# print prefill('0',[])
print prefill(None,{})