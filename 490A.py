# http://codeforces.com/contest/490/problem/A
from collections import defaultdict
n = int(raw_input())
temp = defaultdict(lambda:0)
sub_student_id = defaultdict(list)
inpt = map(int, raw_input().split(' '))
sub = [None] * (n)

for idx ,val in enumerate(inpt):
    temp[val] = temp[val] + 1
    sub_student_id[val].append(idx+1)

if len(temp.keys()) !=3 :
    print 0
else:
    nteams = sorted(temp.values())
    nteam = nteams[0] if nteams else 0
    i = 0
    print  nteam 
    while i < nteam:
        z = sub_student_id.get(1)
        o = sub_student_id.get(2)
        t = sub_student_id.get(3)
        # print z , o ,t
        print z[i] ,o[i], t[i]
        i = i +1
