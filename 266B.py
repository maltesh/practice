# https://codeforces.com/problemset/problem/266/B

n ,t = map(int , raw_input().split( ' '))
pos = list(raw_input())
rtn = 0
ct = 0
while rtn < t:
    for idx,val in enumerate(list(pos)):
        if val =='B' :
            if idx+1 < len(pos) and pos[idx+1] == 'G':
                pos[idx], pos[idx+1]= pos[idx+1],pos[idx]
    rtn = rtn+1
    

print ''.join(pos)