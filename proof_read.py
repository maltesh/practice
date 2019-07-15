import re
def proofread(string):
    
    t = string[:]
    string = string.split(' ')
    temp = []
    bl = False
    # print string
    for key,sttr in enumerate( string ):
            
        if sttr:
            re1 = re.compile(re.escape('ie'), re.IGNORECASE)
            sttr = re1.sub('ei',sttr)
            sttr = sttr.lower()
            
            if bl:
                sttr = sttr.title()
                bl = False
            if sttr.find('.')>=0:
                bl = True
            else:
                bl =False
            
            if key ==0:
                sttr = sttr.title()

        temp.append(sttr)

    temp =   ' ' .join(temp)
    return temp