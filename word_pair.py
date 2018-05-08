#https://www.codewars.com/kata/find-the-word-pair/train/python

import itertools
# def compound_match(words, target):    
#     fnd_wrods={}
#     vals =None
#     kys = []
#     for item in itertools.combinations(words,2): 
#         k0 = words.index(item[0])
#         k1 = words.index(item[1])
#         if item[0]+item[1]==target:
#             vals = [item[0],item[1]]
#             kys = [k0,k1]
#             vals.append(kys)
#             return vals
#         elif item[1]+item[0] == target:            
#             kys = [k1,k0]
#             vals = [item[0],item[1]]
#             vals.append(kys)
#             return vals

#     if vals:
#         vals.append(kys)
    
#     return vals


import itertools
def compound_match(words,target):
    vals =[]
    keys =[]
    fvals =[]
    fkeys =[]
    for index,word in enumerate(set(words)):
        if target.endswith(word) or \
            target.startswith(word) :
            if word not in vals:
                vals.append(word)
                keys.append(index)
        if len(vals) >= 2:
            for item in itertools.combinations(vals,2):
                k0 = words.index(item[0])
                k1 = words.index(item[1])
                if target == item[0]+item[1] :
                    # print k0,k1
                    if k0 < k1:                        
                        fvals = [item[0],item[1]]
                        fkeys = [k0,k1]                        
                        fvals.append(fkeys)
                        return fvals
                    else:
                        fvals = [item[1],item[0]]
                        fkeys = [k0,k1]                        
                        fvals.append(fkeys)
                        return fvals
                elif target == item[1]+item[0] :
                    
                    if k0 < k1:
                        fvals = [item[0],item[1]]
                        fkeys = [k1,k0]
                        fvals.append(fkeys)
                        return fvals    
                    else:
                        fvals = [item[1],item[0]]
                        fkeys = [k1,k0]
                        fvals.append(fkeys)
                        return fvals    
    if len(fvals)==0:
        return None

arr1 = ['super','bow','bowl','tar','get','book','let']
arr2 = ['bow','crystal','organic','ally','rain','line']
arr3 = ['top','main','tree','ally','fin','line']
arr4 = ['bel', 'bed', 'low', 'grab', 'be', 'knight']

# print compound_match(arr3, 'treetop')
print compound_match(arr1, 'superbowl')
print compound_match(arr2, 'crystalline')
print compound_match(arr2, 'rainbow')
print compound_match(arr2, 'organically')
print compound_match(arr3, 'treefinally')
print compound_match(arr4, 'beknight')
print compound_match(arr4, 'bellow')

# print compound_match(arr4, 'bellow') , 'tobe',"['bel','low',[0,2]]"
# print compound_match(arr4, 'below'),' tobe ',"['low','be', [4,2]]"
# print compound_match(arr4, 'beknight')

# print compound_match(arr3, 'treefinally')
# print compound_match(arr1, 'superbowl'),
# print compound_match(arr2, 'rainbow')
# print compound_match(arr3, 'treefinally')