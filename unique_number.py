# https://www.codewars.com/kata/find-the-unique-number-1/train/python
def find_uniq(arr):
    t = set(arr)
    return t[1]  if arr.count(t[0])>1 else t[0]

# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b
