#https://www.codewars.com/kata/scramblies/train/python

#For each character c of the second String, we increment the value stored in the array at the position c - 'a': this corresponds to the
# alphabetical position of the character (based from 0: 'a' -> 0, 'b' -> 1, ..., 'z' -> 25).
#Then for each character c of the first String, we decrement the value stored at the alphabetical position.
#inally, if at the end of this process, we end up with at least one value that is strictly positive, we know that the second String
#wasn't contained in the first one. This is because it means that we encountered a character in str2 more times than it was in str1 (it was incremented more times than it was decremented).

def scramble(s1,s2):
    parent={}
    for s in s2:
        if parent.get(s,None) is None:
            parent[s]=1
        else:
            parent[s]=1+parent[s]
    for s in s1:
        if parent.get(s,None) is not None:
            parent[s]=parent[s]-1

    for key,valu in parent.iteritems():
        if valu >= 1:
            return False
    return True

print scramble('rkqodlw','world')
print scramble('cedewaraaossoqqyt','codewars')
print scramble('katas','steak')
print scramble('scriptjava','javascript')
print scramble('scriptingjava','javascript')