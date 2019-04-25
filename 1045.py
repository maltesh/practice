from collections import Counter
import itertools


all_strs = []
input = int(raw_input())

while input >0 :
    all_strs.append(str(raw_input()))

def find_palis(all_strs_lst):
    t = 0
    combs = itertools.combinations(all_strs_lst,2)
    for s1,s2 in combs:
        if validate_count(s1+s1)
            t = t +1
    print t

def validate_count(ip_str):
    c = Counter(ip_str)
    temp = True
    if len(ip_str)%2 == 0:
        for v_itr in c.iteritems():
            if v_itr[1] % 2 == 1:
                temp = False
                break
        
    else:
        ct = 0        
        # odd
        for v_itr in c.iteritems():
            if v_itr[1] % 2 == 1:
                ct = ct+1
        if ct > 1:
            temp = False

    return temp
    
find_palis(all_strs)
