import math

def sum_for_list(lst):
    factors = {}
    for item in lst:
        if item >3:
            print sieve(item)
        else:
            factors[item]=[item]
    pass




def factors(n):


def sieve(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

# def sieve(n):
#     all_nos =[]
#     all_nos.insert(0,False)
#     all_nos.insert(1,False)
#     all_nos[2:] = [i for i in range(2,n)]
#     limit =  int(math.sqrt(n))
#     no=2
#     print all_nos





# def sieve(n):
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# def sieve(n):
#     if n %2 ==0 :
#         n = n/2
#     else
#
#
#     temp = [i for i in range(2,n)]
#     limt = int(math.sqrt(n))
#     # print  temp
#     # print limt
#
#
#     for no in range(2,limt+1):
#         for index,value in enumerate(temp):
#             if value%no ==0 :
#                 temp[index]=0
#         # print index, " === >",value
#     print temp
a = [12]
sum_for_list(a)