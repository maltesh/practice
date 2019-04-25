# https://codeforces.com/problemset/problem/579/A


input = int(raw_input())

min_bacteria = 1
temp = 0
def getTotalCount(n):
    global temp , min_bacteria
    while n :
        temp = temp + ( n & 1 )
        n = n >>1
    return temp
print getTotalCount(input)