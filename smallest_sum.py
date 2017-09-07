#https://www.codewars.com/kata/smallest-possible-sum

# def solution(lst):
#     while True:
#         max_ = max(lst)
#         min_ = min(lst)
#         mx_idx = lst.index(max_)
#         mn_idx = lst.index(min_)
#         if lst.count(lst[0]) == len(lst) :
#             return sum(lst)
#             break            
#         elif lst[mx_idx]>lst[mn_idx]:            
#             lst[mx_idx] =lst[mx_idx] - lst[mn_idx]


def GCD (a,b):
    if b==0:
        return a;
    return GCD(b,a%b)


def solution(lst):
    ct = len(lst)
    ele = lst[0]
    lst = iter(lst[1:])
    for item in lst:
        ele = GCD(item,ele)
    return int(ele * ct)
        
    

print solution ([1, 21, 55])
