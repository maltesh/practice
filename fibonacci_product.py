# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):
    if prod in [0,1]:
        return prod
    
    a = 0 
    b = 1
    while True:
        c = a +b 
        a = b 
        b = c
        if a*b <= prod:
            q,r = divmod(b,a)
            # print (a,b,q,r)
            if  a*b == prod:
                return [a,b,True]
        else:
            return [a,b, False]

       
print (productFib(714))