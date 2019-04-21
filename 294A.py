# https://codeforces.com/contest/294/problem/A

wires = int(raw_input())
birds_in_wires = map(int,raw_input().split(' '))
birds  = dict(zip(range(1,len(birds_in_wires)+1) , birds_in_wires))
m = int(raw_input())

temp  = {}
# print birds
i = 1
while m > 0 :
    x, y = map(int,raw_input().split( ' '))
    down, up = y-1, birds[x]-y
    if x-1 > 0:
        birds[x-1] = birds[x-1] + down
    if x+1 <= wires:
        birds[x+1] = birds[x+1] + up
    birds[x] = 0    
    m = m-1

for item in birds.values():
    print item
