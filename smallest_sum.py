#https://www.codewars.com/kata/smallest-possible-sum

def solution(lst):
    while True:
        max_ = max(lst)
        min_ = min(lst)
        mx_idx = lst.index(max_)
        mn_idx = lst.index(min_)
        if lst.count(lst[0]) == len(lst) :
            return sum(lst)
            break            
        elif lst[mx_idx]>lst[mn_idx]:            
            lst[mx_idx] =lst[mx_idx] - lst[mn_idx]


print solution ([1, 21, 55])