
#https://www.hackerrank.com/challenges/beautiful-binary-string?h_r=next-challenge&h_v=zen
#n = int(raw_input().strip())
#B = raw_input().strip()
s = B[:]
count =0
if B:
    while s.find('010') >= 0:
        count = count + 1
        index = s.find('010')
        s = s[:index]+'011'+s[index+3:]
print count
