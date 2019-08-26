def persistence(n):
    k = 0
    while len(list(str(n))) !=1 :
        g = 1
        for  v in map(int,list(str(n))):
            g = g * v
        k = k + 1
        n = g
    return k

print persistence(999)