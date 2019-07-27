#http://codeforces.com/contest/567/problem/A
n = int(raw_input())
i = 0
temp = map(int, raw_input().split(' '))
def f_min_max(item, arr):
    temp = sorted(map( lambda x : abs(item -x) ,arr ))

#    for itm in arr:
#        temp.append( abs(item - itm))

#    temp = sorted(temp)
    print min(temp), max(temp)

while i < n:
    item = temp[i]
    mx = max([abs(item - temp[0]), abs(temp[-1]- item)])
    if i == 0:
        mn =  abs(temp[i+1] - item)
    elif i == n-1:
        mn = abs(item - temp[i-1])

    else:
        mn = min([abs(item - temp[i-1]) , abs(item - temp[i+1])])
    i = i + 1

    print mn , mx
