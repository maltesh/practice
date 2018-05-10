#https://www.codewars.com/kata/sum-by-factors/python
def prime_factors(n):
    if n<0:
        n = n * -1
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

from collections import defaultdict

def sum_for_list(lst):
    fctr = []
    common_factos = defaultdict(list)
    for item in lst:
        tt = prime_factors(item)
        if tt:
            fctr.append(tt)
            for ele in set(tt):
                common_factos[ele].append(item)

    # Find common element in list of list
    if fctr:
        result = set(fctr[0])
        for s in fctr[1:]:
            result = result.union(s)
    fr = []
    for ky in sorted(common_factos.keys()):
        if ky in result:
            fr.append([ky,sum(common_factos[ky])])        
    return  fr

if '__main__' == __name__:
    a = [12, 15]
    # print sum_for_list(a)
    # print sum_for_list( [15, 30, -45] )
    # print sum_for_list([15, 21, 24, 30, -45])
    print sum_for_list([-29804, -4209, -28265, -72769, -31744])
    # print prime_factors(45)
    # [[2, 54], [3, 45], [5, 0], [7, 21]]