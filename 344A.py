# http://codeforces.com/contest/344/problem/A


def lg_groups():
    n  = int(raw_input())
    i = 0
    inpt2 = ''
    ct = 0 
    while i < n:
        inpt = raw_input()
        if inpt != inpt2:
            ct = ct + 1
        inpt2 = inpt
        i = i+1
    return ct

if __name__ == "__main__":
    print lg_groups()