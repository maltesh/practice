#https://www.hackerrank.com/challenges/two-characters?h_r=next-challenge&h_v=zen

import sys
import itertools


s_len = len(s)
s_len = int(raw_input().strip())

max_count = 0
lis = list(s)
uniq = set(s)
max_uniq_count =  len(uniq)

while max_uniq_count >= 2:
    ll = max_uniq_count
    for leter in itertools.combinations(uniq,ll-2):
        temp = s
        for each_char in leter:
            temp = temp.replace(each_char,'')
        if any([fl1 == sl1 for fl1,sl1 in zip(temp,temp[1:])]) == False:
            if max_count < len(temp):
                max_count = len(temp)
        if not temp:
            max_count =  len(s)
        max_uniq_count = max_uniq_count -1
print  max_count
