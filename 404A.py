# http://codeforces.com/contest/404/problem/A
n = int(input())
i = 0
s1 = set()
s2 = set()
while i < n:
    inp = list(raw_input())
    t = 0
    j = 0
    while j < n:
        
        if i == j or i == n -1-j:
            s1.add(inp[j])
        else:
            s2.add(inp[j])
        j = j +1
    i = i+ 1
if len(s1) ==1 and  len(s2) == 1:
    if len(s1.intersection(s2)) ==0 :
        print 'YES'
    else: 
        print 'NO'
else:
    print 'NO'