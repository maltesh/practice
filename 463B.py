# http://codeforces.com/contest/463/problem/B

n = int(input())
pylons = list(map(int , raw_input().split(' ')))
energy = 0
k = 0 
mny = pylons[0]
fp = pylons[0]
for i in range(1,n):
    # print (fp, pylons[i], mny, energy)

    if fp- pylons[i]>0:
        energy = energy + abs(fp-pylons[i])

    else:
        if energy >= (pylons[i] -fp)  :
            energy = energy - (pylons[i] -fp) 
        else:
            #mny = pylons[i]
              mny = mny + abs(fp-pylons[i])-energy
              energy = 0
        # energy = energy + abs(fp-pylons[i])
    # else:
        
    fp = pylons[i]
print (mny)