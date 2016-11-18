#https://www.hackerrank.com/challenges/similar-strings
n,q = map(int, raw_input().strip().split(' '))
S = raw_input().strip()
while q > 0:
    cont = 0
    l,r = map (int ,raw_input().strip().split(' '))
    slic = S[l:r]
    if l > 0:
        patern = S[l-1:r]

        i = 0
        diff = r - l + 1
        real_pat = [ fl == sl for fl,sl in zip(patern,patern[1:]) ]
        print patern
        all_paterns = [S[i:i+diff]  for i  in range(0,len(S)) if len(patern) == len(S[i:i+diff])]
        print all_paterns
        for ptrn in all_paterns:

    print cont
    q = q - 1

