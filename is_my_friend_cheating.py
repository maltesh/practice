#https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python
# http://codereview.stackexchange.com/questions/124569/product-of-2-numbers-equals-sum-of-numbers-between-them
#Tips: Write down the formula. Sum from 1 to n. Then Sum - (a + b) == axb, a and b have to be int.

def removNb(n):
    total_sum = n*(n+1)/2
    result =[]
    for  i in xrange(n/2,n):
        num = (total_sum-i)/i-1
        if num * i ==total_sum -i-num:
            result.append((i,num))
            result.append((num,i))

    return sorted(result)

from math import sqrt
# def removNb(n):
#     all_nos = range(n+1)
#     total_sum = sum(all_nos)
#     print sqrt(total_sum+1)-1
#     print ((n - 1) * n / 2) / (n + 1)
#     result =[]
#     for  key,value in enumerate(range(1,n)):
#         for mm in all_nos[value:]:
#             if value*mm  == total_sum-value-mm:
#                 result.append( (value,mm))
#                 result.append( (mm,value))
#
#     return result
print removNb(26)