# https://codeforces.com/problemset/problem/467/B

n ,m ,k = map(int,raw_input().split(' '))
temp = 1
plyrs =[]
while m  >= temp:
    plyrs.append( int(raw_input()) )
    temp = temp + 1
val  = int(raw_input())

# plyrs = [1,2,3,4]
# m =3
# k =3
def fedor_new_game(plyrs, val,k):
    ans = 0
    for plyr in plyrs:
        if  getTotalCount(plyr ^ val) <= k:
            ans = ans+1
    return ans

def getTotalCount(n):
    temp = 0
    while n :
        temp = temp + ( n & 1 )
        n = n >>1
    return temp
print fedor_new_game(plyrs, val,k)