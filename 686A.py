# http://codeforces.com/contest/686/problem/A

n , x = map(int, raw_input().split( ' '))
i = 0
total = x
dk = 0
while i < n:
    ip = raw_input().split(' ')
    num = eval(ip[0]+ip[1]) #formatting

    if total  + num  > 0:
        total = total+num
    else:
        dk = dk +1

    i = i +1

print total , dk