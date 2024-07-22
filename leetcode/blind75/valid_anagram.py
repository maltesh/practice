from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


a =Solution()

s = "anagram"
t = "nagaram"
assert True == a.isAnagram(s, t)

s = "rat"
t = "car"
assert False == a.isAnagram(s, t)