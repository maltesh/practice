# https://www.codewars.com/kata/give-me-a-diamond/train/python

import math
def diamond(n):
    # Make some diamonds!
    if n< 0 or n%2 == 0:
        return None
    no  = int(math.ceil(float(n)//2))
    i = 0
    temp = []
    cr = '*'
    k = 1
    while i < n :
        spc = int(float(n - k)/2)
        temp.append(''.center(spc, ' ')+   cr *k   + '\n')            
        i = i + 1
        if i <= no:
            k = k + 2 
        else:
            k = k - 2 

    return ''.join(temp)

print diamond(3)


# def diamond(n):
#     if n > 0 and n % 2 == 1:
#         diamond = ""
#         for i in range(n):
#             diamond += " " * abs((n/2) - i)
#             diamond += "*" * (n - abs((n-1) - 2 * i))
#             diamond += "\n"
#         return diamond
#     else:
#         return None