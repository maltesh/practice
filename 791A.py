# https://codeforces.com/contest/791/problem/A

limak , bob = map(int,raw_input().split(' '))
l_f = 3
b_f = 2
temp = 0 
while limak <= bob :
    temp = temp + 1
    limak = limak * l_f    
    bob = bob * b_f


print temp