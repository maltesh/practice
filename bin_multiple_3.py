#https://www.codewars.com/kata/54de279df565808f8b00126a/train/python
#https://www.codewars.com/kata/validate-credit-card-number


def validate(n):
    l = map(int,list(str(n)))
    rng=[]
    if len(str(n))%2==1:
        rng = range(1,len(l),2)
    else:
        rng = range(0,len(l),2)
    
    for index in rng:
        item =  int(l[index]) * 2
        l[index] = item
        if item  > 9:
            temp = str(item)
            l[index] =  int(temp[0])+ int(temp[1])
    ssum = sum(l)*9
    if  sum(l)%10 == 0:
        return True
    return False 



print validate(123)
print validate(1)
print validate(2121)
print validate(1230)

#rint validate(891)

#print validate(1714)
