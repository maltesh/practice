# https://codeforces.com/contest/680/problem/B

from itertools import izip
n ,b = map(int,raw_input().split(' '))
temp = map(int,raw_input().split(' '))

sq1 = temp[0: b-1]
sq2 = temp[b:]
ct = 0
diff = None

if len(sq1) > len(sq2):
    diff = sq1[0:len(sq1) -len(sq2)]
else:
    diff = sq2[len(sq1):]

temp1 = izip(reversed(sq1), sq2)
for item in temp1:
    if item[0] and item[1]:
        ct = ct+2

if temp[b-1]:
    ct = ct+1

for t in diff:
    if t:
        ct =ct +1
print ct