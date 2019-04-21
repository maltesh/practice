# https://codeforces.com/contest/112/problem/A

frst = raw_input()
sec = raw_input()
t = False
for i , val in enumerate(frst):
    if frst[i].lower() < sec[i].lower(): 
        print -1
        t = True
        break
    elif frst[i].lower() > sec[i].lower():
        print  1
        t = True
        break
if not t :
    print 0