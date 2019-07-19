k , r  = map(int , raw_input().split(' '))
i = 1
while True:
    if (i*k)%10 in [0,r] :
        print i
        break
    i = i +1