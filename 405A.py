# https://codeforces.com/contest/405/problem/A

n = int(raw_input())
temp = map(int, raw_input().split(' '))
temp = map(str,sorted(temp))
print ' ' .join(temp)