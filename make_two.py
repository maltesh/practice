# https://www.codewars.com/kata/make-equal/discuss
def count(a, t, x):
    ct = 0
    print a ,t,x
    #if x== 1:
    #    return 0
    for item in a:
        try:
            if item-t == 0 :
                print item
                ct =ct +1
            elif  (item - t) % x  == 0:
                ct = ct+1
        except :
            continue
        
    return ct

def proofread(string):
    original = 'ie'
    replacement = 'ei'
    t = string[:]
    string = string.split('.')
    temp = []
    print(t)
    for sttr in string:
     #   print (sttr)
        if sttr:
            sttr = sttr[0].upper() + sttr[1:].lower()
            sttr = sttr.replace(original,replacement)
            if t.index('.') >= 0:
                sttr = sttr + '.'
            temp.append(sttr)
    return ' '.join(temp)
    


print count([55796, 80967, 54129, 1329, 98814, 44994, 17627, 30874, 66305, 60274, 18907, 95993, 63229, 95968, 66196, 2301, 36932, 73287, 74829, 50041, 4423, 18385, 4109, 9563, 30598, 36290, 
36684, 3292, 61132, 74187, 73571, 10237, 10237, 10237, 10237, 10237, 10237, 10237, 10237, 10237, 10237] ,10237, 0)