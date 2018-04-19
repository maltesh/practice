from itertools import combinations
from collections import Counter


# def sum_pairs(ints, s):
    
    # def rem(ele):
    #     ints.remove(ele)
        
    # del_el=[]
    # c = Counter(ints)
    # d_e = [val  for val,key in c.items() if val>s]
    # map(rem,d_e)
#     temp = 

#     for tpl in combinations(ints,2) :
#         if sum(tpl) == s :
#             temp.append( list(tpl))
    
#     t = 100
#     itm =None
#     print temp
#     if temp:
#         for item in temp:
#             d =item[1]-item[0] 
#             if d<0:
#                 d = -1 * d 
#             if  d <= t  :
#                 t= d
#                 itm =item
#         return  itm
#     return None

#https://codereview.stackexchange.com/questions/74152/given-an-array-of-integers-return-all-pairs-that-add-up-to-100/74187#74187
from collections import Counter
# def sum_pairs(ints,s):
    
#     temp = []
#     for i in xrange(len(ints)):
#         for j in xrange(1,len(ints)):            
#             if i!=j and ints[i]+ints[j] == s:
#                 if temp.count(sorted([i,j])) == 0:
#                     temp.append(sorted([i,j]))

#     d=100000
#     tpl =None
#     for item in  temp:
#         if item[1]-item[0] < d:
#             d = item[1]-item[0]
#             tpl = item
#     if tpl:
#         return  [ints[tpl[0]],ints[tpl[1]]  ]
#     else:
#         return None


def sum_pairs(ints,s):
    my_map={}
    pair = None
    maxIndex =''
    for index in xrange(len(ints)):
        a = ints[index]
        b = s -a
        j = my_map.get(b,None)
        if j is not None and index <= maxIndex and j<= maxIndex:
            return [a,b] if index < j else [b,a]

        if my_map.get(a,None) is None or index<my_map.get(None):
            my_map[a]=index
        
    return pair


def sum_pairs(ints,s):
    my_map={}
    pair = None
    maxIndex =''
#     print s,ints
    rng = xrange(len(ints))
    for index in rng:
        a = ints[index]
        b = s -a
#         if a == s:
#             return [index,index]
        j = my_map.get(b,None)
        if j is not None and index <= maxIndex and j <= maxIndex:
            maxIndex = index if index >j else j
            return [a,b] if index < j else [b,a]
#             pair = sorted([ints[index],ints[j]] )
#             if ints[index]<0 or ints[j]<0:
#                 pair = [ints[j],ints[index]]

        if my_map.get(a,None) is None or index < my_map.get(None):
            my_map[a]=index
        
    return pair


print sum_pairs( [1, 4, 8, 7, 3, 15],8)        
print sum_pairs([10, 5, 2, 3, 7, 5,11],10)
print sum_pairs([11, 3, 7, 5],         10)
print sum_pairs([4, 3, 2, 3, 4],         6)
print sum_pairs([20, -13, 40],-7)

print sum_pairs([1, -2, 3, 0, -6, 1],-6)

print sum_pairs([13,1,1,1,1,1,1,1],13)
