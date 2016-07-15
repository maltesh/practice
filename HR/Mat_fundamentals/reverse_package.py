#https://www.hackerrank.com/challenges/reverse-game

# N/2For all n>N/2 are in descending order  and n<N/2 occupy ascending order


import sys
# lines = sys.stdin.readlines()
lines = [2,'3 1']
for line in lines[1:]:
    n,k = map(int,line.split( " "))
    if(k>=n/2):
        print(2*(n-k-1))
    else:
        print(2*k+1)