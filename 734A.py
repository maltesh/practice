# https://codeforces.com/contest/734/problem/A

n = int(raw_input())
gms = str(raw_input())

if gms.count('A') > gms.count('D'):
    print 'Anton'
if gms.count('A') < gms.count('D'):
    print 'Danik'
if gms.count('A') == gms.count('D'):
    print 'Friendship'