import string

def is_pangram(s):
    ss = ''.join(map(str.lower, set(s)))
    chrs = string.ascii_lowercase
    a= []
    for cr in chrs:
        idx = ss.find(cr)
        if idx >=0 :
            a.append( chrs[0: idx] + chrs[idx+1:])
    return True if len(a)==26 else False   


# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())         
        
# pangram = "The quick, rown fox jumps over the lazy dog!"
# print (is_pangram(pangram))