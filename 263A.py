# https://codeforces.com/contest/263/problem/A

n = 5
t = 0 
temp = []

r , c = 0 , 0

def ff (x) :
    return 0 if x is '0' else 1

while t  < n:     
     row = map (ff,raw_input().split( ' '))     
     temp.append(row)
     for idx, val in  enumerate(row):
         if val : 
             r , c = t , idx         
     t = t + 1
    

print abs(r-2)+ abs(2-c)