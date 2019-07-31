n,m,a = map(int,raw_input().split(' ' ))
fx = int(float(m)/a)
fy = int(float(n)/a)

if m %a != 0:
    fx = fx+1
if n%a != 0:
    fy =  fy+1

print fx* fy

