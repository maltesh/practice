#https://www.hackerrank.com/challenges/similar-strings

def comp(x,y):
    for i in range(len(x)):
        for j in range(len(x)):
            if i !=j:
                if  x[i]==x[j]:
                    if y[i] != y[j]:
                        return False
                        break
                else:
                    if y[i] == y[j]:
                        return False
                        break
    return True

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
        real_pat = [ fl == sl for fl,sl in zip(patern,patern[1:])]
        all_paterns = [S[i:i+diff]  for i  in range(0,len(S)) if len(patern) == len(S[i:i+diff])]
        yyeah = False
        for ptrn in all_paterns:
            if comp(ptrn,patern):
                cont = cont + 1
    print cont
    q = q - 1

