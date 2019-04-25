#https://codeforces.com/problemset/problem/1065/G

input = str(raw_input())
n,m,k = map(int,input.split(' '))

def fib(n,computed={0:0,1:1}):
    if computed.get(n,False):
        computed[n] = fib(n-1,computed)+ fib(n-1,computed)
    return str(computed[n])
    
