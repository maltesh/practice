# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        stk = []
        for idx, cr in enumerate(s):
            if cr in ['[', '{','('] :
                stk.append(cr)
            else:
                if len(stk):
                    pp = stk.pop()
                    if cr == ')' and  pp !='(':
                        return False
                    if cr == '}' and  pp !='{':
                        return False
                    if cr == ']' and  pp !='[':
                        return False
                else:
                    return False
        if len(stk)==0:
            return True

s ="([)]"
a =Solution()
# assert False == a.isValid(s)


s = "()"
assert True == a.isValid(s)

s = "()[]{}"
assert True == a.isValid(s)

s = "(]"
assert False == a.isValid(s)

s = "]"
assert False == a.isValid(s)