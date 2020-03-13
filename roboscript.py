# https://www.codewars.com/kata/5870fa11aa0428da750000da/train/python
import re
from collections import defaultdict
def highlight(code):
    dflt = '<span style="color: orange">{delim}</span>'
    obj = {
       'F': '<span style="color: pink">{delim}</span>',
       'L': '<span style="color: red">{delim}</span>',
       'R': '<span style="color: green">{delim}</span>'
    }
    ln = len(code)
    temp = [item[0] for item in re.findall(r"((.)\2*)", code)]

    k = []
    y = defaultdict(int)
    ignr_idx = -1
    jj = 0
    for i , item in enumerate( temp ):
        try:
            j = i
            ans = i
            while (isinstance(int(temp[j]) ,int)) :
                ans = max (ans, j-i)
                j = j+1
                ignr_idx = j
        except Exception   as e:
            pass
        if ignr_idx> i :
            jj = ignr_idx - i 
            y [ignr_idx] = max (jj , y[ignr_idx])
        
        # print(k)

    gg =[]
    for ky,val in y.items():
        temp[ky-val] = ''.join(temp[ky-val:ky])
        for m in range(ky-val+1, ky ):
            temp[m] = None
    temp = list(filter(lambda x: x != None,temp))
    print (temp)
    op=''
    for itm in temp:
        k1 = re.findall('[a-zA-Z()]', itm)
        k2 = re.findall('[0-9]', itm)
        # print (k1)
        try:
            if k1 and k2:
                ipc = int(k2[0])* k1[0]
                op += obj[k1[0]].format(delim=ipc)

            elif not k1 and len(k2)>0:
                if  len(k1)==1:
                    op += obj[k2[0]].format(delim=k2[0])
                else:
                    op += dflt.format(delim=itm)
            elif k1:
                if set(k1) == set([')','(']):
                    op += ''.join(k1)
                elif set(k1)  == set([')']):
                    op += ''.join(k1)
                elif set(k1)  == set(['(']):
                    op += ''.join(k1)
                elif k1[0] in [')','(']:
                    op += k1[0]
                else:
                    op += obj[k1[0]].format(delim=k1[0])


        except Exception as e:
            pass
    
    return op

print(highlight('4(80L4)4FL(()665R7L33995843535(8L8528903FR79F8F(F636355F282R636R0(R)R)('))
 
 