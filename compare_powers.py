#https://www.codewars.com/kata/compare-powers/python
import math
def compare_powers(n1,n2):
    no1 = (int)(n1[1] * math.log10(n1[0])) + 1
    no2 = (int)(n2[1] * math.log10(n2[0])) + 1
    if no1 == no2:
        return 0;
    if no1 > no2:
        return -1
    else:
        return 1
